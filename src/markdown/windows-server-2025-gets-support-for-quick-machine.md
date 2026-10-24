---
title: "Quick Machine Recovery on Windows Server 2025: Setup Guide"
description: "Enable and configure Quick Machine Recovery on Windows Server 2025 after the October 2026 update. Step-by-step setup, WinRE requirements, and fixes."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Quick Machine Recovery on Windows Server 2025: How to Enable It (October 2026 Update)

Quick Machine Recovery (QMR) is finally available on Windows Server 2025 — but only if you've installed the **October 2026 security update** (build 10.0.26100.xxxx or later) and your recovery partition is correctly configured. QMR lets a server boot into Windows Recovery Environment (WinRE), automatically contact Microsoft's recovery service, and pull down a targeted fix without an admin physically touching the machine. This guide walks you through enabling it, verifying prerequisites, and fixing the two most common setup failures. If your servers are headless or in remote datacenters, this is the single most valuable patching feature Microsoft has shipped for Server 2025 this year.

## Prerequisites Before You Enable QMR

QMR does not work out of the box. Confirm every item below before you start — skipping any one of these is the #1 cause of "QMR is unavailable" errors.

| Requirement | Detail | How to Verify |
|---|---|---|
| OS build | Windows Server 2025 with Oct 2026 update | `winver` → build 26100.xxxx+ |
| WinRE partition | Enabled and ≥ 500 MB free | `reagentc /info` |
| Network in WinRE | DHCP or static IP with internet egress | Test from recovery console |
| Cloud attach | Azure Arc or Intune enrollment (recommended) | Azure portal → Arc agents |
| Telemetry | Optional/Required diagnostic data enabled | `gpedit.msc` → Data Collection |
| UEFI + Secure Boot | Required for automated remediation | `msinfo32` → System Summary |

## Step-by-Step: Enable Quick Machine Recovery

1. **Install the October 2026 update.** Run `Get-WindowsUpdate -Install` or pull it from WSUS/Windows Update for Business. Reboot and confirm the build number with `winver`.
2. **Verify WinRE is enabled.** Open an elevated terminal and run:
   ```
   reagentc /info
   ```
   You should see `Windows Recovery Environment: Enabled` and a valid WinRE location. If it says `Disabled`, run `reagentc /enable`.
3. **Check free space on the recovery partition.** QMR needs headroom to stage the remediation package. Run `diskpart` → `list partition` and confirm the recovery partition has at least 500 MB free. If not, use `reagentc /disable`, resize with `diskpart`, then `reagentc /enable`.
4. **Enable the QMR policy.** In `gpedit.msc`, navigate to **Computer Configuration → Administrative Templates → Windows Components → Windows Recovery Environment**. Enable **"Configure Quick Machine Recovery"** and set the remediation scan interval (default 30 minutes).
5. **Or push via PowerShell (faster for fleets):**
   ```powershell
   Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WinRE" `
     -Name "QuickMachineRecovery" -Value 1 -Type DWord
   ```
6. **Confirm network access from WinRE.** Boot to recovery (`shutdown /r /o /t 0`), open the command prompt, and run `ipconfig /all` plus `ping 8.8.8.8`. If there's no connectivity, QMR cannot reach the service.
7. **Trigger a test scan.** From the running OS, run `reagentc /scan` and check `C:\Windows\Logs\WinRE\` for QMR entries. A successful handshake logs a remediation ID.
8. **Validate with a dry run.** In a lab VM, simulate a boot failure (rename `winload.efi` on a snapshot) and confirm QMR kicks in and remediates automatically.

## Common Issues and What You Should Know

**"QMR is unavailable on this device."** This almost always means the October 2026 update isn't fully staged or WinRE is disabled. Re-run `reagentc /info` and reinstall the cumulative update.

**No network in WinRE.** WinRE uses a stripped driver set. If your NIC isn't present, inject the driver into the WinRE image with `dism /Add-Driver` against `winre.wim`. This is mandatory for servers with Broadcom or Mellanox 10/25GbE adapters.

**BitLocker prompts block automation.** QMR can't remediate a locked volume. Ensure recovery keys are escrowed to Entra ID or AD, and configure the "Allow network unlock" policy so WinRE can reach the key server.

**Cost and licensing reality check.** QMR itself is free with Server 2025 licensing, but the cloud remediation channel requires Azure Arc-connected machines. Arc is free for servers, but you'll need outbound 443 to `*.his.arc.azure.com` and `*.guestconfiguration.azure.com`. Budget for the network egress if you're on metered links.

**Alternatives.** If QMR doesn't fit your air-gapped environment, fall back to **Windows Server Update Services + scheduled WinRE scripts**, or third-party tools like **Dell OpenManage** and **HPE iLO 6** remote remediation. QMR's advantage is zero-touch automation; its limitation is the cloud dependency.

## Frequently Asked Questions (FAQ)

### Does Quick Machine Recovery work on Windows Server 2022 or 2019?
No. QMR on servers is exclusive to Windows Server 2025 with the October 2026 security update. Earlier versions and Windows 10/11 clients have separate, more limited recovery features.

### Is Quick Machine Recovery enabled by default after the October 2026 update?
No. The update ships the capability, but the policy is off by default. You must enable "Configure Quick Machine Recovery" via Group Policy, Intune, or the registry before it activates.

### Can QMR recover a server with a failed boot drive?
Partially. QMR repairs boot configuration, driver, and update-related failures by staging fixes in WinRE. It cannot recover from physical disk failure or a corrupted recovery partition — keep hardware RAID and backup coverage in place.

## Final Verdict

If you run Windows Server 2025 in remote or headless environments, **enable Quick Machine Recovery today** — it's the cheapest insurance against a 3 a.m. drive to the datacenter. Start with a pilot group of 5–10 servers, verify WinRE space and network egress first, then roll out via Intune or GPO. For air-gapped fleets, skip QMR and invest in iLO/iDRAC remote management instead. Either way, don't wait for your first unbootable server to test this.