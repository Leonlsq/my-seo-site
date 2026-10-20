---
title: "ConnectWise Breach: How to Check if Your M365 Tenant Was Hit"
description: "Hackers breached Microsoft 365 tenants via the ConnectWise Cloud Backup supply-chain attack. Here's how to audit your tenant, revoke rogue app identities, and lock down access."
pubDate: 2026-10-20
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## ConnectWise Cloud Backup Breach: How to Check if Your Microsoft 365 Tenant Was Compromised

ConnectWise has shut down customer access to its Cloud Backup service (formerly SkyKick Cloud Backup) after attackers accessed application identities and used them to compromise Microsoft 365 tenants. If your MSP or IT team ever ran SkyWink/ConnectWise Cloud Backup against your M365 environment, that backup app had broad, persistent access to your mailboxes, OneDrive, and SharePoint — and that's exactly the kind of credential attackers love. This guide gives you a concrete, 20-minute audit you can run today in the Microsoft 365 admin center and Entra ID (Azure AD) to find rogue app identities, revoke them, and confirm whether your tenant was touched.

**Direct takeaway:** The single highest-value check is your **Enterprise Applications** list in Entra ID. Any app tied to ConnectWise, SkyKick, or Cloud Backup that you did not personally re-authorize after the shutdown notice is a red flag. Revoke first, investigate second.

## Step-by-Step Guide: Audit and Revoke Compromised App Identities

Work through these in order. You need at least the **Cloud Application Administrator** or **Global Administrator** role.

### Step 1 — Pull the list of enterprise applications and service principals
1. Go to **entra.microsoft.com → Identity → Applications → Enterprise applications**.
2. Set the **Application type** filter to *All Applications* and search for: `ConnectWise`, `SkyKick`, `Cloud Backup`, `Backup`.
3. For each match, click the app → **Properties** and note the **Object ID** and **Application (client) ID**.
4. Cross-check the **Sign-in logs** (Enterprise applications → [app] → Sign-in logs) for the last 30 days. Look for sign-ins from unexpected IPs or countries.

### Step 2 — Inspect API permissions (the real damage vector)
1. Open each suspicious app → **Permissions** (or **API permissions** in App registrations).
2. Flag any **Application permissions** (not Delegated) on `Mail.Read`, `Mail.ReadWrite`, `Files.ReadWrite.All`, `Sites.FullControl.All`, or `User.Read.All`. Backup tools legitimately request these — which is why a stolen app identity is so dangerous.
3. Check **Granted consent** dates. A re-consent you didn't request is a compromise indicator.

### Step 3 — Revoke access and rotate secrets
1. In the app's **Overview**, click **Delete** (or disable via **Properties → Enabled for users to sign-in = No** first if you need to preserve logs).
2. Go to **App registrations → [app] → Certificates & secrets** and **delete all client secrets and certificates**.
3. Remove any **service principal** from roles: **Enterprise applications → [app] → Users and groups** (remove assignments) and check **Azure role assignments** for the service principal.
4. Run a **revoke sign-in sessions** action: `Revoke-AzureADUserAllRefreshToken` (legacy) or in the portal, **Users → [user] → Revoke sessions**.

### Step 4 — Validate mailbox and audit log activity
1. Open **Microsoft Purview → Audit** and search the **MailItemsAccessed**, **FileAccessed**, and **Add-MailboxPermission** operations for the last 90 days.
2. Filter **User** to the service principal's app name if present, or by the affected users.
3. Look for **New-InboxRule** or **Set-Mailbox** events — attackers often add forwarding rules (e.g., forward to an external address) after gaining mailbox access.

### Step 5 — Check for persistence
- **OAuth consent grants:** Entra → Enterprise applications → **Admin consent requests** and **User consent** settings.
- **New app registrations** created in the last 30 days: Entra → App registrations → sort by *Created date*.
- **New global/admin roles** assigned unexpectedly.

## Common Issues, Alternatives, and What You Should Know

**"The app is already gone from my tenant."** ConnectWise pulling the service doesn't remove the app identity from *your* tenant. You must delete the enterprise app and service principal yourself — Microsoft does not do this for you.

**"We never used Cloud Backup."** SkyKick was widely resold through MSPs. Even if your direct vendor relationship was different, check for apps named after your MSP or `SkyKick` — MSPs often deploy under their own branding.

**Backup gap risk.** With ConnectWise Cloud Backup offline, you may have no third-party M365 backup right now. Options to restore coverage:

| Alternative | M365 coverage | Notes |
|---|---|---|
| Microsoft 365 Backup (native) | Mail, OneDrive, SharePoint | Included with qualifying licenses; limited retention |
| Veeam Backup for Microsoft 365 | Full | Mature, self-hosted or cloud |
| AvePoint Cloud Backup | Full | Enterprise-focused |
| Druva / Rubrik | Full | Cloud-native, higher cost |

**Cost reality:** Rebuilding trust after a supply-chain compromise means rotating *every* secret the backup app ever held, not just deleting the app. Budget a few hours for a full credential sweep.

**Don't forget conditional access.** Add a policy blocking legacy auth and requiring compliant devices for any app with `Mail.*` application permissions — this limits blast radius if another vendor app is compromised.

## Frequently Asked Questions (FAQ)

### How do I know if my Microsoft 365 tenant was affected by the ConnectWise breach?
Check **Entra ID → Enterprise applications** for ConnectWise/SkyKick apps, review their **sign-in logs** for anomalous IPs, and audit **MailItemsAccessed** and **New-InboxRule** events in Purview for the last 90 days. Unexpected forwarding rules or sign-ins from new locations are the strongest indicators.

### Does deleting the ConnectWise app from my tenant fix the compromise?
No. Deleting the app stops *future* access, but you must also **rotate all client secrets/certificates**, **revoke user refresh tokens**, and **audit mailbox rules** created while the app had access. Attackers may have established persistence via OAuth grants or forwarding rules.

### Is Microsoft 365 Backup a safe replacement for ConnectWise Cloud Backup?
It's a reasonable stopgap for mail, OneDrive, and SharePoint if your licensing qualifies, but it has shorter retention and fewer restore options than Veeam, AvePoint, or Druva. For compliance-heavy tenants, a dedicated third-party backup is still recommended.

### What permissions made the ConnectWise Cloud Backup app so dangerous if compromised?
Backup apps require **application-level** (not delegated) permissions like `Mail.ReadWrite`, `Files.ReadWrite.All`, and `Sites.FullControl.All` to back up data across all users. A stolen app identity with those permissions can read or modify every mailbox and file in the tenant without a user ever signing in.

## Final Verdict

Treat this as an active incident until proven otherwise. **Do the Entra audit today** — it takes 20 minutes and is the only way to know if a rogue app identity is sitting in your tenant. If you find one, delete it, rotate every secret, revoke sessions, and scan for inbox rules. Then close the backup gap with a dedicated third-party tool (Veeam or AvePoint for most SMBs) and add conditional access policies so the next supply-chain compromise can't reach your mailboxes. Don't wait for ConnectWise's post-mortem — your exposure window is now.