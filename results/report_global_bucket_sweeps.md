# Results report global_bucket_sweeps (generated 2026-11-19 16:03)

Numbers only. Registered in PREREG_UNIFIED_v1.md addendum global_bucket_sweeps (exploratory). Node cpu05, shared non-exclusive. Receipt = within the connector 30 s limit. Same-seed pairs, t 95% CI over pair differences, per-pair values shown, no p-values. Chain-scan counts not used.

## Inventory (completed with summary / present)
- block I1: BudgetR125 3, BudgetR250 3, BudgetR500 3, SizeFixedP20 3, SizeStatic 3, none 3 (scheduled 18)
- block I3: BudgetR125 3, BudgetR250 3, BudgetR500 3, SizeFixedP20 3, SizeStatic 3, none 3 (scheduled 18)
- block I6: BudgetR125 3, BudgetR250 3, BudgetR500 3, SizeFixedP20 3, SizeStatic 3, none 3 (scheduled 18)
- block L1: BudgetR250 4, BudgetR500 4, SizeStatic 4, none 4 (scheduled 16)
- block MX: BudgetAdapt500 4, BudgetR250 4, BudgetR500 4, SizeStatic 4, none 4 (scheduled 20)
- block ZG: BudgetAdapt500 4, BudgetR125 4, BudgetR250 4, SizeStatic 4, none 4 (scheduled 20)
- block NM: BudgetAdapt500 4, BudgetR250 4, SizeStatic 4, none 4 (scheduled 16)
- runs without summary (apparatus failure, NOT replaced): none

## Block I1

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR125 | 3 | 154 / 0.126 | 0.615 | 0 [0, 0, 0] | 0 | 17723 [17745, 17675, 17748] | 7077 | 0 | 0 | 0 | 0 | 0 | 1 | 28506 | 0 |
| BudgetR250 | 3 | 306 / 0.251 | 0.235 | 0 [0, 0, 0] | 0 | 16533 [16521, 16719, 16359] | 8267 | 0 | 0 | 0 | 0 | 0 | 1 | 30047 | 0 |
| BudgetR500 | 3 | 400 / 0.328 | 0.000 | 0 [0, 0, 0] | 0 | 16170 [16247, 16200, 16062] | 8630 | 0 | 0 | 0 | 0 | 0 | 1 | 29379 | 0 |
| SizeFixedP20 | 3 | 315 / 0.258 | 0.212 | 0 [0, 0, 0] | 0 | 16449 [16437, 16634, 16277] | 8351 | 0 | 0 | 0 | 0 | 0 | 1 | 30386 | 0 |
| SizeStatic | 3 | 0 / 0.000 | 1.000 | 0 [0, 0, 0] | 0 | 18885 [18812, 18978, 18866] | 5915 | 0 | 0 | 0 | 0 | 0 | 1 | 25638 | 0 |
| none | 3 | 400 / 0.328 | 0.000 | 0 [0, 0, 0] | 0 | 16198 [16149, 16154, 16292] | 8602 | 0 | 0 | 0 | 0 | 0 | 1 | 29821 | n/a |

