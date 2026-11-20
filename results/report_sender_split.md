# Results report sender_split (generated 2026-11-19 18:54)

Numbers only. Registered in PREREG_UNIFIED_v1.md addendum sender_split (exploratory). Nodes cpu01-cpu03 (one block never split across nodes), shared non-exclusive. Receipt = within the connector 30 s limit. Same-seed pairs, t 95% CI over pair differences, per-pair values shown, no p-values. Chain-scan counts not used.

## Inventory (completed with summary / present)
- block X1: BudgetR250 4, SenderBucket 4, SizeStatic 4, none 4 (scheduled 16)
- block X2: BudgetR250 4, SenderBucket 4, SizeStatic 4, none 4 (scheduled 16)
- block X3: BudgetR250 4, SenderBucket 4, SizeStatic 4, none 4 (scheduled 16)
- block X4: BudgetR250 4, SenderBucket 4, SizeStatic 4, none 4 (scheduled 16)
- runs without summary (apparatus failure, NOT replaced): none

## Block X1

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | 4 | 306 / 0.251 | 0.729 | 311 [357, 380, 111, 396] | 311 | 19895 [19821, 19773, 20088, 19897] | 4185 | 0 | 0 | 0 | 0 | 0 | 1 | 23897 | 0 |
| SenderBucket | 4 | 369 / 0.302 | 0.693 | 277 [277, 277, 277, 277] | 277 | 19507 [19420, 19408, 19499, 19701] | 4603 | 0 | 0 | 0 | 0 | 0 | 1 | 24882 | 25200 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 400 [400, 400, 400, 400] | 400 | 22045 [22051, 22091, 22060, 21978] | 1955 | 0 | 0 | 0 | 0 | 0 | 1 | 22156 | 0 |
| none | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 14536 [14619, 14483, 14437, 14603] | 9807 | 0 | 0 | 0 | 0 | 0 | 1 | 30208 | n/a |

