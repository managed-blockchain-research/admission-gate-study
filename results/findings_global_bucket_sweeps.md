# FINDINGS global_bucket_sweeps - reporting scope fixed BEFORE reading results (written 2026-11-19 09:50, while mixed_zgc_sustained_pulse/global_bucket_sweeps were running)
Only the header exists; results are added after report_global_bucket_sweeps.md and verify_global_bucket_sweeps.out are read and reviewed blind.

## Primary question (decides the main text)
In block MX (attack + look-alike in one run), how much of the legitimate heavy traffic does each arm keep (per-class admission rate and per-class receipt-within-30-s rate for the legitimate heavy class and for the attack class separately), compared with SizeStatic, SizeGraded, fixed-probability and none, same seeds, same node?
## Secondary question
Blocks I1/I3/I6 (attack intensity 1/3/6 burst workers): benign receipts and benign rejections per arm; whether the ordering of arms is stable across intensities.
## Appendix only
L1 (look-alike alone), ZG, NM, BudgetAdapt500 vs fixed-R, per-run tables. All arms and blocks are reported, including unfavourable ones.
## Parameters to state in Methods
Global (service-wide) bucket, not per sender or peer; heavy = calldata > 65,604 B (post-hoc threshold); capacity 200,000 B (about two heavy transactions); initial bucket full; refill 125/250/500 KB/s; Adapt500 = 500 KB/s x (1 - 0.75 grad(u_t)). Attack and legitimate heavy share the bucket, so an attack can exhaust it and block legitimate heavy transactions; report this directly.
## Interpretation limits
Source of any gain = metering of heavy bytes, not attack identification (the Isolation Forest is not involved). Exploratory; n = 4-5 seeds per cell; thresholds post hoc; mostly Besu G1 512 MB.
## Items added from the blind review
mixed_zgc_sustained_pulse Sticky (TS/TP): also report first activation time, hold time after the last attack, and benign rejections during recovery; no difference means only "no gain observed for this 30 s hold". mixed_zgc_sustained_pulse ZGC LearnedScore: shows the detector is inert there, not how an active runtime-aware control behaves under ZGC. `onchain/offered` is a harness validity label only (numerator includes attack); separate measurement artefact from real non-confirmation before interpreting the NM values (0.945-0.947).