### Block I1 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 2687 [2372, 3002] | [2663, 2824, 2574]
- SizeStatic - none | nonLA_ok30 | 2687 [2372, 3002] | [2663, 2824, 2574]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -400 [-400, -400] | [-400, -400, -400]
- SizeStatic - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0]
- SizeStatic - none | gc_pause_ms | -4183 [-6420, -1946] | [-5123, -3328, -4099]
- BudgetR125 - none | benign_ok30 | 1524 [1350, 1698] | [1596, 1521, 1456]
- BudgetR125 - none | nonLA_ok30 | 1524 [1350, 1698] | [1596, 1521, 1456]
- BudgetR125 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - none | attack_block_rate | 0.615 [0.615, 0.615] | [0.615, 0.615, 0.615]
- BudgetR125 - none | heavy_admitted | -246 [-246, -246] | [-246, -246, -246]
- BudgetR125 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0]
- BudgetR125 - none | gc_pause_ms | -1315 [-9301, 6671] | [-3901, -2328, 2284]
- BudgetR250 - none | benign_ok30 | 335 [-289, 958] | [372, 565, 67]
- BudgetR250 - none | nonLA_ok30 | 335 [-289, 958] | [372, 565, 67]
- BudgetR250 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - none | attack_block_rate | 0.235 [0.235, 0.235] | [0.235, 0.235, 0.235]
- BudgetR250 - none | heavy_admitted | -94 [-94, -94] | [-94, -94, -94]
- BudgetR250 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0]
- BudgetR250 - none | gc_pause_ms | 226 [-5380, 5832] | [-2003, 171, 2509]
- BudgetR500 - none | benign_ok30 | -29 [-467, 409] | [98, 46, -230]
- BudgetR500 - none | nonLA_ok30 | -29 [-467, 409] | [98, 46, -230]
- BudgetR500 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - none | attack_block_rate | 0.000 [0.000, 0.000] | [0.0, 0.0, 0.0]
- BudgetR500 - none | heavy_admitted | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - none | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - none | gc_pause_ms | -442 [-2434, 1550] | [-326, -1296, 295]
- SizeFixedP20 - none | benign_ok30 | 251 [-369, 871] | [288, 480, -15]
- SizeFixedP20 - none | nonLA_ok30 | 251 [-369, 871] | [288, 480, -15]
- SizeFixedP20 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeFixedP20 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeFixedP20 - none | attack_block_rate | 0.212 [0.202, 0.221] | [0.212, 0.215, 0.207]
- SizeFixedP20 - none | heavy_admitted | -85 [-88, -81] | [-85, -86, -83]
- SizeFixedP20 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0]
- SizeFixedP20 - none | gc_pause_ms | 565 [-2442, 3573] | [-180, -86, 1962]
- BudgetR250 - SizeFixedP20 | benign_ok30 | 84 [80, 87] | [84, 85, 82]
- BudgetR250 - SizeFixedP20 | nonLA_ok30 | 84 [80, 87] | [84, 85, 82]
- BudgetR250 - SizeFixedP20 | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeFixedP20 | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeFixedP20 | attack_block_rate | 0.023 [0.014, 0.033] | [0.022, 0.02, 0.027]
- BudgetR250 - SizeFixedP20 | heavy_admitted | -9 [-13, -6] | [-9, -8, -11]
- BudgetR250 - SizeFixedP20 | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0]
- BudgetR250 - SizeFixedP20 | gc_pause_ms | -340 [-3551, 2872] | [-1823, 257, 547]
- BudgetR250 - SizeStatic | benign_ok30 | -2352 [-2687, -2017] | [-2291, -2259, -2507]
- BudgetR250 - SizeStatic | nonLA_ok30 | -2352 [-2687, -2017] | [-2291, -2259, -2507]
- BudgetR250 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | attack_block_rate | -0.765 [-0.765, -0.765] | [-0.765, -0.765, -0.765]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 4409 [-346, 9164] | [3120, 3499, 6608]
- BudgetR500 - SizeStatic | benign_ok30 | -2716 [-3041, -2390] | [-2565, -2778, -2804]
- BudgetR500 - SizeStatic | nonLA_ok30 | -2716 [-3041, -2390] | [-2565, -2778, -2804]
- BudgetR500 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - SizeStatic | attack_block_rate | -1.000 [-1.000, -1.000] | [-1.0, -1.0, -1.0]
- BudgetR500 - SizeStatic | heavy_admitted | 400 [400, 400] | [400, 400, 400]
- BudgetR500 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - SizeStatic | gc_pause_ms | 3741 [30, 7452] | [4797, 2032, 4394]
- BudgetR125 - SizeStatic | benign_ok30 | -1163 [-1471, -854] | [-1067, -1303, -1118]
- BudgetR125 - SizeStatic | nonLA_ok30 | -1163 [-1471, -854] | [-1067, -1303, -1118]
- BudgetR125 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | attack_block_rate | -0.385 [-0.385, -0.385] | [-0.385, -0.385, -0.385]
- BudgetR125 - SizeStatic | heavy_admitted | 154 [154, 154] | [154, 154, 154]
- BudgetR125 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | gc_pause_ms | 2868 [-4698, 10435] | [1222, 1000, 6383]

## Block I3

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR125 | 3 | 154 / 0.126 | 0.872 | 0 [0, 0, 0] | 0 | 20974 [20962, 20905, 21054] | 3026 | 0 | 0 | 0 | 0 | 0 | 1 | 22425 | 0 |
| BudgetR250 | 3 | 306 / 0.251 | 0.745 | 0 [0, 0, 0] | 0 | 19760 [20071, 19626, 19582] | 4240 | 0 | 0 | 0 | 0 | 0 | 1 | 24380 | 0 |
| BudgetR500 | 3 | 600 / 0.492 | 0.500 | 0 [0, 0, 0] | 0 | 17742 [17795, 17770, 17662] | 6258 | 0 | 0 | 0 | 0 | 0 | 1 | 26186 | 0 |
| SizeFixedP20 | 3 | 965 / 0.791 | 0.196 | 0 [0, 0, 0] | 0 | 15036 [14801, 15238, 15070] | 8964 | 0 | 0 | 0 | 0 | 0 | 1 | 27800 | 0 |
| SizeStatic | 3 | 0 / 0.000 | 1.000 | 0 [0, 0, 0] | 0 | 22006 [21994, 22119, 21905] | 1994 | 0 | 0 | 0 | 0 | 0 | 1 | 22211 | 0 |
| none | 3 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0] | 0 | 14080 [13974, 14329, 13938] | 9920 | 0 | 0 | 0 | 0 | 0 | 1 | 30900 | n/a |

