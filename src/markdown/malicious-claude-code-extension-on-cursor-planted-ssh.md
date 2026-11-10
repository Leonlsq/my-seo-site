---
title: "Malicious Claude Code Extension: How to Check & Remove SSH Backdoor"
description: "Exposed to the fake Claude Code Cursor extension? Follow this step-by-step guide to detect and remove the SSH backdoor, rotate keys, and secure VS Code."
pubDate: 2026-10-31
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Check If You Installed the Malicious Claude Code Extension (and Remove the SSH Backdoor)

On October 29, a trojanized build of Anthropic's **Claude Code** VS Code extension was live on Cursor's extension marketplace for roughly **11 hours**, exposing up to **5,000 developers** to malware that silently installs a **persistent SSH backdoor** on your machine. If you installed or updated Claude Code through Cursor during that window, treat your workstation as compromised until you've verified otherwise. This guide gives you a concrete, copy-paste checklist to **detect the backdoor, remove it, and rotate any credentials** that may have leaked — in about 15 minutes.

The short version: **don't panic-uninstall everything.** Work through the steps below in order, because deleting the extension before you capture forensic evidence (like the malicious `authorized_keys` entry) can make cleanup and incident reporting harder.

## Step-by-Step: Detect and Remove the SSH Backdoor

### Step 1 — Confirm whether you're in the exposure window
Check your extension install/update history. The malicious build was distributed for ~11 hours on **October 29**. In Cursor, open the Extensions panel, find **Claude Code**, and check the version and "Last Updated" timestamp. If it was installed or updated on October 29, continue. If it predates that day and hasn't updated since, you're likely in the clear — but still run Steps 3–4 as a sanity check.

### Step 2 — Inspect your SSH `authorized_keys` files (the core indicator)
The backdoor's persistence mechanism is an attacker-controlled public key added to your SSH authorized keys. On **macOS/Linux**, run:

```bash
cat ~/.ssh/authorized_keys
cat ~/.ssh/authorized_keys2 2>/dev/null
sudo cat /root/.ssh/authorized_keys 2>/dev/null
```

On **Windows**, check:
- `C:\Users\<you>\.ssh\authorized_keys`
- `C:\ProgramData\ssh\administrators_authorized_keys`

**What to look for:** any key you did not add yourself, especially keys with comments like `claude`, `cursor`, `dev`, or random strings, or `from=` / `command=` restrictions you never configured. **Screenshot and save a copy** of any suspicious line before deleting it — you'll want it for incident reporting.

### Step 3 — Check for rogue SSH daemons and persistence
The malware aims to keep SSH access alive. Verify what's listening:

```bash
# macOS/Linux
sudo lsof -iTCP:22 -sTCP:LISTEN
sudo launchctl list | grep -i ssh        # macOS
systemctl list-units --type=service | grep -i ssh   # Linux
```

On Windows, run `Get-Service *ssh*` and `netstat -ano | findstr :22` in PowerShell. Look for SSH services or listeners you didn't enable — **Remote Login / OpenSSH Server should be OFF** unless you deliberately turned it on.

Also check scheduled persistence:
- macOS: `~/Library/LaunchAgents`, `/Library/LaunchDaemons`
- Linux: `crontab -l`, `~/.config/systemd/user/`, `/etc/systemd/system/`
- Windows: Task Scheduler for unfamiliar entries, and `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

### Step 4 — Remove the extension and the backdoor
1. In Cursor, uninstall **Claude Code** from the Extensions panel.
2. Delete the malicious line(s) from every `authorized_keys` file you found in Step 2 (edit with `nano`/`vim`, or on Windows with Notepad — **do not** delete the whole file if it contains your own legitimate keys).
3. Disable any rogue SSH service you identified in Step 3 (`sudo systemctl disable --now ssh` on Linux, `Stop-Service sshd` on Windows).
4. Reinstall Claude Code **only** from the official Anthropic source (see below), not from a third-party marketplace listing.

### Step 5 — Rotate every credential the machine could reach
A backdoor means assume compromise. Rotate, in this order:
- **SSH keys** — generate new keypairs (`ssh-keygen -t ed25519`) and remove old public keys from GitHub, GitLab, servers, and cloud providers.
- **Cloud/API tokens** — AWS, GCP, Azure, Anthropic API keys, GitHub PATs.
- **Passwords** stored in browsers or password managers on that machine.
- **CI/CD secrets** and any `.env` files in project folders.

## Common Issues, Alternatives, or What You Should Know

**"I can't tell which key is malicious."** Compare against your known keys — check the fingerprint of each key in `authorized_keys` with `ssh-keygen -lf` and match it to keys you generated. Anything unmatched is suspect.

**"Is Cursor itself malicious?"** No evidence points to Cursor as the attacker; the issue was a **supply-chain compromise of a specific extension build** distributed through its marketplace. Still, review your installed extensions and prefer **verified publishers**.

**Safe install sources for Claude Code:**

| Source | Trust level | Notes |
|---|---|---|
| Anthropic official site / docs | ✅ Highest | Always the canonical download |
| Official VS Code Marketplace (verified publisher) | ✅ High | Confirm publisher identity |
| Cursor marketplace (third-party listings) | ⚠️ Verify | Check version + publisher before install |
| Random GitHub forks / `.vsix` files | ❌ Avoid | Common malware vector |

**Prevention checklist going forward:**
- Enable **extension auto-update review** rather than silent updates.
- Turn on **2FA** everywhere and use **hardware keys** for SSH where possible.
- Run untrusted tooling in a **VM or container**, not your daily-driver machine.
- Set up **file integrity monitoring** on `~/.ssh`.

## Frequently Asked Questions (FAQ)

### How do I know if the malicious Claude Code extension infected my computer?
Check `~/.ssh/authorized_keys` (and the Windows equivalent) for SSH public keys you didn't add, and confirm whether Claude Code was installed or updated on **October 29**. An unrecognized key plus an October 29 update is a strong indicator.

### Does uninstalling the Claude Code extension remove the SSH backdoor?
**No.** Uninstalling the extension removes the delivery mechanism, but the backdoor persists via the injected `authorized_keys` entry and any rogue SSH service. You must manually remove the key and disable the service (Steps 2–4).

### Was the official Anthropic Claude Code extension affected?
The compromise was a **malicious build distributed through Cursor's marketplace**, not the canonical Anthropic release. Install only from Anthropic's official source and verify the publisher before updating.

## Final Verdict

If you installed Claude Code via Cursor on **October 29**, assume exposure and run the full five-step checklist today — **check `authorized_keys`, kill rogue SSH services, uninstall the extension, and rotate every credential** the machine could reach. The 15 minutes you spend verifying is far cheaper than a persistent backdoor sitting on your dev machine. Going forward, install Claude Code only from Anthropic's official channel, review extension publishers before every update, and keep SSH Remote Login disabled unless you actively need it.