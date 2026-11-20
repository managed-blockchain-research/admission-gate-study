# Results report deferral_rerun (re-run of deferral_first_batch_excluded after the client-parser fix) (generated 2026-11-20 06:08)

Numbers only. Registered in PREREG_UNIFIED_v1.md addendum deferral_rerun (re-run of deferral_first_batch_excluded after the client-parser fix) (exploratory). One block per node, shared non-exclusive nodes (cpu01-10 class). DUR = 360 s. Receipt = within the connector 30 s limit. Same-seed pairs, t 95% CI over pair differences, per-pair values shown, no p-values. Chain-scan counts not used.

## Inventory (completed with summary / present)
- block D1R: BudgetR250 4, ShapeR250D180 4, ShapeR250D60 4, SizeStatic 4, none 4 (scheduled 20)
- block D2R: BudgetR250 4, ShapeR250D180 4, ShapeR250D60 4, SizeStatic 4, none 4 (scheduled 20)
- block D3R: BudgetR250 4, ShapeR250D180 4, ShapeR250D60 4, SizeStatic 4, none 4 (scheduled 20)
- runs without summary (apparatus failure, NOT replaced): none

## Block D1R

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | 4 | 306 / 0.251 | 0.793 | 260 [394, 130, 154, 360] | 260 | 22992 [22696, 23083, 23423, 22764] | 13744 | 0 | 0 | 0 | 0 | 0 | 1 | 9732 | 0 |
| ShapeR250D180 | 4 | 764 / 0.626 | 0.382 | 130 [193, 181, 69, 77] | 130 | 21794 [21662, 21777, 22059, 21676] | 15045 | 0 | 0 | 0 | 0 | 0 | 1 | 10852 | 37800 |
| ShapeR250D60 | 4 | 459 / 0.376 | 0.605 | 257 [306, 308, 122, 292] | 257 | 22075 [21935, 22059, 22306, 21999] | 14660 | 0 | 0 | 0 | 0 | 0 | 1 | 10339 | 37800 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 400 [400, 400, 400, 400] | 400 | 25556 [25565, 25521, 25705, 25433] | 11044 | 0 | 0 | 0 | 0 | 0 | 1 | 7504 | 0 |
| none | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 16310 [16306, 16173, 16503, 16260] | 20641 | 0 | 0 | 0 | 0 | 0 | 1 | 15219 | n/a |

### Block D1R heavy-class terminal partition (means per run; sent_now / deferred_sent / deferred_unfinished / sent_unfinished / dropped; confirmed; end-to-end <=120 s; defer p50/p90 s)

| arm | class | n | sent now | deferred sent | deferred unfinished (censored) | sent unfinished | dropped | confirmed | e2e<=120 s | defer p50 / p90 s |
|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | A | 800 | 166 | 0 | 0 | 0 | 634 | 138 | 138 | n/a / n/a |
| BudgetR250 | LA | 400 | 140 | 0 | 0 | 0 | 260 | 136 | 136 | n/a / n/a |
| ShapeR250D180 | A | 800 | 2 | 492 | 0 | 0 | 306 | 420 | 222 | 108.5 / 176.1 |
| ShapeR250D180 | LA | 400 | 1 | 269 | 0 | 0 | 130 | 239 | 129 | 118.8 / 173.7 |
| ShapeR250D60 | A | 800 | 2 | 314 | 0 | 0 | 484 | 267 | 267 | 54.8 / 60.0 |
| ShapeR250D60 | LA | 400 | 1 | 142 | 0 | 0 | 257 | 134 | 134 | 47.1 / 60.0 |
| SizeStatic | A | 800 | 0 | 0 | 0 | 0 | 800 | 0 | 0 | n/a / n/a |
| SizeStatic | LA | 400 | 0 | 0 | 0 | 0 | 400 | 0 | 0 | n/a / n/a |
| none | A | 800 | 800 | 0 | 0 | 0 | 0 | 466 | 466 | n/a / n/a |
| none | LA | 400 | 400 | 0 | 0 | 0 | 0 | 352 | 352 | n/a / n/a |