### Block I3 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 7926 [7626, 8225] | [8020, 7790, 7967]
- SizeStatic - none | nonLA_ok30 | 7926 [7626, 8225] | [8020, 7790, 7967]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1200 [-1200, -1200] | [-1200, -1200, -1200]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1]
- SizeStatic - none | gc_pause_ms | -8690 [-16786, -593] | [-11416, -9573, -5080]
- BudgetR125 - none | benign_ok30 | 6893 [6192, 7594] | [6988, 6576, 7116]
- BudgetR125 - none | nonLA_ok30 | 6893 [6192, 7594] | [6988, 6576, 7116]
- BudgetR125 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - none | attack_block_rate | 0.872 [0.872, 0.872] | [0.872, 0.872, 0.872]
- BudgetR125 - none | heavy_admitted | -1046 [-1046, -1046] | [-1046, -1046, -1046]
- BudgetR125 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1]
- BudgetR125 - none | gc_pause_ms | -8475 [-14109, -2841] | [-10682, -8593, -6151]
- BudgetR250 - none | benign_ok30 | 5679 [4683, 6676] | [6097, 5297, 5644]
- BudgetR250 - none | nonLA_ok30 | 5679 [4683, 6676] | [6097, 5297, 5644]
- BudgetR250 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - none | attack_block_rate | 0.745 [0.745, 0.745] | [0.745, 0.745, 0.745]
- BudgetR250 - none | heavy_admitted | -894 [-894, -894] | [-894, -894, -894]
- BudgetR250 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1]
- BudgetR250 - none | gc_pause_ms | -6520 [-12003, -1037] | [-8832, -6292, -4436]
- BudgetR500 - none | benign_ok30 | 3662 [3171, 4153] | [3821, 3441, 3724]
- BudgetR500 - none | nonLA_ok30 | 3662 [3171, 4153] | [3821, 3441, 3724]
- BudgetR500 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - none | attack_block_rate | 0.500 [0.500, 0.500] | [0.5, 0.5, 0.5]
- BudgetR500 - none | heavy_admitted | -600 [-600, -600] | [-600, -600, -600]
- BudgetR500 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0]
- BudgetR500 - none | gc_pause_ms | -4714 [-10993, 1565] | [-7075, -5019, -2048]
- SizeFixedP20 - none | benign_ok30 | 956 [564, 1348] | [827, 909, 1132]
- SizeFixedP20 - none | nonLA_ok30 | 956 [564, 1348] | [827, 909, 1132]
- SizeFixedP20 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeFixedP20 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeFixedP20 - none | attack_block_rate | 0.196 [0.175, 0.217] | [0.187, 0.198, 0.203]
- SizeFixedP20 - none | heavy_admitted | -235 [-260, -210] | [-224, -237, -244]
- SizeFixedP20 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0]
- SizeFixedP20 - none | gc_pause_ms | -3100 [-8176, 1975] | [-5454, -1787, -2060]
- BudgetR250 - SizeFixedP20 | benign_ok30 | 4723 [3537, 5910] | [5270, 4388, 4512]
- BudgetR250 - SizeFixedP20 | nonLA_ok30 | 4723 [3537, 5910] | [5270, 4388, 4512]
- BudgetR250 - SizeFixedP20 | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeFixedP20 | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeFixedP20 | attack_block_rate | 0.549 [0.528, 0.570] | [0.558, 0.547, 0.542]
- BudgetR250 - SizeFixedP20 | heavy_admitted | -659 [-684, -634] | [-670, -657, -650]
- BudgetR250 - SizeFixedP20 | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1]
- BudgetR250 - SizeFixedP20 | gc_pause_ms | -3420 [-6066, -774] | [-3378, -4505, -2376]
- BudgetR250 - SizeStatic | benign_ok30 | -2246 [-2973, -1519] | [-1923, -2493, -2323]
- BudgetR250 - SizeStatic | nonLA_ok30 | -2246 [-2973, -1519] | [-1923, -2493, -2323]
- BudgetR250 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | attack_block_rate | -0.255 [-0.255, -0.255] | [-0.255, -0.255, -0.255]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 2170 [-1225, 5564] | [2584, 3281, 644]
- BudgetR500 - SizeStatic | benign_ok30 | -4264 [-4455, -4072] | [-4199, -4349, -4243]
- BudgetR500 - SizeStatic | nonLA_ok30 | -4264 [-4455, -4072] | [-4199, -4349, -4243]
- BudgetR500 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - SizeStatic | attack_block_rate | -0.500 [-0.500, -0.500] | [-0.5, -0.5, -0.5]
- BudgetR500 - SizeStatic | heavy_admitted | 600 [600, 600] | [600, 600, 600]
- BudgetR500 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - SizeStatic | gc_pause_ms | 3976 [1928, 6023] | [4341, 4554, 3032]
- BudgetR125 - SizeStatic | benign_ok30 | -1032 [-1483, -581] | [-1032, -1214, -851]
- BudgetR125 - SizeStatic | nonLA_ok30 | -1032 [-1483, -581] | [-1032, -1214, -851]
- BudgetR125 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | attack_block_rate | -0.128 [-0.128, -0.128] | [-0.128, -0.128, -0.128]
- BudgetR125 - SizeStatic | heavy_admitted | 154 [154, 154] | [154, 154, 154]
- BudgetR125 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | gc_pause_ms | 214 [-2568, 2997] | [734, 980, -1071]

## Block I6

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR125 | 3 | 154 / 0.126 | 0.936 | 0 [0, 0, 0] | 0 | 22747 [22740, 22749, 22752] | 53 | 0 | 0 | 0 | 0 | 0 | 1 | 18909 | 0 |
| BudgetR250 | 3 | 306 / 0.251 | 0.873 | 0 [0, 0, 0] | 0 | 22584 [22599, 22572, 22582] | 216 | 0 | 0 | 0 | 0 | 0 | 1 | 19157 | 0 |
| BudgetR500 | 3 | 603 / 0.495 | 0.749 | 0 [0, 0, 0] | 0 | 21739 [21810, 21678, 21728] | 1061 | 0 | 0 | 0 | 0 | 0 | 1 | 21993 | 0 |
| SizeFixedP20 | 3 | 1924 / 1.577 | 0.198 | 0 [0, 0, 0] | 0 | 13195 [13092, 13378, 13114] | 9605 | 0 | 0 | 0 | 0 | 0 | 1 | 30735 | 0 |
| SizeStatic | 3 | 0 / 0.000 | 1.000 | 0 [0, 0, 0] | 0 | 22724 [22731, 22724, 22716] | 76 | 0 | 0 | 0 | 0 | 0 | 1 | 16892 | 0 |
| none | 3 | 2400 / 1.967 | 0.000 | 0 [0, 0, 0] | 0 | 11758 [11736, 11636, 11903] | 11042 | 0 | 0 | 0 | 0 | 0 | 1 | 34028 | n/a |

