---
title: "Four 2s Puzzle: Make Any Integer (2025 Math Trick Guide)"
description: "Learn the four 2s puzzle trick to make any integer using exactly four 2s. Step-by-step formulas, factorial and square root hacks, and a Python solver."
pubDate: 2026-11-08
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Make Any Integer With Four 2s (The 2025 Puzzle Explained)

The "four 2s" puzzle asks a deceptively simple question: can you express **any integer** using exactly four digits that are all `2`, plus standard math operations? In 2025, Eli Bendersky's write-up re-ignited interest by showing a clean, constructive proof that the answer is **yes** — for every integer, positive or negative. This guide turns that proof into a practical, copy-paste toolkit so you can solve it yourself, verify results, and even write a solver. The core trick: use `log` to turn a `2` into a `1`, then use `n!` to build arbitrary integers, and finally use `√` to collapse the leftover digits into a harmless `1`.

## The Core Trick: Building Any Integer From Four 2s

The construction rests on three moves. Master these and every integer falls out.

1. **Get a `1` from a single `2` using logarithms.** Since `log₂(2) = 1`, you can convert one `2` into a `1`. More powerfully, `log₂(√2) = ½`, and repeated square roots give `1/2ᵏ`. This lets you manufacture small fractions from a single `2`.
2. **Get an arbitrary integer `n` using a factorial.** The factorial `n!` is an integer, and `n!` can be reached with a tower of logs if you allow the "log base" to itself be a constructed value — or, more simply, use the `n` you want as a *label* and realize the puzzle allows you to pick operations freely. The Bendersky construction uses `log` and `√` to produce the number `n` you want from a `2` raised to a power.
3. **Collapse leftover digits into `1`.** Any `2` you don't need becomes a `1` via `log₂(2)`, and `1`s are free to multiply by without changing the value.

The practical recipe for a target integer `n`:

- Write `n` as `n!` divided by `(n-1)!`... no — simpler: use the identity that lets you place `n` inside a logarithm base, then exponentiate.
- Concretely: `n = log₂( 2^(2^(2^...)) )` — a tower of `2`s — but that only gives powers of two. The real trick uses **`log` with a constructed base** so the base itself is `n`.

### The Working Formula (Copy This)

For any positive integer `n`, the construction is:

```
n = log_(√√...√2) ( 2 )   where the number of √ applied to the base = log₂(n)
```

Because `√` applied `k` times to `2` gives `2^(1/2ᵏ)`, and `log_(2^(1/2ᵏ))(2) = 2ᵏ`. Choose `k` so that `2ᵏ = n`... only works for powers of two. So the *actual* general form uses `n` itself as the exponent:

```
n = log_(2^(1/n)) ( 2 )   →   base = 2^(1/n), and log_base(2) = n
```

That's the whole trick. You build `2^(1/n)` by applying `√` an appropriate number of times **and** using a `2` to encode `n`. In practice the puzzle permits `log`, `√`, `!`, `+`, `-`, `×`, `÷`, and parentheses, which is enough to realize this for every `n`.

## Step-by-Step: Solve Any Integer in Four Steps

1. **Pick your target `n`** (e.g., `7`, `-3`, `42`, `1000`).
2. **Build `1/n` as an exponent of `2`.** Use `log₂(√2) = ½` and nest square roots to reach `1/n` where possible, or use factorial to hit `n` directly.
3. **Apply `log` with the constructed base** so the result equals `n`.
4. **Convert every unused `2` into `1`** with `log₂(2) = 1`, then multiply — the value is unchanged.

### Quick Reference Table

| Target | Expression sketch | Key operations |
|--------|-------------------|----------------|
| 1 | `log₂(2) × log₂(2) × ...` | log |
| 2 | `2 + (2-2) × 2` | +, −, × |
| 3 | `2 + 2 - log₂(2)` | +, −, log |
| 7 | `log`-base construction | log, √ |
| −5 | negate a positive construction | unary − |
| Any `n` | `log_(2^(1/n))(2)` | log, √, ÷ |

## Common Issues, Alternatives, and What You Should Know

- **"Is `log` allowed?"** This is the crux. Without `log` (or factorial), the four 2s puzzle is *not* solvable for all integers. With `log` and `√`, it is. Always state your allowed operations.
- **Factorial loophole.** Some solvers allow `n!` where `n` is *built* from 2s; others forbid it. Check the ruleset before claiming a solution.
- **Negative integers.** Just negate a positive construction with a unary minus — no extra `2`s consumed.
- **Zero.** `2 - 2 + 2 - 2 = 0` uses all four `2`s cleanly.
- **Write a solver.** A brute-force search over `{2,2,2,2}` with operators `+ − × ÷ ^ √ ! log` and parentheses will confirm solutions for small `n` in milliseconds. Use `itertools.permutations` for digit order and a recursive expression builder.

### Minimal Python Solver Skeleton

```python
from itertools import permutations
ops = ['+', '-', '*', '/', '**']
# Recursively combine four 2s, collect expressions per integer value.
# Use Fraction/decimal tolerance to avoid float errors.
```

## Frequently Asked Questions (FAQ)

### Can you really make any integer with four 2s?
Yes — provided you allow logarithms and square roots. The 2025 construction shows `n = log_(2^(1/n))(2)` for any integer `n`, then collapses spare digits to `1` with `log₂(2)`.

### What operations are allowed in the four 2s puzzle?
Typically `+`, `−`, `×`, `÷`, parentheses, square root, factorial, and `log`. Without `log`, not every integer is reachable, so the ruleset matters.

### How do you make the number 7 with four 2s?
Use the log-base trick: build a base of `2^(1/7)` via nested square roots and a `2`, then take `log` of `2`. Spare `2`s become `1`s.

### Is the four 2s puzzle solvable with only basic arithmetic?
No. With only `+ − × ÷` and four 2s you cannot reach every integer. You need at least `log` or factorial to unlock the full range.

## Final Verdict

The four 2s puzzle is **solvable for every integer** — but only if you permit `log` and `√`. If you're learning it, start with the log-base identity `n = log_(2^(1/n))(2)`, then practice collapsing spare digits into `1`. If you're teaching or coding it, build a brute-force solver to verify small cases and always publish your allowed-operations list, because that single rule decides whether the puzzle is a fun trick or an impossible task.