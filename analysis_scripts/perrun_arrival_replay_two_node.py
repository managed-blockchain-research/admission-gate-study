#!/usr/bin/env python3.11
"""Per-run tables for the arrival-replay (11zz) and two-node (11aab) families."""
import glob,gzip,json,re,csv,collections
R='<path>/runs/'; O='<path>/'
def labels(od):
    c=collections.Counter(); a=collections.Counter()
    for f in glob.glob(od+'labels/labels_w*.jsonl.gz'):
        for l in gzip.open(f,'rt'):
            x=json.loads(l)
            if x.get('type')!='tx': continue
            o=(x.get('submit') or {}).get('outcome'); cl=x['label']
            if cl=='attack': a[o]+=1
            elif cl!='skipped':
                c[o]+=1
                if cl=='benign' and o=='ok' and x['submit']['latency_ms']<=30000: c['ok30']+=1
    return c,a
rows=[]
for d in sorted(glob.glob(R+'ARRIVAL_*')):
    if 'SMOKE' in d or not glob.glob(d+'/*/summary.json'): continue
    m=re.match(r'.*ARRIVAL_(\w+?)_(\w+?)_s(\d+)$',d); od=glob.glob(d+'/*/')[0]; c,a=labels(od); s=json.load(open(od+'summary.json'))
    off=sum(v for k,v in c.items() if k not in('ok30',))
    rows.append(dict(block=m.group(1),arm=m.group(2),seed=m.group(3),ordinary_offered=off,ordinary_not_sent=c['not-sent'],ordinary_ok=c['ok'],ordinary_ok30=c['ok30'],attack_n=sum(a.values()),attack_not_sent=a['not-sent'],node_death=int(s.get('time_to_node_death_s') is not None),oom=int(bool(s.get('oom_lines'))),verdict=s.get('verdict')))
w=csv.DictWriter(open(O+'acc11zz_per_run.csv','w',newline=''),fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows); print('zz',len(rows))
rows=[]
for d in sorted(glob.glob(R+'TWONODE_*')):
    if 'SMOKE' in d or d.split('/')[-1].startswith('_INFRAFAIL') or not glob.glob(d+'/*/summary.json'): continue
    m=re.match(r'.*TWONODE_(\w+?)_(\w+?)_s(\d+)$',d); od=glob.glob(d+'/*/')[0]; c,a=labels(od); s=json.load(open(od+'summary.json'))
    rs=[l.strip().split(',') for l in open(od+'nodeB_sample.csv') if l.strip()]
    ints=lambda i:[int(r[i]) for r in rs if len(r)>i and r[i].isdigit()]
    pa,pb,rb=ints(3),ints(4),ints(5)
    gb=0.0; gmax=0.0
    for l in gzip.open(od+'gc_B.log.gz','rt',errors='ignore'):
        mm=re.search(r'Pause (?:Young|Full|Remark|Cleanup).*?(\d+\.\d+)ms\s*$',l)
        if mm: gb+=float(mm.group(1)); gmax=max(gmax,float(mm.group(1)))
    rows.append(dict(block=m.group(1),arm=m.group(2),seed=m.group(3),ordinary_offered=sum(v for k,v in c.items() if k!='ok30'),ordinary_not_sent=c['not-sent'],ordinary_ok=c['ok'],attack_n=sum(a.values()),attack_not_sent=a['not-sent'],nodeA_gc_total_ms=s.get('gc_pause_total_ms'),nodeA_gc_max_ms=s.get('gc_pause_max_ms'),nodeB_gc_total_ms=round(gb,1),nodeB_gc_max_ms=gmax,nodeA_peak_rss_mb=s.get('peak_rss_mb'),nodeB_peak_rss_mb=round(max(rb)/1024,1) if rb else '',peak_pool_A=max(pa) if pa else '',peak_pool_B=max(pb) if pb else '',oom=int(bool(s.get('oom_lines'))),node_death=int(s.get('time_to_node_death_s') is not None),verdict=s.get('verdict')))
w=csv.DictWriter(open(O+'acc11aab_per_run.csv','w',newline=''),fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows); print('aab',len(rows))
