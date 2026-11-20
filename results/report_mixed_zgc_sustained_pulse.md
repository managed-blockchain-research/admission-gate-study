# Results report mixed_zgc_sustained_pulse (generated 2026-11-19 15:18)

Numbers only. Registered in PREREG_UNIFIED_v1.md addendum mixed_zgc_sustained_pulse (exploratory). Node cpu05, shared non-exclusive. Receipt = within the connector 30 s limit. Same-seed pairs, t 95% CI over pair differences, per-pair values shown, no p-values. Chain-scan counts not used.

## Inventory (completed with summary / present)
- block M: OracleBlock 4, PressureOnly 4, RandShed48 4, SizeGraded 4, SizeStatic 4, none 4 (scheduled 24)
- block Z: LearnedScore 4, OracleBlock 4, PressureOnly 4, SizeStatic 4, none 4 (scheduled 20)
- block N: OracleBlock 5, PressureOnly 5, SizeStatic 5, none 5 (scheduled 20)
- block TS: PressureOnly 3, SizeGraded 3, SizeStatic 3, SizeSticky 3, none 3 (scheduled 15)
- block TP: PressureOnly 3, SizeGraded 3, SizeStatic 3, SizeSticky 3, none 3 (scheduled 15)
- runs without summary (apparatus failure, NOT replaced): none

## Block M

| arm | n | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OracleBlock | 4 | 1.000 | 0 [0, 0, 0, 0] | 0 | 19889 [19628, 20024, 20005, 19900] | 4508 | 0 | 0 | 0 | 0 | 0 | 1 | 24809 | 0 |
| PressureOnly | 4 | 0.111 | 2990 [2748, 2964, 2934, 3314] | 43 | 21106 [21149, 21366, 21001, 20909] | 297 | 1 | 6 | 0 | 0 | 0 | 1 | 20028 | 0 |
| RandShed48 | 4 | 0.053 | 1192 [1166, 1196, 1222, 1185] | 20 | 18329 [18130, 18317, 18563, 18307] | 4870 | 0 | 0 | 0 | 0 | 0 | 1 | 27619 | 0 |
| SizeGraded | 4 | 0.191 | 73 [66, 70, 89, 66] | 73 | 15382 [15463, 15154, 15708, 15202] | 8946 | 0 | 0 | 0 | 0 | 0 | 1 | 28924 | 0 |
| SizeStatic | 4 | 1.000 | 400 [400, 400, 400, 400] | 400 | 22057 [22054, 22114, 22028, 22031] | 1943 | 0 | 0 | 0 | 0 | 0 | 1 | 23069 | 0 |
| none | 4 | 0.000 | 0 [0, 0, 0, 0] | 0 | 14688 [14706, 14629, 14863, 14553] | 9657 | 0 | 0 | 0 | 0 | 0 | 1 | 30676 | n/a |

### Block M paired differences (A - B), t 95% CI [per-pair]

