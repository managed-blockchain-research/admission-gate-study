# Offline analyses for the response letter (generated 2026-11-19 01:05)

## O1/O2 detectors on the stored per-transaction table (train = benign training records; attack = hold-out/calibration attack records; benign eval subsampled 100k)
| feature set | detector | AUROC vs benign (no look-alike) | TPR@FPR1% (no look-alike) | AUROC vs benign incl. look-alike | TPR@FPR1% incl. look-alike |
|---|---|---|---|---|---|
| frozen6 (as deployed) | IsolationForest(200) | 0.899 | 0.000 | 0.887 | 0.000 |
| frozen6 (as deployed) | LOF(k=20, 20k train) | 1.000 | 1.000 | 0.980 | 0.000 |
| frozen6 (as deployed) | EllipticEnvelope(20k train) | 0.999 | 1.000 | 0.978 | 0.000 |
| frozen6 (as deployed) | OneClassSVM(rbf, 5k train) | 1.000 | 1.000 | 0.980 | 0.000 |
| wire-only 5 (no opcode_count: drop vcr_log) | IsolationForest(200) | 0.913 | 0.067 | 0.898 | 0.033 |
| wire-only 5 (no opcode_count: drop vcr_log) | LOF(k=20, 20k train) | 1.000 | 1.000 | 0.979 | 0.000 |
| wire-only 5 (no opcode_count: drop vcr_log) | EllipticEnvelope(20k train) | 1.000 | 1.000 | 0.979 | 0.000 |
| wire-only 5 (no opcode_count: drop vcr_log) | OneClassSVM(rbf, 5k train) | 1.000 | 1.000 | 0.980 | 0.000 |
| wire-only 3 (gas_limit, bytecode_size, wei-based ed_log) | IsolationForest(200) | 0.895 | 0.000 | 0.875 | 0.000 |
| wire-only 3 (gas_limit, bytecode_size, wei-based ed_log) | LOF(k=20, 20k train) | 1.000 | 1.000 | 0.980 | 0.000 |
| wire-only 3 (gas_limit, bytecode_size, wei-based ed_log) | EllipticEnvelope(20k train) | 1.000 | 1.000 | 0.980 | 0.000 |
| wire-only 3 (gas_limit, bytecode_size, wei-based ed_log) | OneClassSVM(rbf, 5k train) | 1.000 | 1.000 | 0.980 | 0.000 |
| calldata rule (bytecode_size > 65,604 B) | rule | - | TPR 1.000 at FPR 0.0000 | - | TPR 1.000 at FPR 0.0221 |

## O3 share of benign attempts with receipt within t seconds (latency of outcome ok; failed/not-sent counted as not receipted); mean over runs
| experiment/arm | n runs | <=5 s | <=10 s | <=20 s | <=30 s | not sent | failed (30 s limit) |
|---|---|---|---|---|---|---|---|
| baseline_controls_attack_only attack none | 5 | 0.141 | 0.253 | 0.424 | 0.594 | 0.000 | 0.406 |
| baseline_controls_attack_only attack GT | 5 | 0.186 | 0.380 | 0.711 | 0.916 | 0.000 | 0.084 |
| baseline_controls_attack_only attack SizeStatic | 6 | 0.192 | 0.385 | 0.721 | 0.920 | 0.000 | 0.080 |
| baseline_controls_attack_only attack BS | 5 | 0.295 | 0.568 | 0.813 | 0.857 | 0.138 | 0.005 |
| baseline_controls_attack_only attack SizeGraded | 5 | 0.134 | 0.253 | 0.438 | 0.623 | 0.000 | 0.377 |
| baseline_besu_1gb ZGC1GB none | 5 | 0.139 | 0.253 | 0.423 | 0.586 | 0.000 | 0.414 |
| baseline_besu_1gb ZGC1GB BS | 4 | 0.550 | 0.694 | 0.783 | 0.792 | 0.207 | 0.000 |

## O4 admission-service decision latency as seen by the load generator (all benign+attack decisions in the runs above; ms): n=599562 p50=1 p99=4 p99.9=13 max=116

## O5 sensitivity of the graded rejection probability p=grad(u_t) to the u_t sampling interval (stored u_t traces, 100 ms native; baseline_controls_attack_only attack-cell none runs; sample-and-hold at the interval, window max for 30 s)
| interval | mean |p_native - p_resampled| | share of time with |dp| > 0.10 | mean p native | mean p resampled |
|---|---|---|---|---|
| 1 s | 0.0956 | 0.200 | 0.215 | 0.216 |
| 5 s | 0.2382 | 0.503 | 0.215 | 0.242 |
| 30 s | 0.6129 | 0.907 | 0.215 | 0.828 |

## O1b follow-up: unseen_replay_detectors.py (post-hoc detector choice, disclosed; criterion fixed earlier: bytes-weighted TPR at benign FPR <= 1%, passes if >= best size rule + 0.20 with bootstrap CI over price tiers excluding 0)
Frozen-6 features: IsolationForest 0.000 (fails), LOF 1.000 (+0.484 over the best rule, passes), EllipticEnvelope 0.516 (equal to rule), OneClassSVM 0.384 (fails). Wire-only 5 features: IsolationForest 0.048, LOF 1.000 (passes), EllipticEnvelope 0.516, OneClassSVM 0.622 (+0.106, fails the 0.20 margin).
**Caution (must accompany any use of these numbers):** the benign evaluation set consists of the same few deterministic traffic classes as the training set (effective sample size = number of distinct class vectors), so a novelty detector such as LOF scores ANY feature vector outside those classes as an outlier. Its 100% detection of 3 KB-98 KB synthetic attack vectors therefore also means it would flag benign transactions of unseen sizes; synthetic benign vectors with the same size grid and features are, by construction, indistinguishable from the synthetic attack vectors (the look-alike situation at every size). FPR on unseen benign sizes was not measured and would be about 1 by construction. These results show that IsolationForest is the weakest of the tested detectors in this setting and that distance-based novelty detectors match or exceed a size rule only on in-distribution traffic; they do NOT show a detector that separates attack from benign transactions of the same shape.
