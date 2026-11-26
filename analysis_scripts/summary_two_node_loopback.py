#!/usr/bin/env python3.11
"""11aab summary -> FINDINGS_11aab.md: two Besu nodes on one Slurm node (loopback peers), gate in front of node A only; node B receives transactions only by gossip. Per arm (mean over seeds): attack blocked, ordinary rejected, receipts, node A and node B GC pauses, node B peak RSS, peak pool sizes, head lag."""
import glob,gzip,json,re,collections,statistics as S
R='<path>/runs/'
def gcB(f):
    p=[]
    for l in gzip.open(f,'rt',errors='ignore'):
        m=re.search(r'Pause (?:Young|Full|Remark|Cleanup).*?(\d+\.\d+)ms\s*$',l)
        if m: p.append(float(m.group(1)))
    return p
def run(d):
    od=glob.glob(d+'/*/')[0]; s=json.load(open(od+'summary.json'))
    c=collections.Counter(); atk=collections.Counter()
    for f in glob.glob(od+'labels/labels_w*.jsonl.gz'):
        for l in gzip.open(f,'rt'):
            x=json.loads(l)
            if x.get('type')!='tx': continue
            o=(x.get('submit') or {}).get('outcome'); cl=x['label']
            if cl=='attack': atk[o]+=1
            elif cl in('benign','lookalike','legit_heavy') or cl not in ('skipped',): c[o]+=1
    rows=[l.strip().split(',') for l in open(od+'nodeB_sample.csv') if l.strip()]
    pa=[int(r[3]) for r in rows if len(r)>3 and r[3].isdigit()]; pb=[int(r[4]) for r in rows if len(r)>4 and r[4].isdigit()]
    rss=[int(r[5]) for r in rows if len(r)>5 and r[5].isdigit()]
    lag=[int(r[1])-int(r[2]) for r in rows if len(r)>2 and r[1].isdigit() and r[2].isdigit()]
    gb=gcB(od+'gc_B.log.gz') if glob.glob(od+'gc_B.log.gz') else []
    off=sum(v for k,v in c.items() if k!='not-sent' and k!=None)+c['not-sent']
    return dict(atk=atk,rej=c['not-sent'],off=off,ok=c['ok'],gcA_n=s.get('gc_pause_count'),gcA_tot=s.get('gc_pause_total_ms'),gcA_max=s.get('gc_pause_max_ms'),gcB_n=len(gb),gcB_tot=sum(gb),gcB_max=max(gb) if gb else 0,rssB=max(rss)/1024 if rss else 0,peakA=s.get('peak_rss_mb'),poolA=max(pa) if pa else 0,poolB=max(pb) if pb else 0,lagmax=max(lag) if lag else 0,oom=bool(s.get('oom_lines')),dead=s.get('time_to_node_death_s') is not None,verdict=s.get('verdict'),fr=s.get('fail_reasons'))
res=collections.defaultdict(list)
for d in sorted(glob.glob(R+'TWONODE_*')):
    if 'SMOKE' in d or not glob.glob(d+'/*/summary.json'): continue
    m=re.match(r'.*TWONODE_(\w+?)_(\w+?)_s(\d+)$',d); res[(m.group(1),m.group(2))].append(run(d))
names={'MN0':'no attack (control)','MN1':'attack submitted to the gated node A','MN2':'attack submitted to the ungated node B (gate on node A only)'}
O=['# 11aab findings: two Besu nodes on one Slurm node, gate in front of node A only (written 2026-11-26)\n','| block | arm | runs | attack blocked | ordinary rejected | node A GC total ms | node A GC max ms | node B GC total ms | node B GC max ms | node A peak RSS MB | node B peak RSS MB | peak pool A | peak pool B | max head lag (blocks) | OOM | node deaths | verdicts |','|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
f=lambda k,rs: S.mean((r[k] or 0) for r in rs)
for (b,a) in sorted(res,key=lambda k:(k[0],k[1]!='none',k[1])):
    rs=res[(b,a)]; an=sum(sum(r['atk'].values()) for r in rs); ab=sum(r['atk']['not-sent'] for r in rs)
    rej=S.mean(r['rej']/max(1,r['off']) for r in rs)
    O.append('| %s | %s | %d | %s | %.4f | %.0f | %.1f | %.0f | %.1f | %.0f | %.0f | %.0f | %.0f | %d | %d | %d | %s |'%(b,a,len(rs),('%.3f'%(ab/an)) if an else '-',rej,f('gcA_tot',rs),f('gcA_max',rs),f('gcB_tot',rs),f('gcB_max',rs),f('peakA',rs),f('rssB',rs),f('poolA',rs),f('poolB',rs),max(r['lagmax'] for r in rs),sum(r['oom'] for r in rs),sum(r['dead'] for r in rs),','.join(sorted({str(r['verdict']) for r in rs}))))
O.append('\nBlocks: '+'; '.join('%s = %s'%kv for kv in names.items())+'.')
O.append('\n## Reading rules\nNode B has no gate and no miner; it receives every transaction only by gossip from node A and is the observer of what the gate does or does not protect. Runs are executions of one seeded design, not independent samples. One run (SizeStatic seed 67903) was refused at start because the nodes had not connected; it was rerun with the same seed after the chains finished and the failed directory is kept.\n')
open('FINDINGS_11aab.md','w').write('\n'.join(O)+'\n'); print('\n'.join(O))
