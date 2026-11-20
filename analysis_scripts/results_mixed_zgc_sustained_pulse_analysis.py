#!/usr/bin/env python3.11
"""11jj analysis -> MORNING_REPORT_11jj.md (numbers only; absolute paths). Blocks: M mixed burst (Besu G1 512), Z ZGC 512, N Nethermind 2048, TS sustained attack, TP short pulse. Same-seed paired differences, t 95% CI over pair differences, per-pair values; exploratory."""
import glob, gzip, json, os, re, csv, math, statistics as S, collections, datetime
OUTD = 'analysis/'
T = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776}
rows = []
for d in sorted(glob.glob('runs/ACC11JJ_*_s6[23][0-9][0-9][0-9]')):
    if 'SMOKE' in d: continue
    m = re.match(r'.*ACC11JJ_(M|Z|N|TS|TP)_(\w+?)_s(\d+)$', d)
    if not m: continue
    blk, arm, seed = m.group(1), m.group(2), int(m.group(3))
    od = [x for x in glob.glob(d + '/*/') if os.path.exists(x + 'summary.json')]
    r = dict(block=blk, arm=arm, seed=seed, has_summary=bool(od))
    if not od: rows.append(r); continue
    od = od[0]; s = json.load(open(od + 'summary.json')); T0 = s['T0']; END = s['END']
    planned = 0; written = 0; atk = collections.Counter(); cls = collections.defaultdict(collections.Counter)
    for f in glob.glob(od + 'labels/labels_w*.jsonl.gz'):
        for line in gzip.open(f, 'rt'):
            x = json.loads(line)
            if x.get('type') == 'header': planned += x['max_attempts']; continue
            if x.get('type') != 'tx': continue
            written += 1; sb = x.get('submit'); oc = sb['outcome'] if sb else 'no-outcome'
            if x['label'] == 'attack': atk['n'] += 1; atk[oc] += 1; continue
            k = 'LA' if (x['label'] == 'lookalike' or x.get('cls') == 'LA') else 'nonLA'
            cls[k]['n'] += 1; cls[k][oc] += 1
    ben = collections.Counter(); ben.update(cls['LA']); ben.update(cls['nonLA'])
    r.update(planned=planned, written=written, planned_no_record=planned - written, attack_n=atk['n'], attack_not_sent=atk['not-sent'], attack_block_rate=(atk['not-sent'] / atk['n'] if atk['n'] else None),
             benign_n=ben['n'], benign_not_sent=ben['not-sent'], benign_ok30=ben['ok'], benign_failed=ben['failed'], benign_unfinished=ben['unfinished'],
             nonLA_ok30=cls['nonLA']['ok'], nonLA_not_sent=cls['nonLA']['not-sent'], LA_n=cls['LA']['n'], rej_LA=cls['LA']['not-sent'], LA_ok30=cls['LA']['ok'])
    r['oom_lines'] = int(s.get('oom_lines') or 0); r['node_death_s'] = s.get('time_to_node_death_s'); r['max_gap_s'] = s.get('max_block_gap_s_after_T0'); r['run_s'] = s.get('run_s'); r['peak_rss_mb'] = s.get('peak_rss_mb')
    r['gc_pause_ms'] = round(s.get('gc_pause_total_ms') or 0) if blk in ('M', 'TS', 'TP') else None
    try:
        at = open(od + 'assert.txt').read(); r['assert_fail_lines'] = sum(1 for l in at.split('\n') if l.startswith('FAIL')); r['assert_pass_lines'] = sum(1 for l in at.split('\n') if l.startswith('PASS'))
    except Exception: r['assert_fail_lines'] = None
    try:
        txt = open(od + 'oom_lines.txt').read(); r['block_processing_failed'] = int('Processing block failed' in txt)
    except Exception: r['block_processing_failed'] = 0
    try:
        ai = json.load(open(od + 'raac_report.json')).get('ai_counters.json', {}).get('counters', {})
        r.update(svc_total=ai.get('total'), svc_flagged=ai.get('flagged'), svc_rej=ai.get('reject'), svc_rej_flagged=ai.get('rejected_flagged'), svc_rej_unflagged=ai.get('rejected_unflagged'), svc_stale=ai.get('decisions_while_stale'))
    except Exception: pass
    rows.append(r)
keys = []
for r in rows:
    for k in r:
        if k not in keys: keys.append(k)
with open(OUTD + 'acc11jj_per_run.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(sorted(rows, key=lambda r: (r['block'], r['arm'], r['seed'])))
ok = [r for r in rows if r['has_summary']]
out = ['# MORNING REPORT 11jj (generated %s)' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), '',
       'Numbers only. Registered in PREREG_UNIFIED_v1.md addendum 11jj (exploratory). Node cpu05, shared non-exclusive. Receipt = within the connector 30 s limit. Same-seed pairs, t 95% CI over pair differences, per-pair values shown, no p-values. Chain-scan counts not used.', '']
