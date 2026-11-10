---
title: "cPGuard Backdoor Attack: How to Check If You're Infected"
description: "Hackers hijacked cPGuard autoupdate to push a backdoor. Run these exact commands to detect, remove, and block the compromise on your server today."
pubDate: 2026-11-04
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## cPGuard Autoupdate Supply Chain Attack: Detect and Remove the Backdoor

If you run cPGuard on a cPanel, DirectAdmin, or Plesk server, treat the autoupdate channel as compromised until you verify your install. Attackers breached the update infrastructure for the cPGuard web security suite and used it to distribute a backdoor plus a data-stealing script to downstream servers. The critical detail: **the malicious payload arrived through the legitimate update mechanism**, meaning your server could be infected even if you never clicked a phishing link or opened a suspicious file. This guide gives you the exact commands to check for indicators of compromise (IOCs), remove the backdoor, rotate credentials, and harden autoupdate so it can't be weaponized again.

## Step-by-Step: Check, Clean, and Harden Your Server

Work through these steps in order. Run all commands as root over SSH, and snapshot the server first if you can.

### Step 1 — Identify your cPGuard version and update history
```bash
cpgcli --version
rpm -qa | grep -i cpguard        # RHEL/AlmaLinux/CloudLinux
dpkg -l | grep -i cpguard        # Debian/Ubuntu
grep -i "cpguard" /var/log/yum.log* /var/log/dpkg.log* 2>/dev/null | tail -50
```
Note any update timestamps that fall inside the reported attack window. If you auto-update, assume the worst and proceed to Step 2.

### Step 2 — Hunt for the backdoor IOCs
The attacker tooling typically drops a rogue PHP script and a cron or systemd persistence mechanism. Check these locations:
```bash
# Suspicious PHP in web roots
find /home/*/public_html /var/www -name "*.php" -mtime -30 -newer /etc/passwd -ls 2>/dev/null

# Rogue cron entries
crontab -l; ls -la /etc/cron.d/ /var/spool/cron/
grep -rE "base64_decode|eval\(|curl|wget" /etc/cron.d/ 2>/dev/null

# Unexpected systemd units and outbound connections
systemctl list-units --type=service --state=running | grep -viE "cpguard|systemd|ssh|crond"
ss -tunp | grep -vE "127.0.0.1|::1"
```
Flag anything that phones home to unfamiliar IPs, decodes base64 payloads, or was created around the update time.

### Step 3 — Isolate and remove
1. Take the server offline from public traffic or block the suspicious egress IPs at the firewall.
2. Quarantine (don't delete yet) any flagged files: `mv /path/to/file /root/quarantine/`.
3. Remove rogue cron jobs and systemd units you didn't create.
4. Reinstall cPGuard from a **known-good, manually verified package** rather than the autoupdate channel.
5. Reboot and re-run the Step 2 checks to confirm nothing respawns.

### Step 4 — Rotate everything the stealer could touch
The data-stealing component targets credentials. Rotate immediately:
- cPanel/WHM root and reseller passwords
- SSH keys (`~/.ssh/authorized_keys` — remove unknown keys)
- Database passwords in `wp-config.php` and app configs
- API tokens (payment gateways, cloud providers, mail relays)
- `.env` secrets and any stored in `/home/*/.`

### Step 5 — Harden autoupdate so this can't repeat
| Control | Action |
|---|---|
| Package signature verification | Enforce GPG/signature checks; reject unsigned updates |
| Staged rollout | Pin to a tested version, update manually after review |
| Egress filtering | Allowlist outbound to vendor IPs only |
| File integrity monitoring | Enable AIDE or `rpm -Va` weekly |
| Least privilege | Run the panel service as a non-root user where supported |

## Common Issues and What You Should Know

- **"My scanner says clean but I still see odd traffic."** Backdoors often hide in memory or in files newer than your scan baseline. Rebuild from a clean image if you can't fully account for the compromise.
- **Autoupdate is convenient — should I disable it?** For security tooling, prefer manual, signature-verified updates. A compromised security suite is worse than a slightly outdated one.
- **Shared hosting users:** You can't fix this yourself. Contact your host and ask whether cPGuard was affected and what remediation they performed.
- **Evidence preservation:** If you're a business handling customer data, preserve logs before wiping and consider breach-notification obligations.

## Frequently Asked Questions (FAQ)
### How do I know if my server was infected by the cPGuard backdoor?
Check your cPGuard version and update logs against the reported attack window, then scan for recently modified PHP files, rogue cron jobs, unexpected systemd services, and outbound connections to unknown IPs. Any hit on those IOCs means you should isolate and remediate immediately.

### Is it safe to keep using cPGuard after this attack?
Yes, but only after reinstalling from a verified good package and rotating all credentials. Treat the autoupdate channel as untrusted until the vendor confirms the infrastructure is clean, and switch to manual, signature-verified updates in the meantime.

### Can the backdoor steal data without me noticing?
Yes — the data-stealing script is designed to exfiltrate credentials and config files quietly. That's why credential rotation (SSH keys, DB passwords, API tokens) is mandatory even if you find no obvious malware.

## Final Verdict
Don't wait for a vendor patch to feel safe. **Assume compromise, verify with the commands above, and rotate every secret** the stealer could have reached. If you can't confirm a clean state, rebuild the server from a trusted image — a backdoored security suite means your trust boundary is already broken, and only a verified-clean rebuild restores it.