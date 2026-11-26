# 11uu findings: confirmation latency as observed by the load generator (effective receipt-polling limit 90 s although 240 s was configured; written 2026-11-24)


## LQ1: Attack-only, 400 attack requests

| arm | runs | class | n with receipt (per run) | p50 s | p95 s | p99 s | p99.9 s | no receipt within 90 s | rejected | gate p99 ms | on-chain tx/s in window | max block gap s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | benign | 24800 | 22.4 | 47.5 | 53.4 | 58.5 | 0.0000 | 0.000 | - | 85.2 | 1 |
| none | 3 | attack | 400 | 23.8 | 40.5 | 47.5 | 48.5 | 0.0000 | 0.000 | - | 85.2 | 1 |
| BudgetR125 | 3 | benign | 24800 | 19.1 | 43.5 | 49.8 | 54.7 | 0.0000 | 0.000 | 4 | 86.0 | 1 |
| BudgetR125 | 3 | attack | 154 | 12.3 | 36.5 | 41.3 | 42.1 | 0.0000 | 0.615 | 4 | 86.0 | 1 |
| BudgetR250 | 3 | benign | 24800 | 21.1 | 46.4 | 52.4 | 58.1 | 0.0000 | 0.000 | 6 | 85.3 | 1 |
| BudgetR250 | 3 | attack | 306 | 10.8 | 24.0 | 27.8 | 28.4 | 0.0000 | 0.235 | 6 | 85.3 | 1 |
| PressureOnly | 3 | benign | 21614 | 5.7 | 15.7 | 22.1 | 30.1 | 0.0000 | 0.128 | 4 | 84.9 | 1 |
| PressureOnly | 3 | attack | 341 | 7.4 | 17.4 | 19.1 | 19.8 | 0.0000 | 0.147 | 4 | 84.9 | 1 |
| RandP20 | 3 | benign | 19809 | 1.1 | 2.1 | 3.0 | 3.7 | 0.0002 | 0.200 | 3 | 79.9 | 1 |
| RandP20 | 3 | attack | 321 | 1.4 | 2.2 | 3.1 | 3.1 | 0.0000 | 0.197 | 3 | 79.9 | 1 |
| RandP40 | 3 | benign | 14673 | 1.0 | 2.1 | 2.1 | 2.5 | 0.0025 | 0.400 | 2 | 60.2 | 1 |
| RandP40 | 3 | attack | 230 | 1.1 | 2.1 | 2.1 | 2.2 | 0.0000 | 0.424 | 2 | 60.2 | 1 |
| SizeFixedP40 | 3 | benign | 24800 | 20.7 | 45.1 | 51.1 | 56.4 | 0.0000 | 0.000 | 5 | 85.7 | 1 |
| SizeFixedP40 | 3 | attack | 243 | 9.1 | 23.2 | 26.8 | 27.8 | 0.0000 | 0.393 | 5 | 85.7 | 1 |
| SizeStatic | 3 | benign | 24797 | 18.1 | 41.4 | 47.1 | 52.1 | 0.0001 | 0.000 | 4 | 86.4 | 1 |

## LMX: Mixed attack + look-alike

| arm | runs | class | n with receipt (per run) | p50 s | p95 s | p99 s | p99.9 s | no receipt within 90 s | rejected | gate p99 ms | on-chain tx/s in window | max block gap s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | benign | 23534 | 24.1 | 51.1 | 56.5 | 61.9 | 0.0194 | 0.000 | - | 83.2 | 1 |
| none | 3 | attack | 800 | 28.0 | 46.4 | 52.8 | 54.7 | 0.0000 | 0.000 | - | 83.2 | 1 |
| none | 3 | lookalike | 400 | 29.1 | 46.4 | 49.5 | 50.7 | 0.0000 | 0.000 | - | 83.2 | 1 |
| BudgetR250 | 3 | benign | 23986 | 15.7 | 38.1 | 44.4 | 49.7 | 0.0006 | 0.000 | 5 | 85.2 | 1 |
| BudgetR250 | 3 | attack | 273 | 8.3 | 35.6 | 43.9 | 72.9 | 0.0120 | 0.654 | 5 | 85.2 | 1 |
| BudgetR250 | 3 | lookalike | 27 | 30.1 | 81.9 | 86.5 | 87.0 | 0.0909 | 0.927 | 5 | 85.2 | 1 |
| PressureOnly | 3 | benign | 20851 | 7.1 | 20.4 | 26.4 | 32.4 | 0.0000 | 0.131 | 4 | 82.7 | 1 |
| PressureOnly | 3 | attack | 683 | 8.5 | 23.3 | 27.5 | 28.6 | 0.0000 | 0.147 | 4 | 82.7 | 1 |
| PressureOnly | 3 | lookalike | 341 | 8.0 | 17.7 | 21.2 | 24.4 | 0.0000 | 0.148 | 4 | 82.7 | 1 |
| RandP40 | 3 | benign | 14083 | 1.0 | 2.0 | 2.1 | 2.1 | 0.0025 | 0.404 | 2 | 59.7 | 1 |
| RandP40 | 3 | attack | 482 | 1.1 | 2.1 | 2.1 | 2.2 | 0.0000 | 0.398 | 2 | 59.7 | 1 |
| RandP40 | 3 | lookalike | 248 | 1.0 | 2.0 | 2.1 | 2.3 | 0.0000 | 0.381 | 2 | 59.7 | 1 |
| SizeFixedP40 | 3 | benign | 24000 | 20.1 | 45.4 | 51.1 | 57.4 | 0.0000 | 0.000 | 5 | 83.7 | 1 |
| SizeFixedP40 | 3 | attack | 481 | 8.1 | 19.5 | 25.5 | 27.8 | 0.0000 | 0.398 | 5 | 83.7 | 1 |
| SizeFixedP40 | 3 | lookalike | 238 | 8.1 | 28.2 | 32.9 | 33.9 | 0.0000 | 0.404 | 5 | 83.7 | 1 |
| SizeStatic | 3 | benign | 23973 | 12.8 | 32.1 | 38.7 | 44.4 | 0.0011 | 0.000 | 5 | 86.0 | 1 |

## LRM: Attack-only, ordinary sizes replayed from public blocks

| arm | runs | class | n with receipt (per run) | p50 s | p95 s | p99 s | p99.9 s | no receipt within 90 s | rejected | gate p99 ms | on-chain tx/s in window | max block gap s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | benign | 24402 | 1.0 | 1.3 | 46.3 | 87.0 | 0.0156 | 0.000 | - | 96.5 | 1 |
| none | 3 | attack | 400 | 1.1 | 2.1 | 2.1 | 2.1 | 0.0000 | 0.000 | - | 96.5 | 1 |
| PressureOnly | 3 | benign | 24389 | 1.0 | 1.7 | 46.3 | 87.0 | 0.0161 | 0.000 | 1 | 96.5 | 1 |
| PressureOnly | 3 | attack | 400 | 1.1 | 1.7 | 1.7 | 1.7 | 0.0000 | 0.000 | 1 | 96.5 | 1 |
| SizeStatic | 3 | benign | 24782 | 1.0 | 1.0 | 1.3 | 2.0 | 0.0000 | 0.001 | 1 | 96.8 | 1 |

## Reading rules
Percentiles are over requests that received a receipt and are averaged over the runs of an arm (three seeds); the share without a receipt within the 90 s limit and the rejected share are given beside them and must be read with them (a policy that rejects heavy requests has no latency for them). Confirmation latency is the load generator's submit-to-receipt time; it is not validator-level timeliness. Differences between arms are descriptive.

