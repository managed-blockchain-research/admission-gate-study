# Cost-benefit frontier and benign-harm breakdown (offline; mixed_zgc_sustained_pulse + global_bucket_sweeps; Besu G1 512 MB blocks only; numbers only)

Rows: block / arm, mean over seeds (n shown). attack block = share of attack transactions rejected; benign rej = benign (non-heavy, non-look-alike) requests rejected by the gate; LA rej = look-alike (legitimate heavy) rejected share; receipts = benign receipts within 30 s; gain = same-seed paired difference vs none (mean).

| exp | block | arm | n | attack block | benign rej (count) | benign rej share | LA rej share | receipts | gain vs none |
|---|---|---|---|---|---|---|---|---|---|
| mixed_zgc_sustained_pulse | M | OracleBlock | 4 | 1.000 | 0 | 0.0000 | 0.000 | 19889 | 5202 |
| mixed_zgc_sustained_pulse | M | PressureOnly | 4 | 0.111 | 2947 | 0.1208 | 0.108 | 21106 | 6418 |
| mixed_zgc_sustained_pulse | M | RandShed48 | 4 | 0.053 | 1172 | 0.0480 | 0.051 | 18329 | 3642 |
| mixed_zgc_sustained_pulse | M | SizeGraded | 4 | 0.191 | 0 | 0.0000 | 0.182 | 15382 | 694 |
| mixed_zgc_sustained_pulse | M | SizeStatic | 4 | 1.000 | 0 | 0.0000 | 1.000 | 22057 | 7369 |
| mixed_zgc_sustained_pulse | M | none | 4 | 0.000 | 0 | 0.0000 | 0.000 | 14688 | 0 |
| mixed_zgc_sustained_pulse | TP | PressureOnly | 3 | 0.071 | 3072 | 0.1234 | n/a | 21699 | 5442 |
| mixed_zgc_sustained_pulse | TP | SizeGraded | 3 | 0.127 | 0 | 0.0000 | n/a | 16414 | 157 |
| mixed_zgc_sustained_pulse | TP | SizeStatic | 3 | 1.000 | 0 | 0.0000 | n/a | 18442 | 2186 |
| mixed_zgc_sustained_pulse | TP | SizeSticky | 3 | 0.534 | 0 | 0.0000 | n/a | 17476 | 1219 |
| mixed_zgc_sustained_pulse | TP | none | 3 | 0.000 | 0 | 0.0000 | n/a | 16257 | 0 |
| mixed_zgc_sustained_pulse | TS | PressureOnly | 3 | 0.138 | 3206 | 0.1406 | n/a | 19134 | 7197 |
| mixed_zgc_sustained_pulse | TS | SizeGraded | 3 | 0.217 | 0 | 0.0000 | n/a | 12167 | 231 |
| mixed_zgc_sustained_pulse | TS | SizeStatic | 3 | 1.000 | 0 | 0.0000 | n/a | 22675 | 10739 |
| mixed_zgc_sustained_pulse | TS | SizeSticky | 3 | 0.722 | 0 | 0.0000 | n/a | 21039 | 9103 |
| mixed_zgc_sustained_pulse | TS | none | 3 | 0.000 | 0 | 0.0000 | n/a | 11936 | 0 |
| global_bucket_sweeps | I1 | BudgetR125 | 3 | 0.615 | 0 | 0.0000 | n/a | 17723 | 1524 |
| global_bucket_sweeps | I1 | BudgetR250 | 3 | 0.235 | 0 | 0.0000 | n/a | 16533 | 335 |
| global_bucket_sweeps | I1 | BudgetR500 | 3 | 0.000 | 0 | 0.0000 | n/a | 16170 | -29 |
| global_bucket_sweeps | I1 | SizeFixedP20 | 3 | 0.212 | 0 | 0.0000 | n/a | 16449 | 251 |
| global_bucket_sweeps | I1 | SizeStatic | 3 | 1.000 | 0 | 0.0000 | n/a | 18885 | 2687 |
| global_bucket_sweeps | I1 | none | 3 | 0.000 | 0 | 0.0000 | n/a | 16198 | 0 |
| global_bucket_sweeps | I3 | BudgetR125 | 3 | 0.872 | 0 | 0.0000 | n/a | 20974 | 6893 |
| global_bucket_sweeps | I3 | BudgetR250 | 3 | 0.745 | 0 | 0.0000 | n/a | 19760 | 5679 |
| global_bucket_sweeps | I3 | BudgetR500 | 3 | 0.500 | 0 | 0.0000 | n/a | 17742 | 3662 |
| global_bucket_sweeps | I3 | SizeFixedP20 | 3 | 0.196 | 0 | 0.0000 | n/a | 15036 | 956 |
| global_bucket_sweeps | I3 | SizeStatic | 3 | 1.000 | 0 | 0.0000 | n/a | 22006 | 7926 |
| global_bucket_sweeps | I3 | none | 3 | 0.000 | 0 | 0.0000 | n/a | 14080 | 0 |
| global_bucket_sweeps | I6 | BudgetR125 | 3 | 0.936 | 0 | 0.0000 | n/a | 22747 | 10989 |
| global_bucket_sweeps | I6 | BudgetR250 | 3 | 0.873 | 0 | 0.0000 | n/a | 22584 | 10826 |
| global_bucket_sweeps | I6 | BudgetR500 | 3 | 0.749 | 0 | 0.0000 | n/a | 21739 | 9980 |
| global_bucket_sweeps | I6 | SizeFixedP20 | 3 | 0.198 | 0 | 0.0000 | n/a | 13195 | 1436 |
| global_bucket_sweeps | I6 | SizeStatic | 3 | 1.000 | 0 | 0.0000 | n/a | 22724 | 10965 |
| global_bucket_sweeps | I6 | none | 3 | 0.000 | 0 | 0.0000 | n/a | 11758 | 0 |
| global_bucket_sweeps | L1 | BudgetR250 | 4 | n/a | 0 | 0.0000 | 0.235 | 16851 | 190 |
| global_bucket_sweeps | L1 | BudgetR500 | 4 | n/a | 0 | 0.0000 | 0.000 | 16679 | 18 |
| global_bucket_sweeps | L1 | SizeStatic | 4 | n/a | 0 | 0.0000 | 1.000 | 18978 | 2317 |
| global_bucket_sweeps | L1 | none | 4 | n/a | 0 | 0.0000 | 0.000 | 16661 | 0 |
| global_bucket_sweeps | MX | BudgetAdapt500 | 4 | 0.440 | 0 | 0.0000 | 0.787 | 18154 | 3615 |
| global_bucket_sweeps | MX | BudgetR250 | 4 | 0.658 | 0 | 0.0000 | 0.919 | 19840 | 5302 |
| global_bucket_sweeps | MX | BudgetR500 | 4 | 0.458 | 0 | 0.0000 | 0.578 | 17946 | 3407 |
| global_bucket_sweeps | MX | SizeStatic | 4 | 1.000 | 0 | 0.0000 | 1.000 | 22098 | 7559 |
| global_bucket_sweeps | MX | none | 4 | 0.000 | 0 | 0.0000 | 0.000 | 14538 | 0 |