### Block I6 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 10965 [10618, 11313] | [10995, 11088, 10813]
- SizeStatic - none | nonLA_ok30 | 10965 [10618, 11313] | [10995, 11088, 10813]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -2400 [-2400, -2400] | [-2400, -2400, -2400]
- SizeStatic - none | heavy_admitted_MBps | -2 [-2, -2] | [-2, -2, -2]
- SizeStatic - none | gc_pause_ms | -17136 [-22374, -11898] | [-18953, -17631, -14824]
- BudgetR125 - none | benign_ok30 | 10989 [10659, 11318] | [11004, 11113, 10849]
- BudgetR125 - none | nonLA_ok30 | 10989 [10659, 11318] | [11004, 11113, 10849]
- BudgetR125 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - none | attack_block_rate | 0.936 [0.936, 0.936] | [0.936, 0.936, 0.936]
- BudgetR125 - none | heavy_admitted | -2246 [-2246, -2246] | [-2246, -2246, -2246]
- BudgetR125 - none | heavy_admitted_MBps | -2 [-2, -2] | [-2, -2, -2]
- BudgetR125 - none | gc_pause_ms | -15120 [-18816, -11423] | [-16802, -14580, -13977]
- BudgetR250 - none | benign_ok30 | 10826 [10497, 11155] | [10863, 10936, 10679]
- BudgetR250 - none | nonLA_ok30 | 10826 [10497, 11155] | [10863, 10936, 10679]
- BudgetR250 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - none | attack_block_rate | 0.873 [0.873, 0.873] | [0.873, 0.873, 0.873]
- BudgetR250 - none | heavy_admitted | -2094 [-2094, -2094] | [-2094, -2094, -2094]
- BudgetR250 - none | heavy_admitted_MBps | -2 [-2, -2] | [-2, -2, -2]
- BudgetR250 - none | gc_pause_ms | -14871 [-20167, -9575] | [-16898, -15068, -12648]
- BudgetR500 - none | benign_ok30 | 9980 [9644, 10317] | [10074, 10042, 9825]
- BudgetR500 - none | nonLA_ok30 | 9980 [9644, 10317] | [10074, 10042, 9825]
- BudgetR500 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - none | attack_block_rate | 0.749 [0.743, 0.755] | [0.746, 0.75, 0.75]
- BudgetR500 - none | heavy_admitted | -1797 [-1811, -1782] | [-1790, -1800, -1800]
- BudgetR500 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1]
- BudgetR500 - none | gc_pause_ms | -12035 [-15538, -8532] | [-13432, -12061, -10612]
- SizeFixedP20 - none | benign_ok30 | 1436 [754, 2118] | [1356, 1742, 1211]
- SizeFixedP20 - none | nonLA_ok30 | 1436 [754, 2118] | [1356, 1742, 1211]
- SizeFixedP20 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- SizeFixedP20 - none | rej_LA | 0 [0, 0] | [0, 0, 0]
- SizeFixedP20 - none | attack_block_rate | 0.198 [0.177, 0.220] | [0.208, 0.191, 0.196]
- SizeFixedP20 - none | heavy_admitted | -476 [-529, -424] | [-500, -459, -470]
- SizeFixedP20 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0]
- SizeFixedP20 - none | gc_pause_ms | -3293 [-8881, 2295] | [-5452, -3464, -963]
- BudgetR250 - SizeFixedP20 | benign_ok30 | 9390 [8966, 9813] | [9507, 9194, 9468]
- BudgetR250 - SizeFixedP20 | nonLA_ok30 | 9390 [8966, 9813] | [9507, 9194, 9468]
- BudgetR250 - SizeFixedP20 | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeFixedP20 | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeFixedP20 | attack_block_rate | 0.674 [0.652, 0.696] | [0.664, 0.681, 0.677]
- BudgetR250 - SizeFixedP20 | heavy_admitted | -1618 [-1670, -1565] | [-1594, -1635, -1624]
- BudgetR250 - SizeFixedP20 | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1]
- BudgetR250 - SizeFixedP20 | gc_pause_ms | -11578 [-11880, -11276] | [-11446, -11604, -11685]
- BudgetR250 - SizeStatic | benign_ok30 | -139 [-167, -112] | [-132, -152, -134]
- BudgetR250 - SizeStatic | nonLA_ok30 | -139 [-167, -112] | [-132, -152, -134]
- BudgetR250 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | attack_block_rate | -0.127 [-0.127, -0.127] | [-0.127, -0.127, -0.127]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 2265 [1605, 2924] | [2055, 2563, 2176]
- BudgetR500 - SizeStatic | benign_ok30 | -985 [-1140, -830] | [-921, -1046, -988]
- BudgetR500 - SizeStatic | nonLA_ok30 | -985 [-1140, -830] | [-921, -1046, -988]
- BudgetR500 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR500 - SizeStatic | attack_block_rate | -0.251 [-0.257, -0.245] | [-0.254, -0.25, -0.25]
- BudgetR500 - SizeStatic | heavy_admitted | 603 [589, 618] | [610, 600, 600]
- BudgetR500 - SizeStatic | heavy_admitted_MBps | 0 [0, 1] | [0, 0, 0]
- BudgetR500 - SizeStatic | gc_pause_ms | 5101 [3187, 7015] | [5521, 5570, 4212]
- BudgetR125 - SizeStatic | benign_ok30 | 23 [-10, 57] | [9, 25, 36]
- BudgetR125 - SizeStatic | nonLA_ok30 | 23 [-10, 57] | [9, 25, 36]
- BudgetR125 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | attack_block_rate | -0.064 [-0.064, -0.064] | [-0.064, -0.064, -0.064]
- BudgetR125 - SizeStatic | heavy_admitted | 154 [154, 154] | [154, 154, 154]
- BudgetR125 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0]
- BudgetR125 - SizeStatic | gc_pause_ms | 2016 [-737, 4769] | [2151, 3051, 847]