### Block D1R paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 9246 [9123, 9368] | [9259, 9348, 9202, 9173]
- SizeStatic - none | benign_not_sent | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | LA_e2e120 | -352 [-382, -321] | [-365, -343, -329, -369]
- SizeStatic - none | LA_dropped | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_confirmed | -352 [-382, -321] | [-365, -343, -329, -369]
- SizeStatic - none | A_e2e120 | -466 [-546, -386] | [-497, -512, -454, -400]
- SizeStatic - none | A_dropped | 800 [800, 800] | [800, 800, 800, 800]
- SizeStatic - none | A_confirmed | -466 [-546, -386] | [-497, -512, -454, -400]
- SizeStatic - none | gc_pause_ms | -7714 [-8863, -6566] | [-7453, -6874, -8566, -7965]
- SizeStatic - none | peak_rss_mb | 40 [7, 73] | [12, 36, 56, 56]
- BudgetR250 - none | benign_ok30 | 6681 [6245, 7117] | [6390, 6910, 6920, 6504]
- BudgetR250 - none | benign_not_sent | 260 [42, 477] | [394, 130, 154, 360]
- BudgetR250 - none | LA_e2e120 | -216 [-469, 38] | [-363, -73, -83, -344]
- BudgetR250 - none | LA_dropped | 260 [42, 477] | [394, 130, 154, 360]
- BudgetR250 - none | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_confirmed | -216 [-469, 38] | [-363, -73, -83, -344]
- BudgetR250 - none | A_e2e120 | -328 [-601, -54] | [-224, -504, -440, -142]
- BudgetR250 - none | A_dropped | 634 [417, 852] | [500, 764, 740, 534]
- BudgetR250 - none | A_confirmed | -328 [-601, -54] | [-224, -504, -440, -142]
- BudgetR250 - none | gc_pause_ms | -5487 [-7441, -3533] | [-4523, -4527, -7090, -5809]
- BudgetR250 - none | peak_rss_mb | 32 [-16, 80] | [22, 64, 48, -5]
- ShapeR250D60 - none | benign_ok30 | 5764 [5592, 5937] | [5629, 5886, 5803, 5739]
- ShapeR250D60 - none | benign_not_sent | 257 [113, 401] | [306, 308, 122, 292]
- ShapeR250D60 - none | LA_e2e120 | -217 [-394, -40] | [-278, -261, -51, -278]
- ShapeR250D60 - none | LA_dropped | 257 [113, 401] | [306, 308, 122, 292]
- ShapeR250D60 - none | LA_deferred_sent | 142 [-2, 286] | [93, 91, 277, 107]
- ShapeR250D60 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_confirmed | -217 [-394, -40] | [-278, -261, -51, -278]
- ShapeR250D60 - none | A_e2e120 | -199 [-374, -24] | [-177, -175, -353, -91]
- ShapeR250D60 - none | A_dropped | 484 [340, 628] | [435, 433, 619, 449]
- ShapeR250D60 - none | A_confirmed | -199 [-374, -24] | [-177, -175, -353, -91]
- ShapeR250D60 - none | gc_pause_ms | -4880 [-5864, -3895] | [-4035, -4836, -5183, -5464]
- ShapeR250D60 - none | peak_rss_mb | 11 [-66, 88] | [-2, -52, 43, 54]
- ShapeR250D180 - none | benign_ok30 | 5483 [5298, 5668] | [5356, 5604, 5556, 5416]
- ShapeR250D180 - none | benign_not_sent | 130 [25, 235] | [193, 181, 69, 77]
- ShapeR250D180 - none | LA_e2e120 | -222 [-258, -187] | [-243, -210, -197, -240]
- ShapeR250D180 - none | LA_dropped | 130 [25, 235] | [193, 181, 69, 77]
- ShapeR250D180 - none | LA_deferred_sent | 269 [164, 374] | [206, 218, 330, 322]
- ShapeR250D180 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_confirmed | -113 [-190, -36] | [-168, -129, -53, -101]
- ShapeR250D180 - none | A_e2e120 | -244 [-332, -156] | [-278, -279, -257, -162]
- ShapeR250D180 - none | A_dropped | 306 [200, 411] | [242, 255, 367, 359]
- ShapeR250D180 - none | A_confirmed | -45 [-108, 18] | [-47, -49, -91, 6]
- ShapeR250D180 - none | gc_pause_ms | -4366 [-6035, -2698] | [-3159, -4631, -5652, -4023]
- ShapeR250D180 - none | peak_rss_mb | 16 [-5, 38] | [24, 19, 26, -3]
- ShapeR250D60 - BudgetR250 | benign_ok30 | -917 [-1206, -628] | [-761, -1024, -1117, -765]
- ShapeR250D60 - BudgetR250 | benign_not_sent | -2 [-197, 192] | [-88, 178, -32, -68]
- ShapeR250D60 - BudgetR250 | LA_e2e120 | -1 [-202, 200] | [85, -188, 32, 66]
- ShapeR250D60 - BudgetR250 | LA_dropped | -2 [-197, 192] | [-88, 178, -32, -68]
- ShapeR250D60 - BudgetR250 | LA_deferred_sent | 142 [-2, 286] | [93, 91, 277, 107]
- ShapeR250D60 - BudgetR250 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | LA_confirmed | -1 [-202, 200] | [85, -188, 32, 66]
- ShapeR250D60 - BudgetR250 | A_e2e120 | 128 [-86, 343] | [47, 329, 87, 51]
- ShapeR250D60 - BudgetR250 | A_dropped | -150 [-345, 44] | [-65, -331, -121, -85]
- ShapeR250D60 - BudgetR250 | A_confirmed | 128 [-86, 343] | [47, 329, 87, 51]
- ShapeR250D60 - BudgetR250 | gc_pause_ms | 608 [-877, 2092] | [488, -309, 1907, 345]
- ShapeR250D60 - BudgetR250 | peak_rss_mb | -22 [-137, 94] | [-24, -116, -5, 59]
- ShapeR250D180 - BudgetR250 | benign_ok30 | -1198 [-1455, -941] | [-1034, -1306, -1364, -1088]
- ShapeR250D180 - BudgetR250 | benign_not_sent | -130 [-360, 101] | [-201, 51, -85, -283]
- ShapeR250D180 - BudgetR250 | LA_e2e120 | -7 [-226, 212] | [120, -137, -114, 104]
- ShapeR250D180 - BudgetR250 | LA_dropped | -130 [-360, 101] | [-201, 51, -85, -283]
- ShapeR250D180 - BudgetR250 | LA_deferred_sent | 269 [164, 374] | [206, 218, 330, 322]
- ShapeR250D180 - BudgetR250 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | LA_confirmed | 103 [-120, 326] | [195, -56, 30, 243]
- ShapeR250D180 - BudgetR250 | A_e2e120 | 84 [-141, 308] | [-54, 225, 183, -20]
- ShapeR250D180 - BudgetR250 | A_dropped | -329 [-559, -98] | [-258, -509, -373, -175]
- ShapeR250D180 - BudgetR250 | A_confirmed | 282 [51, 514] | [177, 455, 349, 148]
- ShapeR250D180 - BudgetR250 | gc_pause_ms | 1121 [-211, 2453] | [1364, -104, 1438, 1786]
- ShapeR250D180 - BudgetR250 | peak_rss_mb | -16 [-52, 20] | [2, -45, -22, 2]
- ShapeR250D180 - ShapeR250D60 | benign_ok30 | -281 [-331, -231] | [-273, -282, -247, -323]
- ShapeR250D180 - ShapeR250D60 | benign_not_sent | -127 [-233, -21] | [-113, -127, -53, -215]
- ShapeR250D180 - ShapeR250D60 | LA_e2e120 | -6 [-155, 144] | [35, 51, -146, 38]
- ShapeR250D180 - ShapeR250D60 | LA_dropped | -127 [-233, -21] | [-113, -127, -53, -215]
- ShapeR250D180 - ShapeR250D60 | LA_deferred_sent | 127 [21, 233] | [113, 127, 53, 215]
- ShapeR250D180 - ShapeR250D60 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_confirmed | 104 [-17, 225] | [110, 132, -2, 177]
- ShapeR250D180 - ShapeR250D60 | A_e2e120 | -45 [-196, 106] | [-101, -104, 96, -71]
- ShapeR250D180 - ShapeR250D60 | A_dropped | -178 [-285, -72] | [-193, -178, -252, -90]
- ShapeR250D180 - ShapeR250D60 | A_confirmed | 154 [37, 271] | [130, 126, 262, 97]
- ShapeR250D180 - ShapeR250D60 | gc_pause_ms | 513 [-803, 1829] | [876, 205, -469, 1441]
- ShapeR250D180 - ShapeR250D60 | peak_rss_mb | 6 [-82, 93] | [26, 71, -17, -57]

