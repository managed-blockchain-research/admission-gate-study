# 11ss findings (mixed, ZGC and Nethermind cells; low-rate attack over twelve accounts; written 2026-11-23)


## MXQ: Besu G1 512 MB, mixed attack + look-alike (800 attack, 400 look-alike requests)

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.000 | 0.596 | 0 | 0 | - |
| PressureOnlyHigh | 3 | 0.076 | 0.074 | 0.080 | 0.783 | 0 | 0 | +0.188 +/- 0.088 (n=3) |
| PressureOnly | 3 | 0.141 | 0.124 | 0.126 | 0.866 | 0 | 0 | +0.270 +/- 0.023 (n=3) |
| RandP20 | 3 | 0.194 | 0.200 | 0.212 | 0.800 | 0 | 0 | +0.204 +/- 0.013 (n=3) |
| PressureOnlyLow | 3 | 0.203 | 0.216 | 0.207 | 0.783 | 0 | 0 | +0.187 +/- 0.056 (n=3) |
| RandP40 | 3 | 0.394 | 0.399 | 0.381 | 0.600 | 0 | 0 | +0.004 +/- 0.010 (n=3) |
| SizeFixedP40 | 3 | 0.395 | 0.000 | 0.424 | 0.689 | 0 | 0 | +0.093 +/- 0.038 (n=3) |
| BudgetR500 | 3 | 0.583 | 0.000 | 0.333 | 0.744 | 0 | 0 | +0.149 +/- 0.040 (n=3) |
| RandP60 | 3 | 0.585 | 0.598 | 0.607 | 0.400 | 0 | 0 | -0.196 +/- 0.021 (n=3) |
| SizeFixedP60 | 3 | 0.588 | 0.000 | 0.603 | 0.758 | 0 | 0 | +0.163 +/- 0.037 (n=3) |
| BudgetR125 | 3 | 0.880 | 0.000 | 0.854 | 0.859 | 0 | 0 | +0.263 +/- 0.020 (n=3) |
| BudgetR250 | 3 | 0.892 | 0.000 | 0.452 | 0.824 | 0 | 0 | +0.229 +/- 0.023 (n=3) |
| SizeStatic | 3 | 1.000 | 0.000 | 1.000 | 0.904 | 0 | 0 | +0.309 +/- 0.018 (n=3) |

## ZGQ: Besu ZGC 512 MB, attack-only (1,200 attack requests)

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | - | 0.452 | 2 | 2 | - |
| RandP20 | 3 | 0.205 | 0.205 | - | 0.557 | 3 | 3 | - |
| PressureOnly | 3 | 0.325 | 0.286 | - | 0.479 | 0 | 0 | - |
| RandP40 | 3 | 0.398 | 0.399 | - | 0.600 | 0 | 0 | - |
| SizeFixedP40 | 3 | 0.421 | 0.000 | - | 0.523 | 3 | 3 | - |
| BudgetR500 | 3 | 0.527 | 0.000 | - | 0.548 | 3 | 3 | - |
| RandP60 | 3 | 0.587 | 0.600 | - | 0.398 | 0 | 0 | - |
| SizeFixedP60 | 3 | 0.606 | 0.000 | - | 0.564 | 3 | 3 | - |
| BudgetR250 | 3 | 0.754 | 0.000 | - | 0.569 | 3 | 3 | - |
| BudgetR125 | 3 | 0.872 | 0.000 | - | 0.410 | 3 | 3 | - |
| SizeStatic | 3 | 0.991 | 0.000 | - | 0.526 | 3 | 3 | - |

## NMQ: Nethermind 2,048 MiB, attack-only (1,200 attack requests)

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | - | 0.551 | 0 | 0 | - |
| PressureOnly | 3 | 0.010 | 0.080 | - | 0.547 | 0 | 2 | -0.005 +/- 0.016 (n=3) |
| RandP20 | 3 | 0.210 | 0.199 | - | 0.777 | 0 | 2 | +0.226 +/- 0.035 (n=3) |
| SizeFixedP40 | 3 | 0.398 | 0.000 | - | 0.639 | 0 | 2 | +0.087 +/- 0.021 (n=3) |
| RandP40 | 3 | 0.406 | 0.399 | - | 0.601 | 0 | 0 | +0.050 +/- 0.020 (n=3) |
| BudgetR500 | 3 | 0.497 | 0.000 | - | 0.655 | 0 | 3 | +0.104 +/- 0.017 (n=3) |
| SizeFixedP60 | 3 | 0.605 | 0.000 | - | 0.669 | 0 | 2 | +0.118 +/- 0.013 (n=3) |
| RandP60 | 3 | 0.612 | 0.599 | - | 0.400 | 0 | 0 | -0.151 +/- 0.012 (n=3) |
| BudgetR250 | 3 | 0.745 | 0.000 | - | 0.692 | 0 | 2 | +0.140 +/- 0.024 (n=3) |
| BudgetR125 | 3 | 0.872 | 0.000 | - | 0.710 | 0 | 2 | +0.159 +/- 0.019 (n=3) |
| SizeStatic | 3 | 1.000 | 0.000 | - | 0.731 | 0 | 2 | +0.180 +/- 0.027 (n=3) |

## MA36: Besu G1 512 MB, 12 accounts, every 36th slot (about 132 attack requests, synchronized)

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | - | 0.683 | 0 | 0 | - |
| RandP20 | 3 | 0.240 | 0.200 | - | 0.800 | 0 | 0 | +0.116 +/- 0.012 (n=3) |
| PressureOnly | 3 | 0.265 | 0.122 | - | 0.877 | 0 | 0 | +0.194 +/- 0.024 (n=3) |
| BudgetR125 | 3 | 0.833 | 0.000 | - | 0.712 | 0 | 0 | +0.029 +/- 0.024 (n=3) |
| BudgetR50 | 3 | 0.833 | 0.000 | - | 0.708 | 0 | 0 | +0.024 +/- 0.004 (n=3) |
| SizeStatic | 3 | 1.000 | 0.000 | - | 0.710 | 0 | 0 | +0.026 +/- 0.019 (n=3) |

## MA72: Besu G1 512 MB, 12 accounts, every 72nd slot (about 66 requests, synchronized)

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | - | 0.680 | 0 | 0 | - |
| PressureOnly | 3 | 0.074 | 0.130 | - | 0.868 | 0 | 0 | +0.189 +/- 0.038 (n=3) |
| RandP20 | 3 | 0.208 | 0.201 | - | 0.799 | 0 | 0 | +0.119 +/- 0.014 (n=3) |
| BudgetR125 | 3 | 0.833 | 0.000 | - | 0.701 | 0 | 0 | +0.021 +/- 0.021 (n=3) |
| BudgetR50 | 3 | 0.833 | 0.000 | - | 0.702 | 0 | 0 | +0.022 +/- 0.014 (n=3) |
| SizeStatic | 3 | 1.000 | 0.000 | - | 0.706 | 0 | 0 | +0.027 +/- 0.011 (n=3) |

## Reading rules
Descriptive statements for these cells only. Receipts of runs whose node died are not comparable and are excluded from paired differences. No interpolated values, no ranking or equivalence claims, no statements about unseen attacks.

