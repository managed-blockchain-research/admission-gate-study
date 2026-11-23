#!/usr/bin/env python3.11
"""Feedback-loop dynamics of blanket pressure shedding from the decision logs (11qq/11rr runs with a pressure ramp). Per run: 1 s series of the pressure reading u_t seen by the gate and of the applied reject probability p. Outputs: time in the ramp, p/u cross-correlation lag, ramp crossings, time from the end of the attack window until u falls below the ramp start (0.60). Descriptive; no stability claim."""
import glob,gzip,json,statistics as S,collections,math
runs=[]
for pat in ('ACC11QQ_Q1_PressureOnly*_s66*','ACC11RR_LM*_PressureOnly_s66*'):
    runs+=[d for d in glob.glob('./runs/'+pat) if 'SMOKE' not in d]
rows=[]
def corr(a,b):
    n=len(a); ma,mb=S.mean(a),S.mean(b); va=sum((x-ma)**2 for x in a); vb=sum((x-mb)**2 for x in b)
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/math.sqrt(va*vb) if va>0 and vb>0 else None
out=['# Pressure-feedback loop, measured (blanket pressure shedding runs; 1 s series from the decision logs; written 2026-11-23)\n','| run | seconds with u in ramp (0.6-0.9) | max u | best lag p->du (s) | corr at best lag | u>=0.6 seconds after window end | ramp crossings (0.6 up) |\n|---|---|---|---|---|---|---|']
for d in sorted(runs):
    f=glob.glob(d+'/*/ai_decisions.jsonl.gz')
    if not f: continue
    hdr=None; sec=collections.defaultdict(lambda:[[],[]])
    for l in gzip.open(f[0],'rt'):
        x=json.loads(l)
        if x.get('type')=='header': hdr=x; continue
        if x.get('type')!='decision' or x.get('u_t') is None: continue
        t0=hdr['ts']; s=int((x['ts']-t0)); sec[s][0].append(x['u_t']); sec[s][1].append(x.get('p') or 0.0)
    ks=sorted(sec); 
    if not ks: continue
    u=[S.mean(sec[k][0]) for k in ks]; p=[S.mean(sec[k][1]) for k in ks]
    du=[u[i+1]-u[i] for i in range(len(u)-1)]
    best=(None,None)
    for lag in range(0,21):
        a=p[:len(du)-lag] if lag else p[:len(du)]; b=du[lag:]
        c=corr(a,b[:len(a)]) if len(a)>10 else None
        if c is not None and (best[1] is None or c<best[1]): best=(lag,c)
    inramp=sum(1 for x in u if 0.6<=x<=0.9)
    # window end: attack window 60-180 s after run start of the load generator; log starts earlier -> use the largest-u time as reference-free metric: time from last p>0.5 second to u<0.6
    cross=sum(1 for i in range(1,len(u)) if u[i-1]<0.6<=u[i])
    name=d.split('/')[-1]
    tail=[i for i,x in enumerate(p) if x>0.02]; after=None
    if tail:
        last=tail[-1]; after=sum(1 for x in u[last:] if x>=0.6)
    out.append('| %s | %d | %.2f | %s | %s | %s | %d |'%(name.replace('ACC11QQ_','').replace('ACC11RR_',''),inramp,max(u),best[0],('%.2f'%best[1]) if best[1] is not None else '-',after,cross))
out.append('\n## Reading rules\nDescriptive. The most negative lag correlation between the applied probability and the following change of u is a rough indicator of the loop delay, not an identified transfer function. No claim of stability or instability is made.\n')
open('./FINDINGS_loop_dynamics.md','w').write('\n'.join(out)+'\n'); print('\n'.join(out))
