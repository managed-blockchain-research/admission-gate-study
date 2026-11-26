# 11aab findings: two Besu nodes on one Slurm node, gate in front of node A only (written 2026-11-26)

| block | arm | runs | attack blocked | ordinary rejected | node A GC total ms | node A GC max ms | node B GC total ms | node B GC max ms | node A peak RSS MB | node B peak RSS MB | peak pool A | peak pool B | max head lag (blocks) | OOM | node deaths | verdicts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MN0 | none | 3 | - | 0.0000 | 25619 | 123.0 | 5559 | 83.8 | 1540 | 1219 | 1312 | 1458 | 4 | 0 | 0 | SURVIVED |
| MN1 | none | 3 | 0.000 | 0.0000 | 27137 | 120.4 | 5768 | 108.8 | 1512 | 1205 | 1288 | 1443 | 5 | 0 | 0 | SURVIVED |
| MN1 | BudgetR125 | 3 | 0.615 | 0.0000 | 25114 | 120.2 | 5265 | 95.8 | 1558 | 1209 | 1251 | 1395 | 3 | 0 | 0 | SURVIVED |
| MN1 | PressureOnly | 3 | 0.285 | 0.1857 | 13943 | 119.0 | 7216 | 91.2 | 1485 | 1207 | 614 | 643 | 3 | 0 | 0 | FAILED |
| MN1 | RandP20 | 3 | 0.188 | 0.1986 | 9489 | 105.8 | 4998 | 78.0 | 1454 | 1189 | 127 | 236 | 3 | 0 | 0 | FAILED |
| MN1 | SizeStatic | 3 | 1.000 | 0.0000 | 25411 | 124.9 | 5444 | 90.0 | 1518 | 1222 | 1200 | 1371 | 3 | 0 | 0 | SURVIVED |
| MN2 | none | 3 | 0.000 | 0.0000 | 24520 | 123.1 | 5122 | 92.8 | 1568 | 1199 | 1291 | 1385 | 2 | 0 | 0 | SURVIVED |
| MN2 | BudgetR125 | 3 | 0.000 | 0.0000 | 25135 | 124.6 | 5188 | 85.8 | 1546 | 1217 | 1263 | 1370 | 3 | 0 | 0 | SURVIVED |
| MN2 | PressureOnly | 3 | 0.000 | 0.1825 | 11681 | 93.7 | 5824 | 76.2 | 1484 | 1202 | 584 | 610 | 3 | 0 | 0 | FAILED |
| MN2 | SizeStatic | 3 | 0.000 | 0.0000 | 25284 | 124.1 | 5453 | 98.9 | 1511 | 1210 | 1265 | 1377 | 3 | 0 | 0 | SURVIVED |

Blocks: MN0 = no attack (control); MN1 = attack submitted to the gated node A; MN2 = attack submitted to the ungated node B (gate on node A only).

## Reading rules
Node B has no gate and no miner; it receives every transaction only by gossip from node A and is the observer of what the gate does or does not protect. Runs are executions of one seeded design, not independent samples. One run (SizeStatic seed 67903) was refused at start because the nodes had not connected; it was rerun with the same seed after the chains finished and the failed directory is kept.


## Reading of the table (2026-11-26)
- Control (MN0, no attack): node A GC total 25.6 s, node B 5.6 s, peak pools 1312/1458; the attack at 3.33% of requests (MN1/MN2 'none') does not raise either node's GC total beyond run-to-run spread (27.1/5.8 s and 24.5/5.1 s). At this attack size the multi-peer cell shows no measurable harm to protect against, so no protection effect of any arm can be read off node B.
- MN1 (attack to the gated node A): SizeStatic blocks all attack requests (1.000) with no ordinary rejection, and node B's GC (5.4 s), RSS (1222 MB) and pool (1371) equal the no-gate values; BudgetR125 blocks 0.615; PressureOnly and RandP20 block 0.285 and 0.188 while rejecting 18.6% and 19.9% of ordinary requests (their runs fail the on-chain/offered check of 0.95), which halves node A's GC total (13.9 s, 9.5 s) and pool size (614, 127) through lower throughput, not through targeting.
- MN2 (attack submitted to the ungated node B): the gate on node A blocks nothing (0.000 for every arm) because the attack never passes it; node A and B figures equal the no-gate row for SizeStatic/BudgetR125, and PressureOnly differs only through its blanket rejection of ordinary requests on A.
- Head lag between the nodes stayed at 5 blocks or fewer in every run; no OOM, no node death.
- Claim boundary: a gate in front of one node protects only traffic that passes through it; the other node's attack traffic is outside its reach. Sizes and rates here are those of the 3.33% cell; the cell does not show node B being degraded by A's attack.
