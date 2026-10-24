---
title: "Rust Style Guide Explained: 7 Rules to Write Cleaner Code"
description: "Master the official Rust Style Guide from Google. Learn formatting rules, naming conventions, and rustfmt config to write idiomatic, review-ready Rust code."
pubDate: 2026-10-22
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Rust Style Guide Explained: Why Google's Rules Matter for Your Codebase

Google's public Rust Style Guide just hit Hacker News with 255 points and 138 comments, and the debate is revealing something important: most Rust developers have never actually read a formal style guide. They rely on `rustfmt`, `clippy`, and "whatever the compiler accepts." That works for solo projects, but the moment you join a team, contribute to open source, or review a 2,000-line pull request, formatting ambiguity becomes friction. Google's guide resolves that friction with explicit, opinionated rules. This article breaks down the seven highest-impact rules from the guide, shows you how to enforce them automatically, and explains where Google's conventions diverge from the Rust community default—so you can decide what to adopt today.

## The 7 Rules That Actually Change Your Code

The guide is long, but these rules deliver the most value per minute of reading. Each one is enforceable with tooling, which is the whole point.

### 1. Formatting Is Non-Negotiable: Use `rustfmt`

Google mandates `rustfmt` with a specific configuration. The critical deviations from defaults:

- **Max line width: 100 characters** (default is 100, but the guide pins it explicitly)
- **`use_small_heuristics = "Max"`** — allows longer single-line structs and function calls
- **`imports_granularity = "Item"`** — one import per line, which produces cleaner diffs
- **`group_imports = "StdExternalCrate"`** — groups `std`, external crates, and local modules separately

Drop this into your `rustfmt.toml`:

```toml
max_width = 100
use_small_heuristics = "Max"
imports_granularity = "Item"
group_imports = "StdExternalCrate"
```

Then run `cargo fmt` and never argue about brace placement again.

### 2. Naming Conventions Follow RFC 430—With Zero Exceptions

The guide defers to the standard Rust naming conventions, but enforces them strictly:

| Item | Convention | Example |
|------|-----------|---------|
| Crates & modules | `snake_case` | `http_client` |
| Types & traits | `UpperCamelCase` | `RequestBuilder` |
| Functions & methods | `snake_case` | `parse_header` |
| Constants & statics | `SCREAMING_SNAKE_CASE` | `MAX_RETRIES` |
| Type parameters | Single uppercase letter | `T`, `K`, `V` |
| Lifetimes | Short lowercase | `'a`, `'src` |

The guide explicitly bans Hungarian notation and abbreviations that obscure meaning. `num_items` beats `n`, and `user_count` beats `usrCnt`.

### 3. Imports Must Be Sorted and Grouped

Google requires three distinct import groups separated by blank lines: standard library, external crates, then crate-local modules. Within each group, imports sort alphabetically. The `group_imports` setting above automates this, but if you're on an older toolchain, enforce it in code review.

### 4. Comments Explain *Why*, Not *What*

The guide is blunt: if a comment restates the code, delete it. Doc comments (`///`) are required for all public items and must include a one-line summary followed by a blank line and details. The first sentence should be a complete sentence ending in a period—this matters because `rustdoc` uses it as the tooltip summary.

### 5. Prefer Explicit Types at API Boundaries

Public function signatures must have explicit types for all parameters and return values. No `impl Trait` in return position unless the trait is sealed or the function is a builder. The reasoning: explicit types make documentation and error messages clearer for downstream users.

### 6. Error Handling: No `unwrap()` in Library Code

The guide prohibits `unwrap()` and `expect()` outside of tests and examples. Use `?` with proper error types, or `expect()` with a message that explains the invariant being violated. This single rule eliminates the most common source of production panics in Rust codebases.

### 7. Line Length and Function Size

Functions should stay under 100 lines; anything longer needs a justification comment or a refactor. The guide also caps nesting at four levels—deeper than that and you should extract a helper function.

## Enforcing the Guide Automatically

Reading rules is easy; enforcing them is where teams fail. Here's the minimal CI setup that catches 90% of violations:

1. **Add `rustfmt.toml`** to your repo root with the config above.
2. **Add a CI step:** `cargo fmt --all -- --check` fails the build on formatting drift.
3. **Run `cargo clippy -- -D warnings`** to catch naming and error-handling violations.
4. **Add `#![deny(missing_docs)]`** to your crate root to enforce doc comments on public items.
5. **Use `cargo deny`** to audit dependencies for license and security issues.

This five-step pipeline takes under 10 minutes to set up and runs on every pull request.

## Where Google's Guide Diverges From Community Defaults

The Hacker News thread surfaced real disagreement. The biggest points of contention:

- **Import granularity:** Google's one-import-per-line style produces longer files but cleaner git diffs. Many community projects prefer merged imports (`use std::{fmt, io};`).
- **100-character lines:** The Rust standard library uses 100, but many projects default to 80 for readability on smaller screens.
- **Strict `unwrap()` ban:** Some commenters argue `expect()` with a clear message is equally safe and more ergonomic in prototype code.

The takeaway: Google's guide is optimized for large, multi-team codebases where consistency beats personal preference. For a solo project, adopt the `rustfmt.toml` and naming rules, and treat the rest as suggestions.

## Frequently Asked Questions (FAQ)

### Is Google's Rust Style Guide official?
No. It's Google's internal style guide for Rust code, published publicly. The official Rust style guide is maintained by the Rust project, but Google's guide is more prescriptive and includes tooling configuration that the official guide leaves open.

### Does the Rust Style Guide conflict with `rustfmt` defaults?
Partially. The guide pins specific `rustfmt` options like `imports_granularity` and `group_imports` that differ from defaults. You must add a `rustfmt.toml` to match the guide—running bare `cargo fmt` will not produce compliant code.

### Should I use Google's guide for open-source projects?
Use it as a reference, not a mandate. Adopt the `rustfmt.toml`, naming conventions, and doc-comment rules—these are widely accepted. The stricter rules (no `unwrap()`, explicit types everywhere) are better suited to libraries with external consumers than to application code.

## Final Verdict

Google's Rust Style Guide is worth reading in full, but you don't need to adopt all of it. Start with the `rustfmt.toml` configuration and the naming conventions—those two changes alone will make your code review process faster and your diffs cleaner. Add the `unwrap()` ban if you're shipping a library. Skip the function-size caps if your team already has strong review culture. The guide's real value isn't its rules; it's the reminder that formatting decisions should be automated, documented, and consistent—not relitigated in every pull request.