### Block X1 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 7510 [7311, 7708] | [7432, 7608, 7623, 7375]
- SizeStatic - none | nonLA_ok30 | 7852 [7656, 8047] | [7747, 7934, 7980, 7746]
- SizeStatic - none | benign_not_sent | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | rej_LA | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1200 [-1200, -1200] | [-1200, -1200, -1200, -1200]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- SizeStatic - none | gc_pause_ms | -8052 [-10269, -5835] | [-6199, -9229, -9014, -7766]
- BudgetR250 - none | benign_ok30 | 5359 [5043, 5676] | [5202, 5290, 5651, 5294]
- BudgetR250 - none | nonLA_ok30 | 5622 [5473, 5771] | [5501, 5604, 5719, 5664]
- BudgetR250 - none | benign_not_sent | 311 [97, 525] | [357, 380, 111, 396]
- BudgetR250 - none | rej_LA | 311 [97, 525] | [357, 380, 111, 396]
- BudgetR250 - none | attack_block_rate | 0.729 [0.462, 0.996] | [0.671, 0.642, 0.979, 0.623]
- BudgetR250 - none | heavy_admitted | -894 [-894, -894] | [-894, -894, -894, -894]
- BudgetR250 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- BudgetR250 - none | gc_pause_ms | -6311 [-8645, -3977] | [-4852, -7836, -7278, -5278]
- SenderBucket - none | benign_ok30 | 4972 [4755, 5188] | [4801, 4925, 5062, 5098]
- SenderBucket - none | nonLA_ok30 | 5204 [4955, 5452] | [5010, 5145, 5313, 5346]
- SenderBucket - none | benign_not_sent | 277 [277, 277] | [277, 277, 277, 277]
- SenderBucket - none | rej_LA | 277 [277, 277] | [277, 277, 277, 277]
- SenderBucket - none | attack_block_rate | 0.693 [0.693, 0.693] | [0.693, 0.693, 0.693, 0.693]
- SenderBucket - none | heavy_admitted | -831 [-831, -831] | [-831, -831, -831, -831]
- SenderBucket - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- SenderBucket - none | gc_pause_ms | -5326 [-7181, -3471] | [-3906, -5136, -6735, -5528]
- SenderBucket - SizeStatic | benign_ok30 | -2538 [-2826, -2250] | [-2631, -2683, -2561, -2277]
- SenderBucket - SizeStatic | nonLA_ok30 | -2648 [-2923, -2373] | [-2737, -2789, -2667, -2400]
- SenderBucket - SizeStatic | benign_not_sent | -123 [-123, -123] | [-123, -123, -123, -123]
- SenderBucket - SizeStatic | rej_LA | -123 [-123, -123] | [-123, -123, -123, -123]
- SenderBucket - SizeStatic | attack_block_rate | -0.307 [-0.307, -0.307] | [-0.307, -0.307, -0.307, -0.307]
- SenderBucket - SizeStatic | heavy_admitted | 369 [369, 369] | [369, 369, 369, 369]
- SenderBucket - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - SizeStatic | gc_pause_ms | 2726 [1275, 4176] | [2293, 4093, 2279, 2238]
- SenderBucket - BudgetR250 | benign_ok30 | -388 [-644, -131] | [-401, -365, -589, -196]
- SenderBucket - BudgetR250 | nonLA_ok30 | -418 [-539, -298] | [-491, -459, -406, -318]
- SenderBucket - BudgetR250 | benign_not_sent | -34 [-248, 180] | [-80, -103, 166, -119]
- SenderBucket - BudgetR250 | rej_LA | -34 [-248, 180] | [-80, -103, 166, -119]
- SenderBucket - BudgetR250 | attack_block_rate | -0.036 [-0.303, 0.231] | [0.021, 0.05, -0.286, 0.07]
- SenderBucket - BudgetR250 | heavy_admitted | 63 [63, 63] | [63, 63, 63, 63]
- SenderBucket - BudgetR250 | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - BudgetR250 | gc_pause_ms | 985 [-999, 2968] | [946, 2700, 543, -250]
- BudgetR250 - SizeStatic | benign_ok30 | -2150 [-2395, -1905] | [-2230, -2318, -1972, -2081]
- BudgetR250 - SizeStatic | nonLA_ok30 | -2230 [-2397, -2063] | [-2246, -2330, -2261, -2082]
- BudgetR250 - SizeStatic | benign_not_sent | -89 [-303, 125] | [-43, -20, -289, -4]
- BudgetR250 - SizeStatic | rej_LA | -89 [-303, 125] | [-43, -20, -289, -4]
- BudgetR250 - SizeStatic | attack_block_rate | -0.271 [-0.538, -0.004] | [-0.329, -0.358, -0.021, -0.377]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 1741 [902, 2580] | [1347, 1393, 1736, 2488]

## Block X2

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | 4 | 306 / 0.251 | 0.670 | 360 [367, 339, 351, 383] | 360 | 19615 [19710, 19591, 19566, 19593] | 4425 | 0 | 0 | 0 | 0 | 0 | 1 | 24530 | 0 |
| SenderBucket | 4 | 648 / 0.531 | 0.693 | 0 [0, 0, 0, 0] | 0 | 17701 [17638, 18118, 17348, 17699] | 6692 | 0 | 0 | 0 | 0 | 0 | 1 | 26801 | 25200 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 402 [402, 402, 402, 402] | 402 | 21689 [21683, 21970, 21494, 21608] | 2309 | 0 | 0 | 0 | 0 | 0 | 1 | 22075 | 0 |
| none | 4 | 1202 / 0.985 | 0.000 | 0 [0, 0, 0, 0] | 0 | 14360 [14355, 14461, 14134, 14491] | 9998 | 0 | 0 | 0 | 0 | 0 | 1 | 30392 | n/a |