- OracleBlock - none | benign_ok30 | 5202 [4857, 5546] | [4922, 5395, 5142, 5347]
- OracleBlock - none | nonLA_ok30 | 5150 [4772, 5527] | [4823, 5343, 5126, 5306]
- OracleBlock - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- OracleBlock - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- OracleBlock - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- OracleBlock - none | gc_pause_ms | -5866 [-8281, -3452] | [-6106, -7917, -4828, -4615]
- PressureOnly - none | benign_ok30 | 6418 [6024, 6813] | [6443, 6737, 6138, 6356]
- PressureOnly - none | nonLA_ok30 | 6406 [6020, 6793] | [6384, 6739, 6158, 6345]
- PressureOnly - none | benign_not_sent | 2990 [2614, 3366] | [2748, 2964, 2934, 3314]
- PressureOnly - none | rej_LA | 43 [32, 55] | [42, 54, 39, 38]
- PressureOnly - none | attack_block_rate | 0.111 [0.094, 0.127] | [0.1, 0.125, 0.109, 0.109]
- PressureOnly - none | gc_pause_ms | -10647 [-14250, -7044] | [-8675, -13854, -9556, -10503]
- SizeStatic - none | benign_ok30 | 7369 [7131, 7607] | [7348, 7485, 7165, 7478]
- SizeStatic - none | nonLA_ok30 | 7714 [7489, 7939] | [7647, 7833, 7546, 7829]
- SizeStatic - none | benign_not_sent | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | rej_LA | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | gc_pause_ms | -7606 [-11429, -3784] | [-7742, -10577, -7404, -4703]
- SizeGraded - none | benign_ok30 | 694 [474, 914] | [757, 525, 845, 649]
- SizeGraded - none | nonLA_ok30 | 712 [465, 958] | [722, 543, 915, 666]
- SizeGraded - none | benign_not_sent | 73 [55, 90] | [66, 70, 89, 66]
- SizeGraded - none | rej_LA | 73 [55, 90] | [66, 70, 89, 66]
- SizeGraded - none | attack_block_rate | 0.191 [0.136, 0.245] | [0.189, 0.165, 0.24, 0.17]
- SizeGraded - none | gc_pause_ms | -1752 [-3450, -53] | [-994, -1425, -3331, -1256]
- SizeStatic - OracleBlock | benign_ok30 | 2168 [1884, 2451] | [2426, 2090, 2023, 2131]
- SizeStatic - OracleBlock | nonLA_ok30 | 2564 [2280, 2848] | [2824, 2490, 2420, 2523]
- SizeStatic - OracleBlock | benign_not_sent | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - OracleBlock | rej_LA | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - OracleBlock | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0, 0.0]
- SizeStatic - OracleBlock | gc_pause_ms | -1740 [-3641, 161] | [-1636, -2660, -2576, -88]
- SizeStatic - PressureOnly | benign_ok30 | 950 [693, 1208] | [905, 748, 1027, 1122]
- SizeStatic - PressureOnly | nonLA_ok30 | 1307 [1039, 1575] | [1263, 1094, 1388, 1484]
- SizeStatic - PressureOnly | benign_not_sent | -2590 [-2966, -2214] | [-2348, -2564, -2534, -2914]
- SizeStatic - PressureOnly | rej_LA | 357 [345, 368] | [358, 346, 361, 362]
- SizeStatic - PressureOnly | attack_block_rate | 0.889 [0.873, 0.906] | [0.9, 0.875, 0.891, 0.891]
- SizeStatic - PressureOnly | gc_pause_ms | 3040 [-259, 6340] | [933, 3277, 2152, 5800]
- OracleBlock - PressureOnly | benign_ok30 | -1217 [-1628, -806] | [-1521, -1342, -996, -1009]
- OracleBlock - PressureOnly | nonLA_ok30 | -1257 [-1678, -836] | [-1561, -1396, -1032, -1039]
- OracleBlock - PressureOnly | benign_not_sent | -2990 [-3366, -2614] | [-2748, -2964, -2934, -3314]
- OracleBlock - PressureOnly | rej_LA | -43 [-55, -32] | [-42, -54, -39, -38]
- OracleBlock - PressureOnly | attack_block_rate | 0.889 [0.873, 0.906] | [0.9, 0.875, 0.891, 0.891]
- OracleBlock - PressureOnly | gc_pause_ms | 4780 [2272, 7289] | [2569, 5937, 4728, 5888]
- RandShed48 - none | benign_ok30 | 3642 [3406, 3877] | [3424, 3688, 3700, 3754]
- RandShed48 - none | nonLA_ok30 | 3616 [3352, 3879] | [3370, 3664, 3702, 3726]
- RandShed48 - none | benign_not_sent | 1192 [1155, 1229] | [1166, 1196, 1222, 1185]
- RandShed48 - none | rej_LA | 20 [17, 24] | [20, 23, 21, 18]
- RandShed48 - none | attack_block_rate | 0.053 [0.046, 0.061] | [0.054, 0.049, 0.051, 0.06]
- RandShed48 - none | gc_pause_ms | -3056 [-5327, -785] | [-2224, -4791, -3606, -1604]
- SizeStatic - RandShed48 | benign_ok30 | 3728 [3420, 4035] | [3924, 3797, 3465, 3724]
- SizeStatic - RandShed48 | nonLA_ok30 | 4098 [3805, 4391] | [4277, 4169, 3844, 4103]
- SizeStatic - RandShed48 | benign_not_sent | -792 [-829, -755] | [-766, -796, -822, -785]
- SizeStatic - RandShed48 | rej_LA | 380 [376, 383] | [380, 377, 379, 382]
- SizeStatic - RandShed48 | attack_block_rate | 0.947 [0.939, 0.954] | [0.946, 0.951, 0.949, 0.94]
- SizeStatic - RandShed48 | gc_pause_ms | -4550 [-6632, -2469] | [-5518, -5786, -3798, -3099]
- OracleBlock - RandShed48 | benign_ok30 | 1560 [1375, 1745] | [1498, 1707, 1442, 1593]
- OracleBlock - RandShed48 | nonLA_ok30 | 1534 [1346, 1722] | [1453, 1679, 1424, 1580]
- OracleBlock - RandShed48 | benign_not_sent | -1192 [-1229, -1155] | [-1166, -1196, -1222, -1185]
- OracleBlock - RandShed48 | rej_LA | -20 [-24, -17] | [-20, -23, -21, -18]
- OracleBlock - RandShed48 | attack_block_rate | 0.947 [0.939, 0.954] | [0.946, 0.951, 0.949, 0.94]
- OracleBlock - RandShed48 | gc_pause_ms | -2810 [-4603, -1017] | [-3882, -3126, -1222, -3011]

