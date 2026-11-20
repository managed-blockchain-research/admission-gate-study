#!/usr/bin/env python3.11
"""Cost-benefit frontier and benign-harm breakdown (offline, from stored labels + per-run CSVs of 11jj and 11kk; numbers only).
(1) frontier: per block/arm mean over seeds of attack block rate, benign rejected (count and share of benign attempts), look-alike rejected share, benign receipts and the paired gain vs none (same seed).
(2) benign harm: for runs of arms that can reject benign transactions (blanket / graded / random), benign not-sent split by transaction class (SL, SH, M, L), by phase (before / during / after the 60-180 s window, by scheduled time) and by sending worker (spread = max/mean over the 27 benign workers)."""
import glob, gzip, json, os, re, csv, collections, statistics as S
D = './'
OUT = D + 'analysis/20261118_access_resub/'
def num(x):
    try: return float(x)
    except Exception: return None
rows = []
for f, tag in ((OUT + 'acc11jj_per_run.csv', '11jj'), (OUT + 'acc11kk_per_run.csv', '11kk')):
    for r in csv.DictReader(open(f)):
        if r.get('has_summary') == 'True': r['exp'] = tag; rows.append(r)
G1 = {'11jj': ('M', 'TS', 'TP'), '11kk': ('I1', 'I3', 'I6', 'L1', 'MX')}
out = ['# Cost-benefit frontier and benign-harm breakdown (offline; 11jj + 11kk; Besu G1 512 MB blocks only; numbers only)', '',
       'Rows: block / arm, mean over seeds (n shown). attack block = share of attack transactions rejected; benign rej = benign (non-heavy, non-look-alike) requests rejected by the gate; LA rej = look-alike (legitimate heavy) rejected share; receipts = benign receipts within 30 s; gain = same-seed paired difference vs none (mean).', '',
       '| exp | block | arm | n | attack block | benign rej (count) | benign rej share | LA rej share | receipts | gain vs none |', '|---|---|---|---|---|---|---|---|---|---|']
key = lambda r: (r['exp'], r['block'], r['arm'])
by = collections.defaultdict(list)
for r in rows:
    if r['block'] in G1[r['exp']]: by[key(r)].append(r)
none = {(k[0], k[1], r['seed']): num(r['benign_ok30']) for k, v in by.items() if k[2] == 'none' for r in v}
for k in sorted(by):
    v = by[k]; m = lambda c: S.mean([num(r[c]) for r in v if num(r.get(c)) is not None]) if any(num(r.get(c)) is not None for r in v) else None
    nb = m('benign_n'); bns = m('benign_not_sent'); la = m('LA_n') if 'LA_n' in v[0] else None
    lar = m('rej_LA'); lan = m('LA_n')
    gain = [num(r['benign_ok30']) - none[(k[0], k[1], r['seed'])] for r in v if (k[0], k[1], r['seed']) in none and num(r['benign_ok30']) is not None]
    f = lambda x, p='%.0f': (p % x) if x is not None else 'n/a'
    ben_rej = (bns - lar) if (bns is not None and lar is not None) else bns
    out.append('| %s | %s | %s | %d | %s | %s | %s | %s | %s | %s |' % (k[0], k[1], k[2], len(v), f(m('attack_block_rate'), '%.3f'), f(ben_rej), f((ben_rej / nb) if (nb and ben_rej is not None) else None, '%.4f'), f((lar / lan) if (lan and lar is not None) else None, '%.3f'), f(m('benign_ok30')), f(S.mean(gain)) if gain else 'n/a'))
# benign harm from labels
blanket = ('PressureOnly', 'SizeGraded', 'RandShed48', 'SizeSticky', 'SizeFixedP20')
res = collections.defaultdict(lambda: collections.Counter()); wk = collections.defaultdict(lambda: collections.Counter()); totals = collections.defaultdict(lambda: collections.Counter())
for tag, pat in (('11jj', 'ACC11JJ_*'), ('11kk', 'ACC11KK_*')):
    for d in sorted(glob.glob(D + 'runs/' + pat + '_s6[23][0-9][0-9][0-9]')):
        if 'SMOKE' in d: continue
        m = re.match(r'.*ACC11(?:JJ|KK)_(\w+?)_(\w+?)_s(\d+)$', d)
        if not m or m.group(1) not in G1[tag] or m.group(2) not in blanket: continue
        for f in glob.glob(d + '/*/labels/labels_w*.jsonl.gz'):
            for line in gzip.open(f, 'rt'):
                x = json.loads(line)
                if x.get('type') != 'tx' or x['label'] != 'benign': continue
                sb = x.get('submit'); ns = bool(sb and sb['outcome'] == 'not-sent')
                t = x.get('t_sched_ms', 0) / 1000.0; ph = 'before' if t < 60 else ('during' if t < 180 else 'after')
                kk = (tag, m.group(1), m.group(2))
                totals[kk][('cls', x.get('cls'))] += 1; totals[kk][('ph', ph)] += 1; totals[kk][('wk', x['worker'])] += 1
                if ns: res[kk][('cls', x.get('cls'))] += 1; res[kk][('ph', ph)] += 1; res[kk][('wk', x['worker'])] += 1
out += ['', '## Benign harm by transaction class, phase and sender (arms that can reject benign requests; counts pooled over seeds)', '',
        '| exp | block | arm | benign rejected | by class (rej / attempts, %) | by phase (before / during / after the 60-180 s window) | rejection share by worker: max / mean (27 benign workers) |', '|---|---|---|---|---|---|---|']
for kk in sorted(res):
    c = res[kk]; t = totals[kk]; tot = sum(v for (a, b), v in c.items() if a == 'cls')
    cl = ', '.join('%s %d/%d (%.2f%%)' % (n, c[('cls', n)], t[('cls', n)], 100.0 * c[('cls', n)] / t[('cls', n)]) for n in ('SL', 'SH', 'M', 'L') if t[('cls', n)])
    ph = ' / '.join('%d (%.2f%%)' % (c[('ph', p)], 100.0 * c[('ph', p)] / t[('ph', p)] if t[('ph', p)] else 0) for p in ('before', 'during', 'after'))
    ws = [(c[('wk', w)] / t[('wk', w)]) for (a, w) in list(t) if a == 'wk' and t[('wk', w)] and w < 27]
    wr = ('%.3f / %.3f' % (max(ws), S.mean(ws))) if ws and S.mean(ws) > 0 else 'n/a'
    out.append('| %s | %s | %s | %d | %s | %s | %s |' % (kk[0], kk[1], kk[2], tot, cl, ph, wr))
out += ['', 'Notes: phases use the scheduled time of the request; before = 0-60 s, during = 60-180 s, after = 180 s to the end of the load. Arms that reject only heavy transactions (none, SizeStatic, OracleBlock, Budget*) reject no benign request and are not listed. Look-alike rejections are shown in the first table (LA rej share) and are not counted as benign here.']
open(OUT + 'frontier_fairness.md', 'w').write('\n'.join(out) + '\n'); print('wrote frontier_fairness.md', len(out), 'lines')
