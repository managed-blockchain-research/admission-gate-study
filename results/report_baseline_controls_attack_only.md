# Results report - experiment baseline_controls_attack_only (generated 2026-11-19 00:55)

Numbers only. Registered in PREREG_UNIFIED_v1.md addendum baseline_controls_attack_only (exploratory, post-hoc threshold 65,604 B). Besu G1 512 MB, node cpu05, same-seed pairs, per-pair values shown, t 95% CI over pair differences, no p-values.
Metric names: "receipt within the connector 30 s limit" (config txWallClockTimeout/transactionPollingTimeout = 30 s); chain-scan inclusion counts are NOT used.

## Inventory (completed runs with summary / scheduled)
- attack cell: OracleBlock 5/5, PressureOnly 5/5, RandShed48 5/5, SizeFixedP20 5/5, SizeGraded 5/5, SizeStatic 5/5, none 5/5
- lookalike cell: PressureOnly 4/4, SizeFixedP20 4/4, SizeGraded 4/4, SizeStatic 4/4, none 4/4
- runs without summary (apparatus failure, NOT replaced): none

## attack cell: per-arm means (per-seed values in brackets)

| arm | n | attack block rate | benign rejected (all) | rejected by class SL/SH/M/L/LA (%) | receipts<=30 s | failed | unfinished | planned no record | realized reject fraction | stale | u_t burst max / frac>=0.6 | post frac>=0.6 | OOM runs | node death | G1 pause ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OracleBlock | 5 | 1.000 | 0 [0, 0, 0, 0, 0] | 0.0/0.0/0.0/0.0/- | 21990 [22059, 21998, 21923, 21862, 22106] | 2010 | 0 | 0 | 0.0476 | 0 | 0.870 / 0.40 | 0.43 | 0 | 0 | 23160 |
| PressureOnly | 5 | 0.153 | 3321 [2971, 3521, 3393, 3553, 3165] | 13.9/13.8/14.2/13.8/- | 20560 [20931, 20438, 20532, 20217, 20682] | 119 | 0 | 0 | 0.1390 | 0 | 0.935 / 0.36 | 0.39 | 0 | 0 | 19202 |
| RandShed48 | 5 | 0.048 | 1167 [1141, 1226, 1151, 1133, 1185] | 4.8/5.0/3.8/4.9/- | 17830 [17785, 18110, 17873, 17601, 17783] | 5002 | 0 | 0 | 0.0486 | 0 | 0.894 / 0.42 | 0.58 | 0 | 0 | 27670 |
| SizeFixedP20 | 5 | 0.198 | 0 [0, 0, 0, 0, 0] | 0.0/0.0/0.0/0.0/- | 15024 [14892, 15138, 14895, 14947, 15249] | 8976 | 0 | 0 | 0.0094 | 0 | 0.898 / 0.48 | 0.70 | 0 | 0 | 29441 |
| SizeGraded | 5 | 0.200 | 0 [0, 0, 0, 0, 0] | 0.0/0.0/0.0/0.0/- | 14940 [14947, 15138, 14876, 14725, 15015] | 9060 | 0 | 0 | 0.0095 | 0 | 0.930 / 0.45 | 0.70 | 0 | 0 | 30378 |
| SizeStatic | 5 | 1.000 | 0 [0, 0, 0, 0, 0] | 0.0/0.0/0.0/0.0/- | 22061 [22061, 22065, 22043, 21953, 22184] | 1939 | 0 | 0 | 0.0476 | 0 | 0.891 / 0.40 | 0.51 | 0 | 0 | 22729 |
| none | 5 | 0.000 | 0 [0, 0, 0, 0, 0] | 0.0/0.0/0.0/0.0/- | 14252 [14297, 14272, 14228, 14124, 14341] | 9748 | 0 | 0 | n/a | n/a | 0.948 / 0.49 | 0.73 | 0 | 0 | 31464 |

### attack cell: same-seed paired differences (A - B), t 95% CI [per-pair]

