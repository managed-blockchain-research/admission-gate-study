# 11xx findings: matched operating points of the per-sender and history-weighted policies (Besu G1 512 MB; three seeds per arm; written 2026-11-26)


## Y1: S1: two attack accounts, six legitimate heavy accounts

| arm | runs | attack blocked | legitimate heavy (look-alike) rejected | ordinary rejected | receipts share |
|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.000 | 0.687 |
| SizeStatic | 3 | 1.000 | 1.000 | 0.000 | 0.974 |
| SenderLow10 | 3 | 0.965 | 0.791 | 0.000 | 0.967 |
| SenderR25 | 3 | 0.920 | 0.522 | 0.000 | 0.955 |
| SenderR50 | 3 | 0.845 | 0.075 | 0.000 | 0.932 |
| SenderBucket | 3 | 0.693 | 0.000 | 0.000 | 0.888 |
| SenderR200 | 3 | 0.388 | 0.000 | 0.000 | 0.807 |
| SenderHigh400 | 3 | 0.000 | 0.000 | 0.000 | 0.685 |
| HistBucket | 3 | 0.965 | 0.000 | 0.000 | 0.936 |
| HistH50 | 3 | 0.965 | 0.000 | 0.000 | 0.933 |
| HistH200 | 3 | 0.965 | 0.000 | 0.000 | 0.934 |
| HistLow25 | 3 | 0.920 | 0.000 | 0.000 | 0.926 |
| HistHigh200 | 3 | 0.965 | 0.000 | 0.000 | 0.937 |

## Y2: S2: twelve fresh attack accounts

| arm | runs | attack blocked | legitimate heavy (look-alike) rejected | ordinary rejected | receipts share |
|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| SizeStatic | 3 | 1.000 | 1.000 | 0.000 | 0.973 |
| SenderLow10 | 3 | 0.791 | 0.791 | 0.000 | 0.979 |
| SenderR25 | 3 | 0.522 | 0.522 | 0.000 | 0.986 |
| SenderR50 | 3 | 0.075 | 0.075 | 0.000 | 0.998 |
| SenderBucket | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| SenderR200 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| SenderHigh400 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| HistBucket | 3 | 0.791 | 0.000 | 0.000 | 1.000 |
| HistH50 | 3 | 0.791 | 0.000 | 0.000 | 1.000 |
| HistH200 | 3 | 0.791 | 0.000 | 0.000 | 1.000 |
| HistLow25 | 3 | 0.522 | 0.000 | 0.000 | 1.000 |
| HistHigh200 | 3 | 0.791 | 0.000 | 0.000 | 1.000 |

## Y3: S3: twelve attack accounts with 10 prior requests each

| arm | runs | attack blocked | legitimate heavy (look-alike) rejected | ordinary rejected | receipts share |
|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| SizeStatic | 3 | 1.000 | 1.000 | 0.000 | 0.974 |
| SenderLow10 | 3 | 0.791 | 0.791 | 0.000 | 0.980 |
| SenderR25 | 3 | 0.522 | 0.522 | 0.000 | 0.986 |
| SenderR50 | 3 | 0.075 | 0.075 | 0.000 | 0.998 |
| SenderBucket | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| SenderR200 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| SenderHigh400 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| HistBucket | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| HistH50 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| HistH200 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| HistLow25 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| HistHigh200 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |

## Y6: S6: fresh legitimate heavy senders

| arm | runs | attack blocked | legitimate heavy (look-alike) rejected | ordinary rejected | receipts share |
|---|---|---|---|---|---|
| none | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| SizeStatic | 3 | 1.000 | 1.000 | 0.000 | 0.979 |
| SenderLow10 | 3 | 0.965 | 0.791 | 0.000 | 0.983 |
| SenderR25 | 3 | 0.920 | 0.522 | 0.000 | 0.989 |
| SenderR50 | 3 | 0.845 | 0.075 | 0.000 | 0.998 |
| SenderBucket | 3 | 0.693 | 0.000 | 0.000 | 1.000 |
| SenderR200 | 3 | 0.388 | 0.000 | 0.000 | 1.000 |
| SenderHigh400 | 3 | 0.000 | 0.000 | 0.000 | 1.000 |
| HistBucket | 3 | 0.965 | 0.791 | 0.000 | 0.983 |
| HistH50 | 3 | 0.965 | 0.791 | 0.000 | 0.983 |
| HistH200 | 3 | 0.965 | 0.791 | 0.000 | 0.983 |
| HistLow25 | 3 | 0.920 | 0.522 | 0.000 | 0.989 |
| HistHigh200 | 3 | 0.965 | 0.791 | 0.000 | 0.983 |

## Reading rules
Descriptive; arms of a family give several operating points (attack blocked against legitimate heavy requests rejected); no interpolation; the accounts and rates are those of the registered scenarios. One run of this experiment (Y1 HistH200 seed 67301) shared its node with a run of the deferral sweep and is flagged co-located.