### Block X2 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 7328 [7071, 7586] | [7328, 7509, 7360, 7117]
- SizeStatic - none | nonLA_ok30 | 7689 [7434, 7944] | [7685, 7872, 7718, 7482]
- SizeStatic - none | benign_not_sent | 402 [402, 402] | [402, 402, 402, 402]
- SizeStatic - none | rej_LA | 402 [402, 402] | [402, 402, 402, 402]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1202 [-1202, -1202] | [-1202, -1202, -1202, -1202]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- SizeStatic - none | gc_pause_ms | -8317 [-10238, -6395] | [-8506, -9606, -6687, -8468]
- BudgetR250 - none | benign_ok30 | 5255 [4994, 5515] | [5355, 5130, 5432, 5102]
- BudgetR250 - none | nonLA_ok30 | 5574 [5323, 5824] | [5677, 5430, 5739, 5448]
- BudgetR250 - none | benign_not_sent | 360 [330, 390] | [367, 339, 351, 383]
- BudgetR250 - none | rej_LA | 360 [330, 390] | [367, 339, 351, 383]
- BudgetR250 - none | attack_block_rate | 0.670 [0.632, 0.708] | [0.661, 0.696, 0.681, 0.641]
- BudgetR250 - none | heavy_admitted | -896 [-896, -896] | [-896, -896, -896, -896]
- BudgetR250 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- BudgetR250 - none | gc_pause_ms | -5862 [-7707, -4017] | [-6059, -7405, -4767, -5217]
- SenderBucket - none | benign_ok30 | 3340 [3000, 3681] | [3283, 3657, 3214, 3208]
- SenderBucket - none | nonLA_ok30 | 3306 [2966, 3647] | [3252, 3623, 3178, 3173]
- SenderBucket - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - none | attack_block_rate | 0.693 [0.693, 0.693] | [0.693, 0.693, 0.693, 0.693]
- SenderBucket - none | heavy_admitted | -554 [-554, -554] | [-554, -554, -554, -554]
- SenderBucket - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- SenderBucket - none | gc_pause_ms | -3591 [-6110, -1072] | [-2568, -5572, -2090, -4134]
- SenderBucket - SizeStatic | benign_ok30 | -3988 [-4199, -3777] | [-4045, -3852, -4146, -3909]
- SenderBucket - SizeStatic | nonLA_ok30 | -4383 [-4589, -4176] | [-4433, -4249, -4540, -4309]
- SenderBucket - SizeStatic | benign_not_sent | -402 [-402, -402] | [-402, -402, -402, -402]
- SenderBucket - SizeStatic | rej_LA | -402 [-402, -402] | [-402, -402, -402, -402]
- SenderBucket - SizeStatic | attack_block_rate | -0.307 [-0.307, -0.307] | [-0.307, -0.307, -0.307, -0.307]
- SenderBucket - SizeStatic | heavy_admitted | 648 [648, 648] | [648, 648, 648, 648]
- SenderBucket - SizeStatic | heavy_admitted_MBps | 1 [1, 1] | [1, 1, 1, 1]
- SenderBucket - SizeStatic | gc_pause_ms | 4726 [3389, 6063] | [5938, 4034, 4597, 4334]
- SenderBucket - BudgetR250 | benign_ok30 | -1914 [-2428, -1401] | [-2072, -1473, -2218, -1894]
- SenderBucket - BudgetR250 | nonLA_ok30 | -2267 [-2789, -1745] | [-2425, -1807, -2561, -2275]
- SenderBucket - BudgetR250 | benign_not_sent | -360 [-390, -330] | [-367, -339, -351, -383]
- SenderBucket - BudgetR250 | rej_LA | -360 [-390, -330] | [-367, -339, -351, -383]
- SenderBucket - BudgetR250 | attack_block_rate | 0.022 [-0.016, 0.061] | [0.031, -0.004, 0.011, 0.051]
- SenderBucket - BudgetR250 | heavy_admitted | 342 [342, 342] | [342, 342, 342, 342]
- SenderBucket - BudgetR250 | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - BudgetR250 | gc_pause_ms | 2271 [613, 3929] | [3491, 1833, 2677, 1083]
- BudgetR250 - SizeStatic | benign_ok30 | -2074 [-2402, -1745] | [-1973, -2379, -1928, -2015]
- BudgetR250 - SizeStatic | nonLA_ok30 | -2116 [-2464, -1768] | [-2008, -2442, -1979, -2034]
- BudgetR250 - SizeStatic | benign_not_sent | -42 [-72, -12] | [-35, -63, -51, -19]
- BudgetR250 - SizeStatic | rej_LA | -42 [-72, -12] | [-35, -63, -51, -19]
- BudgetR250 - SizeStatic | attack_block_rate | -0.330 [-0.368, -0.292] | [-0.339, -0.304, -0.319, -0.359]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 2455 [1543, 3366] | [2447, 2201, 1920, 3251]