## Block D2R

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | 4 | 306 / 0.251 | 0.745 | 0 [0, 0, 0, 0] | 0 | 22800 [22933, 22825, 22662, 22781] | 13800 | 0 | 0 | 0 | 0 | 0 | 1 | 11301 | 0 |
| ShapeR250D180 | 4 | 764 / 0.626 | 0.363 | 0 [0, 0, 0, 0] | 0 | 21540 [21719, 21172, 21635, 21633] | 15060 | 0 | 0 | 0 | 0 | 0 | 1 | 13438 | 37800 |
| ShapeR250D60 | 4 | 459 / 0.376 | 0.617 | 0 [0, 0, 0, 0] | 0 | 22048 [22005, 21857, 22160, 22168] | 14552 | 0 | 0 | 0 | 0 | 0 | 1 | 11136 | 37800 |
| SizeStatic | 4 | 0 / 0.000 | 1.000 | 0 [0, 0, 0, 0] | 0 | 25684 [25829, 25727, 25620, 25559] | 10916 | 0 | 0 | 0 | 0 | 0 | 1 | 8081 | 0 |
| none | 4 | 1200 / 0.984 | 0.000 | 0 [0, 0, 0, 0] | 0 | 15950 [15934, 15999, 15981, 15887] | 20650 | 0 | 0 | 0 | 0 | 0 | 1 | 16374 | n/a |

