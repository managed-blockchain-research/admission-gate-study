#!/usr/bin/env python3.11
"""11uu analysis -> MORNING_REPORT_11uu.md (numbers only; absolute paths). Blocks: M mixed burst (Besu G1 512), Z ZGC 512, N Nethermind 2048, TS sustained attack, TP short pulse. Same-seed paired differences, t 95% CI over pair differences, per-pair values; exploratory."""
import glob, gzip, json, os, re, csv, math, statistics as S, collections, datetime
OUTD = '<path>/'
T = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776}
rows = []
for d in sorted(glob.glob('<path>/runs/LATFIRST_*_s667[0-9][0-9]')):
    if 'SMOKE' in d: continue
    m = re.match(r'.*LATFIRST_(LQ1|LMX|LRM)_(\w+?)_s(\d+)$', d)
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
    heavy_n = atk['n'] + cls['LA']['n']; heavy_ns = atk['not-sent'] + cls['LA']['not-sent']
    r.update(planned=planned, written=written, planned_no_record=planned - written, attack_n=atk['n'], attack_not_sent=atk['not-sent'], attack_block_rate=(atk['not-sent'] / atk['n'] if atk['n'] else None),
             benign_n=ben['n'], benign_not_sent=ben['not-sent'], benign_ok30=ben['ok'], benign_failed=ben['failed'], benign_unfinished=ben['unfinished'],
             heavy_offered=heavy_n, heavy_not_sent=heavy_ns, heavy_admitted=heavy_n - heavy_ns, heavy_admitted_MBps=round((heavy_n - heavy_ns) * 98372 / 1e6 / 120.0, 3), heavy_admit_share=((heavy_n - heavy_ns) / heavy_n if heavy_n else None),
             nonLA_ok30=cls['nonLA']['ok'], nonLA_not_sent=cls['nonLA']['not-sent'], LA_n=cls['LA']['n'], rej_LA=cls['LA']['not-sent'], LA_ok30=cls['LA']['ok'])
    r['oom_lines'] = int(s.get('oom_lines') or 0); r['node_death_s'] = s.get('time_to_node_death_s'); r['max_gap_s'] = s.get('max_block_gap_s_after_T0'); r['run_s'] = s.get('run_s'); r['peak_rss_mb'] = s.get('peak_rss_mb')
    r['gc_pause_ms'] = round(s.get('gc_pause_total_ms') or 0) if blk in ('I1', 'I3', 'I6', 'L1', 'MX') else None
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
with open(OUTD + 'acc11uu_per_run.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(sorted(rows, key=lambda r: (r['block'], r['arm'], r['seed'])))
ok = [r for r in rows if r['has_summary']]
out = ['# MORNING REPORT 11uu (generated %s)' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), '',
       'Numbers only. Registered in PREREG_UNIFIED_v1.md addendum 11uu (exploratory). Node node, shared non-exclusive. Receipt = within the connector 30 s limit. Same-seed pairs, t 95% CI over pair differences, per-pair values shown, no p-values. Chain-scan counts not used.', '']
sched = {'I1': 18, 'I3': 18, 'I6': 18, 'L1': 16, 'MX': 20, 'ZG': 20, 'NM': 16}
out.append('## Inventory (completed with summary / present)')
for b in sched: out.append('- block %s: ' % b + ', '.join('%s %d' % (a, sum(1 for r in ok if r['block'] == b and r['arm'] == a)) for a in sorted({r['arm'] for r in rows if r['block'] == b})) + ' (scheduled %d)' % sched[b])
out.append('- runs without summary (apparatus failure, NOT replaced): ' + (', '.join('%s/%s/%d' % (r['block'], r['arm'], r['seed']) for r in rows if not r['has_summary']) or 'none'))
def mean(v): v = [x for x in v if x is not None]; return S.mean(v) if v else None
PAIRS = {b: [('SizeStatic', 'none'), ('BudgetR125', 'none'), ('BudgetR250', 'none'), ('BudgetR500', 'none'), ('SizeFixedP20', 'none'), ('BudgetAdapt500', 'none'), ('BudgetR250', 'SizeFixedP20'), ('BudgetR250', 'SizeStatic'), ('BudgetR500', 'SizeStatic'), ('BudgetR125', 'SizeStatic'), ('BudgetAdapt500', 'BudgetR500'), ('BudgetAdapt500', 'SizeStatic')] for b in ('I1', 'I3', 'I6', 'L1', 'MX', 'ZG', 'NM')}
MET = ['benign_ok30', 'nonLA_ok30', 'benign_not_sent', 'rej_LA', 'attack_block_rate', 'heavy_admitted', 'heavy_admitted_MBps', 'gc_pause_ms']
for b in sched:
    rr = [r for r in ok if r['block'] == b]
    if not rr: continue
    out += ['', '## Block %s' % b, '', '| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for a in sorted({r['arm'] for r in rr}):
        v = [r for r in rr if r['arm'] == a]
        fm = lambda k, f='%.0f': (f % mean([r.get(k) for r in v])) if mean([r.get(k) for r in v]) is not None else 'n/a'
        out.append('| %s | %d | %s / %s | %s | %s %s | %s | %s %s | %s | %s | %s | %d | %d | %d | %s | %s | %s |' % (a, len(v), fm('heavy_admitted'), fm('heavy_admitted_MBps', '%.3f'), fm('attack_block_rate', '%.3f'), fm('benign_not_sent'), [r['benign_not_sent'] for r in v], fm('rej_LA'), fm('benign_ok30'), [r['benign_ok30'] for r in v], fm('benign_failed'), fm('benign_unfinished'), fm('planned_no_record'),
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
out += ['', '## Caveats fixed in advance', '- tau 65,604 B post-hoc; Budget = heavy-byte token bucket (C 200 KB; R fixed 125/250/500 KB/s or adaptive 500 KB/s x (1 - 0.75 grad(u_t)), tokens consumed only by heavy transactions; small transactions always pass) - a class-selective token-bucket policer, prior art; attack intensity blocks I1/I3/I6 use 1/3/6 burst workers (about 400/1,200/2,400 heavy transactions) so BENIGN attempts also differ between blocks (22,800 to 24,800): compare arms only within a block; L1 = one look-alike worker (about 400, 0.33 MB/s), no attack; MX = 2 attack workers + 1 look-alike worker; GC pause only for G1 blocks; ZGC/NM survival and OOM-exception lines are descriptive; shared node node.']
open(OUTD + 'MORNING_REPORT_11uu.md', 'w').write('\n'.join(out) + '\n'); print('wrote MORNING_REPORT_11uu.md,', len(ok), 'runs with summary of', len(rows))