## Block Z

| arm | n | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LearnedScore | 4 | 0.000 | 0 [0, 0, 0, 0] | 0 | 6666 [6514, 6525, 6687, 6936] | 8180 | 8 | 9542 | 3 | 3 | 0 | 2 | n/a | 177 |
| OracleBlock | 4 | 0.996 | 0 [0, 0, 0, 0] | 0 | 7461 [7763, 7307, 7364, 7411] | 6842 | 0 | 9958 | 4 | 4 | 0 | 2 | n/a | 192 |
| PressureOnly | 4 | 0.249 | 5025 [9729, 10370, 0, 0] | 0 | 10079 [13661, 12800, 6918, 6936] | 8033 | 48 | 816 | 0 | 0 | 0 | 1 | n/a | 0 |
| SizeStatic | 4 | 1.000 | 0 [0, 0, 0, 0] | 0 | 7246 [6937, 7348, 7400, 7301] | 10273 | 8 | 6502 | 3 | 3 | 0 | 2 | n/a | 122 |
| none | 4 | 0.000 | 0 [0, 0, 0, 0] | 0 | 6694 [6728, 6467, 6918, 6662] | 7604 | 6 | 10164 | 3 | 3 | 0 | 1 | n/a | n/a |

### Block Z paired differences (A - B), t 95% CI [per-pair]