## Block L1

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | 4 | 306 / 0.251 | n/a | 94 [94, 94, 94, 94] | 94 | 16851 [17111, 16954, 16670, 16669] | 8255 | 0 | 0 | 0 | 0 | 0 | 1 | 31913 | 0 |
| BudgetR500 | 4 | 400 / 0.328 | n/a | 0 [0, 0, 0, 0] | 0 | 16679 [16880, 16752, 16540, 16545] | 8465 | 0 | 0 | 0 | 0 | 0 | 1 | 29918 | 0 |
| SizeStatic | 4 | 0 / 0.000 | n/a | 400 [400, 400, 400, 400] | 400 | 18978 [19047, 18922, 18895, 19048] | 5822 | 0 | 0 | 0 | 0 | 0 | 1 | 27888 | 0 |
| none | 4 | 400 / 0.328 | n/a | 0 [0, 0, 0, 0] | 0 | 16661 [16787, 16833, 16346, 16678] | 8494 | 0 | 0 | 0 | 0 | 0 | 1 | 28874 | n/a |

### Block L1 paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 2317 [2010, 2624] | [2260, 2089, 2549, 2370]
- SizeStatic - none | nonLA_ok30 | 2672 [2373, 2971] | [2656, 2423, 2870, 2740]
- SizeStatic - none | benign_not_sent | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | rej_LA | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | heavy_admitted | -400 [-400, -400] | [-400, -400, -400, -400]
- SizeStatic - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- SizeStatic - none | gc_pause_ms | -986 [-2712, 740] | [412, -673, -1925, -1759]
- BudgetR250 - none | benign_ok30 | 190 [-70, 450] | [324, 121, 324, -9]
- BudgetR250 - none | nonLA_ok30 | 239 [-25, 503] | [414, 149, 339, 55]
- BudgetR250 - none | benign_not_sent | 94 [94, 94] | [94, 94, 94, 94]
- BudgetR250 - none | rej_LA | 94 [94, 94] | [94, 94, 94, 94]
- BudgetR250 - none | heavy_admitted | -94 [-94, -94] | [-94, -94, -94, -94]
- BudgetR250 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- BudgetR250 - none | gc_pause_ms | 3039 [-2488, 8565] | [7308, 4421, 428, -2]
- BudgetR500 - none | benign_ok30 | 18 [-223, 260] | [93, -81, 194, -133]
- BudgetR500 - none | nonLA_ok30 | 30 [-221, 280] | [186, -123, 143, -88]
- BudgetR500 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR500 - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR500 - none | heavy_admitted | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR500 - none | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR500 - none | gc_pause_ms | 1044 [-768, 2856] | [65, 2402, 1567, 141]
- BudgetR250 - SizeStatic | benign_ok30 | -2127 [-2464, -1790] | [-1936, -1968, -2225, -2379]
- BudgetR250 - SizeStatic | nonLA_ok30 | -2433 [-2770, -2096] | [-2242, -2274, -2531, -2685]
- BudgetR250 - SizeStatic | benign_not_sent | -306 [-306, -306] | [-306, -306, -306, -306]
- BudgetR250 - SizeStatic | rej_LA | -306 [-306, -306] | [-306, -306, -306, -306]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 4025 [202, 7848] | [6896, 5094, 2353, 1757]
- BudgetR500 - SizeStatic | benign_ok30 | -2299 [-2557, -2041] | [-2167, -2170, -2355, -2503]
- BudgetR500 - SizeStatic | nonLA_ok30 | -2643 [-2904, -2382] | [-2470, -2546, -2727, -2828]
- BudgetR500 - SizeStatic | benign_not_sent | -400 [-400, -400] | [-400, -400, -400, -400]
- BudgetR500 - SizeStatic | rej_LA | -400 [-400, -400] | [-400, -400, -400, -400]
- BudgetR500 - SizeStatic | heavy_admitted | 400 [400, 400] | [400, 400, 400, 400]
- BudgetR500 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR500 - SizeStatic | gc_pause_ms | 2030 [-710, 4770] | [-347, 3075, 3492, 1900]

## Block MX

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetAdapt500 | 4 | 534 / 0.437 | 0.440 | 315 [246, 247, 385, 381] | 315 | 18154 [18136, 18191, 18298, 17989] | 5923 | 0 | 0 | 0 | 0 | 0 | 1 | 25680 | 0 |
| BudgetR250 | 4 | 306 / 0.251 | 0.658 | 368 [394, 355, 389, 332] | 368 | 19840 [19768, 19934, 19703, 19955] | 4189 | 0 | 0 | 0 | 0 | 0 | 1 | 23884 | 0 |
| BudgetR500 | 4 | 602 / 0.494 | 0.458 | 231 [398, 327, 200, 0] | 231 | 17946 [17788, 17623, 18011, 18360] | 6217 | 0 | 0 | 0 | 0 | 0 | 1 | 26086 | 0 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 400 [400, 400, 400, 400] | 400 | 22098 [21949, 22204, 22245, 21993] | 1902 | 0 | 0 | 0 | 0 | 0 | 1 | 21724 | 0 |
| none | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 14538 [14566, 14532, 14533, 14523] | 9789 | 0 | 0 | 0 | 0 | 0 | 1 | 29532 | n/a |

