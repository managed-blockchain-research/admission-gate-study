#!/usr/bin/env python3.11
"""Static plant gain of the pressure signal from constant-probability runs (RandP arms of 11qq/11ss: every request rejected with a fixed probability p, independent of the signal). For each run: mean and 90th percentile of the pressure reading seen by the gate over the decisions of the run, and the share of time above the ramp start. Across p: least-squares slope du/dp and the resulting loop gain of the pressure-graded rule (ramp slope 1/0.30 per unit of u). Descriptive; not an identified transfer function."""
import glob,gzip,json,statistics as S,collections,re,math
runs=collections.defaultdict(list)
for pat in ('ACC11QQ_Q1_RandP*_s66*','ACC11QQ_Q1_none_s66*','ACC11SS_MXQ_RandP*_s664*','ACC11SS_NMQ_RandP*_s664*','ACC11SS_ZGQ_RandP*_s664*'):
    for d in glob.glob('<path>/runs/'+pat):
        if 'SMOKE' in d: continue
        m=re.match(r'.*ACC11(QQ|SS)_(\w+?)_(\w+?)_s(\d+)$',d); blk,arm=m.group(2),m.group(3)
        f=glob.glob(d+'/*/ai_decisions.jsonl.gz')
        if not f: continue
        us=[]
        for l in gzip.open(f[0],'rt'):
            x=json.loads(l)
            if x.get('type')=='decision' and x.get('u_t') is not None and not x.get('stale'): us.append(x['u_t'])
        if len(us)<1000: continue
        us.sort(); p=None
        mp=re.match(r'RandP(\d+)',arm); p=int(mp.group(1))/100 if mp else None
        runs[(blk,arm,p)].append((S.mean(us),us[int(0.9*len(us))],sum(1 for u in us if u>=0.6)/len(us)))
out=['# Static gain of the pressure signal (constant rejection probability runs; written 2026-11-24)\n','| cell | arm | p | runs | mean u | 90th pct u | share u >= 0.60 |','|---|---|---|---|---|---|---|']
byblk=collections.defaultdict(list)
for (blk,arm,p),v in sorted(runs.items(),key=lambda x:(x[0][0],x[0][2] or 0)):
    mu=S.mean(a for a,_,_ in v); p90=S.mean(b for _,b,_ in v); sh=S.mean(c for _,_,c in v)
    out.append('| %s | %s | %s | %d | %.3f | %.3f | %.3f |'%(blk,arm,'' if p is None else '%.1f'%p,len(v),mu,p90,sh))
    if p is not None: byblk[blk].append((p,mu))
out.append('\n## Slope du/dp (least squares over the arms; mean u against p) and loop gain of the pressure-graded rule\n')
out.append('| cell | points | du/dp | loop gain K = (1/0.30) x du/dp |\n|---|---|---|---|')
for blk,pts in byblk.items():
    if len(pts)<3: continue
    xs=[p for p,_ in pts]; ys=[u for _,u in pts]; mx,my=S.mean(xs),S.mean(ys)
    sl=sum((x-mx)*(y-my) for x,y in pts)/sum((x-mx)**2 for x in xs)
    out.append('| %s | %d | %+.3f | %+.2f |'%(blk,len(pts),sl,sl/0.30))
out.append('\n## Reading rules\nThe slope is a static relation between a constant rejection probability and the mean post-collection reading; it does not give the delay or the dynamics of the loop. The sign shows the direction of the effect of rejection on the signal: a negative slope means that more rejection lowers the reading. The loop gain is the product with the ramp slope and is only a rough size; a stability statement needs the delay (see the step-input runs).\n')
open('<path>/FINDINGS_stability_static.md','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
