#!/usr/bin/env python3.11
"""Arrival pattern, sender rates, calldata size and inclusion delay of one day of public Ethereum mainnet pending transactions (Flashbots Mempool Dumpster, CC0; metadata CSV, downloaded read-only; nothing was sent to any network). usage: analyze_mempool_day.py <csv> <out.md>"""
import sys,pandas as pd,numpy as np
csv,out=sys.argv[1],sys.argv[2]
d=pd.read_csv(csv,usecols=['timestamp_ms','from','nonce','gas','gas_price','data_size','included_at_block_height','inclusion_delay_ms'])
n=len(d); d=d.sort_values('timestamp_ms'); t=d['timestamp_ms'].values/1000.0
span=t[-1]-t[0]; per_s=np.bincount((t-t[0]).astype(int)); ia=np.diff(t)
L=['# Public mempool, one day (Flashbots Mempool Dumpster, %s; written 2026-11-24)\n'%csv.split('/')[-1],'Read-only download of the public metadata file; nothing was sent to any network.\n']
L.append('## Arrivals\n- transactions: %d over %.0f s (%.2f tx/s mean)'%(n,span,n/span))
L.append('- per-second count: mean %.2f, p50 %.0f, p95 %.0f, p99 %.0f, max %d; index of dispersion (variance/mean) %.2f (Poisson = 1)'%(per_s.mean(),np.percentile(per_s,50),np.percentile(per_s,95),np.percentile(per_s,99),per_s.max(),per_s.var()/per_s.mean()))
L.append('- inter-arrival time (ms): p50 %.0f, p95 %.0f, p99 %.0f, p99.9 %.0f'%tuple(np.percentile(ia*1000,[50,95,99,99.9])))
s=d.groupby('from').size().sort_values(ascending=False)
L.append('\n## Senders\n- distinct senders: %d; transactions per sender: median %.0f, p90 %.0f, p99 %.0f, max %d'%(len(s),s.median(),s.quantile(.9),s.quantile(.99),s.max()))
L.append('- the busiest 10 senders send %.1f%% of all transactions; the busiest 1%% of senders send %.1f%%'%(100*s.iloc[:10].sum()/n,100*s.iloc[:max(1,len(s)//100)].sum()/n))
ds=d['data_size'].values
L.append('\n## Calldata size (bytes), pending transactions\n- median %.0f, p90 %.0f, p99 %.0f, p99.9 %.0f, max %d'%(*np.percentile(ds,[50,90,99,99.9]),ds.max()))
for th in (1000,10000,32000,65604,100000): L.append('- share above %d B: %.5f (%d)'%(th,(ds>th).mean(),(ds>th).sum()))
L.append('- zero-calldata share: %.3f'%((ds==0).mean()))
inc=d[d['inclusion_delay_ms'].notna()&(d['inclusion_delay_ms']>0)]
L.append('\n## Inclusion delay (first seen to block timestamp), transactions that were later included\n- n %d (%.1f%% of the file); delay (s): p50 %.1f, p95 %.1f, p99 %.1f, p99.9 %.1f'%(len(inc),100*len(inc)/n,*np.percentile(inc['inclusion_delay_ms']/1000.0,[50,95,99,99.9])))
big=d[ds>65604]
L.append('\n## Heavy transactions (> 65,604 B)\n- count %d (%.4f%% of transactions); per-hour counts: median %.0f, max %d; distinct senders %d'%(len(big),100*len(big)/n,pd.Series(((big['timestamp_ms']/1000.0-t[0])//3600).astype(int)).value_counts().median(),pd.Series(((big['timestamp_ms']/1000.0-t[0])//3600).astype(int)).value_counts().max(),big['from'].nunique()))
L.append('\n## Reading rules\nDescriptive, one day, public pending transactions seen by the dataset sources (a transaction seen by several sources is listed once at its first-seen time). It describes arrival timing, senders and sizes of ordinary public traffic; it does not describe attack traffic or private order flow.\n')
open(out,'w').write('\n'.join(L)+'\n'); print('\n'.join(L))
