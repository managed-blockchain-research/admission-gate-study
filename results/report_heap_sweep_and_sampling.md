# Results report heap_sweep_and_sampling (generated 2026-11-20 07:44)

Numbers only. Registered in PREREG_UNIFIED_v1.md addendum heap_sweep_and_sampling (exploratory). Blocks on separate nodes (one block never split across nodes), shared non-exclusive, class cpu01-10. Receipt = within the connector 30 s limit. Same-seed pairs, t 95% CI over pair differences, per-pair values shown, no p-values. Chain-scan counts not used.

## Inventory (completed with summary / present)
- block S1: PressureOnly 4, PressureOnlyS15 4, PressureOnlyS5 4, none 4 (scheduled 16)
- block H1: PressureOnly 4, SizeStatic 4, none 4 (scheduled 12)
- block H3: PressureOnly 4, SizeStatic 4, none 4 (scheduled 12)
- block H4: PressureOnly 4, SizeStatic 4, none 4 (scheduled 12)
- block H1L: SizeStatic 4, none 4 (scheduled 8)
- block H3L: SizeStatic 4, none 4 (scheduled 8)
- block H4L: SizeStatic 4, none 4 (scheduled 8)
- runs without summary (apparatus failure, NOT replaced): none

## Block S1

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PressureOnly | 4 | 1012 / 0.830 | 0.156 | 2943 [2931, 2849, 3186, 2805] | 0 | 20986 [20984, 20966, 20814, 21179] | 72 | 0 | 0 | 0 | 0 | 0 | 1 | 19010 | 0 |
| PressureOnlyS15 | 4 | 1077 / 0.883 | 0.103 | 2182 [1587, 1497, 2043, 3602] | 0 | 19526 [19672, 17793, 21085, 19556] | 2291 | 0 | 0 | 0 | 0 | 0 | 1 | 23376 | 0 |
| PressureOnlyS5 | 4 | 1049 / 0.860 | 0.126 | 2852 [3220, 2355, 3200, 2633] | 0 | 20586 [20348, 20465, 20490, 21041] | 512 | 2 | 48 | 0 | 0 | 0 | 1 | 20508 | 0 |
| none | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 14064 [14165, 14121, 14063, 13906] | 9936 | 0 | 0 | 0 | 0 | 0 | 1 | 29982 | n/a |

### Block S1 paired differences (A - B), t 95% CI [per-pair]