## Block X3

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | 4 | 151 / 0.124 | 0.833 | 385 [335, 402, 402, 402] | 385 | 20529 [20262, 20333, 20500, 21022] | 3482 | 0 | 0 | 0 | 0 | 0 | 1 | 24482 | 0 |
| SenderBucket | 4 | 1206 / 0.989 | 0.000 | 0 [0, 0, 0, 0] | 0 | 14320 [14313, 14106, 14342, 14517] | 10029 | 0 | 0 | 0 | 0 | 0 | 1 | 31076 | 25200 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 402 [402, 402, 402, 402] | 402 | 21422 [21434, 21240, 21332, 21682] | 2572 | 0 | 0 | 0 | 0 | 0 | 1 | 22996 | 0 |
| none | 4 | 1206 / 0.989 | 0.000 | 0 [0, 0, 0, 0] | 0 | 14256 [14331, 14017, 13964, 14710] | 10092 | 0 | 0 | 0 | 0 | 0 | 1 | 30525 | n/a |

### Block X3 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 7166 [6898, 7435] | [7103, 7223, 7368, 6972]
- SizeStatic - none | nonLA_ok30 | 7520 [7258, 7781] | [7461, 7571, 7717, 7330]
- SizeStatic - none | benign_not_sent | 402 [402, 402] | [402, 402, 402, 402]
- SizeStatic - none | rej_LA | 402 [402, 402] | [402, 402, 402, 402]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1206 [-1206, -1206] | [-1206, -1206, -1206, -1206]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- SizeStatic - none | gc_pause_ms | -7529 [-9996, -5062] | [-6372, -6014, -8920, -8811]
- BudgetR250 - none | benign_ok30 | 6274 [5874, 6674] | [5931, 6316, 6536, 6312]
- BudgetR250 - none | nonLA_ok30 | 6610 [6167, 7053] | [6222, 6664, 6885, 6670]
- BudgetR250 - none | benign_not_sent | 385 [332, 439] | [335, 402, 402, 402]
- BudgetR250 - none | rej_LA | 385 [332, 439] | [335, 402, 402, 402]
- BudgetR250 - none | attack_block_rate | 0.833 [0.833, 0.833] | [0.833, 0.833, 0.833, 0.833]
- BudgetR250 - none | heavy_admitted | -1055 [-1109, -1002] | [-1005, -1072, -1072, -1072]
- BudgetR250 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- BudgetR250 - none | gc_pause_ms | -6043 [-7532, -4554] | [-4993, -5631, -6397, -7152]
- SenderBucket - none | benign_ok30 | 64 [-317, 445] | [-18, 89, 378, -193]
- SenderBucket - none | nonLA_ok30 | 63 [-312, 437] | [-13, 99, 364, -199]
- SenderBucket - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - none | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0, 0.0]
- SenderBucket - none | heavy_admitted | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - none | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- SenderBucket - none | gc_pause_ms | 551 [-3320, 4422] | [2071, 3163, -1732, -1297]
- SenderBucket - SizeStatic | benign_ok30 | -7102 [-7225, -6980] | [-7121, -7134, -6990, -7165]
- SenderBucket - SizeStatic | nonLA_ok30 | -7457 [-7575, -7339] | [-7474, -7472, -7353, -7529]
- SenderBucket - SizeStatic | benign_not_sent | -402 [-402, -402] | [-402, -402, -402, -402]
- SenderBucket - SizeStatic | rej_LA | -402 [-402, -402] | [-402, -402, -402, -402]
- SenderBucket - SizeStatic | attack_block_rate | -1.000 [-1.000, -1.000] | [-1.0, -1.0, -1.0, -1.0]
- SenderBucket - SizeStatic | heavy_admitted | 1206 [1206, 1206] | [1206, 1206, 1206, 1206]
- SenderBucket - SizeStatic | heavy_admitted_MBps | 1 [1, 1] | [1, 1, 1, 1]
- SenderBucket - SizeStatic | gc_pause_ms | 8080 [6642, 9519] | [8443, 9177, 7188, 7514]
- SenderBucket - BudgetR250 | benign_ok30 | -6210 [-6575, -5844] | [-5949, -6227, -6158, -6505]
- SenderBucket - BudgetR250 | nonLA_ok30 | -6548 [-6960, -6135] | [-6235, -6565, -6521, -6869]
- SenderBucket - BudgetR250 | benign_not_sent | -385 [-439, -332] | [-335, -402, -402, -402]
- SenderBucket - BudgetR250 | rej_LA | -385 [-439, -332] | [-335, -402, -402, -402]
- SenderBucket - BudgetR250 | attack_block_rate | -0.833 [-0.833, -0.833] | [-0.833, -0.833, -0.833, -0.833]
- SenderBucket - BudgetR250 | heavy_admitted | 1055 [1002, 1109] | [1005, 1072, 1072, 1072]
- SenderBucket - BudgetR250 | heavy_admitted_MBps | 1 [1, 1] | [1, 1, 1, 1]
- SenderBucket - BudgetR250 | gc_pause_ms | 6594 [3789, 9400] | [7064, 8794, 4665, 5855]
- BudgetR250 - SizeStatic | benign_ok30 | -893 [-1232, -554] | [-1172, -907, -832, -660]
- BudgetR250 - SizeStatic | nonLA_ok30 | -910 [-1296, -523] | [-1239, -907, -832, -660]
- BudgetR250 - SizeStatic | benign_not_sent | -17 [-70, 37] | [-67, 0, 0, 0]
- BudgetR250 - SizeStatic | rej_LA | -17 [-70, 37] | [-67, 0, 0, 0]
- BudgetR250 - SizeStatic | attack_block_rate | -0.167 [-0.167, -0.167] | [-0.167, -0.167, -0.167, -0.167]
- BudgetR250 - SizeStatic | heavy_admitted | 151 [97, 204] | [201, 134, 134, 134]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 1486 [83, 2889] | [1379, 383, 2523, 1659]

