# Static gain of the pressure signal (constant rejection probability runs; written 2026-11-24)

| cell | arm | p | runs | mean u | 90th pct u | share u >= 0.60 |
|---|---|---|---|---|---|---|
| MXQ | RandP20 | 0.2 | 3 | 0.489 | 0.727 | 0.308 |
| MXQ | RandP40 | 0.4 | 3 | 0.473 | 0.692 | 0.207 |
| MXQ | RandP60 | 0.6 | 3 | 0.470 | 0.626 | 0.164 |
| NMQ | RandP20 | 0.2 | 3 | 0.299 | 0.608 | 0.145 |
| NMQ | RandP40 | 0.4 | 3 | 0.207 | 0.470 | 0.000 |
| NMQ | RandP60 | 0.6 | 3 | 0.114 | 0.208 | 0.000 |
| Q1 | RandP20 | 0.2 | 3 | 0.484 | 0.731 | 0.309 |
| Q1 | RandP40 | 0.4 | 3 | 0.487 | 0.700 | 0.264 |
| Q1 | RandP60 | 0.6 | 3 | 0.484 | 0.640 | 0.185 |
| Q1 | RandP80 | 0.8 | 3 | 0.452 | 0.628 | 0.155 |
| ZGQ | RandP20 | 0.2 | 3 | 0.765 | 0.977 | 0.783 |
| ZGQ | RandP40 | 0.4 | 3 | 0.709 | 0.975 | 0.707 |
| ZGQ | RandP60 | 0.6 | 3 | 0.517 | 0.797 | 0.311 |

## Slope du/dp (least squares over the arms; mean u against p) and loop gain of the pressure-graded rule

| cell | points | du/dp | loop gain K = (1/0.30) x du/dp |
|---|---|---|---|
| MXQ | 3 | -0.048 | -0.16 |
| NMQ | 3 | -0.462 | -1.54 |
| Q1 | 4 | -0.048 | -0.16 |
| ZGQ | 3 | -0.621 | -2.07 |

## Reading rules
The slope is a static relation between a constant rejection probability and the mean post-collection reading; it does not give the delay or the dynamics of the loop. The sign shows the direction of the effect of rejection on the signal: a negative slope means that more rejection lowers the reading. The loop gain is the product with the ramp slope and is only a rough size; a stability statement needs the delay (see the step-input runs).