- PressureOnly - none | benign_ok30 | 6922 [6544, 7300] | [6819, 6845, 6751, 7273]
- PressureOnly - none | nonLA_ok30 | 6922 [6544, 7300] | [6819, 6845, 6751, 7273]
- PressureOnly - none | benign_not_sent | 2943 [2672, 3214] | [2931, 2849, 3186, 2805]
- PressureOnly - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | attack_block_rate | 0.156 [0.119, 0.194] | [0.138, 0.135, 0.181, 0.172]
- PressureOnly - none | heavy_admitted | -188 [-232, -143] | [-165, -162, -217, -206]
- PressureOnly - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- PressureOnly - none | gc_pause_ms | -10973 [-15286, -6660] | [-10625, -7400, -12075, -13792]
- PressureOnlyS5 - none | benign_ok30 | 6522 [5853, 7192] | [6183, 6344, 6427, 7135]
- PressureOnlyS5 - none | nonLA_ok30 | 6522 [5853, 7192] | [6183, 6344, 6427, 7135]
- PressureOnlyS5 - none | benign_not_sent | 2852 [2170, 3534] | [3220, 2355, 3200, 2633]
- PressureOnlyS5 - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnlyS5 - none | attack_block_rate | 0.126 [0.069, 0.183] | [0.172, 0.089, 0.134, 0.109]
- PressureOnlyS5 - none | heavy_admitted | -151 [-219, -83] | [-206, -107, -161, -131]
- PressureOnlyS5 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- PressureOnlyS5 - none | gc_pause_ms | -9475 [-14073, -4877] | [-10325, -5344, -10143, -12087]
- PressureOnlyS15 - none | benign_ok30 | 5463 [3275, 7651] | [5507, 3672, 7022, 5650]
- PressureOnlyS15 - none | nonLA_ok30 | 5463 [3275, 7651] | [5507, 3672, 7022, 5650]
- PressureOnlyS15 - none | benign_not_sent | 2182 [629, 3735] | [1587, 1497, 2043, 3602]
- PressureOnlyS15 - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnlyS15 - none | attack_block_rate | 0.103 [0.044, 0.161] | [0.149, 0.062, 0.11, 0.089]
- PressureOnlyS15 - none | heavy_admitted | -123 [-193, -53] | [-179, -74, -132, -107]
- PressureOnlyS15 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- PressureOnlyS15 - none | gc_pause_ms | -6606 [-13883, 671] | [-5381, -1671, -6692, -12680]
- PressureOnlyS5 - PressureOnly | benign_ok30 | -400 [-744, -56] | [-636, -501, -324, -138]
- PressureOnlyS5 - PressureOnly | nonLA_ok30 | -400 [-744, -56] | [-636, -501, -324, -138]
- PressureOnlyS5 - PressureOnly | benign_not_sent | -91 [-614, 432] | [289, -494, 14, -172]
- PressureOnlyS5 - PressureOnly | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnlyS5 - PressureOnly | attack_block_rate | -0.030 [-0.100, 0.039] | [0.034, -0.046, -0.047, -0.062]
- PressureOnlyS5 - PressureOnly | heavy_admitted | 36 [-47, 119] | [-41, 55, 56, 75]
- PressureOnlyS5 - PressureOnly | heavy_admitted_MBps | 0 [-0, 0] | [0, 0, 0, 0]
- PressureOnlyS5 - PressureOnly | gc_pause_ms | 1498 [206, 2790] | [300, 2056, 1932, 1705]
- PressureOnlyS15 - PressureOnly | benign_ok30 | -1459 [-3705, 787] | [-1312, -3173, 271, -1623]
- PressureOnlyS15 - PressureOnly | nonLA_ok30 | -1459 [-3705, 787] | [-1312, -3173, 271, -1623]
- PressureOnlyS15 - PressureOnly | benign_not_sent | -760 [-2420, 899] | [-1344, -1352, -1143, 797]
- PressureOnlyS15 - PressureOnly | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnlyS15 - PressureOnly | attack_block_rate | -0.054 [-0.124, 0.016] | [0.012, -0.073, -0.071, -0.082]
- PressureOnlyS15 - PressureOnly | heavy_admitted | 64 [-19, 148] | [-14, 88, 85, 99]
- PressureOnlyS15 - PressureOnly | heavy_admitted_MBps | 0 [-0, 0] | [0, 0, 0, 0]
- PressureOnlyS15 - PressureOnly | gc_pause_ms | 4367 [899, 7835] | [5244, 5729, 5383, 1112]

## Block H1

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PressureOnly | 4 | 535 / 0.439 | 0.370 | 5071 [3485, 408, 7857, 8535] | 0 | 8186 [8422, 8169, 8076, 8078] | 2807 | 0 | 8208 | 4 | 2 | 0 | 1 | n/a | 221 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 0 [0, 0, 0, 0] | 0 | 9049 [8754, 9364, 8912, 9166] | 1853 | 0 | 13703 | 4 | 4 | 1 | 1 | n/a | 215 |
| none | 4 | 720 / 0.590 | 0.000 | 0 [0, 0, 0, 0] | 0 | 8192 [8009, 8395, 7972, 8394] | 3986 | 0 | 12302 | 4 | 4 | 2 | 1 | n/a | n/a |

