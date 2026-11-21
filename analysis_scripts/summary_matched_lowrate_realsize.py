#!/usr/bin/env python3.11
"""11qq/11rr matched-operating-point and low-rate/real-size summary -> FINDINGS_11qq_11rr.md (numbers only; descriptive; same-seed paired t-95% CI over pair differences)."""
import csv,collections,statistics as S,math
D='./'
T={1:12.706,2:4.303,3:3.182,4:2.776,5:2.571,6:2.447,7:2.365,8:2.306}
rows=list(csv.DictReader(open(D+'acc11qq_per_run.csv')))+list(csv.DictReader(open(D+'acc11rr_per_run.csv')))
def f(r,k):
    try: return float(r[k])
    except: return None
for r in rows:
    r['ok']=f(r,'benign_ok30')/f(r,'benign_n'); r['rej']=f(r,'benign_not_sent')/f(r,'benign_n'); r['ab']=f(r,'attack_block_rate') if r['attack_n'] not in ('0','') else None
by=collections.defaultdict(list)
for r in rows: by[(r['block'],r['arm'])].append(r)
def m(blk,arm,k):
    v=[r[k] for r in by[(blk,arm)] if r[k] is not None]; return S.mean(v) if v else None
def pair(blk,arm,k,base='none'):
    A={r['seed']:r[k] for r in by[(blk,arm)]}; B={r['seed']:r[k] for r in by[(blk,base)]}
    # pair by seed offset within block (same seed numbers across arms)
    ds=[A[s]-B[s] for s in A if s in B and A[s] is not None and B[s] is not None]
    if len(ds)<2: return None
    mu=S.mean(ds); h=T[len(ds)-1]*S.stdev(ds)/math.sqrt(len(ds)); return mu,h,len(ds)
out=['# 11qq / 11rr findings (Besu G1 512 MB, 100 tx/s, 240 s, window 60-180 s; same-seed pairs; intervals descriptive; written 2026-11-22)\n']
fam={'RandP (content-blind, probability p)':['RandP20','RandP40','RandP60','RandP80'],
     'SizeFixedP (heavy only, probability p)':['SizeFixedP20','SizeFixedP40','SizeFixedP60','SizeFixedP80'],
     'Global bucket (rate kB/s)':['BudgetR125','BudgetR250','BudgetR500','BudgetR1000','BudgetR2000'],
     'Blanket pressure shedding (ramp)':['PressureOnlyLow','PressureOnly','PressureOnlyHigh'],
     'Size static / graded':['SizeStatic','SizeGraded']}
out.append('## Q1: realized operating points (400 attack requests; mean over 3 seeds; benign cost = share of ordinary requests rejected; receipts = share of ordinary requests with a receipt within 30 s)\n')
out.append('| family | arm | attack blocked | ordinary rejected | receipts | receipts gain vs none (paired, 95% CI) |\n|---|---|---|---|---|---|')
pts=collections.defaultdict(list)
for fa,arms in fam.items():
    for a in arms:
        ab,rej,ok=m('Q1',a,'ab'),m('Q1',a,'rej'),m('Q1',a,'ok'); p=pair('Q1',a,'ok')
        pts[fa].append((ab,rej,ok,a))
        out.append('| %s | %s | %.3f | %.3f | %.3f | %+.3f +/- %.3f |'%(fa,a,ab,rej,ok,p[0],p[1]))
out.append('| reference | none | 0.000 | 0.000 | %.3f | |'%m('Q1','none','ok'))
out.append('\n## Q1: benign cost and receipts at matched attack-blocked rates (linear interpolation between neighbouring realized points of the same family; INTERPOLATED, not run; points outside a family\'s realized range are omitted)\n')
out.append('| target attack blocked | family | ordinary rejected | receipts |\n|---|---|---|---|')
for t in (0.2,0.4,0.6,0.8):
    for fa,pl in pts.items():
        pl=sorted(pl+[(0.0,0.0,m('Q1','none','ok'),'none')]) if fa not in ('Size static / graded',) else sorted(pl)
        val=None
        for (a1,r1,o1,_),(a2,r2,o2,_) in zip(pl,pl[1:]):
            if a1<=t<=a2 and a2>a1:
                w=(t-a1)/(a2-a1); val=(r1+w*(r2-r1),o1+w*(o2-o1)); break
        if val: out.append('| %.1f | %s | %.3f | %.3f |'%(t,fa,val[0],val[1]))
out.append('\n## Low-rate attack (one burst worker sends every m-th slot; LM3: %s attack requests, about 109 kB/s; LM6: %s requests, about 54 kB/s; bucket rate 125 kB/s) \n'%(by[('LM3','none')][0]['attack_n'],by[('LM6','none')][0]['attack_n']))
out.append('| block | arm | attack blocked | ordinary rejected | receipts | receipts gain vs none (paired, 95% CI) |\n|---|---|---|---|---|---|')
for b in ('LM3','LM6'):
    for a in ['none','SizeStatic','PressureOnly','RandP20','BudgetR50','BudgetR125']:
        p=pair(b,a,'ok') if a!='none' else None
        out.append('| %s | %s | %.3f | %.3f | %.3f | %s |'%(b,a,m(b,a,'ab'),m(b,a,'rej'),m(b,a,'ok'),('%+.3f +/- %.3f'%(p[0],p[1])) if p else ''))
out.append('\n## Replay of the real size distribution (ordinary requests: calldata lengths drawn from 60,144 public-block transactions; size only)\n')
out.append('| block | arm | attack blocked | ordinary rejected (share) | ordinary rejected (requests per run) | receipts |\n|---|---|---|---|---|---|')
for b,arms in (('RMA',['none','SizeStatic','SizeGraded','PressureOnly','RandP20','BudgetR125']),('RMN',['none','SizeStatic','PressureOnly'])):
    for a in arms:
        ab=m(b,a,'ab'); n=m(b,a,'rej'); nr=S.mean(f(r,'benign_not_sent') for r in by[(b,a)])
        out.append('| %s | %s | %s | %.4f | %.1f | %.3f |'%(b,a,'%.3f'%ab if ab is not None else '-',n,nr,m(b,a,'ok')))
out.append('\n## Reading rules\nAllowed: descriptive statements for these cells. Not allowed: statements for other sizes, rates, windows or runtimes; equivalence or ranking claims; statements about real traffic beyond calldata sizes (the replay drops the gas, state and arrival structure of real transactions); interpolated values are not measurements.\n')
open(D+'FINDINGS_11qq_11rr.md','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
