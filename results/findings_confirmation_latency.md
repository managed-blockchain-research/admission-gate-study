# 11ww findings: confirmation latency as observed by the load generator (receipt limit 240 s verified by the timeout audit files; written 2026-11-24)


## LQ1: Attack-only, 400 attack requests

| arm | runs | class | n with receipt (per run) | p50 s | p95 s | p99 s | p99.9 s | no receipt within 240 s | rejected | gate p99 ms | on-chain tx/s in window | max block gap s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | benign | 24800 | 22.1 | 47.7 | 53.1 | 58.8 | 0.0000 | 0.000 | - | 85.1 | 1 |
| none | 3 | attack | 400 | 28.8 | 43.6 | 50.8 | 51.9 | 0.0000 | 0.000 | - | 85.1 | 1 |
| BudgetR125 | 3 | benign | 24800 | 19.8 | 43.8 | 49.7 | 54.8 | 0.0000 | 0.000 | 6 | 85.8 | 1 |
| BudgetR125 | 3 | attack | 154 | 13.5 | 39.1 | 43.3 | 44.5 | 0.0000 | 0.615 | 6 | 85.8 | 1 |
| BudgetR250 | 3 | benign | 24800 | 21.4 | 46.4 | 52.4 | 57.8 | 0.0000 | 0.000 | 6 | 85.2 | 1 |
| BudgetR250 | 3 | attack | 306 | 11.2 | 23.2 | 27.1 | 28.2 | 0.0000 | 0.235 | 6 | 85.2 | 1 |
| PressureOnly | 3 | benign | 21771 | 6.1 | 16.4 | 21.7 | 29.7 | 0.0000 | 0.122 | 5 | 85.2 | 1 |
| PressureOnly | 3 | attack | 346 | 6.5 | 16.4 | 18.6 | 19.7 | 0.0000 | 0.136 | 5 | 85.2 | 1 |
| RandP20 | 3 | benign | 19798 | 1.1 | 2.1 | 3.0 | 3.8 | 0.0003 | 0.201 | 2 | 79.7 | 1 |
| RandP20 | 3 | attack | 318 | 1.6 | 2.1 | 2.8 | 3.0 | 0.0000 | 0.204 | 2 | 79.7 | 1 |
| RandP40 | 3 | benign | 14654 | 1.0 | 2.0 | 2.1 | 2.1 | 0.0022 | 0.401 | 2 | 59.7 | 1 |
| RandP40 | 3 | attack | 240 | 1.1 | 2.1 | 2.1 | 2.2 | 0.0000 | 0.400 | 2 | 59.7 | 1 |
| SizeFixedP40 | 3 | benign | 24800 | 20.8 | 45.1 | 51.1 | 57.1 | 0.0000 | 0.000 | 5 | 85.5 | 1 |
| SizeFixedP40 | 3 | attack | 237 | 9.1 | 23.5 | 26.6 | 27.2 | 0.0000 | 0.408 | 5 | 85.5 | 1 |
| SizeStatic | 3 | benign | 24800 | 18.1 | 41.1 | 47.1 | 52.8 | 0.0000 | 0.000 | 5 | 86.2 | 1 |

## LMX: Mixed attack + look-alike

| arm | runs | class | n with receipt (per run) | p50 s | p95 s | p99 s | p99.9 s | no receipt within 240 s | rejected | gate p99 ms | on-chain tx/s in window | max block gap s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | benign | 23462 | 23.8 | 51.4 | 57.4 | 62.8 | 0.0000 | 0.000 | - | 83.3 | 1 |
| none | 3 | attack | 800 | 27.5 | 44.2 | 51.2 | 52.6 | 0.0000 | 0.000 | - | 83.3 | 1 |
| none | 3 | lookalike | 400 | 29.2 | 47.4 | 50.1 | 50.8 | 0.0000 | 0.000 | - | 83.3 | 1 |
| BudgetR250 | 3 | benign | 24000 | 15.1 | 38.1 | 44.7 | 79.1 | 0.0000 | 0.000 | 4 | 85.5 | 1 |
| BudgetR250 | 3 | attack | 243 | 12.1 | 52.6 | 85.5 | 116.7 | 0.0000 | 0.697 | 4 | 85.5 | 1 |
| BudgetR250 | 3 | lookalike | 63 | 42.5 | 96.1 | 99.9 | 101.2 | 0.0000 | 0.842 | 4 | 85.5 | 1 |
| PressureOnly | 3 | benign | 20543 | 4.7 | 15.4 | 21.8 | 30.1 | 0.0000 | 0.144 | 6 | 83.0 | 1 |
| PressureOnly | 3 | attack | 685 | 6.4 | 17.5 | 21.6 | 23.0 | 0.0000 | 0.144 | 6 | 83.0 | 1 |
| PressureOnly | 3 | lookalike | 345 | 6.1 | 17.1 | 21.1 | 22.1 | 0.0000 | 0.138 | 6 | 83.0 | 1 |
| RandP40 | 3 | benign | 14247 | 1.0 | 2.1 | 2.1 | 2.2 | 0.0017 | 0.399 | 2 | 59.9 | 1 |
| RandP40 | 3 | attack | 469 | 1.1 | 2.1 | 2.1 | 2.3 | 0.0000 | 0.414 | 2 | 59.9 | 1 |
| RandP40 | 3 | lookalike | 240 | 1.0 | 2.0 | 2.1 | 2.1 | 0.0000 | 0.401 | 2 | 59.9 | 1 |
| SizeFixedP40 | 3 | benign | 24000 | 20.1 | 45.4 | 51.4 | 57.4 | 0.0000 | 0.000 | 5 | 83.8 | 1 |
| SizeFixedP40 | 3 | attack | 474 | 9.1 | 26.1 | 33.2 | 35.2 | 0.0000 | 0.408 | 5 | 83.8 | 1 |
| SizeFixedP40 | 3 | lookalike | 248 | 9.3 | 20.7 | 23.1 | 23.8 | 0.0000 | 0.380 | 5 | 83.8 | 1 |
| SizeStatic | 3 | benign | 24000 | 13.1 | 32.4 | 38.7 | 73.1 | 0.0000 | 0.000 | 4 | 86.3 | 1 |

## LRM: Attack-only, ordinary sizes replayed from public blocks

| arm | runs | class | n with receipt (per run) | p50 s | p95 s | p99 s | p99.9 s | no receipt within 240 s | rejected | gate p99 ms | on-chain tx/s in window | max block gap s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | benign | 23790 | 1.0 | 1.0 | 2.0 | 2.0 | 0.0106 | 0.000 | - | 97.4 | 1 |
| none | 3 | attack | 400 | 1.1 | 1.1 | 1.1 | 1.1 | 0.0000 | 0.000 | - | 97.4 | 1 |
| PressureOnly | 3 | benign | 23793 | 1.0 | 1.0 | 2.0 | 2.0 | 0.0106 | 0.000 | 2 | 97.4 | 1 |
| PressureOnly | 3 | attack | 400 | 1.1 | 1.1 | 1.1 | 1.4 | 0.0000 | 0.000 | 2 | 97.4 | 1 |
| SizeStatic | 3 | benign | 24785 | 1.0 | 1.0 | 1.0 | 2.0 | 0.0000 | 0.001 | 1 | 96.9 | 1 |

## Reading rules
Percentiles are over requests that received a receipt and are averaged over the runs of an arm (three seeds); the share without a receipt within the 240 s limit and the rejected share are given beside them and must be read with them (a policy that rejects heavy requests has no latency for them). Confirmation latency is the load generator's submit-to-receipt time; it is not validator-level timeliness. Differences between arms are descriptive.

