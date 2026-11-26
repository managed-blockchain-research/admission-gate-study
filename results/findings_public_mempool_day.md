# Public mempool, one day (Flashbots Mempool Dumpster, 2026-11-20.csv; written 2026-11-24)

Read-only download of the public metadata file; nothing was sent to any network.

## Arrivals
- transactions: 1019788 over 86400 s (11.80 tx/s mean)
- per-second count: mean 11.80, p50 10, p95 23, p99 35, max 784; index of dispersion (variance/mean) 6.21 (Poisson = 1)
- inter-arrival time (ms): p50 49, p95 289, p99 494, p99.9 818

## Senders
- distinct senders: 335966; transactions per sender: median 1, p90 2, p99 16, max 13708
- the busiest 10 senders send 7.9% of all transactions; the busiest 1% of senders send 55.0%

## Calldata size (bytes), pending transactions
- median 68, p90 388, p99 4740, p99.9 28804, max 128260
- share above 1000 B: 0.05079 (51797)
- share above 10000 B: 0.00349 (3554)
- share above 32000 B: 0.00092 (943)
- share above 65604 B: 0.00036 (363)
- share above 100000 B: 0.00011 (112)
- zero-calldata share: 0.418

## Inclusion delay (first seen to block timestamp), transactions that were later included
- n 907349 (89.0% of the file); delay (s): p50 6.6, p95 30.1, p99 1918.1, p99.9 31164.5

## Heavy transactions (> 65,604 B)
- count 363 (0.0356% of transactions); per-hour counts: median 12, max 96; distinct senders 21

## Reading rules
Descriptive, one day, public pending transactions seen by the dataset sources (a transaction seen by several sources is listed once at its first-seen time). It describes arrival timing, senders and sizes of ordinary public traffic; it does not describe attack traffic or private order flow.

