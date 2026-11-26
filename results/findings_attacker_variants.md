# 11vv findings: attacker variants (Besu G1 512 MB; three seeds per arm; written 2026-11-25)


## MS36: 12 accounts, every 36th slot, STAGGERED (attack requests per run: 134)

| arm | runs | attack blocked | ordinary rejected | receipts share | node deaths | receipts gain vs none (paired) |
|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.664 | 0 | - |
| BudgetR125 | 3 | 0.000 | 0.000 | 0.668 | 0 | +0.003 +/- 0.003 |
| BudgetR50 | 3 | 0.537 | 0.000 | 0.692 | 0 | +0.028 +/- 0.014 |
| PressureOnly | 3 | 0.159 | 0.124 | 0.876 | 0 | +0.212 +/- 0.013 |
| RandP20 | 3 | 0.192 | 0.200 | 0.800 | 0 | +0.136 +/- 0.018 |
| SizeStatic | 3 | 1.000 | 0.000 | 0.715 | 0 | +0.050 +/- 0.006 |

## MS72: 12 accounts, every 72nd slot, STAGGERED (attack requests per run: 67)

| arm | runs | attack blocked | ordinary rejected | receipts share | node deaths | receipts gain vs none (paired) |
|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.674 | 0 | - |
| BudgetR125 | 3 | 0.000 | 0.000 | 0.680 | 0 | +0.006 +/- 0.019 |
| BudgetR50 | 3 | 0.075 | 0.000 | 0.682 | 0 | +0.008 +/- 0.009 |
| PressureOnly | 3 | 0.134 | 0.128 | 0.871 | 0 | +0.197 +/- 0.008 |
| RandP20 | 3 | 0.174 | 0.201 | 0.799 | 0 | +0.125 +/- 0.006 |
| SizeStatic | 3 | 1.000 | 0.000 | 0.694 | 0 | +0.020 +/- 0.011 |

## SZ32: attack payload 32,768 B (calldata 32,836 B, below the 65,604 B threshold) (attack requests per run: 400)

| arm | runs | attack blocked | ordinary rejected | receipts share | node deaths | receipts gain vs none (paired) |
|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.723 | 0 | - |
| BudgetR125 | 3 | 0.000 | 0.000 | 0.724 | 0 | +0.002 +/- 0.018 |
| PressureOnly | 3 | 0.123 | 0.114 | 0.886 | 0 | +0.163 +/- 0.030 |
| RandP20 | 3 | 0.209 | 0.200 | 0.800 | 0 | +0.077 +/- 0.022 |
| SizeStatic | 3 | 0.000 | 0.000 | 0.716 | 0 | -0.007 +/- 0.020 |

## SZ64: attack payload 65,000 B (calldata 65,092 B, below the threshold) (attack requests per run: 400)

| arm | runs | attack blocked | ordinary rejected | receipts share | node deaths | receipts gain vs none (paired) |
|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.691 | 0 | - |
| BudgetR125 | 3 | 0.000 | 0.000 | 0.684 | 0 | -0.007 +/- 0.019 |
| PressureOnly | 3 | 0.117 | 0.119 | 0.879 | 0 | +0.188 +/- 0.010 |
| RandP20 | 3 | 0.193 | 0.200 | 0.800 | 0 | +0.109 +/- 0.007 |
| SizeStatic | 3 | 0.000 | 0.000 | 0.693 | 0 | +0.001 +/- 0.008 |

## SZ131: attack payload 131,072 B (above the threshold) (attack requests per run: 400)

| arm | runs | attack blocked | ordinary rejected | receipts share | node deaths | receipts gain vs none (paired) |
|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.778 | 0 | - |
| BudgetR125 | 3 | 0.713 | 0.000 | 0.775 | 0 | -0.004 +/- 0.015 |
| PressureOnly | 3 | 0.150 | 0.110 | 0.886 | 0 | +0.108 +/- 0.029 |
| RandP20 | 3 | 0.195 | 0.200 | 0.796 | 0 | +0.018 +/- 0.015 |
| SizeStatic | 3 | 1.000 | 0.000 | 0.763 | 0 | -0.015 +/- 0.013 |

## RV: attack rate rising (m 12 -> 1 over the window) (attack requests per run: 89)

| arm | runs | attack blocked | ordinary rejected | receipts share | node deaths | receipts gain vs none (paired) |
|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.687 | 0 | - |
| BudgetR125 | 3 | 0.124 | 0.000 | 0.677 | 0 | -0.010 +/- 0.017 |
| PressureOnly | 3 | 0.139 | 0.134 | 0.866 | 0 | +0.179 +/- 0.002 |
| RandP20 | 3 | 0.210 | 0.200 | 0.800 | 0 | +0.113 +/- 0.006 |
| SizeStatic | 3 | 1.000 | 0.000 | 0.704 | 0 | +0.017 +/- 0.007 |

## RS: attack rate step (m 12, then 1 from 120 s) (attack requests per run: 217)

| arm | runs | attack blocked | ordinary rejected | receipts share | node deaths | receipts gain vs none (paired) |
|---|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.680 | 0 | - |
| BudgetR125 | 3 | 0.567 | 0.000 | 0.696 | 0 | +0.016 +/- 0.012 |
| PressureOnly | 3 | 0.174 | 0.122 | 0.877 | 0 | +0.197 +/- 0.030 |
| RandP20 | 3 | 0.223 | 0.200 | 0.800 | 0 | +0.119 +/- 0.014 |
| SizeStatic | 3 | 1.000 | 0.000 | 0.721 | 0 | +0.041 +/- 0.014 |

## Reading rules
Descriptive statements for these cells; the share blocked is over the attack requests of the run; not allowed: statements for other sizes, rates or real attackers.