- OracleBlock - none | benign_ok30 | 768 [377, 1158] | [1035, 840, 446, 749]
- OracleBlock - none | nonLA_ok30 | 768 [377, 1158] | [1035, 840, 446, 749]
- OracleBlock - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- OracleBlock - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- OracleBlock - none | attack_block_rate | 0.996 [0.985, 1.006] | [1.0, 0.997, 1.0, 0.986]
- PressureOnly - none | benign_ok30 | 3385 [-2597, 9367] | [6933, 6333, 0, 274]
- PressureOnly - none | nonLA_ok30 | 3385 [-2597, 9367] | [6933, 6333, 0, 274]
- PressureOnly - none | benign_not_sent | 5025 [-4216, 14265] | [9729, 10370, 0, 0]
- PressureOnly - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | attack_block_rate | 0.249 [-0.209, 0.706] | [0.477, 0.517, 0.0, 0.0]
- SizeStatic - none | benign_ok30 | 553 [104, 1001] | [209, 881, 482, 639]
- SizeStatic - none | nonLA_ok30 | 553 [104, 1001] | [209, 881, 482, 639]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- LearnedScore - none | benign_ok30 | -28 [-412, 355] | [-214, 58, -231, 274]
- LearnedScore - none | nonLA_ok30 | -28 [-412, 355] | [-214, 58, -231, 274]
- LearnedScore - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- LearnedScore - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- LearnedScore - none | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0, 0.0]
- SizeStatic - OracleBlock | benign_ok30 | -215 [-873, 443] | [-826, 41, 36, -110]
- SizeStatic - OracleBlock | nonLA_ok30 | -215 [-873, 443] | [-826, 41, 36, -110]
- SizeStatic - OracleBlock | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - OracleBlock | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - OracleBlock | attack_block_rate | 0.004 [-0.006, 0.015] | [0.0, 0.003, 0.0, 0.014]
- SizeStatic - PressureOnly | benign_ok30 | -2832 [-8871, 3206] | [-6724, -5452, 482, 365]
- SizeStatic - PressureOnly | nonLA_ok30 | -2832 [-8871, 3206] | [-6724, -5452, 482, 365]
- SizeStatic - PressureOnly | benign_not_sent | -5025 [-14265, 4216] | [-9729, -10370, 0, 0]
- SizeStatic - PressureOnly | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - PressureOnly | attack_block_rate | 0.751 [0.294, 1.209] | [0.523, 0.483, 1.0, 1.0]

## Block N

| arm | n | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OracleBlock | 5 | 1.000 | 0 [0, 0, 0, 0, 0] | 0 | 17466 [17544, 17492, 17428, 17479, 17388] | 6534 | 0 | 0 | 5 | 0 | 0 | 1 | n/a | 0 |
| PressureOnly | 5 | 0.008 | 1896 [1714, 1749, 2163, 2008, 1846] | 0 | 13098 [13115, 12982, 13313, 13054, 13026] | 9006 | 0 | 0 | 2 | 0 | 0 | 1 | n/a | 0 |
| SizeStatic | 5 | 1.000 | 0 [0, 0, 0, 0, 0] | 0 | 17530 [17586, 17631, 17434, 17416, 17582] | 6470 | 0 | 0 | 5 | 0 | 0 | 1 | n/a | 0 |
| none | 5 | 0.000 | 0 [0, 0, 0, 0, 0] | 0 | 13050 [13034, 13025, 13234, 12940, 13016] | 10950 | 0 | 0 | 2 | 0 | 0 | 1 | n/a | n/a |

### Block N paired differences (A - B), t 95% CI [per-pair]