## Benign harm by transaction class, phase and sender (arms that can reject benign requests; counts pooled over seeds)

| exp | block | arm | benign rejected | by class (rej / attempts, %) | by phase (before / during / after the 60-180 s window) | rejection share by worker: max / mean (27 benign workers) |
|---|---|---|---|---|---|---|
| mixed_zgc_sustained_pulse | M | PressureOnly | 11787 | SL 3554/28780 (12.35%), SH 1524/12460 (12.23%), M 110/964 (11.41%), L 6599/53772 (12.27%) | 1878 (7.83%) / 4887 (11.31%) / 5022 (17.45%) | 0.129 / 0.122 |
| mixed_zgc_sustained_pulse | M | RandShed48 | 4687 | SL 1417/28785 (4.92%), SH 629/12466 (5.05%), M 42/964 (4.36%), L 2599/53785 (4.83%) | 1218 (5.08%) / 2054 (4.75%) / 1415 (4.91%) | 0.059 / 0.049 |
| mixed_zgc_sustained_pulse | TP | PressureOnly | 9217 | SL 2720/22381 (12.15%), SH 1169/9683 (12.07%), M 108/739 (14.61%), L 5220/41878 (12.46%) | 1102 (6.12%) / 4713 (13.43%) / 3402 (15.76%) | 0.134 / 0.123 |
| mixed_zgc_sustained_pulse | TS | PressureOnly | 9618 | SL 2903/20507 (14.16%), SH 1222/8882 (13.76%), M 100/687 (14.56%), L 5393/38324 (14.07%) | 708 (4.37%) / 4882 (15.07%) / 4028 (20.34%) | 0.153 / 0.141 |

Notes: phases use the scheduled time of the request; before = 0-60 s, during = 60-180 s, after = 180 s to the end of the load. Arms that reject only heavy transactions (none, SizeStatic, OracleBlock, Budget*) reject no benign request and are not listed. Look-alike rejections are shown in the first table (LA rej share) and are not counted as benign here.
