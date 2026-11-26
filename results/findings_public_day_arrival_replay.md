# 11zz findings: replay of arrival counts and sizes of public mainnet traffic (written 2026-11-25)


## ER50: window p50 (11.6 tx/s mean), one attacking account (400 attack requests)

| arm | runs | ordinary offered per run | attack blocked | ordinary rejected | receipts within 30 s | no receipt (any reason) | p50 s | p99 s | p99.9 s | node deaths | OOM runs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | 2725 | 0.000 | 0.0000 | 0.9971 | 0.0029 | 1.0 | 2.0 | 2.0 | 0 | 0 |
| BudgetR125 | 3 | 2725 | 0.616 | 0.0001 | 0.9969 | 0.0029 | 1.0 | 1.7 | 2.0 | 0 | 0 |
| PressureOnly | 3 | 2725 | 0.000 | 0.0000 | 0.9971 | 0.0029 | 1.0 | 1.7 | 2.0 | 0 | 0 |
| RandP20 | 3 | 2725 | 0.217 | 0.1961 | 0.8012 | 0.0033 | 1.0 | 2.0 | 2.0 | 0 | 0 |
| SizeStatic | 3 | 2725 | 1.000 | 0.0005 | 0.9966 | 0.0029 | 1.0 | 1.0 | 1.7 | 0 | 0 |

## ER99: window p99 (16.9 tx/s mean), one attacking account (400 attack requests)

| arm | runs | ordinary offered per run | attack blocked | ordinary rejected | receipts within 30 s | no receipt (any reason) | p50 s | p99 s | p99.9 s | node deaths | OOM runs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | 4015 | 0.000 | 0.0000 | 0.9961 | 0.0039 | 1.0 | 2.0 | 16.3 | 0 | 0 |
| BudgetR125 | 3 | 4015 | 0.615 | 0.0002 | 0.9978 | 0.0019 | 1.0 | 1.4 | 2.0 | 0 | 0 |
| PressureOnly | 3 | 4015 | 0.000 | 0.0000 | 0.9961 | 0.0039 | 1.0 | 2.0 | 16.3 | 0 | 0 |
| RandP20 | 3 | 4014 | 0.208 | 0.1978 | 0.7976 | 0.0057 | 1.0 | 2.0 | 16.0 | 0 | 0 |
| SizeStatic | 3 | 4015 | 1.000 | 0.0006 | 0.9975 | 0.0019 | 1.0 | 1.0 | 2.0 | 0 | 0 |

## ENO: window p99, no attack

| arm | runs | ordinary offered per run | attack blocked | ordinary rejected | receipts within 30 s | no receipt (any reason) | p50 s | p99 s | p99.9 s | node deaths | OOM runs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 3 | 4122 | - | 0.0000 | 0.9968 | 0.0032 | 1.0 | 1.0 | 15.2 | 0 | 0 |
| PressureOnly | 3 | 4122 | - | 0.0000 | 0.9970 | 0.0030 | 1.0 | 1.0 | 15.3 | 0 | 0 |
| SizeStatic | 3 | 4119 | - | 0.0005 | 0.9972 | 0.0023 | 1.0 | 1.0 | 2.0 | 0 | 0 |

## Reading rules
Ordinary requests are the requests kept after thinning to the replayed per-second counts; the senders are the 30 load-generator accounts and the sizes are the replayed calldata lengths; the attack is the registered 98 KB attack. Descriptive statements about one day of public traffic; not about other days, private order flow or real attackers.