## Block X4

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | 4 | 306 / 0.251 | 0.937 | 145 [144, 153, 150, 133] | 145 | 19792 [19825, 19843, 19808, 19693] | 4459 | 0 | 0 | 0 | 0 | 0 | 1 | 24571 | 0 |
| SenderBucket | 4 | 927 / 0.760 | 0.000 | 277 [277, 277, 277, 277] | 277 | 15583 [15781, 15669, 15401, 15481] | 8518 | 0 | 0 | 0 | 0 | 0 | 1 | 28355 | 25200 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 400 [400, 400, 400, 400] | 400 | 21524 [21646, 21581, 21508, 21362] | 2472 | 0 | 0 | 0 | 0 | 0 | 1 | 22215 | 0 |
| none | 4 | 1204 / 0.987 | 0.000 | 0 [0, 0, 0, 0] | 0 | 14529 [14717, 14612, 14381, 14407] | 9824 | 0 | 0 | 0 | 0 | 0 | 1 | 29829 | n/a |

### Block X4 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 6995 [6853, 7137] | [6929, 6969, 7127, 6955]
- SizeStatic - none | nonLA_ok30 | 7352 [7202, 7503] | [7269, 7320, 7488, 7333]
- SizeStatic - none | benign_not_sent | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | rej_LA | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1204 [-1204, -1204] | [-1204, -1204, -1204, -1204]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- SizeStatic - none | gc_pause_ms | -7614 [-9340, -5888] | [-8355, -8732, -6737, -6632]
- BudgetR250 - none | benign_ok30 | 5263 [5053, 5473] | [5108, 5231, 5427, 5286]
- BudgetR250 - none | nonLA_ok30 | 5366 [5137, 5594] | [5192, 5335, 5538, 5397]
- BudgetR250 - none | benign_not_sent | 145 [131, 159] | [144, 153, 150, 133]
- BudgetR250 - none | rej_LA | 145 [131, 159] | [144, 153, 150, 133]
- BudgetR250 - none | attack_block_rate | 0.937 [0.919, 0.954] | [0.938, 0.927, 0.93, 0.951]
- BudgetR250 - none | heavy_admitted | -898 [-898, -898] | [-898, -898, -898, -898]
- BudgetR250 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- BudgetR250 - none | gc_pause_ms | -5258 [-6201, -4315] | [-5602, -5072, -4512, -5845]
- SenderBucket - none | benign_ok30 | 1054 [1016, 1091] | [1064, 1057, 1020, 1074]
- SenderBucket - none | nonLA_ok30 | 1306 [1236, 1377] | [1293, 1310, 1258, 1364]
- SenderBucket - none | benign_not_sent | 277 [277, 277] | [277, 277, 277, 277]
- SenderBucket - none | rej_LA | 277 [277, 277] | [277, 277, 277, 277]
- SenderBucket - none | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0, 0.0]
- SenderBucket - none | heavy_admitted | -277 [-277, -277] | [-277, -277, -277, -277]
- SenderBucket - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- SenderBucket - none | gc_pause_ms | -1474 [-3058, 111] | [-2932, -1237, -709, -1017]
- SenderBucket - SizeStatic | benign_ok30 | -5941 [-6120, -5763] | [-5865, -5912, -6107, -5881]
- SenderBucket - SizeStatic | nonLA_ok30 | -6046 [-6243, -5849] | [-5976, -6010, -6230, -5969]
- SenderBucket - SizeStatic | benign_not_sent | -123 [-123, -123] | [-123, -123, -123, -123]
- SenderBucket - SizeStatic | rej_LA | -123 [-123, -123] | [-123, -123, -123, -123]
- SenderBucket - SizeStatic | attack_block_rate | -1.000 [-1.000, -1.000] | [-1.0, -1.0, -1.0, -1.0]
- SenderBucket - SizeStatic | heavy_admitted | 927 [927, 927] | [927, 927, 927, 927]
- SenderBucket - SizeStatic | heavy_admitted_MBps | 1 [1, 1] | [1, 1, 1, 1]
- SenderBucket - SizeStatic | gc_pause_ms | 6140 [4648, 7632] | [5423, 7495, 6028, 5615]
- SenderBucket - BudgetR250 | benign_ok30 | -4209 [-4448, -3970] | [-4044, -4174, -4407, -4212]
- SenderBucket - BudgetR250 | nonLA_ok30 | -4059 [-4313, -3806] | [-3899, -4025, -4280, -4033]
- SenderBucket - BudgetR250 | benign_not_sent | 132 [118, 146] | [133, 124, 127, 144]
- SenderBucket - BudgetR250 | rej_LA | 132 [118, 146] | [133, 124, 127, 144]
- SenderBucket - BudgetR250 | attack_block_rate | -0.937 [-0.954, -0.919] | [-0.938, -0.927, -0.93, -0.951]
- SenderBucket - BudgetR250 | heavy_admitted | 621 [621, 621] | [621, 621, 621, 621]
- SenderBucket - BudgetR250 | heavy_admitted_MBps | 1 [1, 1] | [1, 1, 1, 1]
- SenderBucket - BudgetR250 | gc_pause_ms | 3784 [2381, 5187] | [2670, 3835, 3803, 4828]
- BudgetR250 - SizeStatic | benign_ok30 | -1732 [-1837, -1627] | [-1821, -1738, -1700, -1669]
- BudgetR250 - SizeStatic | nonLA_ok30 | -1987 [-2088, -1886] | [-2077, -1985, -1950, -1936]
- BudgetR250 - SizeStatic | benign_not_sent | -255 [-269, -241] | [-256, -247, -250, -267]
- BudgetR250 - SizeStatic | rej_LA | -255 [-269, -241] | [-256, -247, -250, -267]
- BudgetR250 - SizeStatic | attack_block_rate | -0.063 [-0.081, -0.046] | [-0.062, -0.073, -0.07, -0.049]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 2356 [443, 4269] | [2753, 3660, 2225, 787]

Provisioning/assertion check (assert.txt FAIL lines per run; PASS lines include heap-limit enforcement): 

## Caveats fixed in advance
- tau 65,604 B post-hoc; Budget = heavy-byte token bucket (C 200 KB; R fixed 125/250/500 KB/s or adaptive 500 KB/s x (1 - 0.75 grad(u_t)), tokens consumed only by heavy transactions; small transactions always pass) - a class-selective token-bucket policer, prior art; attack intensity blocks I1/I3/I6 use 1/3/6 burst workers (about 400/1,200/2,400 heavy transactions) so BENIGN attempts also differ between blocks (22,800 to 24,800): compare arms only within a block; L1 = one look-alike worker (about 400, 0.33 MB/s), no attack; MX = 2 attack workers + 1 look-alike worker; GC pause only for G1 blocks; ZGC/NM survival and OOM-exception lines are descriptive; shared node cpu01.