### Block MX paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 7559 [7308, 7811] | [7383, 7672, 7712, 7470]
- SizeStatic - none | nonLA_ok30 | 7886 [7619, 8154] | [7716, 8013, 8048, 7769]
- SizeStatic - none | benign_not_sent | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | rej_LA | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1200 [-1200, -1200] | [-1200, -1200, -1200, -1200]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- SizeStatic - none | gc_pause_ms | -7808 [-9830, -5785] | [-7323, -7081, -7118, -9708]
- BudgetR250 - none | benign_ok30 | 5302 [5087, 5516] | [5202, 5402, 5170, 5432]
- BudgetR250 - none | nonLA_ok30 | 5600 [5441, 5758] | [5532, 5704, 5499, 5664]
- BudgetR250 - none | benign_not_sent | 368 [321, 414] | [394, 355, 389, 332]
- BudgetR250 - none | rej_LA | 368 [321, 414] | [394, 355, 389, 332]
- BudgetR250 - none | attack_block_rate | 0.658 [0.600, 0.716] | [0.625, 0.674, 0.631, 0.703]
- BudgetR250 - none | heavy_admitted | -894 [-894, -894] | [-894, -894, -894, -894]
- BudgetR250 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- BudgetR250 - none | gc_pause_ms | -5648 [-7848, -3448] | [-6117, -5062, -4100, -7314]
- BudgetR500 - none | benign_ok30 | 3407 [2884, 3930] | [3222, 3091, 3478, 3837]
- BudgetR500 - none | nonLA_ok30 | 3572 [3308, 3835] | [3554, 3359, 3614, 3759]
- BudgetR500 - none | benign_not_sent | 231 [-46, 509] | [398, 327, 200, 0]
- BudgetR500 - none | rej_LA | 231 [-46, 509] | [398, 327, 200, 0]
- BudgetR500 - none | attack_block_rate | 0.458 [0.107, 0.809] | [0.253, 0.329, 0.5, 0.75]
- BudgetR500 - none | heavy_admitted | -598 [-605, -590] | [-600, -590, -600, -600]
- BudgetR500 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- BudgetR500 - none | gc_pause_ms | -3446 [-5811, -1082] | [-3863, -2259, -2291, -5372]
- BudgetAdapt500 - none | benign_ok30 | 3615 [3412, 3818] | [3570, 3659, 3765, 3466]
- BudgetAdapt500 - none | nonLA_ok30 | 3866 [3607, 4124] | [3749, 3858, 4098, 3758]
- BudgetAdapt500 - none | benign_not_sent | 315 [189, 440] | [246, 247, 385, 381]
- BudgetAdapt500 - none | rej_LA | 315 [189, 440] | [246, 247, 385, 381]
- BudgetAdapt500 - none | attack_block_rate | 0.440 [0.300, 0.579] | [0.512, 0.519, 0.366, 0.361]
- BudgetAdapt500 - none | heavy_admitted | -666 [-682, -651] | [-656, -662, -678, -670]
- BudgetAdapt500 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- BudgetAdapt500 - none | gc_pause_ms | -3852 [-6954, -751] | [-3942, -4138, -1294, -6035]
- BudgetR250 - SizeStatic | benign_ok30 | -2258 [-2595, -1920] | [-2181, -2270, -2542, -2038]
- BudgetR250 - SizeStatic | nonLA_ok30 | -2287 [-2595, -1978] | [-2184, -2309, -2549, -2105]
- BudgetR250 - SizeStatic | benign_not_sent | -32 [-79, 14] | [-6, -45, -11, -68]
- BudgetR250 - SizeStatic | rej_LA | -32 [-79, 14] | [-6, -45, -11, -68]
- BudgetR250 - SizeStatic | attack_block_rate | -0.342 [-0.400, -0.284] | [-0.375, -0.326, -0.369, -0.297]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | gc_pause_ms | 2159 [954, 3364] | [1206, 2019, 3018, 2394]
- BudgetR500 - SizeStatic | benign_ok30 | -4152 [-4775, -3529] | [-4161, -4581, -4234, -3633]
- BudgetR500 - SizeStatic | nonLA_ok30 | -4315 [-4770, -3860] | [-4162, -4654, -4434, -4010]
- BudgetR500 - SizeStatic | benign_not_sent | -169 [-446, 109] | [-2, -73, -200, -400]
- BudgetR500 - SizeStatic | rej_LA | -169 [-446, 109] | [-2, -73, -200, -400]
- BudgetR500 - SizeStatic | attack_block_rate | -0.542 [-0.893, -0.191] | [-0.748, -0.671, -0.5, -0.25]
- BudgetR500 - SizeStatic | heavy_admitted | 602 [595, 610] | [600, 610, 600, 600]
- BudgetR500 - SizeStatic | heavy_admitted_MBps | 0 [0, 1] | [0, 0, 0, 0]
- BudgetR500 - SizeStatic | gc_pause_ms | 4361 [3338, 5385] | [3460, 4822, 4827, 4336]
- BudgetAdapt500 - BudgetR500 | benign_ok30 | 208 [-435, 851] | [348, 568, 287, -371]
- BudgetAdapt500 - BudgetR500 | nonLA_ok30 | 294 [-90, 678] | [195, 499, 484, -1]
- BudgetAdapt500 - BudgetR500 | benign_not_sent | 84 [-307, 474] | [-152, -80, 185, 381]
- BudgetAdapt500 - BudgetR500 | rej_LA | 84 [-307, 474] | [-152, -80, 185, 381]
- BudgetAdapt500 - BudgetR500 | attack_block_rate | -0.018 [-0.497, 0.460] | [0.26, 0.19, -0.134, -0.389]
- BudgetAdapt500 - BudgetR500 | heavy_admitted | -69 [-84, -54] | [-56, -72, -78, -70]
- BudgetAdapt500 - BudgetR500 | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- BudgetAdapt500 - BudgetR500 | gc_pause_ms | -406 [-2313, 1501] | [-79, -1879, 997, -663]
- BudgetAdapt500 - SizeStatic | benign_ok30 | -3944 [-4091, -3797] | [-3813, -4013, -3947, -4004]
- BudgetAdapt500 - SizeStatic | nonLA_ok30 | -4021 [-4169, -3873] | [-3967, -4155, -3950, -4011]
- BudgetAdapt500 - SizeStatic | benign_not_sent | -85 [-211, 40] | [-154, -153, -15, -19]
- BudgetAdapt500 - SizeStatic | rej_LA | -85 [-211, 40] | [-154, -153, -15, -19]
- BudgetAdapt500 - SizeStatic | attack_block_rate | -0.560 [-0.700, -0.421] | [-0.488, -0.481, -0.634, -0.639]
- BudgetAdapt500 - SizeStatic | heavy_admitted | 534 [518, 549] | [544, 538, 522, 530]
- BudgetAdapt500 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - SizeStatic | gc_pause_ms | 3955 [1916, 5994] | [3381, 2943, 5824, 3673]

