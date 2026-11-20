import glob,gzip,json,os
rows=[]
for d in sorted(glob.glob('runs/ACC11KK_*_s6[23][0-9][0-9][0-9]')):
    if 'SMOKE' in d: continue
    od=[x for x in glob.glob(d+'/*/') if os.path.exists(x+'summary.json')]
    if not od: continue
    od=od[0]; name=d.split('ACC11KK_')[1]
    L=dict(ok=0,failed=0,unf=0,ns=0,a_ns=0,noout=0)
    for f in glob.glob(od+'labels/labels_w*.jsonl.gz'):
        for line in gzip.open(f,'rt'):
            r=json.loads(line)
            if r.get('type')!='tx' or r['label']!='benign':
                if r.get('type')=='tx' and r['label']!='benign' and (r.get('submit') or {}).get('outcome')=='not-sent': L['a_ns']+=1
                continue
            sb=r.get('submit'); oc=sb['outcome'] if sb else 'no-outcome'
            if oc=='ok': L['ok']+=1
            elif oc=='failed': L['failed']+=1
            elif oc=='not-sent': L['ns']+=1
            else: L['unf']+=1
    T=dict(ok=0,fail=0,R=0); mt=[]
    for f in glob.glob(od+'tierstats/w*.json'):
        mt.append(os.path.getmtime(f)); st=json.load(open(f))['stats']
        for c in 'SML':
            for t,l,ok in st.get(c,[]):
                T['ok' if ok==1 else 'fail']+=1
        T['R']+=len(st.get('R',[]))
    s=json.load(open(od+'summary.json'))
    sm=os.path.getmtime(od+'summary.json')
    died=any(k for k in s if 'death' in k.lower() and s[k]) if isinstance(s,dict) else False
    dok=L['ok']-T['ok']; dfail=L['failed']+L['unf']-T['fail']; dR=L['ns']+L['a_ns']-T['R']
    if dok or dfail or dR:
        rows.append((name,dok,dfail,L['unf'],dR,round(sm-max(mt)) if mt else None,len(mt)))
print('run | d_receipts(labels-tier) | d_nonreceipt | labels_unfinished | d_notsent | summary_mtime-last_tierstats_mtime s | n_tierfiles')
for r in rows: print(*r,sep=' | ')
print(len(rows),'runs with any difference')
