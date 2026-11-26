# Admission-gate study: data, scripts and apparatus

Companion material for the manuscript "Admission Control for Calldata-Heavy Transactions in Managed Ethereum Clients: What Can a Gate Separate, and at What Cost?".

The campaign (1,591 registered runs plus one excluded batch of 60) is organised in experiment families. Each file name carries a descriptive family name. The pre-registration document and the bodies of the analysis scripts use the original two-letter family ids (for example 11jj); this table maps them.

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
| 11ss | operating_point_sweeps_other_cells | Operating-point sweeps on the mixed, ZGC and Nethermind cells; low-rate attack over twelve accounts (synchronized arrivals) | VI-B |
| 11tt | comparison_policies_gate_outage | CPU-ramp (DAGOR-style) and circuit-breaker comparison policies, a supervised gradient-boosting detector in the live gate, fail-open versus fail-closed gate during a 20 s gate freeze | VI-B, VI-C |
| 11uu | confirmation_latency_first_batch | Confirmation latency, attack-only / mixed / replayed-size cells (first batch; effective receipt limit 90 s because the deployment script overwrote the client setting) | VI-D |
| 11ww | confirmation_latency | Repeat of the latency experiment with the receipt limit set after the deployment (240 s, audited); used in the paper | VI-D |
| 11vv | attacker_variants | Staggered arrivals over twelve accounts, attack sizes below and above the threshold, rising and stepped rates | VI-D |
| 11xx | sender_history_matched_sweeps | Per-sender buckets 10-400 kB/s and five history-weighted settings in four sender scenarios | VI-D |
| 11yy | deferral_limit_sweep | Deferral limit sweep (30-300 s, shaper 250 kB/s) on attack-only, look-alike-only and mixed streams | VI-D |
| 11zz | public_day_arrival_replay | Replay of per-second arrival counts of two 240 s windows of one public day with replayed calldata sizes | VI-D |
| 11aaa | pressure_step_response | Step of the rejection probability (0.2/0.4/0.6) and a control arm; static loop gain | VI-D |
| 11aab | two_node_loopback | Two Besu nodes on one host as loopback peers, gate in front of node A only; attack to the gated or the ungated node | VI-D |

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

## Added in v1.2
Families 11ss and 11tt: per-run tables, summaries, analysis scripts, self-check and pin files, the workload module with the fail-closed option (`apparatus/tt/`), the supervised-detector service files and the trained artifact (`apparatus/sup_service/`, deterministic training script), the pressure-loop description (`results/findings_pressure_loop_dynamics.md`) and the registration sections 11ss and 11tt with their amendments. Launch scripts and raw run directories are still not included.

## Added in v1.3
Families 11uu, 11ww, 11vv, 11xx, 11yy, 11zz, 11aaa and 11aab (table above): per-run tables (latency, attacker variants, sender and history sweeps, deferral limit sweep, arrival replay, two-node cell), results reports, analysis scripts (including the per-run table scripts and the static loop-gain script), self-check and pin files, the workload modules with the staggered/size/rate options (`apparatus/attacker_variants_module/`), the arrival-replay mode and the public-day windows (`apparatus/arrival_replay_module/`), the two-node mode (`apparatus/two_node_module/`), the step-input policy service (`apparatus/step_service/`), the public-mempool one-day summary (`results/findings_public_mempool_day.md`; metadata of a public archive only, nothing was sent to a network) and the registration sections 11uu to 11aab with their amendments. The two-node cell contains 30 runs; one further run that was refused at start because the nodes had not connected was repeated with the same seed (the refused directory is kept internally). Launch scripts and raw run directories are still not included.