## Block ZG

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetAdapt500 | 4 | 178 / 0.146 | 0.829 | 0 [0, 0, 0, 0] | 0 | 6980 [6771, 7082, 6847, 7222] | 6693 | 0 | 10486 | 4 | 4 | 0 | 2 | n/a | 149 |
| BudgetR125 | 4 | 126 / 0.103 | 0.877 | 0 [0, 0, 0, 0] | 0 | 7111 [6981, 6863, 7123, 7478] | 6664 | 0 | 10402 | 4 | 4 | 0 | 2 | n/a | 144 |
| BudgetR250 | 4 | 240 / 0.197 | 0.755 | 0 [0, 0, 0, 0] | 0 | 6879 [6699, 6703, 6994, 7119] | 7334 | 0 | 10006 | 4 | 4 | 0 | 2 | n/a | 134 |
| SizeStatic | 4 | 1 / 0.001 | 0.998 | 0 [0, 0, 0, 0] | 0 | 7118 [6951, 6770, 7118, 7634] | 9018 | 9 | 8081 | 3 | 3 | 0 | 2 | n/a | 110 |
| none | 4 | 604 / 0.495 | 0.000 | 0 [0, 0, 0, 0] | 0 | 6635 [6588, 6596, 6661, 6694] | 4874 | 0 | 13087 | 4 | 4 | 0 | 2 | n/a | n/a |

### Block ZG paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 484 [-36, 1003] | [363, 174, 457, 940]
- SizeStatic - none | nonLA_ok30 | 484 [-36, 1003] | [363, 174, 457, 940]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 0.998 [0.993, 1.003] | [1.0, 1.0, 0.994, 1.0]
- SizeStatic - none | heavy_admitted | -602 [-649, -556] | [-629, -622, -565, -593]
- SizeStatic - none | heavy_admitted_MBps | -0 [-1, -0] | [-1, -1, 0, 0]
- BudgetR125 - none | benign_ok30 | 476 [126, 827] | [393, 267, 462, 784]
- BudgetR125 - none | nonLA_ok30 | 476 [126, 827] | [393, 267, 462, 784]
- BudgetR125 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR125 - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR125 - none | attack_block_rate | 0.877 [0.872, 0.881] | [0.873, 0.879, 0.877, 0.877]
- BudgetR125 - none | heavy_admitted | -477 [-513, -441] | [-495, -496, -449, -469]
- BudgetR125 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- BudgetR250 - none | benign_ok30 | 244 [-11, 499] | [111, 107, 333, 425]
- BudgetR250 - none | nonLA_ok30 | 244 [-11, 499] | [111, 107, 333, 425]
- BudgetR250 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | attack_block_rate | 0.755 [0.739, 0.772] | [0.764, 0.765, 0.748, 0.745]
- BudgetR250 - none | heavy_admitted | -364 [-445, -282] | [-382, -399, -386, -287]
- BudgetR250 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- BudgetAdapt500 - none | benign_ok30 | 346 [48, 643] | [183, 486, 186, 528]
- BudgetAdapt500 - none | nonLA_ok30 | 346 [48, 643] | [183, 486, 186, 528]
- BudgetAdapt500 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - none | attack_block_rate | 0.829 [0.811, 0.847] | [0.829, 0.84, 0.834, 0.813]
- BudgetAdapt500 - none | heavy_admitted | -425 [-484, -366] | [-453, -442, -434, -371]
- BudgetAdapt500 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | benign_ok30 | -240 [-557, 78] | [-252, -67, -124, -515]
- BudgetR250 - SizeStatic | nonLA_ok30 | -240 [-557, 78] | [-252, -67, -124, -515]
- BudgetR250 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | attack_block_rate | -0.243 [-0.258, -0.228] | [-0.236, -0.235, -0.246, -0.255]
- BudgetR250 - SizeStatic | heavy_admitted | 239 [155, 323] | [247, 223, 179, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR125 - SizeStatic | benign_ok30 | -7 [-176, 162] | [30, 93, 5, -156]
- BudgetR125 - SizeStatic | nonLA_ok30 | -7 [-176, 162] | [30, 93, 5, -156]
- BudgetR125 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR125 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR125 - SizeStatic | attack_block_rate | -0.122 [-0.129, -0.115] | [-0.127, -0.121, -0.116, -0.123]
- BudgetR125 - SizeStatic | heavy_admitted | 125 [113, 137] | [134, 126, 116, 124]
- BudgetR125 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - SizeStatic | benign_ok30 | -138 [-638, 363] | [-180, 312, -271, -412]
- BudgetAdapt500 - SizeStatic | nonLA_ok30 | -138 [-638, 363] | [-180, 312, -271, -412]
- BudgetAdapt500 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - SizeStatic | attack_block_rate | -0.169 [-0.190, -0.149] | [-0.171, -0.16, -0.16, -0.187]
- BudgetAdapt500 - SizeStatic | heavy_admitted | 177 [118, 236] | [176, 180, 131, 222]
- BudgetAdapt500 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]

