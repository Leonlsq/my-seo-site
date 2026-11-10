---
title: "3AM Ransomware: How to Harden Your School Network Now"
description: "Stop 3AM ransomware lateral movement: a step-by-step guide to segmenting unmanaged hosts, blocking RDP, and locking down the school estate."
pubDate: 2026-11-04
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why One Unmanaged Host Can Encrypt 37 of 50 School Machines

The 3AM ransomware affiliate that hit a UK school estate did not need a zero-day. It needed one unmanaged host, a flat network, and a few hours. According to the incident breakdown, roughly **37 of nearly 50 reachable machines** were encrypted after the attacker pivoted from a single unmanaged device — a textbook lateral movement chain that most school IT teams can block in a single maintenance window.

This guide is not the news story. It is the remediation playbook: the exact segmentation, authentication, and backup controls that would have stopped this attack, written so a two-person school IT team can implement them this week. If your estate has any unmanaged Windows hosts, shared local admin passwords, or RDP reachable between VLANs, treat the steps below as urgent.

**The core takeaway:** 3AM (and its affiliates) exploits *reachability*, not sophistication. Cut reachability and the blast radius collapses from 37 machines to one.

## Step-by-Step Guide: Hardening the School Estate Against 3AM

### Step 1: Find and Isolate Every Unmanaged Host
An unmanaged host is any device not enrolled in Intune, your RMM, or domain policy — lab PCs, staff laptops, spare machines in storage closets.

1. Pull a full inventory from your DHCP leases and switch ARP tables for the last 30 days.
2. Cross-reference against your MDM/RMM enrollment list. Anything left over is unmanaged.
3. Immediately move unmanaged hosts to a quarantine VLAN with **no route to production subnets**.
4. Enroll or reimage each host before returning it to the network. Do not "temporarily" re-enable it.

### Step 2: Segment the Network (The Single Highest-Impact Fix)
The attack reached ~50 machines from one foothold because the network was flat. Fix that first.

| Zone | Devices | Allowed Outbound | Allowed Inbound |
|---|---|---|---|
| Admin/Server VLAN | DCs, backup, hypervisors | Patch CDN, backup target | Only from jump host |
| Staff VLAN | Staff laptops | Internet, SaaS, print | Nothing from student/lab |
| Student/Lab VLAN | Lab PCs, Chromebooks | Internet (filtered) | Nothing |
| Quarantine VLAN | Unmanaged/unknown | Internet only | Nothing |
| IoT/AV VLAN | Cameras, projectors, printers | Vendor cloud | Nothing |

Rules to enforce on the firewall between zones:
- **Deny SMB (445), RDP (3389), WinRM (5985/5986), and WMI (135) between all user VLANs.** These are the four protocols 3AM affiliates abuse for lateral movement.
- Allow only the jump host (a hardened, MFA-protected admin VM) to reach server management ports.
- Log and alert on any denied inter-VLAN SMB/RDP attempt — that alert is your early-warning tripwire.

### Step 3: Kill Shared Local Admin Credentials
3AM affiliates harvest credentials and reuse them across hosts. One shared local admin password = 37 encrypted machines.

1. Deploy **Windows LAPS** (built into Windows 11 23H2+ and available for Windows 10) to randomize and rotate local admin passwords per device.
2. Remove local admin rights from standard staff accounts.
3. Audit for duplicate local admin passwords with a tool like PingCastle or Purple Knight before you deploy LAPS.
4. Enforce a separate, named admin account for IT staff — never the shared "admin" account.

### Step 4: Close the RDP and Remote-Access Gaps
- Disable RDP on all endpoints that do not require it (most school machines do not).
- Where remote access is needed, require it through a VPN or zero-trust gateway with MFA — never expose 3389 to the internet or to user VLANs.
- Disable NLA-bypass legacy settings and enforce **Network Level Authentication**.
- Block inbound RDP at the perimeter firewall and alert on any outbound RDP attempt (a common C2/exfil channel).

### Step 5: Build an Immutable, Offline Backup
Ransomware encryption is only a disaster if recovery fails.

1. Follow the **3-2-1-1 rule**: 3 copies, 2 media types, 1 offsite, 1 immutable/offline.
2. Keep at least one backup copy **offline or on immutable storage** (WORM bucket, tape, or a powered-off NAS).
3. Test a full restore of a lab machine and a domain controller quarterly — document the time-to-restore.
4. Protect backup credentials separately from domain credentials so a compromised domain admin cannot delete backups.

### Step 6: Patch and Monitor the Foothold Vectors
- Patch internet-facing services (VPN, webmail, RMM agents) within 7 days of a critical CVE — 3AM affiliates routinely exploit unpatched edge devices.
- Enable **EDR with ransomware behavior blocking** on every managed host.
- Turn on **Windows Defender Attack Surface Reduction (ASR)** rules, especially "Block credential stealing from lsass.exe" and "Block executable content from email/webmail."
- Forward logs to a SIEM or a free option like Wazuh and alert on mass file-rename events.

## Common Issues, Alternatives, and What You Should Know

- **"We can't segment — it's one flat /16 and the switches are unmanaged."** You can still segment at the firewall with VLAN tagging on managed switches; if switches are truly unmanaged, prioritize replacing the core switch — it is the cheapest blast-radius reduction available.
- **"LAPS broke our legacy lab software."** Exclude specific lab images from LAPS only after documenting the business reason; better, fix the software's dependency on a shared local admin.
- **Budget reality:** A managed 24-port switch runs roughly £150–£400; a year of EDR for 50 endpoints is often under £2,000. Compare that to the average school ransomware recovery cost — downtime, data loss, and reputational damage routinely run into six figures.
- **Alternative to full SIEM:** Wazuh (open source) or Microsoft Defender for Business (bundled in many education licenses) gives you the alerting you need without a dedicated SOC.
- **AI-assisted attacks raise the bar on speed, not skill.** Expect faster reconnaissance and phishing; your controls must be automated (LAPS, ASR, immutable backups) rather than manual.

## Frequently Asked Questions (FAQ)

### What is the 3AM ransomware and how does it spread in schools?
3AM is a ransomware family operated by affiliates who buy access and then move laterally using stolen credentials, SMB, and RDP. In schools it typically enters via an unpatched edge device or phishing, then spreads from an unmanaged or weakly secured host across a flat network.

### How do I stop ransomware spreading from one PC to 37 others?
Segment the network so user VLANs cannot reach each other over SMB/RDP, deploy Windows LAPS to eliminate shared local admin passwords, disable RDP where unnecessary, and keep an immutable offline backup. These four controls alone would have contained the UK school incident.

### Is Windows LAPS free for schools?
Yes. Windows LAPS is built into Windows 11 23H2 and later and is available as a free update for supported Windows 10/11 and Windows Server versions. It requires no extra licensing beyond your existing Windows estate.

### How often should schools test ransomware backups?
At minimum quarterly, with a documented restore of both an endpoint and a domain controller. Test time-to-restore, not just backup success — a backup you cannot restore in hours is not a recovery plan.

## Final Verdict

The UK school estate did not fall to a sophisticated AI attack — it fell to a flat network and an unmanaged host. **Do these three things this week, in this order:** quarantine every unmanaged host, block SMB/RDP between user VLANs at the firewall, and deploy Windows LAPS. Those steps are free or near-free and would have cut the 37-machine blast radius to a single device. Then schedule immutable backups and EDR rollout next month. 3AM affiliates scan for reachability, not prestige — make your estate boring to reach and you stop being a target.