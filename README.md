# Admission-gate study: data, scripts and apparatus

Companion material for the manuscript "What Can an Admission Gate Separate? A Controlled Characterization of Policies for Calldata-Heavy Transactions in Managed Ethereum Clients".

The campaign (850 registered runs plus one excluded batch of 60) is organised in experiment families. Each file name carries a descriptive family name. The pre-registration document and the bodies of the analysis scripts use the original two-letter family ids (for example 11jj); this table maps them.

| Family (id in file bodies and in the pre-registration) | File prefix | Content | Paper section |
|---|---|---|---|
| 11ff | baseline_besu_g1_512mb | Besu G1 512 MB: no defense, ground-truth filter, blanket shedding, ZGC cells | VI-A, VI-C |
| 11gg | baseline_besu_1gb | Besu 1 GB heap cells (G1 and ZGC) | VI-C |
| 11hh | baseline_nethermind_2gib | Nethermind 2 GiB cells | VI-C |
| 11ii | baseline_controls_attack_only | Attack-only controls: size rules, random and fixed-probability shedding | VI-A, VI-B |
| 11jj | mixed_zgc_sustained_pulse | Mixed attack plus look-alike traffic, ZGC, Nethermind size rule, sustained and pulsed attacks with a pressure hold | VI-A, VI-B, VI-C |
| 11kk | global_bucket_sweeps | Global heavy-byte bucket: intensity sweep, below-budget stream, mixed traffic, ZGC, Nethermind | VI-A, VI-B |
| 11mm | sender_split | Per-sender bucket and sender fragmentation (four scenarios) | (superseded by the history experiment scenarios; see VI-B) |
| 11nn | deferral_first_batch_excluded | First deferral batch (EXCLUDED: the load generator treated the defer answer as accept) | not used |
| 11nr | deferral_rerun | Deferral re-run after the client fix (used in the paper) | VI-B |
| 11oo | heap_sweep_and_sampling | Nethermind heap sweep (1024/3072/4096 MiB, two loads, benign-only control) and gate-side pressure refresh interval | VI-C |
| 11pp | history_weighted | History-weighted per-sender bucket, six scenarios | VI-B |
| 11qq | matched_operating_points | Operating-point sweeps per policy family on the attack-only Besu cell (19 arms); its blocks LR5 and LR10 contain 400 attack requests like the main cell (module granularity) and are replicates, not low-rate results | VI-B |
| 11rr | lowrate_and_realsize_replay | Sustained low-rate attack (every 3rd/6th slot) and replay of the calldata-size distribution of public mainnet transactions (with and without attack) | VI-B, Appendix B |

## Folders
- `results/`: per-run tables (one row per run: counts of attack, look-alike and ordinary requests by outcome, survival fields, GC pause), results reports with paired differences and per-pair values, findings notes with the allowed and not-allowed wording of each result, metric definitions, and the output of the independent consistency check of every run (`verification_*`).
- `analysis_scripts/`: scripts that produce the reports, the frontier and benign-harm tables, the offline detector analysis, and the consistency check.
- `apparatus/`: pinned parameter files (hashes of launchers, services and workload modules), the policy services (global bucket, per-sender, history-weighted, deferral shaper), the workload modules for the sender-split, deferral and history experiments, and the job-start self-check scripts.
- `preregistration/`: an excerpt of the registration document with the design of every experiment reported here and its amendment log (dated; each entry says whether any run had started). Sections of other studies are removed.

## Reading notes
- Receipts are benign transactions with a receipt within the load generator's 30 s limit; rejected requests are not receipts.
- Receipts of runs that end in node death are not comparable (transactions after the death are not recorded).
- The excluded deferral batch is kept for completeness; the re-run is the data used for any statement about deferral.
- The original run directories (raw labels, logs) are not included; the per-run tables are derived from them and the consistency check compares three independent sources inside each run.

## Differences between the published files and the files that ran
The pinned parameter files `apparatus/ACC_PINS_*.json` record the SHA-256 of the launchers, services, workload modules and self-check scripts exactly as they ran. For publication, comments, absolute paths and a few identifiers were edited: absolute paths became relative placeholders, names of unrelated studies were removed, and the names of two internal switches of the instrumented client build were renamed (the monitor-only mode switch is `GOV_MODE`, the run tag variable is `RUN_TAG`). No decision logic was changed. The hashes of the published copies are in `apparatus/SHA256_PUBLISHED_FILES.txt`; they differ from the pinned hashes for that reason. The launcher shell scripts and the instrumented client builds are not included.

## What is not included
Raw run directories (labels, logs), the instrumented client builds, the cluster launch scripts, and the code of the earlier, withdrawn evaluation. The scripts in `analysis_scripts/` therefore document how each table was computed from the raw data; they cannot be re-run without it.

## License
MIT License (see `LICENSE`). The data tables and documents are released under the same terms.

## Added in v1.1
Families 11qq and 11rr (above): per-run tables, analysis scripts, the workload module with the two new optional modes (`apparatus/raacV5BurstReal.js`), the size sample used for the replay (`apparatus/real_sizes.json`, calldata lengths only), the read-only block-sampling script and the sampled lengths (`results/realtrace/`), the self-check and pin files, and the registration sections 11qq and 11rr. The sampled blocks were read from a public node with read-only calls; nothing was sent to the main network. Launch scripts and raw run directories are still not included.