## Block NM

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetAdapt500 | 4 | 596 / 0.489 | 0.503 | 0 [0, 0, 0, 0] | 0 | 15776 [15635, 15856, 15798, 15813] | 8224 | 0 | 0 | 0 | 0 | 0 | 1 | n/a | 0 |
| BudgetR250 | 4 | 306 / 0.251 | 0.745 | 0 [0, 0, 0, 0] | 0 | 16550 [16492, 16584, 16602, 16520] | 7450 | 0 | 0 | 1 | 0 | 0 | 1 | n/a | 0 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 0 [0, 0, 0, 0] | 0 | 17509 [17406, 17424, 17569, 17638] | 6491 | 0 | 0 | 4 | 0 | 1 | 1 | n/a | 0 |
| none | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 13154 [13018, 13104, 13484, 13011] | 10846 | 0 | 0 | 2 | 0 | 0 | 1 | n/a | n/a |

### Block NM paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 4355 [4000, 4710] | [4388, 4320, 4085, 4627]
- SizeStatic - none | nonLA_ok30 | 4355 [4000, 4710] | [4388, 4320, 4085, 4627]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | attack_block_rate | 1.000 [1.000, 1.000] | [1.0, 1.0, 1.0, 1.0]
- SizeStatic - none | heavy_admitted | -1200 [-1200, -1200] | [-1200, -1200, -1200, -1200]
- SizeStatic - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- BudgetR250 - none | benign_ok30 | 3395 [3100, 3690] | [3474, 3480, 3118, 3509]
- BudgetR250 - none | nonLA_ok30 | 3395 [3100, 3690] | [3474, 3480, 3118, 3509]
- BudgetR250 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | attack_block_rate | 0.745 [0.745, 0.745] | [0.745, 0.745, 0.745, 0.745]
- BudgetR250 - none | heavy_admitted | -894 [-894, -894] | [-894, -894, -894, -894]
- BudgetR250 - none | heavy_admitted_MBps | -1 [-1, -1] | [-1, -1, -1, -1]
- BudgetAdapt500 - none | benign_ok30 | 2621 [2272, 2970] | [2617, 2752, 2314, 2802]
- BudgetAdapt500 - none | nonLA_ok30 | 2621 [2272, 2970] | [2617, 2752, 2314, 2802]
- BudgetAdapt500 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - none | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - none | attack_block_rate | 0.503 [0.502, 0.504] | [0.503, 0.502, 0.503, 0.502]
- BudgetAdapt500 - none | heavy_admitted | -604 [-604, -603] | [-604, -603, -604, -603]
- BudgetAdapt500 - none | heavy_admitted_MBps | -0 [-0, -0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | benign_ok30 | -960 [-1147, -773] | [-914, -840, -967, -1118]
- BudgetR250 - SizeStatic | nonLA_ok30 | -960 [-1147, -773] | [-914, -840, -967, -1118]
- BudgetR250 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - SizeStatic | attack_block_rate | -0.255 [-0.255, -0.255] | [-0.255, -0.255, -0.255, -0.255]
- BudgetR250 - SizeStatic | heavy_admitted | 306 [306, 306] | [306, 306, 306, 306]
- BudgetR250 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - SizeStatic | benign_ok30 | -1734 [-1914, -1553] | [-1771, -1568, -1771, -1825]
- BudgetAdapt500 - SizeStatic | nonLA_ok30 | -1734 [-1914, -1553] | [-1771, -1568, -1771, -1825]
- BudgetAdapt500 - SizeStatic | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - SizeStatic | rej_LA | 0 [0, 0] | [0, 0, 0, 0]
- BudgetAdapt500 - SizeStatic | attack_block_rate | -0.497 [-0.498, -0.496] | [-0.497, -0.498, -0.497, -0.498]
- BudgetAdapt500 - SizeStatic | heavy_admitted | 596 [596, 597] | [596, 597, 596, 597]
- BudgetAdapt500 - SizeStatic | heavy_admitted_MBps | 0 [0, 0] | [0, 0, 0, 0]

Provisioning/assertion check (assert.txt FAIL lines per run; PASS lines include heap-limit enforcement): ZG/SizeStatic/63751: fail=2 pass=4

## Caveats fixed in advance
- tau 65,604 B post-hoc; Budget = heavy-byte token bucket (C 200 KB; R fixed 125/250/500 KB/s or adaptive 500 KB/s x (1 - 0.75 grad(u_t)), tokens consumed only by heavy transactions; small transactions always pass) - a class-selective token-bucket policer, prior art; attack intensity blocks I1/I3/I6 use 1/3/6 burst workers (about 400/1,200/2,400 heavy transactions) so BENIGN attempts also differ between blocks (22,800 to 24,800): compare arms only within a block; L1 = one look-alike worker (about 400, 0.33 MB/s), no attack; MX = 2 attack workers + 1 look-alike worker; GC pause only for G1 blocks; ZGC/NM survival and OOM-exception lines are descriptive; shared node cpu01.