- OracleBlock - none | benign_ok30 | 4416 [4243, 4590] | [4510, 4467, 4194, 4539, 4372]
- OracleBlock - none | nonLA_ok30 | 4416 [4243, 4590] | [4510, 4467, 4194, 4539, 4372]
- OracleBlock - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- OracleBlock - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0, 0]
- OracleBlock - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0, 1.0]
- PressureOnly - none | benign_ok30 | 48 [-31, 127] | [81, -43, 79, 114, 10]
- PressureOnly - none | nonLA_ok30 | 48 [-31, 127] | [81, -43, 79, 114, 10]
- PressureOnly - none | benign_not_sent | 1896 [1663, 2129] | [1714, 1749, 2163, 2008, 1846]
- PressureOnly - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0, 0]
- PressureOnly - none | attack_block_rate | 0.008 [-0.006, 0.023] | [0.001, 0.004, 0.008, 0.028, 0.0]
- SizeStatic - none | benign_ok30 | 4480 [4277, 4683] | [4552, 4606, 4200, 4476, 4566]
- SizeStatic - none | nonLA_ok30 | 4480 [4277, 4683] | [4552, 4606, 4200, 4476, 4566]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0, 1.0]
- SizeStatic - OracleBlock | benign_ok30 | 64 [-64, 192] | [42, 139, 6, -63, 194]
- SizeStatic - OracleBlock | nonLA_ok30 | 64 [-64, 192] | [42, 139, 6, -63, 194]
- SizeStatic - OracleBlock | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - OracleBlock | rej_LA | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - OracleBlock | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0, 0.0, 0.0]
- SizeStatic - PressureOnly | benign_ok30 | 4432 [4179, 4684] | [4471, 4649, 4121, 4362, 4556]
- SizeStatic - PressureOnly | nonLA_ok30 | 4432 [4179, 4684] | [4471, 4649, 4121, 4362, 4556]
- SizeStatic - PressureOnly | benign_not_sent | -1896 [-2129, -1663] | [-1714, -1749, -2163, -2008, -1846]
- SizeStatic - PressureOnly | rej_LA | 0 [0, 0] | [0, 0, 0, 0, 0]
- SizeStatic - PressureOnly | attack_block_rate | 0.992 [0.977, 1.006] | [0.999, 0.996, 0.992, 0.972, 1.0]

## Block TS

| arm | n | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PressureOnly | 3 | 0.138 | 3206 [3461, 2987, 3170] | 0 | 19134 [18965, 19117, 19319] | 460 | 0 | 0 | 0 | 0 | 0 | 1 | 21428 | 0 |
| SizeGraded | 3 | 0.217 | 0 [0, 0, 0] | 0 | 12167 [12003, 12363, 12136] | 10633 | 0 | 0 | 0 | 0 | 0 | 1 | 29083 | 0 |
| SizeStatic | 3 | 1.000 | 0 [0, 0, 0] | 0 | 22675 [22680, 22680, 22665] | 5 | 12 | 108 | 0 | 0 | 0 | 1 | 16782 | 0 |
| SizeSticky | 3 | 0.722 | 0 [0, 0, 0] | 0 | 21039 [21330, 21608, 20180] | 1734 | 3 | 24 | 0 | 0 | 0 | 1 | 21512 | 0 |
| none | 3 | 0.000 | 0 [0, 0, 0] | 0 | 11936 [11968, 11707, 12134] | 10862 | 0 | 2 | 0 | 0 | 0 | 1 | 33089 | n/a |

