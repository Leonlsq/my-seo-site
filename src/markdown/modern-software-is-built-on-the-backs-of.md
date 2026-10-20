---
title: "How to Audit Your Open-Source Dependencies for Bus Factor Risk"
description: "A step-by-step guide to finding single-maintainer open-source packages in your stack and reducing supply chain risk before the next xz-style backdoor."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Your `package-lock.json` Is a Security Liability (And How to Fix It)

The xz-utils backdoor, the polyfill.io hijack, and the left-pad fiasco all share one root cause: a critical piece of infrastructure maintained by one or two unpaid volunteers. If you run `npm audit` and call it a day, you're auditing *known CVEs* — not the structural risk that a single burned-out maintainer gets phished, sells the project, or simply walks away. This guide gives you a repeatable audit workflow to find your highest-risk dependencies, score them, and mitigate them. Budget 2–3 hours for a mid-sized Node or Python repo.

## Step-by-Step: The Bus Factor Audit Workflow

### Step 1 — Generate a full dependency inventory
Don't trust `package.json` alone; transitive dependencies are where the risk hides.

- **Node.js:** `npm ls --all --json > deps.json` (or `pnpm list --depth Infinity`)
- **Python:** `pipdeptree --json-tree > deps.json`
- **Go:** `go mod graph > deps.txt`
- **Rust:** `cargo tree > deps.txt`

Expect 400–1,500 packages for a typical web app. You will not review them all manually — that's what the next steps are for.

### Step 2 — Pull maintainer and funding signals
For each direct dependency, check these five signals. This is the core scoring rubric:

| Signal | Where to Check | Red Flag |
|---|---|---|
| Maintainer count | GitHub Insights → Contributors (last 12 months) | 1 active committer |
| Funding | GitHub Sponsors, Open Collective, Tidelift | No funding link at all |
| Commit cadence | Repo commit history | No commits in 18+ months *and* open security issues |
| Ownership changes | `npm view <pkg> maintainers` / repo transfer history | Recent maintainer/org handoff |
| Install scripts | `npm view <pkg> scripts` / `setup.py` | `postinstall` running arbitrary code |

### Step 3 — Score and triage
Assign each package a simple 0–5 risk score: +2 for single maintainer, +1 for no funding, +1 for install scripts, +1 for stale security issues. Anything scoring **3 or higher** goes on your watchlist. In practice, 5–15% of a typical dependency tree lands here.

### Step 4 — Automate the monitoring
Manual audits rot within weeks. Add continuous checks:

1. **Renovate or Dependabot** with `minimumReleaseAge: "3 days"` to dodge fast-moving supply chain attacks (the xz backdoor sat in a release branch for weeks before exploitation).
2. **Socket.dev** or **Phylum** in CI to flag install scripts and obfuscated code.
3. **`npm audit signatures`** (npm 9+) to verify provenance attestations where publishers support them.
4. A quarterly cron job that re-runs Steps 1–3 and diffs the watchlist.

### Step 5 — Mitigate, don't panic
You rarely need to rip out a dependency. Rank mitigations by cost:

- **Vendor it:** copy the source into your repo for tiny packages (<500 LOC) and pin it.
- **Lockfile discipline:** commit lockfiles, use `npm ci`, and enable `--ignore-scripts` in CI where your build allows.
- **Network egress rules:** block outbound connections from CI runners except to your registry mirror — this alone neutralizes most install-script exfiltration.
- **Fund what you keep:** a $50/month Open Collective contribution to your top 3 riskiest dependencies is cheaper than a single incident response hour.

## Common Issues, Alternatives, and What You Should Know

**"My dependency count is too high to audit."** That's the finding. Use `depcheck` and `npm-prune` to remove unused packages first — teams routinely cut 20–30% of dependencies before auditing.

**"Provenance attestations aren't universal."** Correct — as of 2026, adoption is strong on npm but spotty on PyPI and crates.io. Treat missing attestations as a yellow flag, not a block.

**Commercial alternatives:** Tidelift (paid maintainer SLAs), Snyk, and Endor Labs all sell dependency risk scoring. They're worth it at 50+ engineers; below that, the free workflow above covers 90% of the value.

**The uncomfortable truth:** audits reduce *your* exposure, but the ecosystem fix is funding. If your company's revenue depends on a package, check whether it has a funding link and use it.

## Frequently Asked Questions (FAQ)

### What is a bus factor in open-source software?
The bus factor is the number of maintainers who could disappear before a project stalls. A bus factor of 1 means one person's absence — or compromise — halts security patches. Core-js, which powers a huge share of the npm ecosystem, was effectively a one-person project for years.

### How do I find which npm packages have only one maintainer?
Run `npm view <package> maintainers` for direct dependencies, or script it across your lockfile with `jq`. Cross-check against GitHub's contributor graph filtered to the last 12 months — a package can list five maintainers on npm while only one has committed since 2023.

### Was the xz-utils backdoor caused by a low bus factor?
Yes. The attacker spent two years social-engineering the sole active maintainer, eventually gaining commit access and shipping a backdoor in liblzma 5.6.0–5.6.1. It was caught by accident when a Microsoft engineer noticed SSH latency. The lesson: maintainer *identity* changes are a top-tier risk signal.

### Does `npm audit` detect supply chain backdoors?
No. `npm audit` checks against CVE databases, so it only flags issues after disclosure. Backdoors like xz or the event-stream incident were malicious by design and invisible to CVE scanning until discovered. You need behavioral analysis (Socket, Phylum) and provenance checks for that class of threat.

## Final Verdict

Run the five-step audit this week on your highest-traffic repo, then automate Steps 3–4 in CI before the quarter ends. The realistic goal isn't a risk-free dependency tree — it's knowing *which* single-maintainer packages you depend on, so a compromise is a contained incident rather than a surprise. And if you find yourself relying on a volunteer's unpaid labor for production revenue, fund it. That's the actual fix; everything else is mitigation.