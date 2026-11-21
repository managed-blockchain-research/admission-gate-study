# 11qq / 11rr findings (Besu G1 512 MB, 100 tx/s, 240 s, window 60-180 s; same-seed pairs; intervals descriptive; written 2026-11-22)

## Q1: realized operating points (400 attack requests; mean over 3 seeds; benign cost = share of ordinary requests rejected; receipts = share of ordinary requests with a receipt within 30 s)

| family | arm | attack blocked | ordinary rejected | receipts | receipts gain vs none (paired, 95% CI) |
|---|---|---|---|---|---|
| RandP (content-blind, probability p) | RandP20 | 0.207 | 0.203 | 0.797 | +0.146 +/- 0.007 |
| RandP (content-blind, probability p) | RandP40 | 0.380 | 0.403 | 0.595 | -0.056 +/- 0.010 |
| RandP (content-blind, probability p) | RandP60 | 0.611 | 0.603 | 0.396 | -0.256 +/- 0.007 |
| RandP (content-blind, probability p) | RandP80 | 0.800 | 0.801 | 0.198 | -0.453 +/- 0.009 |
| SizeFixedP (heavy only, probability p) | SizeFixedP20 | 0.199 | 0.000 | 0.669 | +0.018 +/- 0.015 |
| SizeFixedP (heavy only, probability p) | SizeFixedP40 | 0.392 | 0.000 | 0.686 | +0.034 +/- 0.016 |
| SizeFixedP (heavy only, probability p) | SizeFixedP60 | 0.616 | 0.000 | 0.717 | +0.066 +/- 0.021 |
| SizeFixedP (heavy only, probability p) | SizeFixedP80 | 0.813 | 0.000 | 0.740 | +0.089 +/- 0.007 |
| Global bucket (rate kB/s) | BudgetR125 | 0.615 | 0.000 | 0.711 | +0.060 +/- 0.012 |
| Global bucket (rate kB/s) | BudgetR250 | 0.235 | 0.000 | 0.668 | +0.016 +/- 0.018 |
| Global bucket (rate kB/s) | BudgetR500 | 0.000 | 0.000 | 0.650 | -0.001 +/- 0.014 |
| Global bucket (rate kB/s) | BudgetR1000 | 0.000 | 0.000 | 0.652 | +0.000 +/- 0.019 |
| Global bucket (rate kB/s) | BudgetR2000 | 0.000 | 0.000 | 0.651 | -0.000 +/- 0.009 |
| Blanket pressure shedding (ramp) | PressureOnlyLow | 0.213 | 0.201 | 0.797 | +0.146 +/- 0.014 |
| Blanket pressure shedding (ramp) | PressureOnly | 0.155 | 0.139 | 0.859 | +0.208 +/- 0.049 |
| Blanket pressure shedding (ramp) | PressureOnlyHigh | 0.080 | 0.068 | 0.838 | +0.187 +/- 0.072 |
| Size static / graded | SizeStatic | 1.000 | 0.000 | 0.762 | +0.110 +/- 0.023 |
| Size static / graded | SizeGraded | 0.192 | 0.000 | 0.665 | +0.014 +/- 0.014 |
| reference | none | 0.000 | 0.000 | 0.651 | |

## Q1: benign cost and receipts at matched attack-blocked rates (linear interpolation between neighbouring realized points of the same family; INTERPOLATED, not run; points outside a family's realized range are omitted)

