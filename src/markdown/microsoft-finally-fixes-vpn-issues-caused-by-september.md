---
title: "Always On VPN Broken After September Update? Fix It Now"
description: "Always On VPN failing after the September 2026 Windows 11 update? Here's Microsoft's official fix plus manual workarounds to restore your connection fast."
pubDate: 2026-11-01
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Always On VPN Failing After the September 2026 Update? Here's the Fix

If your Always On VPN (AOVPN) tunnel started dropping or refusing to connect right after installing the September 2026 Windows 11 security updates, you're not alone — and you're not misconfigured. Microsoft confirmed that the cumulative security rollup broke AOVPN connection establishment on a subset of devices, primarily those using IKEv2 with certificate-based authentication behind certain NAT configurations. Microsoft has now shipped a resolution, but the fix isn't automatic for everyone. This guide gives you the **fastest path to a working VPN**, the manual workarounds if the patch hasn't reached your device, and how to verify you're actually protected.

**The short version:** Install the latest cumulative update (Microsoft's out-of-band fix), reboot, and re-test your tunnel. If you can't patch yet, the IKEv2-to-SSTP fallback or a profile re-import will restore connectivity in most cases.

## Step-by-Step: Restore Your Always On VPN Connection

Work through these in order. Most users are back online after Step 2.

### Step 1: Confirm you're affected by the September regression
Check whether the failure matches the known signature before you start changing settings:

- **Symptom:** VPN status shows "Connecting" then fails with error **809**, **868**, or a generic **"The connection was terminated by the remote computer"**.
- **Timing:** Failures began within 24–48 hours of installing the September 2026 security update.
- **Scope:** Affects IKEv2 device tunnels; user tunnels and SSTP profiles are largely unaffected.
- **Event log check:** Open Event Viewer → `Applications and Services Logs → Microsoft → Windows → RasClient`. Look for Event ID **20227** with the 809/868 codes.

### Step 2: Install Microsoft's resolution update
Microsoft's fix ships as a cumulative update. Here's how to force it:

1. Open **Settings → Windows Update**.
2. Click **Check for updates** and install **all** pending cumulative updates (the fix supersedes the September rollup).
3. If Windows Update doesn't offer it, download the standalone package from the **Microsoft Update Catalog** — search for the KB number listed in Microsoft's release health dashboard for your build.
4. **Reboot** — the fix requires a restart to re-register the VPN service components.

### Step 3: Re-import your VPN profile (if the tunnel still fails)
The update can corrupt cached profile data. Rebuild it cleanly:

1. Open **Settings → Network & Internet → VPN**.
2. Select your AOVPN profile → **Remove**.
3. Re-deploy the profile via your MDM/Intune or re-run the `Add-VpnConnection` PowerShell cmdlet with your original parameters.
4. Run `rasdial "YourVPNName"` in an elevated Command Prompt to test outside the GUI.

### Step 4: Verify the fix held
- Confirm `Get-VpnConnection` returns `ConnectionStatus : Connected`.
- Run `ipconfig` and check the tunnel adapter has a valid IP.
- Ping an internal resource (e.g., `ping intranet.corp.local`) to confirm routing.

## Workarounds If You Can't Patch Yet

If you're on a managed device where the update is blocked, or you need connectivity *right now*, these fallbacks work:

| Workaround | Effort | Reliability | Best For |
|---|---|---|---|
| Switch tunnel type to **SSTP** temporarily | Low | High | Quick restore, non-IKEv2 environments |
| Re-import VPN profile | Low | Medium | Corrupted profile cache |
| Disable/re-enable the **RasMan** service | Low | Medium | Service stuck after update |
| Roll back the September update | Medium | High (short-term) | Unmanaged devices, urgent deadlines |
| Use **Windows Sandbox** or a secondary device | High | High | Isolating whether it's device-specific |

**To switch to SSTP temporarily:** In the VPN profile properties → **Security** tab → set *Type of sign-in info* and *Tunnel type* to SSTP, then reconnect. Note: this requires your VPN gateway to accept SSTP — many enterprise gateways do, but check with IT first.

⚠️ **Do not** permanently roll back the September security update. It patched actively exploited vulnerabilities. Roll back only as a stopgap and reinstall the fixed update as soon as possible.

## What You Should Know Before You Patch

- **It's a security update, not a feature update.** Skipping it leaves you exposed to the CVEs it addressed — patch as soon as your IT policy allows.
- **The fix is cumulative.** You don't need a separate hotfix; the next monthly rollup includes it. If you're on a deferral ring, you may wait up to 30 days — ask IT to expedite.
- **Device tunnels vs. user tunnels behave differently.** The regression hit device tunnels hardest; if only some users are affected, check which tunnel type their profile uses.
- **Third-party VPN clients were unaffected.** This was specific to the built-in Windows AOVPN client stack.

## Frequently Asked Questions (FAQ)

### Why did the September 2026 Windows 11 update break Always On VPN?
The cumulative security update introduced a regression in the IKEv2 connection negotiation path used by Always On VPN device tunnels, causing handshake failures (errors 809/868) on affected devices. Microsoft confirmed the issue and released a corrective cumulative update.

### How do I fix Always On VPN error 809 after the September update?
Install the latest cumulative update via Windows Update and reboot. If the error persists, remove and re-import your VPN profile, then test with `rasdial` from an elevated command prompt. As a stopgap, switch the tunnel type to SSTP if your gateway supports it.

### Is it safe to uninstall the September 2026 security update to fix my VPN?
Only as a temporary measure. The update patched actively exploited vulnerabilities, so uninstalling it re-exposes your device. Roll back only if you're blocked, then reinstall the fixed cumulative update as soon as it's available.

### Does this affect user tunnels or only device tunnels?
The regression primarily impacted IKEv2 **device tunnels**. User tunnels and SSTP-based profiles were largely unaffected, which is why some users on the same network stayed connected.

## Final Verdict

**Patch first, workaround second.** The cleanest fix is Microsoft's cumulative update — install it, reboot, and re-test your tunnel. Only reach for the SSTP fallback or a profile re-import if you're genuinely blocked and can't wait for the patch. Whatever you do, **don't leave the September security update uninstalled long-term**; the VPN outage is annoying, but the vulnerabilities it patched are worse. If you manage devices at scale, push the fixed cumulative update through Intune immediately and add an AOVPN connectivity check to your post-patch validation script.