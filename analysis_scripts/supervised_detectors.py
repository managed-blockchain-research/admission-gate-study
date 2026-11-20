#!/usr/bin/env python3.11
"""Offline, post-hoc supervised-detector comparison + feature ablation (reviewer item). No cluster use, no existing file modified.
Data/feature definitions reused from detector_refit.py / unseen_replay_detectors.py.
DATA FACT: the stored table has NO attack rows in role 'train' (attack only in calibration (7200) and holdout (7200), 30 price tiers each,
class-deterministic: 1 feature vector per tier-price). Therefore, 'attack from the training role' is replaced by:
  design A: train on calibration-role attack, evaluate attack on holdout-role attack (same 30 price tiers -> tier-memorisation possible)
  design B: train on calibration-role attack from EVEN price tiers, evaluate on holdout-role attack from ODD price tiers (unseen tiers)
Benign training = benign TRAIN-role records (random 60k subsample for the supervised models; IF uses all benign train, as detector_refit.py).
Look-alikes (rollup 'lookalike', 'lookalike_hard') are NEVER in training. Threshold = 99th pct of benign calibration scores (FPR<=1% target)."""
import gzip, csv, sys, numpy as np, warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import IsolationForest, RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
rows = []
with gzip.open('./impl/raac2/diag/all_scored.csv.gz', 'rt') as f:
    for r in csv.DictReader(f): rows.append((float(r['gas_price']), float(r['gas_limit']), float(r['wei_value']), float(r['bytecode_size']), float(r['opcode_count']), r['grp'], r['role'], r['label']))
A = np.array([r[:5] for r in rows]); grp = np.array([r[5] for r in rows]); role = np.array([r[6] for r in rows]); lab = np.array([r[7] for r in rows])
def feats(gp, gl, wv, bs, oc): return {'vcr_log': np.log1p(wv) / (np.log1p(oc) + 1), 'ed_log': np.log1p(wv) / (np.log1p(gl) + 1), 'ri': gl * bs / 1e9, 'gas_price': gp, 'gas_limit': gl, 'bytecode_size': bs}
F = feats(*A.T)
tiers = np.sort(np.unique(A[grp == 'attack'][:, 0])); NT = len(tiers); tier_of = np.searchsorted(tiers, A[:, 0]); tier_of = np.clip(tier_of, 0, NT - 1)
isben = np.char.startswith(grp, 'benign'); ev = np.isin(role, ['calibration', 'holdout'])
ben_tr = isben & (role == 'train'); ben_cal = isben & (role == 'calibration'); ben_ho = isben & (role == 'holdout'); ben_ev = ben_cal | ben_ho
atk_cal = (grp == 'attack') & (role == 'calibration'); atk_ho = (grp == 'attack') & (role == 'holdout')
roll = (grp == 'lookalike') & ev; hard = (grp == 'lookalike_hard') & ev
rng = np.random.default_rng(20261119)
sub_b = rng.choice(np.where(ben_tr)[0], 60000, replace=False)
sizes = [3000, 6000, 12000, 24000, 48000, 65000, 70000, 98372]
G = np.array([(g, 8e6, 0.0, float(s), float(round(s * 129234 / 98372))) for s in sizes for g in tiers]); GF = feats(*G.T); gsize = G[:, 3]; gtier = np.tile(np.arange(NT), len(sizes))
sets = {'frozen6': ['vcr_log', 'ed_log', 'ri', 'gas_price', 'gas_limit', 'bytecode_size'],
        'wire-only5 (no vcr_log)': ['ed_log', 'ri', 'gas_price', 'gas_limit', 'bytecode_size'],
        'payload (bytecode_size)': ['bytecode_size'], 'bytecode_size+gas_limit': ['bytecode_size', 'gas_limit'], 'gas-only (gas_price,gas_limit)': ['gas_price', 'gas_limit']}
for c in sets['frozen6']: sets['single: ' + c] = [c]
def mk(name):
    if name == 'LogReg': return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight='balanced', random_state=1))
    if name == 'RandForest': return RandomForestClassifier(n_estimators=50, max_depth=6, min_samples_leaf=5, class_weight='balanced', random_state=1, n_jobs=4)
    if name == 'GradBoost': return GradientBoostingClassifier(n_estimators=100, max_depth=3, random_state=1)
B = 2000; brng = np.random.default_rng(7)
BI = brng.integers(0, NT, (B, NT))
def tier_mean(v, mask): # per-tier mean of v over rows in mask
    t = tier_of[mask]; out = np.full(NT, np.nan)
    for k in range(NT):
        s = t == k
        if s.any(): out[k] = v[s].mean()
    return out