| target attack blocked | family | ordinary rejected | receipts |
|---|---|---|---|
| 0.2 | RandP (content-blind, probability p) | 0.196 | 0.792 |
| 0.2 | SizeFixedP (heavy only, probability p) | 0.000 | 0.669 |
| 0.2 | Global bucket (rate kB/s) | 0.000 | 0.665 |
| 0.2 | Blanket pressure shedding (ramp) | 0.187 | 0.811 |
| 0.2 | Size static / graded | 0.000 | 0.666 |
| 0.4 | RandP (content-blind, probability p) | 0.420 | 0.578 |
| 0.4 | SizeFixedP (heavy only, probability p) | 0.000 | 0.687 |
| 0.4 | Global bucket (rate kB/s) | 0.000 | 0.687 |
| 0.4 | Size static / graded | 0.000 | 0.690 |
| 0.6 | RandP (content-blind, probability p) | 0.593 | 0.405 |
| 0.6 | SizeFixedP (heavy only, probability p) | 0.000 | 0.715 |
| 0.6 | Global bucket (rate kB/s) | 0.000 | 0.709 |
| 0.6 | Size static / graded | 0.000 | 0.714 |
| 0.8 | RandP (content-blind, probability p) | 0.801 | 0.198 |
| 0.8 | SizeFixedP (heavy only, probability p) | 0.000 | 0.738 |
| 0.8 | Size static / graded | 0.000 | 0.738 |

## Low-rate attack (one burst worker sends every m-th slot; LM3: 134 attack requests, about 109 kB/s; LM6: 67 requests, about 54 kB/s; bucket rate 125 kB/s) 

| block | arm | attack blocked | ordinary rejected | receipts | receipts gain vs none (paired, 95% CI) |
|---|---|---|---|---|---|
| LM3 | none | 0.000 | 0.000 | 0.675 |  |
| LM3 | SizeStatic | 1.000 | 0.000 | 0.714 | +0.039 +/- 0.008 |
| LM3 | PressureOnly | 0.147 | 0.133 | 0.864 | +0.189 +/- 0.040 |
| LM3 | RandP20 | 0.164 | 0.201 | 0.799 | +0.123 +/- 0.003 |
| LM3 | BudgetR50 | 0.537 | 0.000 | 0.691 | +0.015 +/- 0.021 |
| LM3 | BudgetR125 | 0.000 | 0.000 | 0.677 | +0.002 +/- 0.011 |
| LM6 | none | 0.000 | 0.000 | 0.682 |  |
| LM6 | SizeStatic | 1.000 | 0.000 | 0.697 | +0.016 +/- 0.015 |
| LM6 | PressureOnly | 0.129 | 0.132 | 0.866 | +0.184 +/- 0.029 |
| LM6 | RandP20 | 0.169 | 0.200 | 0.800 | +0.118 +/- 0.014 |
| LM6 | BudgetR50 | 0.075 | 0.000 | 0.687 | +0.005 +/- 0.005 |
| LM6 | BudgetR125 | 0.000 | 0.000 | 0.682 | +0.001 +/- 0.018 |

## Replay of the real size distribution (ordinary requests: calldata lengths drawn from 60,144 public-block transactions; size only)

| block | arm | attack blocked | ordinary rejected (share) | ordinary rejected (requests per run) | receipts |
|---|---|---|---|---|---|
| RMA | none | 0.000 | 0.0000 | 0.0 | 0.999 |
| RMA | SizeStatic | 1.000 | 0.0007 | 18.0 | 0.999 |
| RMA | SizeGraded | 0.000 | 0.0000 | 0.0 | 0.999 |
| RMA | PressureOnly | 0.002 | 0.0006 | 14.3 | 0.998 |
| RMA | RandP20 | 0.201 | 0.1998 | 4927.0 | 0.799 |
| RMA | BudgetR125 | 0.623 | 0.0003 | 7.0 | 0.999 |
| RMN | none | - | 0.0000 | 0.0 | 0.999 |
| RMN | SizeStatic | - | 0.0006 | 15.3 | 0.999 |
| RMN | PressureOnly | - | 0.0000 | 0.0 | 0.999 |

## Reading rules
Allowed: descriptive statements for these cells. Not allowed: statements for other sizes, rates, windows or runtimes; equivalence or ranking claims; statements about real traffic beyond calldata sizes (the replay drops the gas, state and arrival structure of real transactions); interpolated values are not measurements.