### Block D2R heavy-class terminal partition (means per run; sent_now / deferred_sent / deferred_unfinished / sent_unfinished / dropped; confirmed; end-to-end <=120 s; defer p50/p90 s)

| arm | class | n | sent now | deferred sent | deferred unfinished (censored) | sent unfinished | dropped | confirmed | e2e<=120 s | defer p50 / p90 s |
|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | A | 1200 | 306 | 0 | 0 | 0 | 894 | 269 | 269 | n/a / n/a |
| ShapeR250D180 | A | 1200 | 3 | 761 | 0 | 0 | 436 | 646 | 343 | 111.8 / 179.9 |
| ShapeR250D60 | A | 1200 | 3 | 456 | 0 | 0 | 741 | 391 | 391 | 59.8 / 60.0 |
| SizeStatic | A | 1200 | 0 | 0 | 0 | 0 | 1200 | 0 | 0 | n/a / n/a |
| none | A | 1200 | 1200 | 0 | 0 | 0 | 0 | 653 | 653 | n/a / n/a |

### Block D2R paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 9734 [9553, 9914] | [9895, 9728, 9639, 9672]
- SizeStatic - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | A_e2e120 | -653 [-715, -591] | [-705, -652, -611, -645]
- SizeStatic - none | A_dropped | 1200 [1200, 1200] | [1200, 1200, 1200, 1200]
- SizeStatic - none | A_confirmed | -653 [-715, -591] | [-705, -652, -611, -645]
- SizeStatic - none | gc_pause_ms | -8292 [-10737, -5848] | [-8569, -8168, -10084, -6348]
- SizeStatic - none | peak_rss_mb | 4 [-44, 52] | [16, 31, -39, 7]
- BudgetR250 - none | benign_ok30 | 6850 [6638, 7062] | [6999, 6826, 6681, 6894]
- BudgetR250 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | A_e2e120 | -384 [-487, -281] | [-480, -364, -338, -355]
- BudgetR250 - none | A_dropped | 894 [894, 894] | [894, 894, 894, 894]
- BudgetR250 - none | A_confirmed | -384 [-487, -281] | [-480, -364, -338, -355]
- BudgetR250 - none | gc_pause_ms | -5073 [-11320, 1175] | [-6085, -415, -9802, -3989]
- BudgetR250 - none | peak_rss_mb | 41 [-36, 118] | [98, 44, -21, 43]
- ShapeR250D60 - none | benign_ok30 | 6097 [5809, 6385] | [6071, 5858, 6179, 6281]
- ShapeR250D60 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | A_e2e120 | -262 [-331, -193] | [-299, -222, -227, -300]
- ShapeR250D60 - none | A_dropped | 741 [740, 742] | [740, 741, 741, 741]
- ShapeR250D60 - none | A_confirmed | -262 [-331, -193] | [-299, -222, -227, -300]
- ShapeR250D60 - none | gc_pause_ms | -5238 [-6785, -3690] | [-4297, -6427, -5616, -4610]
- ShapeR250D60 - none | peak_rss_mb | 19 [-45, 83] | [52, 36, -39, 28]
- ShapeR250D180 - none | benign_ok30 | 5590 [5139, 6040] | [5785, 5173, 5654, 5746]
- ShapeR250D180 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | A_e2e120 | -310 [-364, -256] | [-357, -304, -276, -304]
- ShapeR250D180 - none | A_dropped | 436 [435, 437] | [436, 436, 435, 436]
- ShapeR250D180 - none | A_confirmed | -7 [-62, 48] | [-47, -5, 37, -12]
- ShapeR250D180 - none | gc_pause_ms | -2936 [-9907, 4036] | [-4891, 3543, -6085, -4309]
- ShapeR250D180 - none | peak_rss_mb | 14 [-51, 78] | [36, 57, -33, -5]
- ShapeR250D60 - BudgetR250 | benign_ok30 | -753 [-1120, -386] | [-928, -968, -502, -613]
- ShapeR250D60 - BudgetR250 | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | LA_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | LA_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | A_e2e120 | 122 [38, 207] | [181, 142, 111, 55]
- ShapeR250D60 - BudgetR250 | A_dropped | -153 [-154, -152] | [-154, -153, -153, -153]
- ShapeR250D60 - BudgetR250 | A_confirmed | 122 [38, 207] | [181, 142, 111, 55]
- ShapeR250D60 - BudgetR250 | gc_pause_ms | -165 [-7108, 6779] | [1788, -6012, 4186, -621]
- ShapeR250D60 - BudgetR250 | peak_rss_mb | -22 [-48, 5] | [-46, -8, -18, -15]
- ShapeR250D180 - BudgetR250 | benign_ok30 | -1260 [-1695, -826] | [-1214, -1653, -1027, -1148]
- ShapeR250D180 - BudgetR250 | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | LA_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | LA_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | A_e2e120 | 74 [21, 127] | [123, 60, 62, 51]
- ShapeR250D180 - BudgetR250 | A_dropped | -458 [-459, -457] | [-458, -458, -459, -458]
- ShapeR250D180 - BudgetR250 | A_confirmed | 378 [315, 440] | [433, 359, 375, 343]
- ShapeR250D180 - BudgetR250 | gc_pause_ms | 2137 [-1141, 5416] | [1194, 3958, 3717, -320]
- ShapeR250D180 - BudgetR250 | peak_rss_mb | -27 [-82, 27] | [-62, 13, -12, -48]
- ShapeR250D180 - ShapeR250D60 | benign_ok30 | -508 [-770, -245] | [-286, -685, -525, -535]
- ShapeR250D180 - ShapeR250D60 | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | A_e2e120 | -48 [-100, 4] | [-58, -82, -49, -4]
- ShapeR250D180 - ShapeR250D60 | A_dropped | -305 [-306, -304] | [-304, -305, -306, -305]
- ShapeR250D180 - ShapeR250D60 | A_confirmed | 255 [208, 302] | [252, 217, 264, 288]
- ShapeR250D180 - ShapeR250D60 | gc_pause_ms | 2302 [-5856, 10460] | [-594, 9970, -469, 301]
- ShapeR250D180 - ShapeR250D60 | peak_rss_mb | -6 [-43, 32] | [-16, 21, 6, -33]