### Block TS paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 10739 [10187, 11291] | [10712, 10973, 10531]
- SizeStatic - none | nonLA_ok30 | 10739 [10187, 11291] | [10712, 10973, 10531]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0]
- SizeStatic - none | gc_pause_ms | -16307 [-20982, -11633] | [-14520, -18271, -16131]
- SizeGraded - none | benign_ok30 | 231 [-684, 1146] | [35, 656, 2]
- SizeGraded - none | nonLA_ok30 | 231 [-684, 1146] | [35, 656, 2]
- SizeGraded - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeGraded - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeGraded - none | attack_block_rate | 0.217 [0.123, 0.311] | [0.204, 0.26, 0.188]
- SizeGraded - none | gc_pause_ms | -4007 [-13590, 5576] | [-1624, -8457, -1939]
- SizeSticky - none | benign_ok30 | 9103 [6732, 11474] | [9362, 9901, 8046]
- SizeSticky - none | nonLA_ok30 | 9103 [6732, 11474] | [9362, 9901, 8046]
- SizeSticky - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeSticky - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeSticky - none | attack_block_rate | 0.722 [0.640, 0.805] | [0.742, 0.74, 0.684]
- SizeSticky - none | gc_pause_ms | -11578 [-15132, -8023] | [-10370, -13158, -11205]
- PressureOnly - none | benign_ok30 | 7197 [6684, 7711] | [6997, 7410, 7185]
- PressureOnly - none | nonLA_ok30 | 7197 [6684, 7711] | [6997, 7410, 7185]
- PressureOnly - none | benign_not_sent | 3206 [2612, 3800] | [3461, 2987, 3170]
- PressureOnly - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- PressureOnly - none | attack_block_rate | 0.138 [0.098, 0.177] | [0.155, 0.135, 0.123]
- PressureOnly - none | gc_pause_ms | -11661 [-12423, -10899] | [-11895, -11314, -11774]
- SizeSticky - SizeGraded | benign_ok30 | 8872 [7088, 10656] | [9327, 9245, 8044]
- SizeSticky - SizeGraded | nonLA_ok30 | 8872 [7088, 10656] | [9327, 9245, 8044]
- SizeSticky - SizeGraded | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeSticky - SizeGraded | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeSticky - SizeGraded | attack_block_rate | 0.505 [0.432, 0.578] | [0.538, 0.481, 0.496]
- SizeSticky - SizeGraded | gc_pause_ms | -7571 [-13779, -1363] | [-8746, -4701, -9266]
- SizeSticky - SizeStatic | benign_ok30 | -1636 [-3495, 224] | [-1350, -1072, -2485]
- SizeSticky - SizeStatic | nonLA_ok30 | -1636 [-3495, 224] | [-1350, -1072, -2485]
- SizeSticky - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeSticky - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeSticky - SizeStatic | attack_block_rate | -0.278 [-0.360, -0.195] | [-0.258, -0.26, -0.316]
- SizeSticky - SizeStatic | gc_pause_ms | 4730 [3461, 5998] | [4150, 5113, 4926]
- SizeStatic - SizeGraded | benign_ok30 | 10508 [10058, 10957] | [10677, 10317, 10529]
- SizeStatic - SizeGraded | nonLA_ok30 | 10508 [10058, 10957] | [10677, 10317, 10529]
- SizeStatic - SizeGraded | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeStatic - SizeGraded | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeStatic - SizeGraded | attack_block_rate | 0.783 [0.689, 0.877] | [0.796, 0.74, 0.812]
- SizeStatic - SizeGraded | gc_pause_ms | -12301 [-17888, -6714] | [-12896, -9814, -14192]

## Block TP

| arm | n | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PressureOnly | 3 | 0.071 | 3072 [3535, 3099, 2583] | 0 | 21699 [21346, 21755, 21995] | 122 | 1 | 6 | 0 | 0 | 0 | 1 | 20780 | 0 |
| SizeGraded | 3 | 0.127 | 0 [0, 0, 0] | 0 | 16414 [16565, 16666, 16011] | 8486 | 0 | 0 | 0 | 0 | 0 | 1 | 31817 | 0 |
| SizeStatic | 3 | 1.000 | 0 [0, 0, 0] | 0 | 18442 [18511, 18578, 18238] | 6458 | 0 | 0 | 0 | 0 | 0 | 1 | 28710 | 0 |
| SizeSticky | 3 | 0.534 | 0 [0, 0, 0] | 0 | 17476 [17054, 17818, 17555] | 7424 | 0 | 0 | 0 | 0 | 0 | 1 | 29042 | 0 |
| none | 3 | 0.000 | 0 [0, 0, 0] | 0 | 16257 [16132, 16338, 16300] | 8643 | 0 | 0 | 0 | 0 | 0 | 1 | 30290 | n/a |

