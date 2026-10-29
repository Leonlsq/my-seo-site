---
title: "Entra ID Passkeys Migration: Step-by-Step Setup Guide"
description: "Microsoft is retiring SMS and voice auth in Feb 2027. Here's how to migrate Entra ID users to passkeys (FIDO2) without sign-in disruptions."
pubDate: 2026-10-29
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Microsoft Is Killing SMS in Entra ID — Here's How to Migrate Users to Passkeys Before February 2027

Microsoft has again urged Entra ID (formerly Azure AD) administrators to move users off SMS and voice authentication before it **retires both methods in February 2027**. If you're an IT admin who just saw the advisory and thought "that's a year away, I'll deal with it later" — don't. Passkey (FIDO2) rollouts are slow, messy, and user-dependent, and the organizations that start now are the ones that avoid the last-minute scramble. This guide walks you through the exact steps to enable, pilot, and enforce passkeys in Entra ID, plus the gotchas that break real-world deployments.

The short version: **enable the Authentication Methods policy, pilot FIDO2 with a small group, communicate with users, then enforce phishing-resistant MFA via Conditional Access** — and stop issuing SMS/voice as a default method well before the 2027 cutoff.

## Step-by-Step: Migrating Entra ID Users to Passkeys

### 1. Confirm your licensing and prerequisites
Passkeys in Entra ID (FIDO2 security keys and, for some scenarios, device-bound passkeys) require **Microsoft Entra ID P1 or P2**, or Microsoft 365 Business Premium. You also need the **Authentication Methods policy** enabled in the Entra admin center (it's the default now, but legacy "legacy MFA" settings can conflict).

### 2. Enable the FIDO2 authentication method
1. Sign in to the **Microsoft Entra admin center** → **Protection** → **Authentication methods** → **Policies**.
2. Select **FIDO2 security key** and set **Enable** to **Yes**.
3. Under **Target**, choose **All users** (or start with a pilot group).
4. Configure **Allow self-service setup** = Yes so users can register their own keys.
5. Set **Enforce attestation** based on your security posture (see table below).
6. Save.

### 3. Run a pilot with 10–50 users
Create a security group (e.g., `SG-Passkey-Pilot`). Target only that group in the FIDO2 policy. This lets you catch hardware, browser, and helpdesk issues before a company-wide push.

### 4. Register passkeys (user flow)
- Go to **mysignins.microsoft.com** → **Security info** → **Add sign-in method** → **Security key** (or **Passkey**).
- Insert a FIDO2 key (USB-A/USB-C/NFC) or use a platform authenticator (Windows Hello, Touch ID) where supported.
- Complete the registration and name the key (e.g., "YubiKey 5C – primary").

### 5. Enforce phishing-resistant MFA via Conditional Access
Create a Conditional Access policy:
- **Assignments:** All users (exclude break-glass accounts).
- **Cloud apps:** All.
- **Grant:** Require **Authentication strength** → **Phishing-resistant MFA**.
- **Enable** in report-only mode first, review sign-in logs, then turn it on.

### 6. Retire SMS/voice as a default
In **Authentication methods**, disable **SMS** and **Voice call** for new enrollments now, and set a hard internal deadline (e.g., Q2 2026) to remove them entirely — well ahead of Microsoft's February 2027 retirement.

### FIDO2 Attestation: Which Setting Should You Pick?

| Setting | What it does | Best for |
|---|---|---|
| **Enforce attestation = Yes** | Only allows keys with a verified, trusted vendor (e.g., YubiKey, Feitian) | High-security orgs, regulated industries |
| **Enforce attestation = No** | Allows any FIDO2-compliant key | Broad BYOD, cost-sensitive rollouts |
| **Allow self-service setup** | Users register their own keys | Reduces helpdesk load |
| **Admin-only setup** | IT provisions keys | Locked-down environments |

## Common Issues, Alternatives, and What You Should Know

- **"Passkey option doesn't appear for users."** Usually the Authentication Methods policy is still targeting a pilot group, or the user is in a legacy MFA policy. Check **Entra → Authentication methods → Activity** for the user.
- **Windows Hello vs. hardware keys.** Windows Hello (platform passkey) is convenient but device-bound — users lose it if the device is wiped. For shared or field devices, issue **hardware FIDO2 keys** (YubiKey 5 series, Feitian K9) as a backup.
- **Break-glass accounts.** Always keep at least two emergency access accounts on a method *not* subject to Conditional Access — otherwise a policy misconfiguration can lock everyone out.
- **Cost reality.** A YubiKey 5 NFC runs roughly **$55–$65**; a cheaper Security Key NFC is ~$25–$30 but lacks some protocols. Budget per-user hardware costs before committing to hardware-only.
- **The "passkey" nuance.** Microsoft's messaging distinguishes **FIDO2 security keys** from **synced passkeys** (e.g., iCloud/Google). Confirm which your tenant supports for your target apps — not every legacy app accepts synced passkeys.
- **Timeline pressure.** Microsoft has repeatedly nudged admins since 2024; the February 2027 date is firm. Treat 2026 as your migration year.

## Frequently Asked Questions (FAQ)

### When is Microsoft retiring SMS and voice authentication in Entra ID?
Microsoft plans to retire SMS and voice call authentication in **February 2027**. Admins are urged to migrate users to phishing-resistant methods like passkeys (FIDO2) and Windows Hello before then to avoid sign-in disruptions.

### Do passkeys in Entra ID cost extra?
Passkeys themselves are free to use, but enabling FIDO2 authentication methods requires **Entra ID P1/P2 or Microsoft 365 Business Premium**. Hardware security keys are a separate per-user cost (~$25–$65 each).

### What's the difference between a passkey and a FIDO2 security key?
A **FIDO2 security key** is a physical hardware device (USB/NFC). A **passkey** is the broader credential — it can be device-bound (Windows Hello, Touch ID) or synced across devices. Entra ID supports both, but availability depends on your app and policy configuration.

### Can I test passkeys without disrupting current sign-ins?
Yes. Run FIDO2 in a **pilot security group**, and set Conditional Access policies to **report-only mode** first. This lets you review sign-in logs and fix issues before enforcing phishing-resistant MFA tenant-wide.

## Final Verdict

**Start your passkey migration now — don't wait for 2027.** The February 2027 SMS/voice retirement is not a drill, and passkey rollouts fail when rushed. My recommended sequence: enable FIDO2 for a pilot group this quarter, issue hardware keys to high-risk users, enforce phishing-resistant MFA via Conditional Access in report-only mode, then flip to enforced by mid-2026. Keep two break-glass accounts on an independent method, and budget for hardware keys if you have field or shared devices. Admins who treat this as a 2026 project will sail through the cutoff; those who wait will be firefighting sign-in failures in January 2027.