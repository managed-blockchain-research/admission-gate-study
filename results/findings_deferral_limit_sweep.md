# 11yy findings: deferral limit sweep (shaper 250 kB/s; load 360 s; three seeds per arm; written 2026-11-26)


## D1R: mixed attack + look-alike (800 attack, 400 look-alike requests)

| arm | runs | look-alike dropped | look-alike delivered | look-alike median delay s | look-alike completed within 120 s | attack dropped | ordinary receipts share |
|---|---|---|---|---|---|---|---|
| none | 3 | 0 | 343 | - | 343 | 0 | 0.446 |
| SizeStatic | 3 | 400 | 0 | - | 0 | 800 | 0.690 |
| BudgetR250 | 3 | 263 | 110 | - | 110 | 631 | 0.623 |
| ShapeR250D30 | 3 | 314 | 56 | 29 | 56 | 503 | 0.606 |
| ShapeR250D60 | 3 | 292 | 95 | 47 | 95 | 449 | 0.597 |
| ShapeR250D120 | 3 | 140 | 256 | 104 | 126 | 448 | 0.591 |
| ShapeR250D180 | 3 | 181 | 210 | 96 | 125 | 255 | 0.592 |
| ShapeR250D300 | 3 | 43 | 236 | 157 | 125 | 88 | 0.586 |

## D2R: attack-only (1,200 attack requests)

| arm | runs | look-alike dropped | look-alike delivered | look-alike median delay s | look-alike completed within 120 s | attack dropped | ordinary receipts share |
|---|---|---|---|---|---|---|---|
| none | 3 | 0 | 0 | - | 0 | 0 | 0.439 |
| SizeStatic | 3 | 0 | 0 | - | 0 | 1200 | 0.698 |
| BudgetR250 | 3 | 0 | 0 | - | 0 | 894 | 0.622 |
| ShapeR250D30 | 3 | 0 | 0 | - | 0 | 817 | 0.610 |
| ShapeR250D60 | 3 | 0 | 0 | - | 0 | 741 | 0.596 |
| ShapeR250D120 | 3 | 0 | 0 | - | 0 | 588 | 0.592 |
| ShapeR250D180 | 3 | 0 | 0 | - | 0 | 436 | 0.593 |
| ShapeR250D300 | 3 | 0 | 0 | - | 0 | 131 | 0.593 |

## D3R: look-alike only (400 requests)

| arm | runs | look-alike dropped | look-alike delivered | look-alike median delay s | look-alike completed within 120 s | attack dropped | ordinary receipts share |
|---|---|---|---|---|---|---|---|
| none | 3 | 0 | 356 | - | 356 | 0 | 0.492 |
| SizeStatic | 3 | 400 | 0 | - | 0 | 0 | 0.563 |
| BudgetR250 | 3 | 94 | 305 | - | 305 | 0 | 0.505 |
| ShapeR250D30 | 3 | 17 | 377 | 18 | 377 | 0 | 0.493 |
| ShapeR250D60 | 3 | 0 | 389 | 18 | 389 | 0 | 0.493 |
| ShapeR250D120 | 3 | 0 | 390 | 18 | 390 | 0 | 0.493 |
| ShapeR250D180 | 3 | 0 | 393 | 18 | 393 | 0 | 0.495 |
| ShapeR250D300 | 3 | 0 | 396 | 18 | 396 | 0 | 0.499 |

## Reading rules
Means per run over three seeds; dropped = rejected after the maximum delay (or at once for the policer); delay = time the shaper held a delivered request; descriptive. The run DEFERLIM_D1R_none_s67401 shared its node with a run of the sender sweep and is flagged co-located.

