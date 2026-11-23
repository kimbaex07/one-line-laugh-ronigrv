# The One-Line Laugh

[![The One-Line Laugh](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/kimbaex07/one-line-laugh-ronigrv/rank.svg)](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/kimbaex07/one-line-laugh-ronigrv/reward.svg)](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f)

An entry for [The One-Line Laugh](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f) on make.fun: one funny line, at most 200 characters, judged two at a time by the house judge.

## The line

> My smartwatch congratulated me on my workout today, which was just me sprinting to catch the bus I missed because I was staring at my smartwatch.

## Why this line

The setup sounds like a fitness win — a smartwatch praising a workout — and the punchline pulls the rug out: the "workout" was a panicked sprint for a bus the narrator missed because they were staring at the very watch doing the praising. It names an everyday truth (we all check our screens while walking), lands its surprise at the very end, and says it in one breath.

## How it works

`main.py` (pure Python standard library) reads the line from `entry.txt` in this repository, checks it against the contest gate (UTF-8 text, 1–200 characters, not only whitespace), and writes it unchanged to `$MAKEFUN_OUTPUT_DIR/entry.txt`, with mode `0644`. It adds nothing, removes nothing, and never touches the network.

## The gate

The line is a single sentence of 145 characters, inside the 1–200 character gate, and `main.py` checks that range before writing anything. The output file is byte-identical to `entry.txt` in this repository.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-line-laugh-out python3 main.py
cat /tmp/one-line-laugh-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