### Block H1 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 856 [675, 1038] | [745, 969, 940, 772]
- SizeStatic - none | nonLA_ok30 | 856 [675, 1038] | [745, 969, 940, 772]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -720 [-1055, -384] | [-456, -925, -848, -649]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -0] | [0, -1, -1, -1]
- PressureOnly - none | benign_ok30 | -6 [-536, 523] | [413, -226, 104, -316]
- PressureOnly - none | nonLA_ok30 | -6 [-536, 523] | [413, -226, 104, -316]
- PressureOnly - none | benign_not_sent | 5071 [-1023, 11166] | [3485, 408, 7857, 8535]
- PressureOnly - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | attack_block_rate | 0.370 [0.070, 0.671] | [0.449, 0.088, 0.459, 0.486]
- PressureOnly - none | heavy_admitted | -185 [-595, 225] | [34, -542, -199, -32]
- PressureOnly - none | heavy_admitted_MBps | -0 [-0, 0] | [0, 0, 0, 0]
- PressureOnly - SizeStatic | benign_ok30 | -863 [-1475, -251] | [-332, -1195, -836, -1088]
- PressureOnly - SizeStatic | nonLA_ok30 | -863 [-1475, -251] | [-332, -1195, -836, -1088]
- PressureOnly - SizeStatic | benign_not_sent | 5071 [-1023, 11166] | [3485, 408, 7857, 8535]
- PressureOnly - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - SizeStatic | attack_block_rate | -0.630 [-0.930, -0.329] | [-0.551, -0.912, -0.541, -0.514]
- PressureOnly - SizeStatic | heavy_admitted | 535 [340, 729] | [490, 383, 649, 617]
- PressureOnly - SizeStatic | heavy_admitted_MBps | 0 [0, 1] | [0, 0, 1, 1]

## Block H3

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PressureOnly | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 13211 [13209, 13169, 13257, 13210] | 10789 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | 0 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 0 [0, 0, 0, 0] | 0 | 17556 [17554, 17679, 17429, 17563] | 6444 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | 0 |
| none | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 13196 [13218, 13166, 13265, 13137] | 10804 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | n/a |

### Block H3 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 4360 [4122, 4597] | [4336, 4513, 4164, 4426]
- SizeStatic - none | nonLA_ok30 | 4360 [4122, 4597] | [4336, 4513, 4164, 4426]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1200 [-1200, -1200] | [-1200, -1200, -1200, -1200]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- PressureOnly - none | benign_ok30 | 15 [-48, 77] | [-9, 3, -8, 73]
- PressureOnly - none | nonLA_ok30 | 15 [-48, 77] | [-9, 3, -8, 73]
- PressureOnly - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0, 0.0]
- PressureOnly - none | heavy_admitted | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - SizeStatic | benign_ok30 | -4345 [-4565, -4125] | [-4345, -4510, -4172, -4353]
- PressureOnly - SizeStatic | nonLA_ok30 | -4345 [-4565, -4125] | [-4345, -4510, -4172, -4353]
- PressureOnly - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - SizeStatic | attack_block_rate | -1.000 [-1.000, -1.000] | [-1.0, -1.0, -1.0, -1.0]
- PressureOnly - SizeStatic | heavy_admitted | 1200 [1200, 1200] | [1200, 1200, 1200, 1200]
- PressureOnly - SizeStatic | heavy_admitted_MBps | 1 [1, 1] | [1, 1, 1, 1]

## Block H4

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PressureOnly | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 13098 [12956, 13134, 13175, 13126] | 10902 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | 0 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 0 [0, 0, 0, 0] | 0 | 17556 [17584, 17598, 17619, 17423] | 6444 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | 0 |
| none | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 13048 [12912, 13110, 13143, 13026] | 10952 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | n/a |

