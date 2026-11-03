---
title: "Smart App Control Broken? How to Fix After KB5127648"
description: "Smart App Control won't activate after the October 2026 KB5127648 update? Here's how to restore it, force re-evaluation, and what to expect step by step."
pubDate: 2026-11-03
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Smart App Control Won't Activate After KB5127648? Here's the Real Fix

If you installed the October 2026 Windows 11 security update (KB5127648) and found Smart App Control stuck in **Evaluation mode**, greyed out, or refusing to flip to **On**, you're not alone — and you're not stuck. Microsoft has confirmed and patched the known issue that blocked activation of Smart App Control after this update. The catch: the fix is delivered through a servicing-side change and a clean re-evaluation cycle, not a magic toggle. This guide walks you through the exact steps to get Smart App Control active again, how to verify it actually took effect, and what to do if the feature still refuses to cooperate on your machine.

The short version: **update Windows again, reboot twice, then reset the Smart App Control evaluation state via Settings or a registry reset.** Below is the full, tested sequence.

## Step-by-Step: Restore Smart App Control After KB5127648

Before you touch anything, confirm your build. The issue primarily affected Windows 11 24H2 and 25H2 devices that received KB5127648 with Smart App Control previously in **Evaluation** mode (the default state for most users).

### Step 1: Confirm your Windows build and update status

Open **Settings → Windows Update → Update history** and check that KB5127648 is listed. Then verify your OS build:

- Press `Win + R`, type `winver`, and hit Enter.
- You should be on a build **at or above 26100.xxxx** (24H2) or **26200.xxxx** (25H2) with the follow-up servicing revision.

If Windows Update shows a newer cumulative update released *after* KB5127648, install it — Microsoft's resolution shipped as a subsequent servicing fix.

### Step 2: Install the follow-up update and reboot twice

1. Go to **Settings → Windows Update → Check for updates**.
2. Install every pending update, including optional cumulative patches.
3. **Reboot. Then reboot again.** The double reboot matters: Smart App Control's evaluation engine re-reads its state on a clean second boot, and many users report the toggle only un-greys after the second restart.

### Step 3: Check the Smart App Control state

Navigate to **Windows Security → App & browser control → Smart App Control settings**.

| Status shown | Meaning | Action |
|---|---|---|
| **On** | Protection active | Nothing to do — you're fixed |
| **Evaluation** | Learning mode, not enforcing | Wait 24–48 hrs of normal use, then recheck |
| **Off** | Manually disabled | Requires a Windows reset to re-enable (see below) |
| **Greyed out** | Blocked by policy or bug | Run the registry reset in Step 4 |

### Step 4: Force a re-evaluation (registry reset)

If the toggle is greyed out or stuck in Evaluation after 48 hours, reset the evaluation state:

1. Open **Registry Editor** (`regedit`) as administrator.
2. Navigate to:
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy`
3. Locate the `VerifiedAndReputablePolicyState` DWORD.
4. Set its value to **1** (Evaluation) to force a fresh re-evaluation, or **0** to disable cleanly.
5. Reboot, then return to Windows Security and check the toggle.

> ⚠️ **Warning:** Back up the registry key first (`File → Export`). Setting this value incorrectly can leave Smart App Control in an inconsistent state.

### Step 5: Verify enforcement is actually working

To confirm Smart App Control is enforcing (not just showing "On"), try running an unsigned executable from a downloaded ZIP. A properly active Smart App Control will **block it with a notification**. If it runs without a prompt, the feature is still in evaluation.

## Common Issues and What You Should Know

**"Off" is a one-way door.** Once Smart App Control is manually turned off (or automatically disabled after detecting incompatible apps), Microsoft requires a **full Windows reinstall or reset** to turn it back on. There is no supported toggle to re-enable it from Off. Plan accordingly.

**Evaluation mode can take days.** Microsoft's documentation states evaluation lasts until the system has enough telemetry to decide — typically a few days of normal use. Don't panic-refresh the toggle hourly.

**Incompatible apps silently disable it.** If you install unsigned drivers, certain game anti-cheat modules, or older installers during evaluation, Smart App Control may auto-flip to Off. Check **Event Viewer → Applications and Services Logs → Microsoft → Windows → CodeIntegrity** for the trigger.

**Group Policy / MDM override.** On managed devices, `Computer Configuration → Administrative Templates → Windows Components → Smart App Control` can force the state. If you're on a work machine, your IT admin's policy wins over any local fix.

**Is it worth re-enabling at all?** Smart App Control blocks a meaningful share of untrusted executables but is aggressive — it will flag legitimate niche tools, portable apps, and mod loaders. If you regularly run unsigned software, leaving it Off (and relying on Defender + SmartScreen) is a defensible choice.

## Frequently Asked Questions (FAQ)

### Why is Smart App Control greyed out after the October update?
The KB5127648 bug corrupted the policy state read by Windows Security, causing the toggle to appear locked. Installing the follow-up servicing update and rebooting twice restores it; if not, the registry reset in Step 4 forces a re-evaluation.

### Can I turn Smart App Control back on if it's set to Off?
No — not without a clean Windows reinstall or reset. Microsoft designed "Off" as permanent to prevent flip-flopping. Only **Evaluation** and **On** states can be toggled via Settings.

### Does KB5127648 affect Windows 10?
No. Smart App Control is a Windows 11-only feature (22H2 and later). The activation bug was specific to Windows 11 24H2/25H2 devices.

### How long does Smart App Control stay in Evaluation mode?
Typically 24–72 hours of normal usage. If it exceeds a week after the fix, run the registry reset or check CodeIntegrity logs for a blocking app.

## Final Verdict

**Update, reboot twice, and re-check before doing anything drastic.** For the vast majority of affected users, the follow-up servicing update plus a double reboot fully restores Smart App Control activation — no registry surgery required. Only reach for the `VerifiedAndReputablePolicyState` reset if the toggle stays greyed out past 48 hours, and back up first. And if you find Smart App Control is blocking tools you actually need, don't fight it: turning it Off is permanent, so make that decision deliberately rather than in frustration. Bottom line — this is a fixed bug, not a broken feature, and a clean update cycle is your fastest path back to protection.