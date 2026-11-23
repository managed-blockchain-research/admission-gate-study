# 11tt findings (comparison policies; fail-closed versus fail-open gate during a 20 s gate outage; written 2026-11-23)


## DQ1: Besu G1 512 MB, attack-only (400 attack requests), comparison policies

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| CPUramp | 3 | 0.000 | 0.000 | - | 0.652 | 0 | 0 | - |
| CircuitBreaker | 3 | 0.000 | 0.000 | - | 0.650 | 0 | 0 | - |
| SupGraded | 3 | 0.181 | 0.000 | - | 0.666 | 0 | 0 | - |
| CPUrampMid | 3 | 0.258 | 0.242 | - | 0.757 | 0 | 0 | - |
| CPUrampLow | 3 | 0.376 | 0.377 | - | 0.622 | 0 | 0 | - |
| SupStatic | 3 | 1.000 | 0.000 | - | 0.761 | 0 | 0 | - |

## DMX: Besu G1 512 MB, mixed attack + look-alike, comparison policies

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| CPUramp | 3 | 0.000 | 0.000 | 0.000 | 0.592 | 0 | 0 | - |
| CircuitBreaker | 3 | 0.003 | 0.001 | 0.003 | 0.594 | 0 | 0 | - |
| SupGraded | 3 | 0.211 | 0.000 | 0.000 | 0.621 | 0 | 0 | - |
| CPUrampMid | 3 | 0.266 | 0.234 | 0.257 | 0.765 | 0 | 0 | - |
| CPUrampLow | 3 | 0.402 | 0.402 | 0.423 | 0.596 | 0 | 0 | - |
| SupStatic | 3 | 1.000 | 0.000 | 0.000 | 0.809 | 0 | 0 | - |

## DZG: Besu ZGC 512 MB, attack-only, comparison policies

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| CPUramp | 3 | 0.000 | 0.000 | - | 0.562 | 3 | 3 | - |
| CircuitBreaker | 3 | 0.382 | 0.329 | - | 0.492 | 0 | 0 | - |

## DNM: Nethermind 2,048 MiB, attack-only, comparison policies

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| CPUramp | 3 | 0.000 | 0.000 | - | 0.544 | 0 | 2 | - |
| CircuitBreaker | 3 | 0.000 | 0.000 | - | 0.550 | 1 | 1 | - |

## FCO: Besu G1 512 MB, attack-only, gate frozen 20 s, FAIL-OPEN (unanswered query = accept)

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| PressureOnly | 3 | 0.127 | 0.117 | - | 0.876 | 0 | 0 | - |
| BudgetR125 | 3 | 0.530 | 0.000 | - | 0.706 | 0 | 0 | - |
| SizeStatic | 3 | 0.847 | 0.000 | - | 0.744 | 0 | 0 | - |

## FCC: same, FAIL-CLOSED (unanswered query = reject)

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| PressureOnly | 3 | 0.253 | 0.178 | - | 0.822 | 0 | 0 | - |
| BudgetR125 | 3 | 0.682 | 0.071 | - | 0.885 | 0 | 0 | - |
| SizeStatic | 3 | 1.000 | 0.071 | - | 0.899 | 0 | 0 | - |

## FCZ: FAIL-CLOSED, gate never frozen

| arm | runs | attack blocked | ordinary rejected | look-alike rejected | receipts share | node deaths | OOM-exception runs | receipts gain vs none (paired, live nodes) |
|---|---|---|---|---|---|---|---|---|
| PressureOnly | 3 | 0.133 | 0.116 | - | 0.878 | 0 | 0 | - |
| BudgetR125 | 3 | 0.615 | 0.000 | - | 0.713 | 0 | 0 | - |
| SizeStatic | 3 | 1.000 | 0.000 | - | 0.766 | 0 | 0 | - |

## Reading rules
Descriptive statements for these cells only. Receipts of runs whose node died are not comparable and are excluded from paired differences. No interpolated values, no ranking or equivalence claims, no statements about unseen attacks.