sched = {'M': 24, 'Z': 20, 'N': 20, 'TS': 15, 'TP': 15}
out.append('## Inventory (completed with summary / present)')
for b in sched: out.append('- block %s: ' % b + ', '.join('%s %d' % (a, sum(1 for r in ok if r['block'] == b and r['arm'] == a)) for a in sorted({r['arm'] for r in rows if r['block'] == b})) + ' (scheduled %d)' % sched[b])
out.append('- runs without summary (apparatus failure, NOT replaced): ' + (', '.join('%s/%s/%d' % (r['block'], r['arm'], r['seed']) for r in rows if not r['has_summary']) or 'none'))
def mean(v): v = [x for x in v if x is not None]; return S.mean(v) if v else None
PAIRS = {'M': [('OracleBlock', 'none'), ('PressureOnly', 'none'), ('SizeStatic', 'none'), ('SizeGraded', 'none'), ('SizeStatic', 'OracleBlock'), ('SizeStatic', 'PressureOnly'), ('OracleBlock', 'PressureOnly'), ('RandShed48', 'none'), ('SizeStatic', 'RandShed48'), ('OracleBlock', 'RandShed48')],
         'Z': [('OracleBlock', 'none'), ('PressureOnly', 'none'), ('SizeStatic', 'none'), ('LearnedScore', 'none'), ('SizeStatic', 'OracleBlock'), ('SizeStatic', 'PressureOnly')],
         'N': [('OracleBlock', 'none'), ('PressureOnly', 'none'), ('SizeStatic', 'none'), ('SizeStatic', 'OracleBlock'), ('SizeStatic', 'PressureOnly')],
         'TS': [('SizeStatic', 'none'), ('SizeGraded', 'none'), ('SizeSticky', 'none'), ('PressureOnly', 'none'), ('SizeSticky', 'SizeGraded'), ('SizeSticky', 'SizeStatic'), ('SizeStatic', 'SizeGraded')],
         'TP': [('SizeStatic', 'none'), ('SizeGraded', 'none'), ('SizeSticky', 'none'), ('PressureOnly', 'none'), ('SizeSticky', 'SizeGraded'), ('SizeSticky', 'SizeStatic'), ('SizeStatic', 'SizeGraded')]}
MET = ['benign_ok30', 'nonLA_ok30', 'benign_not_sent', 'rej_LA', 'attack_block_rate', 'gc_pause_ms']
for b in sched:
    rr = [r for r in ok if r['block'] == b]
    if not rr: continue
    out += ['', '## Block %s' % b, '', '| arm | n | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for a in sorted({r['arm'] for r in rr}):
        v = [r for r in rr if r['arm'] == a]
        fm = lambda k, f='%.0f': (f % mean([r.get(k) for r in v])) if mean([r.get(k) for r in v]) is not None else 'n/a'
        out.append('| %s | %d | %s | %s %s | %s | %s %s | %s | %s | %s | %d | %d | %d | %s | %s | %s |' % (a, len(v), fm('attack_block_rate', '%.3f'), fm('benign_not_sent'), [r['benign_not_sent'] for r in v], fm('rej_LA'), fm('benign_ok30'), [r['benign_ok30'] for r in v], fm('benign_failed'), fm('benign_unfinished'), fm('planned_no_record'),
                   sum(1 for r in v if r['oom_lines']), sum(1 for r in v if r['node_death_s'] is not None), sum(r.get('block_processing_failed', 0) for r in v), fm('max_gap_s'), fm('gc_pause_ms'), fm('svc_stale')))
    out += ['', '### Block %s paired differences (A - B), t 95%% CI [per-pair]' % b, '']
    by = {(r['arm'], r['seed']): r for r in rr}
    for a, bb in PAIRS[b]:
        seeds = sorted({s for (x, s) in by if x == a} & {s for (x, s) in by if x == bb})
        if len(seeds) < 2: continue
        for met in MET:
            try: dd = [by[(a, s)][met] - by[(bb, s)][met] for s in seeds]
            except Exception: continue
            if any(x is None for x in dd): continue
            mu = S.mean(dd); h = T[len(dd) - 1] * S.stdev(dd) / math.sqrt(len(dd)); fmt = '%.3f' if 'rate' in met else '%.0f'
            out.append('- %s - %s | %s | %s [%s, %s] | %s' % (a, bb, met, fmt % mu, fmt % (mu - h), fmt % (mu + h), [round(x, 3) if 'rate' in met else round(x) for x in dd]))
out.append('')
out.append('Provisioning/assertion check (assert.txt FAIL lines per run; PASS lines include heap-limit enforcement): ' + ', '.join('%s/%s/%d: fail=%s pass=%s' % (r['block'], r['arm'], r['seed'], r.get('assert_fail_lines'), r.get('assert_pass_lines')) for r in ok if r.get('assert_fail_lines')))
out += ['', '## Caveats fixed in advance', '- threshold 65,604 B post-hoc; SizeStatic/SizeGraded/SizeSticky differ in intensity as well as feedback/hold; SizeSticky = SizeGraded with a 30 s sliding-maximum pressure hold (30 s chosen a priori); mixed block = 2 attack workers (800) + 1 look-alike worker (400) in the same window; sustained block = 2,400 attack tx, pulse block = 300 attack tx (different attack volume from the 1,200 baseline); GC pause only for G1 blocks; ZGC/NM survival and OOM-exception lines are descriptive; NM OOM exceptions at END+5-20 s coincide with post-run scans; shared node.']
open(OUTD + 'MORNING_REPORT_11jj.md', 'w').write('\n'.join(out) + '\n'); print('wrote MORNING_REPORT_11jj.md,', len(ok), 'runs with summary of', len(rows))
