# Real benign transaction sizes (public Ethereum mainnet blocks, read-only; collected 2026-11-20)
Sample: 240 blocks drawn uniformly at random (seed 20261120) from the ~90 days before head 26455209, 60144 transactions, mean 250.6 tx/block. Source: public JSON-RPC eth_getBlockByNumber (full transactions); only the calldata length, gas limit and gas price were kept. No attack traffic was sent.

## Calldata length (bytes)
- p50: 68
- p90: 1092
- p99: 7044
- p99.9: 58116
- p100: 128004
- share of transactions above 1000 B: 0.10866 (6535 of 60144)
- share of transactions above 10000 B: 0.00627 (377 of 60144)
- share of transactions above 32000 B: 0.00178 (107 of 60144)
- share of transactions above 65604 B: 0.00062 (37 of 60144)
- share of transactions above 100000 B: 0.00030 (18 of 60144)
- zero-calldata share: 0.325

## Reading rules
Allowed: the sample describes sizes of ordinary mainnet transactions in this window. Not allowed: statements about attack traffic, about other windows, or about rollup batches submitted through blobs (blob data is not in calldata).
