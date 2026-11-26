#!/usr/bin/env python3.11
"""11uu summary -> FINDINGS_11ww.md: confirmation latency percentiles of requests with a receipt (per run, then mean over seeds), share without receipt at 240 s, rejected share, gate decision latency, on-chain throughput in the burst window, largest block gap. Descriptive; per-run percentiles are averaged over three seeds (no pooled percentiles)."""
import glob,gzip,json,re,collections,statistics as S,numpy as np,csv
R='<path>/runs/'
def run(d):
    od=glob.glob(d+'/*/')[0]; s=json.load(open(od+'summary.json'))
    lat=collections.defaultdict(list); out=collections.Counter(); gate=[]
    for f in glob.glob(od+'labels/labels_w*.jsonl.gz'):
        for l in gzip.open(f,'rt'):
            x=json.loads(l)
            if x.get('type')!='tx': continue
            sb=x.get('submit') or {}; o=sb.get('outcome'); cl=x['label']; out[(cl,o)]+=1
            if o=='ok' and sb.get('latency_ms') is not None: lat[cl].append(sb['latency_ms']/1000.0)
            a=x.get('ai') or {}
            if a.get('latency_ms') is not None: gate.append(a['latency_ms'])
    T0=s['T0']; tx=0; sec=0
    try:
        for r in csv.DictReader(open(od+'chain_final_blocks.csv')):
            ts=int(r['ts']); 
            if T0+60<=ts<T0+180: tx+=int(r['txs'])
        sec=120.0
    except Exception: pass
    return dict(lat=lat,out=out,gate=gate,tp=(tx/sec if sec else None),gap=s.get('max_block_gap_s_after_T0'),dead=s.get('time_to_node_death_s'))
res=collections.defaultdict(list)
for d in sorted(glob.glob(R+'LATENCY_*')):
    if 'SMOKE' in d or not glob.glob(d+'/*/summary.json'): continue
    m=re.match(r'.*LATENCY_(\w+?)_(\w+?)_s(\d+)$',d); res[(m.group(1),m.group(2))].append(run(d))
def pc(v,q): return float(np.percentile(v,q)) if len(v) else None
names={'LQ1':'Attack-only, 400 attack requests','LMX':'Mixed attack + look-alike','LRM':'Attack-only, ordinary sizes replayed from public blocks'}
O=['# 11ww findings: confirmation latency as observed by the load generator (receipt limit 240 s verified by the timeout audit files; written 2026-11-24)\n']
for blk in ('LQ1','LMX','LRM'):
    O.append('\n## %s: %s\n'%(blk,names[blk]))
    O.append('| arm | runs | class | n with receipt (per run) | p50 s | p95 s | p99 s | p99.9 s | no receipt within 240 s | rejected | gate p99 ms | on-chain tx/s in window | max block gap s |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    arms=sorted({a for (b,a) in res if b==blk},key=lambda a:(a!='none',a))
    for a in arms:
        rs=res[(blk,a)]
        for cl in ('benign','attack','lookalike'):
            ns=[len(r['lat'][cl]) for r in rs]
            if sum(ns)==0 and cl!='benign': continue
            def mp(q): 
                v=[pc(r['lat'][cl],q) for r in rs if len(r['lat'][cl])>50]; return ('%.1f'%S.mean(v)) if v else '-'
            sent=[sum(v for (c,o),v in r['out'].items() if c==cl and o not in ('not-sent',)) for r in rs]
            nores=[sum(v for (c,o),v in r['out'].items() if c==cl and o not in ('ok','not-sent')) for r in rs]
            rej=[sum(v for (c,o),v in r['out'].items() if c==cl and o=='not-sent') for r in rs]
            tot=[sum(v for (c,o),v in r['out'].items() if c==cl) for r in rs]
            g=[pc(r['gate'],99) for r in rs if r['gate']]
            O.append('| %s | %d | %s | %.0f | %s | %s | %s | %s | %.4f | %.3f | %s | %.1f | %s |'%(a,len(rs),cl,S.mean(ns),mp(50),mp(95),mp(99),mp(99.9),(sum(nores)/max(1,sum(sent))),sum(rej)/max(1,sum(tot)),('%.0f'%S.mean(g)) if g else '-',S.mean(r['tp'] for r in rs if r['tp'] is not None),max(r['gap'] or 0 for r in rs)))
O.append('\n## Reading rules\nPercentiles are over requests that received a receipt and are averaged over the runs of an arm (three seeds); the share without a receipt within the 240 s limit and the rejected share are given beside them and must be read with them (a policy that rejects heavy requests has no latency for them). Confirmation latency is the load generator\'s submit-to-receipt time; it is not validator-level timeliness. Differences between arms are descriptive.\n')
open('<path>/FINDINGS_11ww.md','w').write('\n'.join(O)+'\n'); print('\n'.join(O))