- OracleBlock - none | benign_ok30 | 7737 [7702, 7773] | [7762, 7726, 7695, 7738, 7765]
- OracleBlock - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- OracleBlock - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0, 1.0]
- OracleBlock - none | gc_pause_ms | -8304 [-10865, -5742] | [-9740, -7358, -10121, -5137, -9163]
- RandShed48 - none | benign_ok30 | 3578 [3373, 3783] | [3488, 3838, 3645, 3477, 3442]
- RandShed48 - none | benign_not_sent | 1167 [1120, 1215] | [1141, 1226, 1151, 1133, 1185]
- RandShed48 - none | attack_block_rate | 0.048 [0.045, 0.051] | [0.05, 0.045, 0.049, 0.046, 0.051]
- RandShed48 - none | gc_pause_ms | -3794 [-5598, -1990] | [-4927, -2680, -4925, -1808, -4630]
- SizeStatic - OracleBlock | benign_ok30 | 72 [17, 126] | [2, 67, 120, 91, 78]
- SizeStatic - OracleBlock | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - OracleBlock | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0, 0.0, 0.0]
- SizeStatic - OracleBlock | gc_pause_ms | -431 [-3293, 2431] | [2020, -995, 1712, -1392, -3499]
- SizeStatic - RandShed48 | benign_ok30 | 4231 [4011, 4451] | [4276, 3955, 4170, 4352, 4401]
- SizeStatic - RandShed48 | benign_not_sent | -1167 [-1215, -1120] | [-1141, -1226, -1151, -1133, -1185]
- SizeStatic - RandShed48 | attack_block_rate | 0.952 [0.949, 0.955] | [0.95, 0.955, 0.951, 0.954, 0.949]
- SizeStatic - RandShed48 | gc_pause_ms | -4941 [-7491, -2391] | [-2793, -5673, -3484, -4721, -8032]
- SizeStatic - none | benign_ok30 | 7809 [7770, 7847] | [7764, 7793, 7815, 7829, 7843]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | gc_pause_ms | -8735 [-11618, -5852] | [-7720, -8353, -8409, -6529, -12662]
- SizeGraded - none | benign_ok30 | 688 [560, 816] | [650, 866, 648, 601, 674]
- SizeGraded - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeGraded - none | attack_block_rate | 0.200 [0.169, 0.231] | [0.196, 0.242, 0.194, 0.175, 0.193]
- SizeGraded - none | gc_pause_ms | -1086 [-1743, -430] | [-599, -1174, -1528, -484, -1647]
- SizeFixedP20 - none | benign_ok30 | 772 [605, 939] | [595, 866, 667, 823, 908]
- SizeFixedP20 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeFixedP20 - none | attack_block_rate | 0.198 [0.182, 0.214] | [0.177, 0.203, 0.203, 0.198, 0.21]
- SizeFixedP20 - none | gc_pause_ms | -2023 [-4358, 311] | [-2085, -1225, -4402, 600, -3004]
- PressureOnly - none | benign_ok30 | 6308 [6049, 6566] | [6634, 6166, 6304, 6093, 6341]
- PressureOnly - none | benign_not_sent | 3321 [3013, 3628] | [2971, 3521, 3393, 3553, 3165]
- PressureOnly - none | attack_block_rate | 0.153 [0.148, 0.158] | [0.147, 0.152, 0.157, 0.152, 0.157]
- PressureOnly - none | gc_pause_ms | -12262 [-13709, -10816] | [-11557, -12955, -13631, -10673, -12495]
- SizeStatic - SizeGraded | benign_ok30 | 7121 [6977, 7265] | [7114, 6927, 7167, 7228, 7169]
- SizeStatic - SizeGraded | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - SizeGraded | attack_block_rate | 0.800 [0.769, 0.831] | [0.804, 0.758, 0.806, 0.825, 0.807]
- SizeStatic - SizeGraded | gc_pause_ms | -7648 [-10052, -5245] | [-7121, -7179, -6881, -6045, -11015]
- SizeStatic - SizeFixedP20 | benign_ok30 | 7037 [6894, 7180] | [7169, 6927, 7148, 7006, 6935]
- SizeStatic - SizeFixedP20 | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - SizeFixedP20 | attack_block_rate | 0.802 [0.786, 0.818] | [0.823, 0.797, 0.797, 0.802, 0.79]
- SizeStatic - SizeFixedP20 | gc_pause_ms | -6711 [-9308, -4114] | [-5635, -7128, -4007, -7129, -9658]
- SizeGraded - SizeFixedP20 | benign_ok30 | -84 [-251, 83] | [55, 0, -19, -222, -234]
- SizeGraded - SizeFixedP20 | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeGraded - SizeFixedP20 | attack_block_rate | 0.002 [-0.031, 0.035] | [0.019, 0.04, -0.009, -0.023, -0.017]
- SizeGraded - SizeFixedP20 | gc_pause_ms | 937 [-936, 2809] | [1486, 51, 2874, -1084, 1357]

## lookalike cell: per-arm means (per-seed values in brackets)

