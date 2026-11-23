#!/usr/bin/env python3.11
"""11ss summary -> FINDINGS_11ss.md. Per block and arm (mean over seeds): attack blocked, ordinary rejected, look-alike rejected (MXQ), receipts share, runs with node death / OOM exception lines; paired receipts gain vs none over seeds where both runs have a live node. Descriptive; t 95% CI over pair differences."""
import csv,collections,statistics as S,math
D='./'
T={1:12.706,2:4.303,3:3.182,4:2.776}
rows=list(csv.DictReader(open(D+'acc11ss_per_run.csv')))
def f(r,k):
    try: return float(r[k])
    except: return None
for r in rows:
    n=f(r,'benign_n'); la0=f(r,'LA_n') or 0; r['ok']=f(r,'benign_ok30')/n; r['rej']=f(r,'nonLA_not_sent')/(n-la0)
    r['ab']=f(r,'attack_block_rate'); r['dead']=bool(r['node_death_s'] not in ('',None)); r['oom']=int(f(r,'oom_lines') or 0)>0
    la=f(r,'LA_n'); r['larej']=(f(r,'rej_LA')/la) if la else None
by=collections.defaultdict(list)
for r in rows: by[(r['block'],r['arm'])].append(r)
def mean(rs,k):
    v=[r[k] for r in rs if r[k] is not None]; return S.mean(v) if v else None
def pair(blk,arm):
    A={r['seed']:r for r in by[(blk,arm)]}; B={r['seed']:r for r in by[(blk,'none')]}
    ds=[A[s]['ok']-B[s]['ok'] for s in A if s in B and not A[s]['dead'] and not B[s]['dead']]
    if len(ds)<2: return None
    return S.mean(ds),T[len(ds)-1]*S.stdev(ds)/math.sqrt(len(ds)),len(ds)
out=['# 11ss findings (mixed, ZGC and Nethermind cells; low-rate attack over twelve accounts; written 2026-11-23)\n']
names={'MXQ':'Besu G1 512 MB, mixed attack + look-alike (800 attack, 400 look-alike requests)','ZGQ':'Besu ZGC 512 MB, attack-only (1,200 attack requests)','NMQ':'Nethermind 2,048 MiB, attack-only (1,200 attack requests)','MA36':'Besu G1 512 MB, 12 accounts, every 36th slot (about 132 attack requests, synchronized)','MA72':'Besu G1 512 MB, 12 accounts, every 72nd slot (about 66 requests, synchronized)'}
for blk in ('MXQ','ZGQ','NMQ','MA36','MA72'):
    out.append('\n## %s: %s\n'%(blk,names[blk]))
    out.append('| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |\n|---|---|---|---|---|---|---|---|---|')
    arms=sorted({a for (b,a) in by if b==blk},key=lambda a:(mean(by[(blk,a)],'ab') if mean(by[(blk,a)],'ab') is not None else -1))
    for a in arms:
        rs=by[(blk,a)]; p=pair(blk,a) if a!='none' else None
        la=mean(rs,'larej')
        out.append('| %s | %d | %.3f | %.3f | %s | %.3f | %d | %d | %s |'%(a,len(rs),mean(rs,'ab') or 0,mean(rs,'rej'),('%.3f'%la) if la is not None else '-',mean(rs,'ok'),sum(r['dead'] for r in rs),sum(r['oom'] for r in rs),('%+.3f +/- %.3f (n=%d)'%p) if p else '-'))
out.append('\n## Reading rules\nDescriptive statements for these cells only. Receipts of runs whose node died are not comparable and are excluded from paired differences. No interpolated values, no ranking or equivalence claims, no statements about unseen attacks.\n')
open(D+'FINDINGS_11ss.md','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
