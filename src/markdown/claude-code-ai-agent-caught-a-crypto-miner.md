---
title: "Claude Code Crypto Miner: How to Detect Hidden Miners on Mac"
description: "Learn how to detect a hidden crypto miner on your Mac after Claude Code flagged one. Step-by-step terminal checks, Activity Monitor tips, and fixes."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Detect a Hidden Crypto Miner on Your Mac (Claude Code Just Proved It Works)

A developer building a temperature-monitor app with Claude Code got an unexpected bonus feature: the AI agent flagged a hidden crypto miner silently running on their overheating Mac. The takeaway is simple — **your Mac can be mining crypto right now without you knowing**, and you don't need a paid antivirus to catch it. This guide shows you exactly how to replicate that detection process yourself in under 15 minutes using built-in macOS tools, plus how to remove what you find and stop it from coming back.

## Step-by-Step: Recreate the Claude Code Detection Method Manually

Claude Code caught the miner because it was already inspecting system processes and CPU telemetry while building the temperature monitor. You can do the same with Terminal. Run these checks in order.

### 1. Check CPU load with `top`

```bash
top -o cpu -n 10
```

Look for any process pinned at **80–100% CPU** that you don't recognize. Legitimate background processes (WindowServer, kernel_task) fluctuate. A miner holds steady at high load for hours. Press `q` to quit.

### 2. Cross-reference with Activity Monitor

Open **Activity Monitor → CPU tab → sort by % CPU descending**. Key red flags:

- A process named something generic like `com.apple.helper`, `mdworker_aux`, or a random string (`xmr-stak`, `xmrig`, `kdevtmpfsi` are classic miner names).
- High CPU usage that **resumes within seconds** of you force-quitting it.
- A process running under your user account that you never launched.

### 3. Inspect network connections for mining pools

```bash
sudo lsof -i -P -n | grep ESTABLISHED
```

Miners connect to mining pool ports, most commonly **3333, 4444, 5555, 7777, 14444, and 45700**. Any outbound connection to an unfamiliar IP on those ports is a strong signal.

### 4. Audit login items and LaunchAgents

```bash
ls -la ~/Library/LaunchAgents /Library/LaunchAgents /Library/LaunchDaemons
```

Compare against what you expect. Malicious miners persist via `.plist` files here so they restart after reboot. Check timestamps — a plist created on a day you didn't install anything is suspicious.

### 5. Scan for unsigned or ad-hoc-signed binaries

```bash
codesign -dv --verbose=4 /path/to/suspicious/binary
```

Legitimate Apple and developer software is signed and notarized. A miner binary usually returns `code object is not signed at all` or an unknown Team ID.

| Check | Tool | Red Flag |
|---|---|---|
| Sustained CPU load | `top` / Activity Monitor | 80–100% for hours, unknown name |
| Outbound connections | `lsof -i` | Ports 3333/4444/5555/7777 |
| Persistence | `ls LaunchAgents` | Unknown `.plist` with recent date |
| Binary signature | `codesign -dv` | Unsigned or unknown Team ID |
| Thermal stress | `sudo powermetrics --samplers smc` | Fans maxed, CPU throttling at idle |

### 6. Use Claude Code itself as a second pair of eyes

If you already use Claude Code, prompt it explicitly: *"List all processes using more than 30% CPU, check LaunchAgents for unsigned plists, and flag any outbound connections to non-standard ports."* The agent can parse `ps aux` and `lsof` output faster than you can eyeball it — which is exactly how the original miner was caught.

## Common Issues, Removal Steps, and What You Should Know

**Removing the miner safely:**

1. Note the process PID from Activity Monitor, then `kill -9 <PID>`.
2. Delete the associated `.plist` from `~/Library/LaunchAgents` (or `/Library/LaunchDaemons` — requires `sudo`).
3. Run `launchctl unload ~/Library/LaunchAgents/<file>.plist` before deleting.
4. Find the binary with `sudo find / -name "<processname>" 2>/dev/null` and remove it.
5. Reboot and re-run steps 1–3 to confirm it doesn't return.

**Where miners come from:** pirated software cracks, fake browser extensions, npm/PyPI packages with malicious postinstall scripts (a real and growing vector for developers), and "free" video converters. If you installed anything from a non-official source in the last month, start there.

**Don't rely on Activity Monitor alone.** Some miners use process-hiding techniques or masquerade as `kernel_task`. Cross-check with `ps aux | sort -nrk 3,3 | head -20` in Terminal, which bypasses some GUI-level obfuscation.

**Cost of a silent miner:** A MacBook Pro mining Monero at full tilt can add **$15–$40/month** in electricity while degrading your SSD and battery. Apple Silicon Macs throttle hard under sustained load, so the miner earns pennies — but you pay the thermal bill.

## Frequently Asked Questions (FAQ)

### Can Claude Code really detect malware on my Mac?
It's not an antivirus, but it can inspect running processes, launch agents, and network connections when prompted — which is how it flagged the crypto miner. Treat it as a diagnostic assistant, not a security suite.

### What are the most common signs of a crypto miner on macOS?
Sustained 80–100% CPU usage from an unknown process, fans running loud at idle, outbound connections to ports 3333/4444/5555, and unknown LaunchAgent plists. Overheating with no visible cause is the classic symptom.

### Is `xmrig` or `kdevtmpfsi` always malware?
Yes, in almost all cases. `xmrig` is legitimate open-source mining software but should never run without your knowledge; `kdevtmpfsi` is a known malicious miner variant. If you didn't install it, remove it.

### Does reinstalling macOS remove a crypto miner?
Usually, but not always — miners in user-level LaunchAgents can survive if you migrate your home folder. Do a clean install without migrating data, or manually audit LaunchAgents after reinstalling.

## Final Verdict

Run the five terminal checks above **today** — they take 10 minutes and cost nothing. If you find a miner, kill the process, delete its LaunchAgent, and audit how it got in. Going forward, prompt Claude Code (or any AI coding agent) to include a quick process-and-network audit whenever you build system-monitoring tools; that's the exact workflow that exposed this miner. Don't buy a $60 antivirus subscription for this — macOS's own `top`, `lsof`, and `launchctl` are enough if you know what to look for.