#!/usr/bin/env python3.11
"""11zz summary -> FINDINGS_11zz.md: replay of the arrival counts and sizes of public mainnet traffic. Per arm (mean over seeds): ordinary requests offered after thinning, attack blocked, ordinary rejected, ordinary receipts within 30 s and share without a receipt, latency percentiles of ordinary requests with a receipt, node deaths."""
import glob,gzip,json,re,collections,statistics as S,numpy as np
R='<path>/runs/'
def run(d):
    od=glob.glob(d+'/*/')[0]; s=json.load(open(od+'summary.json'))
    c=collections.Counter(); lat=[]; atk=collections.Counter()
    for f in glob.glob(od+'labels/labels_w*.jsonl.gz'):
        for l in gzip.open(f,'rt'):
            x=json.loads(l)
            if x.get('type')!='tx': continue
            o=(x.get('submit') or {}).get('outcome'); cl=x['label']
            if cl=='benign':
                c[o]+=1
                if o=='ok': lat.append(x['submit']['latency_ms']/1000.0)
                if o=='ok' and x['submit']['latency_ms']<=30000: c['ok30']+=1
            elif cl=='attack': atk[o]+=1
            elif cl=='skipped': c['skipped']+=1
    off=sum(v for k,v in c.items() if k not in ('skipped','ok30'))
    return dict(off=off,rej=c['not-sent'],ok=c['ok'],ok30=c['ok30'],lat=lat,atk=atk,dead=s.get('time_to_node_death_s') is not None,verdict=s.get('verdict'),oom=bool(s.get('oom_lines')))
res=collections.defaultdict(list)
for d in sorted(glob.glob(R+'ARRIVAL_*')):
    if 'SMOKE' in d or not glob.glob(d+'/*/summary.json'): continue
    m=re.match(r'.*ARRIVAL_(\w+?)_(\w+?)_s(\d+)$',d); res[(m.group(1),m.group(2))].append(run(d))
names={'ER50':'window p50 (11.6 tx/s mean), one attacking account (400 attack requests)','ER99':'window p99 (16.9 tx/s mean), one attacking account (400 attack requests)','ENO':'window p99, no attack'}
O=['# 11zz findings: replay of arrival counts and sizes of public mainnet traffic (written 2026-11-25)\n']
for b in ('ER50','ER99','ENO'):
    O.append('\n## %s: %s\n'%(b,names[b]))
    O.append('| arm | runs | ordinary offered per run | attack blocked | ordinary rejected | receipts within 30 s | no receipt (any reason) | p50 s | p99 s | p99.9 s | node deaths | OOM runs |\n|---|---|---|---|---|---|---|---|---|---|---|---|')
    arms=sorted({a for (bb,a) in res if bb==b},key=lambda a:(a!='none',a))
    for a in arms:
        rs=res[(b,a)]; off=S.mean(r['off'] for r in rs)
        an=sum(sum(r['atk'].values()) for r in rs); ab=sum(r['atk']['not-sent'] for r in rs)
        rej=S.mean(r['rej']/r['off'] for r in rs); ok30=S.mean(r['ok30']/r['off'] for r in rs)
        nores=S.mean((r['off']-r['rej']-r['ok'])/max(1,r['off']-r['rej']) for r in rs)
        pc=lambda q: S.mean(float(np.percentile(r['lat'],q)) for r in rs if len(r['lat'])>50)
        O.append('| %s | %d | %.0f | %s | %.4f | %.4f | %.4f | %.1f | %.1f | %.1f | %d | %d |'%(a,len(rs),off,('%.3f'%(ab/an)) if an else '-',rej,ok30,nores,pc(50),pc(99),pc(99.9),sum(r['dead'] for r in rs),sum(r['oom'] for r in rs)))
O.append('\n## Reading rules\nOrdinary requests are the requests kept after thinning to the replayed per-second counts; the senders are the 30 load-generator accounts and the sizes are the replayed calldata lengths; the attack is the registered 98 KB attack. Descriptive statements about one day of public traffic; not about other days, private order flow or real attackers.\n')
open('<path>/FINDINGS_11zz.md','w').write('\n'.join(O)+'\n'); print('\n'.join(O))