def ci(per_tier, valid=None):
    ok = ~np.isnan(per_tier); pt = per_tier[ok]
    pt0 = pt.mean(); bs = np.array([pt[brng.integers(0, len(pt), len(pt))].mean() for _ in range(B)])
    return pt0, np.quantile(bs, .025), np.quantile(bs, .975)
def auc_contrib(pos, negs_sorted):
    l = np.searchsorted(negs_sorted, pos, 'left'); r = np.searchsorted(negs_sorted, pos, 'right'); return (l + 0.5 * (r - l)) / len(negs_sorted)
def fm(t): return '%.3f [%.3f,%.3f]' % t
def evaluate(score_fn, XS, XG, atk_eval, tag):
    s_all = score_fn(XS); neg = s_all[ben_ev]; nsort = np.sort(neg); thr = float(np.quantile(s_all[ben_cal], 0.99))
    out = {'thr': thr, 'fpr_cal': float((s_all[ben_cal] > thr).mean()), 'fpr_ho': float((s_all[ben_ho] > thr).mean())}
    sa = s_all[atk_eval]; ta = tier_of[atk_eval]
    def per_tier(v):
        o = np.full(NT, np.nan)
        for k in range(NT):
            s = ta == k
            if s.any(): o[k] = v[s].mean()
        return o
    out['auc_ben'] = ci(per_tier(auc_contrib(sa, nsort))); out['tpr'] = ci(per_tier((sa > thr).astype(float)))
    for nm, m in (('roll', roll), ('hard', hard)):
        sl = s_all[m]; lsort = np.sort(sl)
        out['auc_' + nm] = ci(per_tier(auc_contrib(sa, lsort)))   # P(attack score > lookalike score)
        out['flag_' + nm] = float((sl > thr).mean())
    flag = score_fn(XG) > thr; out['per_size'] = [float(flag[gsize == s].mean()) for s in sizes]
    ev_tiers = np.unique(ta)
    def bw(wt): return float((gsize * flag * wt[gtier]).sum() / (gsize * wt[gtier]).sum())
    base = np.zeros(NT); base[ev_tiers] = 1; v = bw(base)
    bsr = [bw(np.bincount(brng.choice(ev_tiers, len(ev_tiers)), minlength=NT).astype(float)) for _ in range(B)]
    out['bw'] = (v, float(np.quantile(bsr, .025)), float(np.quantile(bsr, .975)))
    return out
def run(design):
    if design == 'A': tr_atk = atk_cal; atk_eval = atk_ho; sel = np.ones(NT, bool); evsel = None
    else:
        tr_atk = atk_cal & (tier_of % 2 == 0); atk_eval = atk_ho & (tier_of % 2 == 1)
    res = []
    for sname, cols in sets.items():
        X = np.column_stack([F[c] for c in cols]); XG = np.column_stack([GF[c] for c in cols])
        trI = np.concatenate([sub_b, np.where(tr_atk)[0]]); y = np.concatenate([np.zeros(len(sub_b)), np.ones(tr_atk.sum())])
        # IF: benign train only
        m = IsolationForest(n_estimators=200, contamination=0.01, random_state=20261016, n_jobs=4).fit(X[ben_tr])
        res.append((sname, 'IsolationForest(benign-only)', evaluate(lambda Z: -m.decision_function(Z), X, XG, atk_eval, design)))
        for mn in ('LogReg', 'RandForest', 'GradBoost'):
            clf = mk(mn).fit(X[trI], y)
            res.append((sname, mn, evaluate(lambda Z: clf.predict_proba(Z)[:, 1], X, XG, atk_eval, design)))
    # simple rules (score = bytecode_size; flag bs > thr)
    bs = A[:, 3]; X = bs[:, None]; XG = GF['bytecode_size'][:, None]
    thr_cal = float(np.quantile(bs[ben_cal], 0.99)); thr_post = (float(bs[ben_ev].max()) + float(A[tr_atk][:, 3].min())) / 2
    for nm, th in (('rule bs>%.0f (benign-cal 99th pct, NO attack data)' % thr_cal, thr_cal), ('rule bs>%.0f (midpoint benign-max/attack-min, POST-HOC uses attack data)' % thr_post, thr_post), ('rule bs>=80000 (fixed 80KB, POST-HOC)', 79999.5)):
        res.append(('payload (bytecode_size)', nm, evaluate_rule(th, X, XG, atk_eval)))
    return res
