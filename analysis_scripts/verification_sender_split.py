#!/usr/bin/env python3.11
"""Independent three-way reconciliation for 11gg and 11hh (a different code path from denominator_ledger.py / acc11*_analysis.py):
(1) label records (labels_w*.jsonl.gz): benign ok / failed / not-sent, attack not-sent; (2) tierstats (tierstats/w*.json): class lists S/M/L (flag 1 = receipt), A (attack), R (rejections, no label);
(3) service counters (raac_report.json ai_counters). Identities checked per run: tierstats R == label benign not-sent + attack not-sent == service rejects (arms with a service); tierstats benign receipts == label benign ok;
tierstats benign failures (flag 0 in S/M/L) == label benign failed + unfinished. Plus G1: summary gc_pause_total_ms vs the sum of 'Pause' lines in gc.log.gz (G1 log is not rotated)."""
import glob, gzip, json, os, re
bad = 0; n = 0
for pat in ('ACC11MM_*_s6[23][0-9][0-9][0-9]',):
    for d in sorted(glob.glob('runs/' + pat)):
        if 'SMOKE' in d: continue
        od = [x for x in glob.glob(d + '/*/') if os.path.exists(x + 'summary.json')]
        if not od: continue
        od = od[0]; n += 1; name = d.split('ACC11')[1]
        # labels
        L = dict(b_ok=0, b_failed=0, b_unf=0, b_ns=0, a_ns=0, a_ok=0)
        for f in glob.glob(od + 'labels/labels_w*.jsonl.gz'):
            for line in gzip.open(f, 'rt'):
                r = json.loads(line)
                if r.get('type') != 'tx': continue
                sb = r.get('submit'); oc = sb['outcome'] if sb else 'no-outcome'
                if r['label'] == 'benign':
                    if oc == 'ok': L['b_ok'] += 1
                    elif oc == 'failed': L['b_failed'] += 1
                    elif oc == 'not-sent': L['b_ns'] += 1
                    else: L['b_unf'] += 1
                else:
                    if oc == 'not-sent': L['a_ns'] += 1
                    if oc == 'ok': L['a_ok'] += 1
        # tierstats
        T = dict(ok=0, fail=0, R=0, A_ok=0)
        for f in glob.glob(od + 'tierstats/w*.json'):
            st = json.load(open(f))['stats']
            for cls in ('S', 'M', 'L'):
                for t, l, ok in st.get(cls, []):
                    if ok == 1: T['ok'] += 1
                    else: T['fail'] += 1
            T['R'] += len(st.get('R', [])); T['A_ok'] += sum(1 for t, l, ok in st.get('A', []) if ok == 1)
        # service
        try:
            c = json.load(open(od + 'raac_report.json')).get('ai_counters.json', {}).get('counters', {}); svc = c.get('reject')
        except Exception: svc = None
        problems = []
        if T['ok'] != L['b_ok']: problems.append('benign receipts tierstats %d != labels %d' % (T['ok'], L['b_ok']))
        if T['fail'] != L['b_failed'] + L['b_unf']: problems.append('benign non-receipt tierstats %d != labels failed+unfinished %d' % (T['fail'], L['b_failed'] + L['b_unf']))
        if T['R'] != L['b_ns'] + L['a_ns']: problems.append('tierstats R %d != labels not-sent %d' % (T['R'], L['b_ns'] + L['a_ns']))
        if svc is not None and svc != T['R']: problems.append('service rejects %s != tierstats R %d' % (svc, T['R']))
        # G1 pause sum
        if any(x in d for x in ('MM_X1_', 'MM_X2_', 'MM_X3_', 'MM_X4_')):
            s = json.load(open(od + 'summary.json')); tot = 0.0
            gz = od + 'gc.log.gz'
            for line in gzip.open(gz, 'rt', errors='ignore'):
                m = re.search(r'Pause (?:Young|Full|Remark|Cleanup)[^\n]*? (\d+\.\d+)ms\s*$', line)
                if m: tot += float(m.group(1))
            if abs(tot - (s.get('gc_pause_total_ms') or 0)) > 0.02 * max(1, s.get('gc_pause_total_ms') or 0): problems.append('G1 pause log %.0f vs summary %.0f' % (tot, s.get('gc_pause_total_ms')))
        if problems: bad += 1; print('MISMATCH', name, problems)
print('runs checked:', n, '| runs with any mismatch:', bad)
