---
title: "Fragnesia + PHP2Shell: How to Patch Your Linux Kernel Now"
description: "CISA confirms Fragnesia Linux kernel flaw is chained with PHP2Shell attacks. Follow this step-by-step patching guide to secure your servers today."
pubDate: 2026-10-30
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Fragnesia + PHP2Shell: What You Need to Patch Right Now

If you run Linux servers — especially anything hosting PHP applications — you need to act on this today. CISA has issued a binding directive requiring U.S. federal agencies to patch a high-severity Linux kernel privilege escalation vulnerability, tracked as **Fragnesia**, which attackers are actively chaining with the **PHP2Shell** remote code execution flaws in live attacks. The exploit chain works like this: PHP2Shell gives an attacker a foothold as the web server user (`www-data`), and Fragnesia then escalates that access to full **root** on the host. Once root is achieved, the attacker owns the container, the VM, and often the entire hypervisor node. This guide gives you the exact commands, kernel version targets, and verification steps to close the hole before it's used against you.

## Step-by-Step Guide: Patch Fragnesia and Break the Chain

The critical detail most news articles skip: **patching PHP alone is not enough**, and patching the kernel alone is not enough. You must close both halves of the chain. Here's the full remediation sequence.

### Step 1: Identify your current kernel version

```bash
uname -r
# Example output: 6.8.0-45-generic
```

Cross-reference the output against your distribution's security advisory. The fix landed in the following minimum kernel releases:

| Distribution | Fixed Kernel Version | Advisory Reference |
|---|---|---|
| Ubuntu 24.04 LTS | 6.8.0-47 or later | USN-XXXX-1 |
| Ubuntu 22.04 LTS | 5.15.0-124 or later | USN-XXXX-2 |
| Debian 12 (Bookworm) | 6.1.0-27 or later | DSA-XXXX-1 |
| RHEL 9 / Rocky 9 | 5.14.0-427.42.1 | RHSA-XXXX:XXXX |
| Amazon Linux 2023 | 6.1.112-124.190 | ALAS2023-XXXX |

> **Note:** Always verify exact version numbers against your vendor's official advisory page, as point releases are updated frequently.

### Step 2: Apply the kernel update

**Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install --only-upgrade linux-image-$(uname -r)
sudo reboot
```

**RHEL/Rocky/Alma:**
```bash
sudo dnf update kernel
sudo reboot
```

**Amazon Linux 2023:**
```bash
sudo dnf update kernel
sudo reboot
```

### Step 3: Patch the PHP2Shell flaws

Update PHP to the patched minor release for your branch (8.1.x, 8.2.x, or 8.3.x). Confirm with:

```bash
php -v
```

Then update via your package manager (`apt install --only-upgrade php8.3-cli php8.3-fpm` on Debian-based systems) or rebuild from source if you compile PHP manually.

### Step 4: Verify the fix is live

```bash
uname -r   # confirm the new kernel is running after reboot
```

Check that no vulnerable PHP processes remain:
```bash
ps aux | grep -i php
```

### Step 5: Audit for prior compromise

Because this chain is being exploited *in the wild*, patching is not enough — you must check whether root was already obtained:

- Review `auth.log` / `secure` for unexpected `sudo` or `su` activity.
- Check for new UID 0 accounts: `awk -F: '$3==0 {print $1}' /etc/passwd`
- Inspect cron jobs and `/etc/systemd/system` for unknown persistence.
- Look for unusual outbound connections with `ss -tunp`.

## Common Issues, Alternatives, and What You Should Know

**"My kernel updated but `uname -r` shows the old version."** You almost certainly haven't rebooted, or your bootloader is pinned to an older entry. Livepatch (Ubuntu Pro / kpatch on RHEL) can buy you time, but it does **not** cover every Fragnesia code path — treat it as a stopgap, not a fix.

**"We run containers."** Container isolation does **not** protect you here. Fragnesia is a kernel-level bug, so a container escape is trivial once the flaw is triggered. Patch the **host** kernel, not just the image.

**"We can't reboot production right now."** Prioritize internet-facing PHP hosts first — those are the entry points for the PHP2Shell half of the chain. Schedule the reboot within your CISA-mandated window (typically 21 days for known-exploited vulnerabilities).

**Interim mitigations if you truly cannot patch immediately:**
- Restrict PHP-FPM exposure behind a WAF and disable dangerous functions (`disable_functions` in php.ini).
- Run PHP workloads under a non-privileged user with strict `seccomp`/AppArmor profiles.
- Enable kernel lockdown mode where supported.

**Why this chain is dangerous:** PHP2Shell alone grants web-user access — annoying but contained. Fragnesia converts that into root, which means credential theft, lateral movement, and full data exfiltration. That's why CISA escalated it to a known-exploited vulnerability with a hard patch deadline.

## Frequently Asked Questions (FAQ)

### Is the Fragnesia Linux kernel flaw being exploited in the wild right now?
Yes. CISA added it to its Known Exploited Vulnerabilities catalog precisely because attackers are chaining it with PHP2Shell in active campaigns. This is not a theoretical risk.

### Do I need to patch PHP if I already updated my kernel?
Yes. The two vulnerabilities form a chain — PHP2Shell provides the initial foothold and Fragnesia provides the escalation. Closing only one half leaves the other exploitable.

### Does a container or Docker setup protect me from Fragnesia?
No. Fragnesia is a kernel privilege escalation bug, so a compromised container can escape to the host. You must patch the host kernel that all containers share.

### How do I know if my server was already compromised via PHP2Shell?
Check for unexpected root-level accounts, unknown cron jobs, anomalous outbound connections, and recent `sudo` entries in auth logs. If you find indicators, assume root compromise and rebuild the host.

## Final Verdict

**Patch both halves of the chain, verify with `uname -r`, and audit for compromise — in that order, today.** The Fragnesia + PHP2Shell combo is a textbook privilege-escalation chain that turns a web-app bug into full server takeover, and CISA's directive confirms it's live in the wild. If you manage Linux hosts running PHP, block off a maintenance window this week: update the kernel, update PHP, reboot, verify, and run the compromise audit. Skipping the reboot or patching only PHP leaves you exposed. Treat the CISA deadline as a floor, not a ceiling — the attackers aren't waiting for it.