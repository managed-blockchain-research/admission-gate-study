# Supervised detectors vs frozen Isolation Forest + feature ablation (offline, post-hoc)
Source: `supervised_detectors.out` (script `supervised_detectors.py`; all numbers below are copied from it, Design A unless noted).
Setup: benign TRAIN records + attack records; look-alikes never trained on. The stored table has NO attack rows in role `train`, so attack training data = calibration-role attack (A: all 30 price tiers; B: even tiers, evaluated on odd holdout tiers). Threshold = 99th pct of benign-calibration scores. Brackets = 95% bootstrap over the 30 price tiers.

| features | model | AUROC attack vs benign | TPR@benign FPR~1% | flags rollup / hard look-alike | bytes-weighted TPR (size grid) |
|---|---|---|---|---|---|
| frozen6 | IsolationForest (benign-only) | 0.898 [0.880,0.917] | 0.000 | 0.066 / 0.000 | 0.000 |
| frozen6 | LogReg / RF / GB | 1.000 / 1.000 / 1.000 | 1.000 | 1.000 / 1.000 | 0.516 / 0.301 / 0.301 |
| wire-only5 (no vcr_log) | IsolationForest | 0.911 [0.893,0.928] | 0.067 [0.000,0.167] | 0.099 / 0.066 | 0.048 [0.000,0.119] |
| wire-only5 | LogReg / RF / GB | 1.000 / 1.000 / 1.000 | 1.000 | 1.000 / 1.000 | 0.516 / 0.301 / 0.301 |
| bytecode_size only | IsolationForest | 0.932 | 0.000 | 0.000 / 0.000 | 0.000 |
| bytecode_size only | LogReg / RF / GB | 1.000 / 1.000 / 1.000 | 1.000 | 1.000 / 1.000 | 0.516 / 0.301 / 0.301 |
| gas-only (price, limit) | IF / LogReg / RF / GB | 0.462 / 0.547 / 0.547 / 0.547 | 0.000 (all) | 1.000 (IF only) / 0 | 0.000 (all) |
| rule bs>65604 (benign-calibration 99th pct, no attack data) | - | 1.000 | 1.000 | 1.000 / 1.000 | 0.516 |
| rule bs>81988 or >=80000 (POST-HOC, uses attack data) | - | 1.000 | 1.000 | 1.000 / 1.000 | 0.301 |

Statements (what the numbers do and do NOT support):
- Attack vs hard look-alike separation is impossible by construction: the hard look-alike is identical to the attack in every wire field; all models and rules give AUROC_hard 0.500 (Design A; IF/LogReg CIs e.g. [0.399,0.600]) and flag it at the same rate as the attack (1.000 for all supervised models).
- Class-deterministic traffic makes supervised accuracy near-perfect wherever the classes differ in any feature, so high accuracy must not be read as evidence of robustness to adaptive attackers. The attack has 1 distinct feature vector and 30 price tiers, so effective n is 30 tier points, not 14400 rows; many CIs collapse to [x,x] because the class is a single point.
- The frozen IF is the weakest: AUROC 0.898 and TPR 0.000 at FPR ~1% (frozen6); supervised models and even a bytecode_size threshold reach TPR 1.000 with FPR_cal 0.0000-0.0087. This supports "a supervised/simple detector separates this attack from this benign mix"; it does NOT show it would generalize to attackers who choose different sizes or fields.
- Feature ablation, including without opcode_count: removing the opcode-dependent vcr_log (wire-only5) leaves all three supervised models at AUROC 1.000 / TPR 1.000; vcr_log alone and ed_log alone are at chance (AUROC 0.516 for supervised models) because wei_value=0 for attack and most benign. For the IF, wire-only5 does not hurt (TPR 0.067 vs 0.000, within CI overlap with 0).
- The signal is carried by payload size: bytecode_size alone gives AUROC 1.000 / TPR 1.000 for all three supervised models; gas-only features carry no attack-vs-benign signal (AUROC 0.462-0.547, TPR 0.000).
- Out-of-range sizes: on the synthetic size grid (3k-98k bytes) the supervised models detect only sizes at/above where they were trained or benign max (bytes-weighted TPR 0.301-0.516; per-size TPR 0.00 up to 65k bytes, 1.00 at 98k). The no-attack-data rule (bs>65604) gets 0.516 (flags 70k and 98k), the post-hoc 80KB-style rules 0.301. Learned models therefore do not beat a one-line size rule.
- The rule threshold chosen on benign calibration only is attack-free (65604 = benign 64KB class size); the 81988/80000 thresholds are post-hoc because they use attack data. Both flag 100% of rollup and hard look-alikes (FPR on look-alikes = 1.000): size rules cannot treat legitimate large payloads differently.
- Rollup look-alike differs from the attack only in gas_limit (2151000 vs 8000000). Models using gas_limit therefore show AUROC_roll 0 or 1 (e.g. gas-only 1.000, IF 0.000); this is a single-field artifact of one class point, not detection skill.
- Design B (train on even tiers, test on unseen odd price tiers): supervised AUROC and TPR stay 1.000 for payload-based sets, so price-tier memorization is not the explanation, but price tiers are a single narrow range (30 values) so this tests little.
- All of this is post-hoc, offline, one benign mix and one attack class; no claim about adaptive adversaries, other workloads, or live deployment.