| arm | n | attack block rate | benign rejected (all) | rejected by class SL/SH/M/L/LA (%) | receipts<=30 s | failed | unfinished | planned no record | realized reject fraction | stale | u_t burst max / frac>=0.6 | post frac>=0.6 | OOM runs | node death | G1 pause ms |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PressureOnly | 4 | n/a | 2965 [3198, 2664, 3008, 2991] | 11.6/12.1/12.5/11.6/13.3 | 21922 [21912, 21570, 22121, 22087] | 309 | 0 | 0 | 0.1177 | 0 | 0.886 / 0.32 | 0.35 | 0 | 0 | 22051 |
| SizeFixedP20 | 4 | n/a | 242 [247, 246, 216, 259] | 0.0/0.0/0.0/0.0/20.2 | 16280 [16356, 16239, 16218, 16309] | 8674 | 0 | 0 | 0.0096 | 0 | 0.905 / 0.44 | 0.65 | 0 | 0 | 31210 |
| SizeGraded | 4 | n/a | 239 [252, 222, 267, 214] | 0.0/0.0/0.0/0.0/19.9 | 16251 [16229, 16223, 16363, 16188] | 8704 | 0 | 0 | 0.0095 | 0 | 0.905 / 0.45 | 0.70 | 0 | 0 | 29516 |
| SizeStatic | 4 | n/a | 1200 [1200, 1200, 1200, 1200] | 0.0/0.0/0.0/0.0/100.0 | 21973 [22026, 21789, 21956, 22122] | 2027 | 0 | 0 | 0.0476 | 0 | 0.908 / 0.39 | 0.47 | 0 | 0 | 24043 |
| none | 4 | n/a | 0 [0, 0, 0, 0] | 0.0/0.0/0.0/0.0/0.0 | 15418 [15038, 15548, 15614, 15471] | 9628 | 0 | 0 | n/a | n/a | 0.914 / 0.45 | 0.79 | 0 | 0 | 32578 |

### lookalike cell: same-seed paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 6556 [6019, 7092] | [6988, 6241, 6342, 6651]
- SizeStatic - none | benign_not_sent | 1200 [1200, 1200] | [1200, 1200, 1200, 1200]
- SizeStatic - none | rej_LA | 1200 [1200, 1200] | [1200, 1200, 1200, 1200]
- SizeStatic - none | gc_pause_ms | -8534 [-9564, -7505] | [-7620, -8726, -9143, -8649]
- SizeGraded - none | benign_ok30 | 833 [450, 1216] | [1191, 675, 749, 717]
- SizeGraded - none | benign_not_sent | 239 [199, 278] | [252, 222, 267, 214]
- SizeGraded - none | rej_LA | 239 [199, 278] | [252, 222, 267, 214]
- SizeGraded - none | gc_pause_ms | -3062 [-5895, -228] | [-985, -5286, -2639, -3336]
- SizeFixedP20 - none | benign_ok30 | 863 [356, 1369] | [1318, 691, 604, 838]
- SizeFixedP20 - none | benign_not_sent | 242 [213, 271] | [247, 246, 216, 259]
- SizeFixedP20 - none | rej_LA | 242 [213, 271] | [247, 246, 216, 259]
- SizeFixedP20 - none | gc_pause_ms | -1368 [-3887, 1151] | [-422, -1573, 38, -3514]
- PressureOnly - none | benign_ok30 | 6505 [5937, 7072] | [6874, 6022, 6507, 6616]
- PressureOnly - none | benign_not_sent | 2965 [2613, 3318] | [3198, 2664, 3008, 2991]
- PressureOnly - none | rej_LA | 160 [109, 211] | [174, 115, 189, 162]
- PressureOnly - none | gc_pause_ms | -10526 [-12541, -8512] | [-9840, -9205, -12068, -10993]
- SizeStatic - SizeGraded | benign_ok30 | 5722 [5445, 6000] | [5797, 5566, 5593, 5934]
- SizeStatic - SizeGraded | benign_not_sent | 961 [922, 1001] | [948, 978, 933, 986]
- SizeStatic - SizeGraded | rej_LA | 961 [922, 1001] | [948, 978, 933, 986]
- SizeStatic - SizeGraded | gc_pause_ms | -5473 [-7828, -3118] | [-6635, -3440, -6504, -5313]
- SizeStatic - SizeFixedP20 | benign_ok30 | 5693 [5515, 5870] | [5670, 5550, 5738, 5813]
- SizeStatic - SizeFixedP20 | benign_not_sent | 958 [929, 987] | [953, 954, 984, 941]
- SizeStatic - SizeFixedP20 | rej_LA | 958 [929, 987] | [953, 954, 984, 941]
- SizeStatic - SizeFixedP20 | gc_pause_ms | -7167 [-9795, -4539] | [-7198, -7153, -9181, -5135]
- SizeGraded - SizeFixedP20 | benign_ok30 | -30 [-232, 173] | [-127, -16, 145, -121]
- SizeGraded - SizeFixedP20 | benign_not_sent | -3 [-69, 63] | [5, -24, 51, -45]
- SizeGraded - SizeFixedP20 | rej_LA | -3 [-69, 63] | [5, -24, 51, -45]
- SizeGraded - SizeFixedP20 | gc_pause_ms | -1694 [-4573, 1186] | [-563, -3713, -2677, 178]

## Caveats fixed in advance
- threshold 65,604 B chosen after seeing earlier results (post-hoc); SizeStatic (p=1) vs SizeGraded differ in intensity AND feedback; SizeFixedP20 (p about 0.20, value from Stage-1 RuleSize) is a fixed-probability control, not an intensity-matched one; RandShed48 is a content-blind volume control (p about 0.048 = attack share).
- attack and look-alike traffic are never in the same run; single heap/collector; p50 latency over confirmed transactions only (right-censored); stale u_t => p = 0 for graded/fixed arms (stale counts reported).
