# 11aaa findings: step response of the pressure reading (Besu G1 512 MB; written 2026-11-25)

| arm | seed | mean u before the step (-120..0 s) | sd before | mean u 30..120 s after | first time outside pre mean +/- 2 sd (5 s moving average), s after the step |
|---|---|---|---|---|---|
| StepP20 | 67801 | 0.465 | 0.189 | 0.581 | none |
| StepP20 | 67802 | 0.475 | 0.182 | 0.586 | none |
| StepP20 | 67803 | 0.460 | 0.165 | 0.605 | none |
| StepP40 | 67801 | 0.449 | 0.179 | 0.578 | none |
| StepP40 | 67802 | 0.469 | 0.195 | 0.550 | none |
| StepP40 | 67803 | 0.411 | 0.182 | 0.553 | none |
| StepP60 | 67801 | 0.452 | 0.141 | 0.533 | none |
| StepP60 | 67802 | 0.439 | 0.176 | 0.565 | none |
| StepP60 | 67803 | 0.443 | 0.153 | 0.543 | none |

## Mean over seeds

| arm | change of mean u (after - before) | runs with a clear first-exit time | median first-exit time s |
|---|---|---|---|
| StepP20 | +0.124 | 0 of 3 | - |
| StepP40 | +0.117 | 0 of 3 | - |
| StepP60 | +0.102 | 0 of 3 | - |

## Reading rules
The step time is the first decision with a positive rejection probability; the reading is the post-collection occupancy seen by the gate (1 Hz source, 0.2 s polling, mean per second). It shows the response of the reading in this cell only; the reading has a collection-cycle sawtooth, so the first-exit time is a rough indicator, not an identified delay.

