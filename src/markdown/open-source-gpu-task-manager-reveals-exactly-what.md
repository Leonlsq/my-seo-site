---
title: "gputaskman: How to Find What's Eating Your VRAM (Setup Guide)"
description: "Learn how to install and use gputaskman, the open-source GPU task manager from Scott Hanselman, to pinpoint exactly which processes are eating your VRAM."
pubDate: 2026-11-08
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What Is gputaskman and Why Your VRAM Is Always Full

If you've ever opened Task Manager, seen your GPU memory pinned at 95%, and had absolutely no idea *why*, you're the exact person **gputaskman** was built for. Released as an open-source GitHub project by Microsoft VP **Scott Hanselman**, gputaskman is a lightweight command-line and TUI (terminal UI) tool that breaks down GPU memory usage **per process** — something Windows Task Manager and even NVIDIA's own tools do a frustratingly poor job of showing you.

The core problem it solves: modern apps leak VRAM. Browser tabs with hardware acceleration, Electron apps like Discord and Slack, game launchers, and background AI tools all quietly reserve GPU memory. When you launch a game or a local LLM and get an "out of memory" crash, the culprit is often *not* the app you just opened. gputaskman surfaces the hidden hogs so you can kill them before they ruin your session.

This guide gets you from zero to a working install and shows you exactly how to read the output. **Direct takeaway:** it's a free, 5-minute setup that will save you hours of guesswork — especially on 8GB and 12GB cards where every megabyte counts.

## Step-by-Step: Install and Run gputaskman

gputaskman is distributed via GitHub, so you'll need **Git** and a package manager. The setup is quick if you follow the order below.

### Prerequisites
- **Windows 10/11**, **Linux**, or **macOS** (Windows has the most mature support)
- **Python 3.10+** or the prebuilt binary (check the repo's Releases tab)
- **NVIDIA drivers** (CUDA) or **AMD ROCm** for full per-process detail
- **Git** installed and on your PATH

### Installation Steps
1. **Clone the repository:**
   ```
   git clone https://github.com/shanselman/gputaskman.git
   cd gputaskman
   ```
2. **Create a virtual environment** (recommended to avoid dependency conflicts):
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/macOS
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Run the tool:**
   ```
   python gputaskman.py
   ```
   Or, if you grabbed a prebuilt binary, just run `./gputaskman` (Linux/macOS) or `gputaskman.exe` (Windows).

### Reading the Output
The TUI refreshes live and shows a table like this:

| PID | Process | VRAM (MB) | GPU % | Type |
|-----|---------|-----------|-------|------|
| 8842 | chrome.exe | 1,204 | 3% | Graphics |
| 1120 | Discord.exe | 512 | 1% | Graphics |
| 4471 | python.exe (llama) | 6,890 | 88% | Compute |
| 3310 | steamwebhelper.exe | 340 | 0% | Graphics |

**Key columns to watch:**
- **VRAM (MB):** the actual memory footprint — sort by this to find the biggest offender.
- **Type:** distinguishes *Graphics* (rendering) from *Compute* (CUDA/AI workloads). A leaked compute process is the #1 cause of "game won't launch" errors.
- **GPU %:** a process sitting at 0% but holding 2GB of VRAM is a textbook leak.

## Common Issues, Workarounds, and What You Should Know

gputaskman is young open-source software, so expect rough edges. Here's what trips people up:

- **"No GPU found" error:** Your driver's management API isn't exposed. Update to the latest NVIDIA Game Ready or AMD Adrenalin driver — older drivers don't report per-process memory.
- **Windows shows generic "GPU" usage only:** Windows natively aggregates VRAM across the whole GPU. gputaskman queries vendor APIs directly, so it works *around* this limitation. If it still fails, run the terminal **as Administrator**.
- **Linux permissions:** you may need to add your user to the `video` and `render` groups (`sudo usermod -aG video,render $USER`) and reboot.
- **WSL2 users:** GPU passthrough via WSLg can hide processes. Run gputaskman natively on the host, not inside WSL.

### Alternatives Worth Comparing

| Tool | Per-Process VRAM | Open Source | Best For |
|------|------------------|-------------|----------|
| **gputaskman** | ✅ Yes | ✅ Yes | Quick CLI diagnosis |
| NVIDIA-SMI | ✅ Yes (NVIDIA only) | ✅ Yes | Scripting, servers |
| Windows Task Manager | ❌ Aggregated | ❌ No | Basic overview |
| GPU-Z | ⚠️ Partial | ❌ No | Hardware sensors |

**When to use what:** For a fast "what's hogging my VRAM right now" check on a gaming PC, gputaskman is the friendliest. For automation and logging on a headless AI server, stick with `nvidia-smi`. GPU-Z remains better for temperature and clock monitoring.

## Frequently Asked Questions (FAQ)

### Is gputaskman free and safe to use?
Yes. It's fully open-source on GitHub (MIT-style license), free to use, and you can audit the entire codebase yourself. Because it only *reads* GPU telemetry, it can't modify or damage your system.

### Does gputaskman work with AMD and Intel GPUs?
AMD support works through ROCm on Linux and Adrenalin APIs on Windows, but it's less mature than NVIDIA. Intel Arc support is limited — expect aggregated data rather than per-process breakdowns on Arc cards for now.

### How do I fix a VRAM leak found by gputaskman?
Identify the PID holding memory at 0% GPU usage, then either close that app normally or force-kill it via Task Manager (`taskkill /PID <id> /F`). Common repeat offenders are browser hardware acceleration, Discord, and Steam's web helper — disabling hardware acceleration in those apps permanently reclaims 500MB–1.5GB.

## Final Verdict

**Install it.** If you game, run local AI models, or do any GPU-heavy work on a card with 8GB or 12GB of VRAM, gputaskman is a genuinely useful diagnostic tool that fills a real gap Windows leaves wide open. It won't replace `nvidia-smi` for server automation or GPU-Z for hardware monitoring, but as a quick "who's eating my VRAM" flashlight, it's excellent — and it's free. Clone the repo, run it once, and keep it in your toolkit for the next mysterious out-of-memory crash.