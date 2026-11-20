# FINDINGS mixed_zgc_sustained_pulse (interim, 93/94 runs; TP SizeGraded seed 63503 pending; written 2026-11-19 after blind review by Codex)
Source: report_mixed_zgc_sustained_pulse.md (generated 13:14, before the last run), verify_mixed_zgc_sustained_pulse.out (26 of 93 runs with label/tierstats/service-counter mismatches, about 22 in block Z). To be regenerated when the last run ends; the header line "Node cpu05" in the generated report is wrong (cpu01).

## Allowed wording (exploratory, n = 3-5 same-seed pairs, post-hoc 65,604 B threshold)
- In the tested conditions, load shedding (blanket, size-based) increased the number of benign transactions with a receipt within the 30 s limit; blanket shedding did so at the cost of thousands of rejected benign requests (block M PressureOnly about 2,990, TS about 3,200, TP about 3,070 per run).
- In block M a static calldata rule rejected all 400 look-alike transactions (same size as the attack, legitimate) in every run.
- In block M the ground-truth filter (no benign rejected) raised receipts by 5,202 [4,857, 5,546] over none; PressureOnly 6,418 and SizeStatic 7,369 are higher in receipts but reject benign traffic, so the receipt count must always be read together with benign-not-sent.
- Sustained attack (TS): SizeSticky 21,039 vs SizeGraded 12,167 vs none 11,936 receipts; attack block rate 0.72 vs 0.22. Pulse attack (TP): differences are small (SizeSticky 17,476, none 16,257; SizeGraded n=2).
- The 30 s hold changed the rejection pattern (more of the burst blocked); this shows an effect of holding the blocked state for this 30 s setting, not a fix for the late first reaction of the pressure signal.
## Unsupported (do not write)
- "SizeStatic distinguishes attack from legitimate traffic" (it rejects the whole look-alike class).
- "A deployable filter reaches the ground-truth result" (the ground-truth arm is non-deployable; SizeStatic's higher receipts come partly from also dropping legitimate traffic).
- "PressureOnly / SizeSticky is best" or "robustly superior" (small n, post-hoc, scenario dependent).
- "Higher receipts = better service" (rejected requests are not counted as receipts); gains are partly load reduction (queueing), not attack removal.
- Any statement that a policy prevents OOM or node death in ZGC or Nethermind. ZGC: none/SizeStatic/LearnedScore 3 of 4 died, OracleBlock 4 of 4, PressureOnly 0 of 4, but two PressureOnly seeds rejected nothing (benign not sent 0) yet survived, so seed variation is large; survival differences are not attributed to the policy. Nethermind: OOM exceptions without node death (none 2/5, PressureOnly 2/5, OracleBlock 5/5, SizeStatic 5/5); cause of the higher exception count in the filter arms is unknown.
- LearnedScore "tested and ineffective" as a policy comparison (known inert; non-informative).
## Checks required before any claim from block Z (and the rest)
1. Explain the 26 mismatches (which source is authoritative; ZGC runs where the node died: client stats truncated?). Z numbers stay provisional until then.
2. Joint table per arm: attempted, admitted, rejected (by class), receipts, failed, unfinished, planned-without-record, node-death time (during load or post-scan).
3. Separate OOM exception, process death and block-production stop, and mark whether it happened during load or in the post-scan.
4. Regenerate after the last TP run; state the multiplicity (many comparisons, no p-values).
## Candidate safe sentence (Codex, adapted)
"Exploratory, small-sample results suggest that load shedding and size-based rules can increase observed 30 s benign receipts in some tested scenarios but may reject substantial legitimate traffic; a static size rule rejected every tested same-size look-alike; the ZGC results are not interpretable until the accounting mismatches are resolved. These data do not establish attack-specific protection, reliability or general superiority."

## Mismatch investigation (2026-11-19 ~15:30; script mismatch_diag_mixed_zgc_sustained_pulse.py, numbers over the 93 runs)
- 26 runs differ between labels (streamed per transaction by the workers) and tierstats (written by the workers at end of round). The cause splits into two groups that account for all 26:
  1. 13 runs (G1: M 1, TS 4, TP 1; ZGC: 7 survivors): the only difference is that labels count benign "unfinished" transactions (still pending at the end) as non-receipts and tierstats do not (difference == labels_unfinished in every one: 2-70 transactions). This is a definition difference, not an error; labels are used.
  2. 13 runs: exactly the 13 ZGC runs in which the node died (OOM; death 126-216 s after Caliper start; LearnedScore 3, OracleBlock 4, SizeStatic 3, none 3). In these runs tierstats lacks records that the labels contain (benign receipts +14 to +180, non-receipts up to +3,284, rejections up to 1,047 not-sent). Where a service ran, labels not-sent equals the service reject counter in all 10 of them (e.g. 1200/1200, 983/983, 798/798, 759/759), so labels are consistent with the independent service counter and tierstats is the truncated source (workers did not finish their end-of-round dump after the node died).
- Decision: labels + service counters are the basis of every number in the report (that was already the case: the report is built from labels); tierstats is not used for node-death runs. The 26 flags do not indicate lost or double-counted transactions in the labels. The ZGC block remains limited by the fact that most runs ended at node death: after death the remaining planned transactions have no record ("planned no record" 6,500-10,200 per run in the death arms), so receipts, failures and not-sent counts of death runs are NOT comparable with survivors; compare survival and time-to-death, not receipts.
- Still open: no per-second timeline of the load phase vs the post-scan for the death times (all deaths occur 126-216 s after Caliper start, i.e. inside the 240 s load, mostly during or right after the 60-180 s burst); node death vs block-production stop not separated (block-processing failures are 0 in all arms).


## UPDATE after the last run (94/94, report regenerated 15:19)
TP block now n = 3 for every arm: SizeSticky - SizeGraded +1,062 [-263, 2,386] (CI includes 0; pulse attack, no difference shown), SizeSticky attack block rate 0.534 vs SizeGraded 0.127. Mismatch classification unchanged: 13 runs unfinished-count definition, 13 runs ZGC node death (all from block Z). Interim statements above remain valid; the pulse comparison with SizeGraded is no longer n = 2.
