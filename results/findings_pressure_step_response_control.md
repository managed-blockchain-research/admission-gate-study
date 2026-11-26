# 11aaa findings with the control arm (change of the mean pressure reading after the step minus the change of the control; written 2026-11-26)

| arm | runs | mean u before | mean u 30-120 s after | change | change minus control |
|---|---|---|---|---|---|
| StepP00 | 3 | 0.458 | 0.645 | +0.187 | - |
| StepP20 | 3 | 0.470 | 0.591 | +0.121 | -0.066 |
| StepP40 | 3 | 0.448 | 0.560 | +0.112 | -0.075 |
| StepP60 | 3 | 0.448 | 0.547 | +0.099 | -0.088 |

## Reading rules
The step time is the first decision with p > 0 (control: 90 s after the first decision); windows 120 s before and 30-120 s after; per-run means of the reading seen by the gate; descriptive; the reading is a collection-cycle sawtooth (sd about 0.18), so the difference of the mean change is the only robust quantity here.

