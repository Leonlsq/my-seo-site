---
title: "Ivanti Connect Secure Zero-Days: How to Patch and Verify (2026)"
description: "Step-by-step guide to patch the two new Ivanti Connect Secure zero-days chained in attacks, plus how to detect compromise and verify your fix."
pubDate: 2026-11-03
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Ivanti Connect Secure Zero-Days: What You Need to Patch Right Now

Ivanti has released security updates for **two more Connect Secure (ICS) remote access gateway vulnerabilities** that attackers have been chaining in real-world zero-day attacks since at least October 1. If you run an Ivanti Connect Secure or Policy Secure appliance exposed to the internet, this is a **patch-now** situation, not a "schedule it for the next maintenance window" situation. The short version: **upgrade to the latest ICS firmware build immediately, run the built-in Integrity Checker Tool (ICT), and audit your logs for indicators of compromise (IoCs)** before you assume you're clean. This guide walks you through the exact patching sequence, verification steps, and detection checks that mainstream news coverage skips.

## Step-by-Step: Patch and Verify Your Ivanti Connect Secure Appliance

The critical detail most people miss: **patching alone does not evict an attacker who already has a foothold.** Because these flaws were exploited as zero-days since October 1, you must treat any unpatched, internet-facing appliance as potentially compromised. Follow this order.

### Step 1 — Identify your current build
1. Log into the admin console.
2. Go to **Maintenance > System Status** and note the **Installed Version** and **Build Number**.
3. Compare against Ivanti's security advisory (published on the Ivanti Product Security portal). If your build predates the patched release, you are vulnerable.

### Step 2 — Snapshot before you touch anything
- Take a **VM snapshot** or full configuration backup first. If the update fails or you later need forensic evidence, you'll want this.
- Export the current **system and admin logs** to external storage. Attackers frequently wipe logs; preserve them now.

### Step 3 — Apply the firmware update
1. Download the patched `.pkg` from the **Ivanti download portal** (verify the SHA-256 hash).
2. Navigate to **Maintenance > Update > Upload Update**.
3. Upload, then click **Install**. The appliance reboots — expect **10–20 minutes** of downtime.
4. Re-check **System Status** to confirm the new build is active.

### Step 4 — Run the Integrity Checker Tool (ICT)
The ICT is your fastest signal for post-exploitation tampering. Run it **in both modes**:

| ICT Mode | What it detects | When to run |
|---|---|---|
| **Internal** (on-box) | Modified system files, injected webshells | Immediately after patching |
| **External** (off-box) | Rootkit-level persistence the on-box tool can't see | If internal ICT shows anomalies |

If either mode returns **non-standard file changes**, do not trust the appliance — proceed to Step 5.

### Step 5 — Hunt for indicators of compromise
- Search logs for **unexpected admin logins**, especially from unfamiliar geographies.
- Look for **new local users** or modified authentication realms.
- Check for **outbound connections** to unknown IPs (attackers often tunnel through the gateway).
- Review **cron jobs and startup scripts** for injected commands.

### Step 6 — Factory reset if compromised
Ivanti's own guidance: if you confirm compromise, **factory reset the appliance and rebuild from a known-good configuration** — patching a backdoored device does not remove the backdoor.

## Common Issues, Detection Gaps, and What You Should Know

- **"I patched, am I safe?"** Only if you were never exploited. Given the October 1 exploitation window, run the ICT regardless.
- **Detection evasion is real.** Sophisticated actors have historically modified the ICT itself on compromised appliances. An **external ICT scan** or a clean rebuild is the only trustworthy confirmation.
- **No public workaround exists.** Unlike some past Ivanti flaws, there is no reliable config toggle to mitigate these — patching is mandatory.
- **Alternatives if you're evaluating your edge stack:** Ivanti competitors like **Palo Alto GlobalProtect, Cisco AnyConnect, and Fortinet FortiClient** have their own patch cadence — but switching mid-incident adds risk. Patch first, migrate later.
- **Automate future response.** Subscribe to Ivanti's security RSS feed and set alerts for CVEs affecting ICS/Policy Secure so you're not learning about the next zero-day from a headline.

## Frequently Asked Questions (FAQ)

### Are the new Ivanti Connect Secure zero-days being actively exploited?
Yes. Ivanti confirmed the two flaws have been **chained in zero-day attacks since at least October 1**, meaning exploitation predates public disclosure — treat exposure as high risk.

### How do I know if my Ivanti appliance was compromised?
Run the **Integrity Checker Tool (both internal and external modes)**, audit admin logs for unknown logins, and check for new users or outbound connections. Any anomaly means factory reset and rebuild.

### Is there a workaround if I can't patch immediately?
Ivanti has not published a reliable mitigation for these specific flaws. If patching is delayed, **restrict internet exposure** of the appliance and monitor logs aggressively — but this is a stopgap, not a fix.

## Final Verdict

**Patch today, verify with the ICT, and assume compromise until proven otherwise.** These two chained zero-days have been live since October 1, so the real risk isn't the patch itself — it's the silent backdoor an attacker may have already planted. Follow the six steps above, run the external ICT if anything looks off, and if you find tampering, do the factory reset. Anything less is leaving a known-exploited gateway open at the edge of your network.