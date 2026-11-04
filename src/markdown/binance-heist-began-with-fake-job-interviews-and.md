---
title: "Homebrew Malware Check: Did a Fake Job Interview Hack Your Mac?"
description: "Binance's $40M+ heist started with a malicious Homebrew download and fake job interviews. Here's how to audit your Mac, remove the backdoor, and lock down dev tools."
pubDate: 2026-11-04
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Binance's Homebrew Attack Explained — and How to Check If Your Mac Is Compromised

The October 29 Binance breach wasn't a brute-force hack. According to Binance's post-incident disclosure, North Korean attackers spent months running fake job interviews to trick developers into installing "coding assessment" packages — including a malicious **Homebrew** formula — that quietly backdoored their machines. Those compromised developer environments eventually gave the attackers a path into the exchange's internal wallet-signing systems. If you're a developer who's downloaded a "take-home test" or installed Homebrew packages from an unverified tap in the last year, this guide is your audit checklist. The short version: check your Homebrew taps, scan for persistence, rotate your keys, and never run a package from a recruiter you haven't verified.

## Step-by-Step: Audit Your Mac for the Fake-Interview Homebrew Backdoor

Attackers target the *developer toolchain* because it sits next to your SSH keys, cloud credentials, and signing certificates. Here's a practical audit you can run in about 20 minutes.

### Step 1: List every Homebrew tap and package you've installed
```bash
brew tap
brew list --formula
brew list --cask
```
Look for **third-party taps** you don't recognize (anything not `homebrew/core` or `homebrew/cask`). A malicious formula is often delivered via a custom tap like `brew tap attacker/repo` followed by `brew install attacker/repo/some-tool`.

### Step 2: Inspect formula install scripts
Homebrew formulas can run arbitrary code at install time. Check for suspicious `system` or `exec` calls:
```bash
grep -rE "curl|wget|bash -c|osascript|chmod \+x" "$(brew --repository)/Library/Taps"
```
Any formula that downloads and executes a remote script during install is a red flag.

### Step 3: Check for persistence mechanisms
Fake "coding assessment" payloads typically establish persistence. Inspect these locations:
- `~/Library/LaunchAgents/` and `/Library/LaunchAgents/` — look for recently added `.plist` files
- `crontab -l` — unexpected scheduled jobs
- `~/Library/Application Support/` — unfamiliar binaries
- Login items under **System Settings → General → Login Items**

### Step 4: Scan for known indicators
Run a reputable scanner (Malwarebytes, Objective-See's **KnockKnock** and **BlockBlock** for persistence, and **LuLu** for outbound connections). KnockKnock specifically enumerates launch agents, kernel extensions, and login items — the exact vectors used in developer-targeted intrusions.

### Step 5: Rotate everything that touched the machine
If you find anything suspicious, assume compromise:
1. Rotate SSH keys (`~/.ssh/id_*`) and remove old entries from `authorized_keys` on remote servers.
2. Revoke and reissue cloud API tokens (AWS, GCP, GitHub PATs).
3. Rotate crypto wallet keys and move funds to a fresh, hardware-backed wallet.
4. Reinstall macOS from a clean image if persistence is confirmed — don't try to "clean" a signing machine.

## Common Issues, Red Flags, and What You Should Know

| Red flag | What it means | Action |
|---|---|---|
| Recruiter sends a `.zip`/`.dmg` "assessment" | Classic delivery vector | Never run; use an isolated VM |
| Custom Homebrew tap in install instructions | Bypasses `homebrew/core` review | Verify the tap owner's identity |
| Formula runs `curl ... \| bash` | Remote code execution at install | Reject the package |
| Unknown LaunchAgent `.plist` | Persistence | Investigate, then remove |
| `sudo` requested for a "test" | Privilege escalation attempt | Stop immediately |

**Safer workflow for take-home tests:** run untrusted code inside a disposable VM (UTM, Parallels, or a cloud sandbox like GitHub Codespaces) with **no access** to your real SSH keys, browser sessions, or password manager. Use a separate macOS user account with no iCloud login.

**Alternatives to risky installs:** prefer packages from `homebrew/core`, verify checksums, and use `brew install --formula <name>` only after reading the formula on GitHub. For Node/Python tooling, pin versions and audit with `npm audit` / `pip-audit`.

**Why this matters beyond Binance:** the same playbook — fake recruiter → malicious dev tool → credential theft — has hit crypto exchanges, DeFi teams, and individual engineers. The Binance case shows the blast radius when a signing system is reachable from a compromised laptop. Treat your dev machine like a production server.

## Frequently Asked Questions (FAQ)

### How do I know if a Homebrew package I installed is malicious?
Check `brew tap` for unknown third-party taps, inspect the formula's install script for `curl`/`bash -c` calls, and scan with KnockKnock for persistence. If you installed a package at a recruiter's request, treat it as compromised and rotate credentials.

### Was the Binance hack caused by Homebrew itself?
No — Homebrew is a legitimate package manager. Attackers abused it by publishing a malicious formula or tap and convincing developers to install it during a fake job interview. The vulnerability was social engineering plus an unverified third-party package, not a flaw in Homebrew's core.

### What should I do if I ran a suspicious "coding assessment" file?
Disconnect from the network, do not enter credentials, run a full malware scan, check LaunchAgents and login items, then rotate SSH keys, API tokens, and wallet keys from a *different* trusted device. If persistence is found, reinstall macOS cleanly.

### Can fake job interviews really lead to a crypto exchange breach?
Yes. Binance's disclosure describes exactly that: months of social engineering against developers, malicious developer software, and eventual access to internal wallet-signing systems. The lesson is that human-targeted attacks on engineers are a direct path to high-value systems.

## Final Verdict

The Binance heist is a wake-up call for every developer: **your laptop is an attack surface, and a recruiter's "assessment" is now a known malware vector.** Don't wait for an incident. Today, run `brew tap` and `brew list`, delete taps you don't recognize, install KnockKnock and BlockBlock for ongoing persistence monitoring, and adopt a hard rule — untrusted code runs only in a disposable VM with zero access to real credentials. If you've recently installed a package from a job-interview process, assume compromise and rotate your keys now. Five minutes of auditing beats a drained wallet.