### Block TP paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 2186 [1626, 2746] | [2379, 2240, 1938]
- SizeStatic - none | nonLA_ok30 | 2186 [1626, 2746] | [2379, 2240, 1938]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0]
- SizeStatic - none | gc_pause_ms | -1580 [-6102, 2942] | [-128, -990, -3622]
- SizeGraded - none | benign_ok30 | 157 [-812, 1126] | [433, 328, -289]
- SizeGraded - none | nonLA_ok30 | 157 [-812, 1126] | [433, 328, -289]
- SizeGraded - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeGraded - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeGraded - none | attack_block_rate | 0.127 [0.026, 0.227] | [0.17, 0.12, 0.09]
- SizeGraded - none | gc_pause_ms | 1527 [-3323, 6377] | [-213, 1155, 3638]
- SizeSticky - none | benign_ok30 | 1219 [522, 1916] | [922, 1480, 1255]
- SizeSticky - none | nonLA_ok30 | 1219 [522, 1916] | [922, 1480, 1255]
- SizeSticky - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeSticky - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeSticky - none | attack_block_rate | 0.534 [0.148, 0.921] | [0.357, 0.6, 0.647]
- SizeSticky - none | gc_pause_ms | -1249 [-7451, 4953] | [-2239, 1591, -3098]
- PressureOnly - none | benign_ok30 | 5442 [4842, 6042] | [5214, 5417, 5695]
- PressureOnly - none | nonLA_ok30 | 5442 [4842, 6042] | [5214, 5417, 5695]
- PressureOnly - none | benign_not_sent | 3072 [1888, 4256] | [3535, 3099, 2583]
- PressureOnly - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- PressureOnly - none | attack_block_rate | 0.071 [-0.014, 0.156] | [0.1, 0.033, 0.08]
- PressureOnly - none | gc_pause_ms | -9510 [-16199, -2821] | [-12529, -8644, -7357]
- SizeSticky - SizeGraded | benign_ok30 | 1062 [-263, 2386] | [489, 1152, 1544]
- SizeSticky - SizeGraded | nonLA_ok30 | 1062 [-263, 2386] | [489, 1152, 1544]
- SizeSticky - SizeGraded | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeSticky - SizeGraded | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeSticky - SizeGraded | attack_block_rate | 0.408 [-0.077, 0.893] | [0.187, 0.48, 0.557]
- SizeSticky - SizeGraded | gc_pause_ms | -2775 [-11829, 6278] | [-2026, 436, -6736]
- SizeSticky - SizeStatic | benign_ok30 | -967 [-2026, 93] | [-1457, -760, -683]
- SizeSticky - SizeStatic | nonLA_ok30 | -967 [-2026, 93] | [-1457, -760, -683]
- SizeSticky - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeSticky - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeSticky - SizeStatic | attack_block_rate | -0.466 [-0.852, -0.079] | [-0.643, -0.4, -0.353]
- SizeSticky - SizeStatic | gc_pause_ms | 331 [-5512, 6174] | [-2111, 2581, 524]
- SizeStatic - SizeGraded | benign_ok30 | 2028 [1599, 2458] | [1946, 1912, 2227]
- SizeStatic - SizeGraded | nonLA_ok30 | 2028 [1599, 2458] | [1946, 1912, 2227]
- SizeStatic - SizeGraded | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeStatic - SizeGraded | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeStatic - SizeGraded | attack_block_rate | 0.873 [0.773, 0.974] | [0.83, 0.88, 0.91]
- SizeStatic - SizeGraded | gc_pause_ms | -3107 [-12462, 6249] | [85, -2145, -7260]

Provisioning/assertion check (assert.txt FAIL lines per run; PASS lines include heap-limit enforcement): Z/LearnedScore/63304: fail=2 pass=4, Z/PressureOnly/63303: fail=2 pass=4, Z/PressureOnly/63304: fail=2 pass=4, Z/SizeStatic/63301: fail=2 pass=4, Z/none/63303: fail=2 pass=4

## Caveats fixed in advance
- threshold 65,604 B post-hoc; SizeStatic/SizeGraded/SizeSticky differ in intensity as well as feedback/hold; SizeSticky = SizeGraded with a 30 s sliding-maximum pressure hold (30 s chosen a priori); mixed block = 2 attack workers (800) + 1 look-alike worker (400) in the same window; sustained block = 2,400 attack tx, pulse block = 300 attack tx (different attack volume from the 1,200 baseline); GC pause only for G1 blocks; ZGC/NM survival and OOM-exception lines are descriptive; NM OOM exceptions at END+5-20 s coincide with post-run scans; shared node.