### Block H4 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 4508 [4323, 4693] | [4672, 4488, 4476, 4397]
- SizeStatic - none | nonLA_ok30 | 4508 [4323, 4693] | [4672, 4488, 4476, 4397]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1200 [-1200, -1200] | [-1200, -1200, -1200, -1200]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- PressureOnly - none | benign_ok30 | 50 [-5, 105] | [44, 24, 32, 100]
- PressureOnly - none | nonLA_ok30 | 50 [-5, 105] | [44, 24, 32, 100]
- PressureOnly - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0, 0.0]
- PressureOnly - none | heavy_admitted | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - none | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - SizeStatic | benign_ok30 | -4458 [-4674, -4243] | [-4628, -4464, -4444, -4297]
- PressureOnly - SizeStatic | nonLA_ok30 | -4458 [-4674, -4243] | [-4628, -4464, -4444, -4297]
- PressureOnly - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- PressureOnly - SizeStatic | attack_block_rate | -1.000 [-1.000, -1.000] | [-1.0, -1.0, -1.0, -1.0]
- PressureOnly - SizeStatic | heavy_admitted | 1200 [1200, 1200] | [1200, 1200, 1200, 1200]
- PressureOnly - SizeStatic | heavy_admitted_MBps | 1 [1, 1] | [1, 1, 1, 1]

## Block H1L

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SizeStatic | 4 | 0 / 0.000 | 0.999 | 0 [0, 0, 0, 0] | 0 | 8776 [8804, 8573, 9162, 8566] | 2101 | 0 | 14142 | 4 | 4 | 2 | 1 | n/a | 247 |
| none | 4 | 167 / 0.137 | 0.000 | 0 [0, 0, 0, 0] | 0 | 8290 [8425, 8668, 7849, 8216] | 2600 | 0 | 14143 | 4 | 4 | 2 | 1 | n/a | n/a |

### Block H1L paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 487 [-455, 1429] | [379, -95, 1313, 350]
- SizeStatic - none | nonLA_ok30 | 487 [-455, 1429] | [379, -95, 1313, 350]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 0.999 [0.995, 1.002] | [1.0, 1.0, 0.996, 1.0]
- SizeStatic - none | heavy_admitted | -167 [-235, -98] | [-143, -161, -229, -134]
- SizeStatic - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]

## Block H3L

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 0 [0, 0, 0, 0] | 0 | 16666 [16639, 16635, 16652, 16740] | 8134 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | 0 |
| none | 4 | 400 / 0.328 | 0.000 | 0 [0, 0, 0, 0] | 0 | 15088 [15201, 14955, 15050, 15146] | 9712 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | n/a |

### Block H3L paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 1578 [1417, 1740] | [1438, 1680, 1602, 1594]
- SizeStatic - none | nonLA_ok30 | 1578 [1417, 1740] | [1438, 1680, 1602, 1594]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -400 [-400, -400] | [-400, -400, -400, -400]
- SizeStatic - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]

## Block H4L

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 0 [0, 0, 0, 0] | 0 | 16762 [16743, 16787, 16723, 16797] | 8038 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | 0 |
| none | 4 | 400 / 0.328 | 0.000 | 0 [0, 0, 0, 0] | 0 | 15160 [15129, 15138, 15182, 15191] | 9640 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | n/a |

### Block H4L paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 1602 [1531, 1674] | [1614, 1649, 1541, 1606]
- SizeStatic - none | nonLA_ok30 | 1602 [1531, 1674] | [1614, 1649, 1541, 1606]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -400 [-400, -400] | [-400, -400, -400, -400]
- SizeStatic - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]

Provisioning/assertion check (assert.txt FAIL lines per run; PASS lines include heap-limit enforcement): 

## Caveats fixed in advance
- tau 65,604 B post-hoc; Budget = heavy-byte token bucket (C 200 KB; R fixed 125/250/500 KB/s or adaptive 500 KB/s x (1 - 0.75 grad(u_t)), tokens consumed only by heavy transactions; small transactions always pass) - a class-selective token-bucket policer, prior art; attack intensity blocks I1/I3/I6 use 1/3/6 burst workers (about 400/1,200/2,400 heavy transactions) so BENIGN attempts also differ between blocks (22,800 to 24,800): compare arms only within a block; L1 = one look-alike worker (about 400, 0.33 MB/s), no attack; MX = 2 attack workers + 1 look-alike worker; GC pause only for G1 blocks; ZGC/NM survival and OOM-exception lines are descriptive; shared node cpu01.