## Block D3R

| arm | n | heavy admitted (count / MB per s in the 120 s window) | attack block rate | benign not sent (per-seed) | LA rejected | receipts<=30 s (per-seed) | failed | unfinished | planned no record | OOM runs | node death | block-processing failed | max gap s | G1 pause ms | stale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | 4 | 306 / 0.251 | n/a | 94 [94, 94, 94, 94] | 94 | 19216 [19123, 19295, 19230, 19215] | 18490 | 0 | 0 | 0 | 0 | 0 | 1 | 12715 | 0 |
| ShapeR250D180 | 4 | 400 / 0.328 | n/a | 0 [0, 0, 0, 0] | 0 | 18759 [18815, 18986, 18893, 18343] | 19028 | 0 | 0 | 0 | 0 | 0 | 1 | 13872 | 37800 |
| ShapeR250D60 | 4 | 400 / 0.328 | n/a | 0 [0, 0, 0, 0] | 0 | 18806 [18732, 18662, 18920, 18912] | 18979 | 0 | 0 | 0 | 0 | 0 | 1 | 13120 | 37800 |
| SizeStatic | 4 | 0 / 0.000 | n/a | 400 [400, 400, 400, 400] | 400 | 21475 [21404, 21683, 21338, 21475] | 15925 | 0 | 0 | 0 | 0 | 0 | 1 | 11124 | 0 |
| none | 4 | 400 / 0.328 | n/a | 0 [0, 0, 0, 0] | 0 | 18636 [18673, 18639, 18632, 18598] | 19127 | 0 | 0 | 0 | 0 | 0 | 1 | 13350 | n/a |