# RESULTS (126/126 runs; report_global_bucket_sweeps.md 16:03; blind review by Codex 2026-11-19 16:30)
## Primary question (MX: attack 800 + look-alike 400, G1 512 MB, n = 4): does the bucket protect legitimate heavy traffic? NO.
Look-alike (legitimate heavy) rejected per run: SizeStatic 400/400; BudgetR250 368 (92%); BudgetAdapt500 315 (79%); BudgetR500 231 (58%; per seed 398, 327, 200, 0). Attack block rate: SizeStatic 1.00; R250 0.66; R500 0.46; Adapt500 0.44. Benign receipts vs none: SizeStatic +7,559 [7,308, 7,811]; R250 +5,302 [5,087, 5,516]; R500 +3,407 [2,884, 3,930]; Adapt500 +3,615 [3,412, 3,818]. Bucket arms vs SizeStatic: R250 -2,258, R500 -4,152, Adapt500 -3,944 (all CIs exclude 0). Adapt500 vs R500: +208 [-435, 851] (no difference). The bucket is global and first-come-first-served, so legitimate heavy and attack share it; admitted heavy counts follow the configured budget (R250 306, R500 602, Adapt500 534 of 1,200) regardless of class.
## Secondary (attack only, I1/I3/I6 = 400/1,200/2,400 attack tx; n = 3)
Benign receipts rise as heavy bytes admitted fall: I6 none 11,758 (1.97 MB/s), FixedP20 13,195 (1.58), R500 21,739 (0.495), R250 22,584 (0.251), R125 22,747 (0.126), SizeStatic 22,724 (0). I3: none 14,080; FixedP20 15,036; R500 17,742; R250 19,760; R125 20,974; SizeStatic 22,006. I1 (400 attack tx, 0.33 MB/s offered): R500 never binds (admits all 400, = none); R125 17,723; SizeStatic 18,885. No benign request was rejected in I1/I3/I6 (benign requests are small).
- The comparison with FixedP20 is NOT a rate-matched test: P20 was taken from an earlier experiment and blocks 0.20 of attack transactions whereas the buckets block 0.50-0.94. Receipt differences confound the mechanism with how much heavy traffic is removed. No claim that the bucket beats a fixed-probability rule.
- Result in words: limiting the heavy bytes admitted (by any rule) is what coincides with more benign receipts; SizeStatic is the best or tied-best in receipts in every block but rejects all legitimate heavy traffic.
## L1 (look-alike only, 400 tx, 0.33 MB/s offered)
R500 rejects 0 (identical to none); R250 rejects 94 (23.5%); SizeStatic rejects 400 (100%). A budget above the legitimate heavy rate keeps legitimate heavy traffic, but the same budget does not stop the attack in I1 (R500 blocks 0.000), so the budget level decides both, and the bucket does not separate the classes.
## ZGC (ZG) and Nethermind (NM)
ZG: node died in 19 of 20 runs (all arms; SizeStatic 3 of 4); receipts ~6.6-7.1 k in all arms; no policy ranking is possible (runs end at node death; censored). NM: OOM exception runs of 4 (no node deaths): none 2, SizeStatic 4, R250 1, Adapt500 0; receipts none 13,154, Adapt500 15,776, R250 16,550, SizeStatic 17,509. Counts too small for comparative claims.
## Verification
20 of 126 runs have label/tierstats differences: 1 is the unfinished-count definition difference, 19 are exactly the ZGC runs where the node died (labels agree with service counters, tierstats truncated), same as mixed_zgc_sustained_pulse. Report header says "Node cpu05" (fixed text in the generator; real nodes cpu01-03: A cpu02, B cpu03; mixed_zgc_sustained_pulse cpu01).
## Allowed wording
"In these exploratory runs, a global token bucket on heavy bytes was associated with more benign receipts when heavy traffic was attack-only, but with attack and same-size legitimate heavy traffic sharing the bucket it rejected 58-92% of the legitimate heavy transactions; it did not protect legitimate heavy traffic and was below the static size rule in receipts. Rate-matched, randomized, per-sender analyses are needed."
## Not allowed
"Token bucket protects legitimate heavy traffic", "meters instead of rejecting" as an advantage in MX, "better than the fixed-probability rule" (not rate-matched), any ZGC/NM policy ranking, any attack-detection claim, equating more receipts with better service.
## Consequence for the paper (decision for the authors)
global_bucket_sweeps does NOT supply a deployable technique that beats the static size rule and keeps legitimate heavy traffic; the characterization framing (measured upper bound, cost of blanket shedding and of size rules on same-size legitimate traffic, detectability limit) is what the evidence supports. The budget idea would need a mechanism that separates the classes (per-sender or per-class metering) before it could be a contribution.

## Added 2026-11-19 (offline, from accglobal_bucket_sweeps_per_run.csv, 90 Besu G1 runs of blocks I1/I3/I6/MX/L1): relation of admitted heavy bytes to GC and receipts (for response item R1-2)
Pearson correlation across the arms/seeds of each block between heavy bytes admitted (MB/s in the 120 s window) and G1 total pause: I1 0.66 (n=18), I3 0.94, I6 0.99, MX 0.96, L1 0.34 (n=16); pooled over blocks 0.52 (blocks differ in offered intensity). Between heavy MB/s admitted and benign receipts within 30 s: -0.99, -1.00, -0.99, -0.99, -0.97. Reading: within a block the amount of heavy calldata let through tracks G1 pause and (inversely) benign receipts; this supports calldata bytes as a usable cost proxy in this workload, NOT a per-transaction allocation measurement and NOT a claim about other workloads (arms differ only in how many heavy transactions are admitted, so the correlation is partly by construction; 3-4 seeds per cell; no causal claim).
