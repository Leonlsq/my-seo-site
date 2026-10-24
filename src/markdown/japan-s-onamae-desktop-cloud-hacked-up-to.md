---
title: "Onamae Cloud Hack: How to Check If Your VPS Was Compromised"
description: "Onamae Desktop Cloud breach hit up to 26,739 VPS servers. Here's how to check for malware, harden your server, and decide if you should migrate now."
pubDate: 2026-10-22
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Onamae Desktop Cloud Was Hacked — Here's How to Check Your VPS Right Now

If you rent a VPS or remote desktop from Onamae Desktop Cloud (お名前.com デスクトップクラウド), the October 2026 breach is not just news — it's a direct threat to your data. Attackers compromised the provider's infrastructure and installed malware on up to **26,739 customer servers**, according to the company's disclosure. That means the threat is at the *host* level, not just a weak password on your end.

The direct takeaway: **assume compromise until you prove otherwise.** This guide gives you a concrete checklist to detect malware, harden your instance, and decide whether to stay or migrate. Do the checks in order — the first 30 minutes matter most.

## Step-by-Step: How to Check and Secure Your Onamae VPS

### Step 1 — Confirm whether your server is in the affected range
Log into the Onamae control panel and check the official incident notice for the affected node/IP ranges. If your instance's IP or host node appears in the disclosure, treat it as compromised. Even if it doesn't, run every check below — attackers often move laterally.

### Step 2 — Look for signs of malware on the host
Because the malware was installed at the infrastructure layer, standard antivirus scans on your VM may miss it. Check these indicators:

- **Unexpected outbound connections.** Run `ss -tupn` (Linux) or `netstat -ano` (Windows) and look for connections to unknown IPs, especially on ports 4444, 8443, or 31337.
- **New scheduled tasks.** Linux: `crontab -l` and `ls -la /etc/cron.*`. Windows: `schtasks /query /fo LIST /v`.
- **Modified startup entries.** Linux: `systemctl list-unit-files --state=enabled`. Windows: check `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.
- **Unexpected admin accounts.** Linux: `cat /etc/passwd` and `awk -F: '$3==0' /etc/passwd`. Windows: `net localgroup administrators`.
- **Hash mismatches.** Compare critical binaries against known-good hashes using `sha256sum` or `Get-FileHash`.

### Step 3 — Isolate and snapshot before you clean
Do **not** wipe immediately. Take a snapshot of the current state (for forensics and any insurance/legal claim), then disconnect the instance from the network. If you run production workloads, fail over to a backup node on a *different* provider first.

### Step 4 — Rebuild from scratch
Given the breach was at the host level, cleaning in place is unreliable. The safest path is:

1. Export only your data files (not binaries, not config scripts).
2. Provision a fresh instance — ideally on a different provider.
3. Reinstall the OS from an official image.
4. Restore data after scanning it in an isolated environment.
5. Rotate **every** credential: SSH keys, API tokens, database passwords, and any secrets stored on the old box.

### Step 5 — Harden the new instance
| Control | Linux command / setting | Windows equivalent |
|---|---|---|
| Disable password SSH | `PasswordAuthentication no` in sshd_config | Disable RDP NLA fallback |
| Firewall default-deny | `ufw default deny incoming` | Windows Defender Firewall inbound block |
| Fail2ban / lockout | `apt install fail2ban` | Account lockout policy |
| Auto-updates | `unattended-upgrades` | Windows Update auto-install |
| MFA on panel | Enable in Onamae/registrar account | Same |

## Common Issues, Alternatives, and What You Should Know

**"My scan came back clean — am I safe?"** Not necessarily. Host-level malware can hide below the OS. A clean scan lowers risk but doesn't eliminate it after a provider-level breach.

**Data exposure risk.** If you stored customer data, credentials, or payment info on the VPS, you may have notification obligations under Japan's APPI or GDPR depending on your users. Document your timeline now.

**Should you migrate?** For most users, yes — at least temporarily. Compare your options:

- **Sakura VPS / ConoHa** — Japanese providers with strong track records and local latency.
- **Vultr / Linode / DigitalOcean** — global coverage, mature security tooling, easy snapshots.
- **AWS Lightsail / GCP** — best if you need compliance and audit logs.

Weigh migration cost (a few hours of setup) against the cost of a second compromise. For anything customer-facing, migration wins.

**Check your backups.** If your backups were stored on the same Onamae infrastructure, they may be tainted. Verify backup integrity and move copies offsite.

## Frequently Asked Questions (FAQ)

### How many servers were affected by the Onamae Desktop Cloud hack?
The company reported malware installed on up to **26,739 customer servers**. Check the official notice for the confirmed count and affected node list as the investigation continues.

### Was my Onamae VPS definitely infected?
Not confirmed for every instance, but the breach occurred at the infrastructure level, so any server on affected nodes should be treated as potentially compromised. Rebuild rather than trust an in-place cleanup.

### Can I just change my password and keep using the server?
No. A password change doesn't remove host-level malware or backdoors. Rebuild the instance from a clean image and rotate all credentials.

### Is Onamae Desktop Cloud safe to use going forward?
Only after the provider completes remediation and publishes a root-cause report. Until then, migrate critical workloads elsewhere and monitor the incident page.

## Final Verdict

Treat the Onamae breach as a **"rebuild now" event, not a "wait and see."** Snapshot, isolate, export data, rebuild on a clean provider, and rotate every secret. If you're a casual user with no sensitive data, a full rebuild is still the only reliable fix. If you run anything customer-facing, migrate to Sakura, Vultr, or AWS Lightsail today and don't look back until Onamae publishes a verified remediation report.