### Block D3R heavy-class terminal partition (means per run; sent_now / deferred_sent / deferred_unfinished / sent_unfinished / dropped; confirmed; end-to-end <=120 s; defer p50/p90 s)

| arm | class | n | sent now | deferred sent | deferred unfinished (censored) | sent unfinished | dropped | confirmed | e2e<=120 s | defer p50 / p90 s |
|---|---|---|---|---|---|---|---|---|---|---|
| BudgetR250 | LA | 400 | 306 | 0 | 0 | 0 | 94 | 306 | 306 | n/a / n/a |
| ShapeR250D180 | LA | 400 | 9 | 391 | 0 | 0 | 0 | 387 | 387 | 18.3 / 32.9 |
| ShapeR250D60 | LA | 400 | 9 | 391 | 0 | 0 | 0 | 386 | 386 | 18.3 / 32.9 |
| SizeStatic | LA | 400 | 0 | 0 | 0 | 0 | 400 | 0 | 0 | n/a / n/a |
| none | LA | 400 | 400 | 0 | 0 | 0 | 0 | 362 | 362 | n/a / n/a |

### Block D3R paired differences (A - B), t 95% CI [per-pair]

- SizeStatic - none | benign_ok30 | 2840 [2592, 3087] | [2731, 3044, 2706, 2877]
- SizeStatic - none | benign_not_sent | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | LA_e2e120 | -362 [-399, -326] | [-347, -344, -394, -364]
- SizeStatic - none | LA_dropped | 400 [400, 400] | [400, 400, 400, 400]
- SizeStatic - none | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | LA_confirmed | -362 [-399, -326] | [-347, -344, -394, -364]
- SizeStatic - none | A_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | A_dropped | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | A_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- SizeStatic - none | gc_pause_ms | -2227 [-3764, -689] | [-2963, -804, -2555, -2585]
- SizeStatic - none | peak_rss_mb | 23 [-24, 70] | [-12, 51, 10, 43]
- BudgetR250 - none | benign_ok30 | 580 [437, 724] | [450, 656, 598, 617]
- BudgetR250 - none | benign_not_sent | 94 [94, 94] | [94, 94, 94, 94]
- BudgetR250 - none | LA_e2e120 | -56 [-93, -20] | [-41, -39, -88, -58]
- BudgetR250 - none | LA_dropped | 94 [94, 94] | [94, 94, 94, 94]
- BudgetR250 - none | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | LA_confirmed | -56 [-93, -20] | [-41, -39, -88, -58]
- BudgetR250 - none | A_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | A_dropped | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | A_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- BudgetR250 - none | gc_pause_ms | -636 [-1883, 612] | [-1246, 305, -285, -1317]
- BudgetR250 - none | peak_rss_mb | 2 [-47, 51] | [36, -12, 18, -33]
- ShapeR250D60 - none | benign_ok30 | 171 [-70, 412] | [59, 23, 288, 314]
- ShapeR250D60 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_e2e120 | 23 [-18, 65] | [51, 21, -11, 32]
- ShapeR250D60 - none | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_deferred_sent | 391 [391, 391] | [391, 391, 391, 391]
- ShapeR250D60 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | LA_confirmed | 23 [-18, 65] | [51, 21, -11, 32]
- ShapeR250D60 - none | A_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | A_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | A_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - none | gc_pause_ms | -231 [-2402, 1940] | [10, 1126, -2128, 68]
- ShapeR250D60 - none | peak_rss_mb | -5 [-31, 22] | [-22, 8, 11, -16]
- ShapeR250D180 - none | benign_ok30 | 124 [-300, 547] | [142, 347, 261, -255]
- ShapeR250D180 - none | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_e2e120 | 25 [-10, 60] | [48, 18, -2, 36]
- ShapeR250D180 - none | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_deferred_sent | 391 [391, 391] | [391, 391, 391, 391]
- ShapeR250D180 - none | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | LA_confirmed | 25 [-10, 60] | [48, 18, -2, 36]
- ShapeR250D180 - none | A_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | A_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | A_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - none | gc_pause_ms | 522 [-645, 1689] | [-513, 578, 837, 1186]
- ShapeR250D180 - none | peak_rss_mb | -10 [-45, 24] | [-34, -8, 18, -18]
- ShapeR250D60 - BudgetR250 | benign_ok30 | -409 [-655, -164] | [-391, -633, -310, -303]
- ShapeR250D60 - BudgetR250 | benign_not_sent | -94 [-94, -94] | [-94, -94, -94, -94]
- ShapeR250D60 - BudgetR250 | LA_e2e120 | 80 [56, 103] | [92, 60, 77, 90]
- ShapeR250D60 - BudgetR250 | LA_dropped | -94 [-94, -94] | [-94, -94, -94, -94]
- ShapeR250D60 - BudgetR250 | LA_deferred_sent | 391 [391, 391] | [391, 391, 391, 391]
- ShapeR250D60 - BudgetR250 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | LA_confirmed | 80 [56, 103] | [92, 60, 77, 90]
- ShapeR250D60 - BudgetR250 | A_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | A_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | A_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D60 - BudgetR250 | gc_pause_ms | 405 [-2010, 2820] | [1256, 821, -1843, 1385]
- ShapeR250D60 - BudgetR250 | peak_rss_mb | -7 [-64, 50] | [-58, 20, -7, 17]
- ShapeR250D180 - BudgetR250 | benign_ok30 | -456 [-898, -15] | [-308, -309, -337, -872]
- ShapeR250D180 - BudgetR250 | benign_not_sent | -94 [-94, -94] | [-94, -94, -94, -94]
- ShapeR250D180 - BudgetR250 | LA_e2e120 | 82 [55, 108] | [89, 57, 86, 94]
- ShapeR250D180 - BudgetR250 | LA_dropped | -94 [-94, -94] | [-94, -94, -94, -94]
- ShapeR250D180 - BudgetR250 | LA_deferred_sent | 391 [391, 391] | [391, 391, 391, 391]
- ShapeR250D180 - BudgetR250 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | LA_confirmed | 82 [55, 108] | [89, 57, 86, 94]
- ShapeR250D180 - BudgetR250 | A_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | A_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | A_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - BudgetR250 | gc_pause_ms | 1158 [-372, 2688] | [733, 273, 1122, 2503]
- ShapeR250D180 - BudgetR250 | peak_rss_mb | -13 [-74, 49] | [-70, 4, 0, 15]
- ShapeR250D180 - ShapeR250D60 | benign_ok30 | -47 [-648, 553] | [83, 324, -27, -569]
- ShapeR250D180 - ShapeR250D60 | benign_not_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_e2e120 | 2 [-8, 11] | [-3, -3, 9, 4]
- ShapeR250D180 - ShapeR250D60 | LA_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_deferred_sent | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_deferred_unfinished | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | LA_confirmed | 2 [-8, 11] | [-3, -3, 9, 4]
- ShapeR250D180 - ShapeR250D60 | A_e2e120 | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | A_dropped | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | A_confirmed | 0 [0, 0] | [0, 0, 0, 0]
- ShapeR250D180 - ShapeR250D60 | gc_pause_ms | 753 [-1901, 3407] | [-523, -548, 2965, 1118]
- ShapeR250D180 - ShapeR250D60 | peak_rss_mb | -6 [-22, 11] | [-12, -16, 7, -2]

Provisioning/assertion check (assert.txt FAIL lines per run; PASS lines include heap-limit enforcement): 

## Caveats fixed in advance
- tau 65,604 B post-hoc; Budget = heavy-byte token bucket (C 200 KB; R fixed 125/250/500 KB/s or adaptive 500 KB/s x (1 - 0.75 grad(u_t)), tokens consumed only by heavy transactions; small transactions always pass) - a class-selective token-bucket policer, prior art; attack intensity blocks I1/I3/I6 use 1/3/6 burst workers (about 400/1,200/2,400 heavy transactions) so BENIGN attempts also differ between blocks (22,800 to 24,800): compare arms only within a block; L1 = one look-alike worker (about 400, 0.33 MB/s), no attack; MX = 2 attack workers + 1 look-alike worker; GC pause only for G1 blocks; ZGC/NM survival and OOM-exception lines are descriptive; shared node cpu01.
