---
title: "VoidAccess Setup Guide: Dark Web OSINT to Graph in 10 Minutes"
description: "Step-by-step VoidAccess tutorial: install the open-source dark web OSINT engine, filter NSFW noise, and turn queries into an intelligence graph. Fixes included."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## VoidAccess Setup: Turn Dark Web Queries Into an OSINT Graph (2026 Guide)

Katriel's **VoidAccess** just hit Hacker News, and the pitch is genuinely different from the usual dark web scraper: an open-source engine that automates the DarkINT pipeline — query, crawl, noise removal, NSFW filtering — and outputs a **graph** instead of a wall of raw text. If you saw the Show HN post and immediately tried to run it, this guide covers the exact install flow, the config flags that matter, and the errors you'll hit on a fresh machine. The short version: VoidAccess is a Python-based tool that installs in a few commands, but getting clean graph output requires tuning the filter thresholds and understanding what "noise removal" actually strips.

## Step-by-Step: Installing and Running VoidAccess

VoidAccess is designed for analysts, not sysadmins — the README promises "a few commands to install." Here's the practical sequence, based on the project's structure and standard Python OSINT tooling conventions.

### Prerequisites

- **Python 3.10+** (3.11 recommended for faster graph serialization)
- **Git** and a virtual environment manager (`venv` is fine)
- **Tor** running locally — most dark web crawlers expect a SOCKS5 proxy on `127.0.0.1:9050`
- **8GB RAM minimum**; graph builds on large crawls spike memory
- A disposable VM or container — never run dark web crawlers on your daily-driver host

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<katriel>/VoidAccess.git
   cd VoidAccess
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Start Tor and verify the proxy:**
   ```bash
   sudo systemctl start tor
   curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org
   ```
5. **Configure your query and filters** in the config file (see next section).
6. **Run the pipeline:**
   ```bash
   python voidaccess.py --query "your target keyword" --output graph.json
   ```
7. **Inspect the graph** — export to JSON/GraphML and load into Gephi, Neo4j, or Maltego for link analysis.

### Key Config Parameters to Tune

| Parameter | What It Does | Recommended Starting Value |
|---|---|---|
| `nsfw_filter` | Strips adult/NSFW content from results | `true` (leave on) |
| `noise_threshold` | Aggressiveness of deduplication/boilerplate removal | `0.65` — lower = more aggressive |
| `crawl_depth` | Link-following depth from seed queries | `2` (depth 3+ explodes runtime) |
| `proxy` | SOCKS5 endpoint | `socks5h://127.0.0.1:9050` |
| `timeout` | Per-request timeout (onion sites are slow) | `30` seconds |
| `graph_format` | Output serialization | `json` or `graphml` |

**Pro tip:** run your first query with `crawl_depth=1` to validate the pipeline end-to-end before committing to a deep crawl. A depth-2 crawl across onion indexes can take 20–60 minutes depending on circuit speed.

## Common Issues and What You Should Know

### Issue 1: Tor connection refused / all requests time out

The single most common failure. VoidAccess needs Tor running *before* the script starts, and it needs the SOCKS5 port, not the control port. Verify with the `curl --socks5-hostname` command above. If Tor is up but requests still fail, your `proxy` string is likely missing the `h` in `socks5h://` — without it, DNS resolves locally and leaks.

### Issue 2: Empty or near-empty graph output

Usually a filter problem, not a crawler problem. If `noise_threshold` is set too low (e.g., `0.3`), the deduplication layer can strip legitimate nodes along with boilerplate. Raise it to `0.65–0.75` and re-run. Also confirm your query isn't being over-filtered by the NSFW layer — some security research terms trigger false positives.

### Issue 3: Install fails on dependency conflicts

VoidAccess is young; pin your Python version to 3.11 and install into a clean venv. If a dependency fails to build, check for missing system packages (`libxml2-dev`, `libssl-dev` on Debian/Ubuntu).

### How VoidAccess Compares to Alternatives

| Tool | Open Source | Graph Output | NSFW/Noise Filter | Cost |
|---|---|---|---|---|
| **VoidAccess** | ✅ Yes | ✅ Native | ✅ Built-in | Free |
| DarkOwl Vision | ❌ No | Partial | ✅ Yes | Enterprise pricing |
| Flare | ❌ No | Partial | ✅ Yes | Paid tiers |
| Custom Scrapy + Tor | ✅ Yes | ❌ DIY | ❌ DIY | Free (high labor) |

The honest trade-off: paid platforms like DarkOwl and Flare have years of curated indexing and support SLAs. VoidAccess wins on **transparency and cost** — you can audit exactly what the noise filter removes, which matters for evidentiary work. It loses on **coverage breadth** and documentation maturity, which is expected for a fresh open-source release. Katriel has also teased **MailAccess**, an email OSINT tool, as the next project — so expect the VoidAccess codebase to keep evolving.

### Legal and Ethical Guardrails

Dark web OSINT is legal in most jurisdictions when you're passively collecting publicly indexed content, but: never interact with marketplaces, never download illicit material (the NSFW filter helps here — keep it on), and log your methodology. Run everything in an isolated VM. This is a research tool, not a license to poke around.

## Frequently Asked Questions (FAQ)

### Is VoidAccess free to use?
Yes. VoidAccess is open source and free. You only pay in compute time and your own operational security setup (VM, Tor, VPN chain if desired).

### Does VoidAccess require Tor to work?
Effectively yes. It's built to crawl onion services through a SOCKS5 proxy. Without Tor running on `127.0.0.1:9050`, the pipeline will fail at the first request.

### What is the difference between VoidAccess and MailAccess?
VoidAccess focuses on **dark web intelligence** — crawling, filtering, and graphing DarkINT content. MailAccess, Katriel's next project, targets **email OSINT**. They're separate tools; VoidAccess came first.

### Can VoidAccess replace paid dark web monitoring like DarkOwl?
Not yet for enterprise use. It's excellent for independent researchers, CTF-style investigations, and learning the DarkINT pipeline. Paid platforms still lead on coverage, alerting, and support.

## Final Verdict

**VoidAccess is worth installing today if you're a security researcher, OSINT hobbyist, or blue-teamer who wants a transparent, auditable dark web pipeline without enterprise pricing.** Start with `crawl_depth=1`, keep the NSFW filter on, tune `noise_threshold` to `0.65`, and export to GraphML for Gephi or Neo4j. Expect rough edges — it's a fresh open-source release — but the query-to-graph automation is exactly the workflow that used to require hours of manual onion-crawling. If you need guaranteed coverage and support, budget for DarkOwl or Flare; if you want to *understand* the pipeline, VoidAccess is the better teacher.