def evaluate_rule(th, X, XG, atk_eval):
    # reuse evaluate with a score that is a step function; threshold passed explicitly by monkeypatch-free approach
    s_all = X[:, 0]; out = {'thr': th, 'fpr_cal': float((s_all[ben_cal] > th).mean()), 'fpr_ho': float((s_all[ben_ho] > th).mean())}
    neg = np.sort(s_all[ben_ev]); sa = s_all[atk_eval]; ta = tier_of[atk_eval]
    def per_tier(v):
        o = np.full(NT, np.nan)
        for k in range(NT):
            s = ta == k
            if s.any(): o[k] = v[s].mean()
        return o
    out['auc_ben'] = ci(per_tier(auc_contrib(sa, neg))); out['tpr'] = ci(per_tier((sa > th).astype(float)))
    for nm, m in (('roll', roll), ('hard', hard)):
        sl = s_all[m]; out['auc_' + nm] = ci(per_tier(auc_contrib(sa, np.sort(sl)))); out['flag_' + nm] = float((sl > th).mean())
    flag = XG[:, 0] > th; out['per_size'] = [float(flag[gsize == s].mean()) for s in sizes]
    ev_tiers = np.unique(ta)
    def bw(wt): return float((gsize * flag * wt[gtier]).sum() / (gsize * wt[gtier]).sum())
    base = np.zeros(NT); base[ev_tiers] = 1
    bsr = [bw(np.bincount(brng.choice(ev_tiers, len(ev_tiers)), minlength=NT).astype(float)) for _ in range(B)]
    out['bw'] = (bw(base), float(np.quantile(bsr, .025)), float(np.quantile(bsr, .975)))
    return out
print('# Supervised detectors + feature ablation (offline, post-hoc)\n')
print('Rows: benign train %d, benign cal %d, benign holdout %d; attack cal %d, attack holdout %d; rollup look-alike (cal+holdout) %d; hard look-alike (holdout) %d; price tiers %d.' % (ben_tr.sum(), ben_cal.sum(), ben_ho.sum(), atk_cal.sum(), atk_ho.sum(), roll.sum(), hard.sum(), NT))
print('Attack feature vectors: distinct (gas_limit,bytecode_size,opcode_count,wei) combos = %d; distinct gas_price tiers = %d -> effective n of the attack class is %d tier points, not %d rows.' % (len({tuple(r) for r in A[grp == 'attack'][:, 1:]}), NT, NT, (grp == 'attack').sum()))
for nm, m in (('attack', grp == 'attack'), ('rollup look-alike', grp == 'lookalike'), ('hard look-alike', grp == 'lookalike_hard')):
    print('- %s: gas_limit=%s bytecode_size=%s opcode_count=%s wei=%s' % (nm, np.unique(A[m][:, 1]), np.unique(A[m][:, 3]), np.unique(A[m][:, 4]), np.unique(A[m][:, 2])))
print('- identical wire fields attack vs hard look-alike (gas_limit,wei,bytecode_size): %s; attack vs rollup: %s\n' % (
    all(np.array_equal(np.unique(A[grp == 'attack'][:, i]), np.unique(A[grp == 'lookalike_hard'][:, i])) for i in (1, 2, 3)),
    all(np.array_equal(np.unique(A[grp == 'attack'][:, i]), np.unique(A[grp == 'lookalike'][:, i])) for i in (1, 2, 3))))
print('Cols: AUROC_ben = attack vs benign(cal+holdout); AUROC_roll/hard = P(attack score > look-alike score) (0.5 = inseparable); TPR@thr = holdout attack flagged at threshold = 99th pct of benign-calibration scores; FPR_cal/FPR_ho = benign flag rate; flag_roll/hard = look-alike flag rate; bytes-wtd TPR over synthetic size grid (3k..98k). Brackets = 95% bootstrap over price tiers (n=tiers, tiny effective n).\n')
for design in ('A', 'B'):
    print('\n## Design %s: %s\n' % (design, 'train attack = calibration-role attack (all 30 tiers); eval attack = holdout-role attack (same tiers)' if design == 'A' else 'train attack = calibration-role even tiers (15); eval attack = holdout-role odd tiers (15, unseen prices)'))
    print('| features | model | AUROC_ben | AUROC_roll | AUROC_hard | TPR@thr | FPR_cal | FPR_ho | flag_roll | flag_hard | per-size TPR (3k,6k,12k,24k,48k,65k,70k,98k) | bytes-wtd TPR |'); print('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for sname, mname, o in run(design):
        print('| %s | %s | %s | %s | %s | %s | %.4f | %.4f | %.3f | %.3f | %s | %s |' % (sname, mname, fm(o['auc_ben']), fm(o['auc_roll']), fm(o['auc_hard']), fm(o['tpr']), o['fpr_cal'], o['fpr_ho'], o['flag_roll'], o['flag_hard'], ['%.2f' % x for x in o['per_size']], fm(o['bw'])))
    sys.stdout.flush()
