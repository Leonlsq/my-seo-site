---
title: "Fix Broken Exchange Online EWS Apps: Microsoft's Re-Enable Guide"
description: "EWS apps broke after Microsoft retired the Exchange Online API. Here's how IT admins re-enable EWS to fix them, step by step."
pubDate: 2026-10-25
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Fix Broken Exchange Online EWS Apps (Microsoft's Re-Enable Method)

If your line-of-business app, PowerShell script, or third-party mail integration suddenly stopped syncing after Microsoft retired Exchange Web Services (EWS) in Exchange Online, you're not alone — and you don't have to rewrite everything overnight. Microsoft has confirmed that IT admins can **re-enable the retired EWS API** for affected tenants to restore broken apps. This guide walks you through exactly how to do it, what to check first, and the risks you need to weigh before flipping the switch. The short version: EWS is off by default for new tenants, but Microsoft provides a re-enable path for tenants with legitimate app dependencies — and you should treat it as a temporary bridge, not a permanent fix.

## Step-by-Step Guide to Re-Enable EWS in Exchange Online

Before you touch anything, confirm the failure is actually EWS-related. Common symptoms include apps returning `401 Unauthorized`, `503 Service Unavailable`, or `The remote server returned an error: (403) Forbidden` when calling `https://outlook.office365.com/EWS/Exchange.asmx`.

### Step 1: Confirm EWS is the culprit
1. Test connectivity to the EWS endpoint with a tool like `EWS Editor` or a simple PowerShell `Invoke-WebRequest`.
2. Check the **Microsoft 365 Message Center** for the EWS retirement notice and confirm your tenant's status.
3. Review app logs for EWS-specific error codes (not Graph or IMAP errors).

### Step 2: Identify dependent apps
Run an inventory of everything calling EWS. Typical offenders:
- Legacy on-premises backup/archiving tools
- Custom PowerShell automation using `EWS Managed API`
- Third-party CRM or ticketing connectors
- Multifunction printers scanning to email via EWS

### Step 3: Re-enable EWS via PowerShell
Connect to Exchange Online PowerShell and run the re-enable command Microsoft documents for affected tenants:

```powershell
Connect-ExchangeOnline -UserPrincipalName admin@yourtenant.com
Set-OrganizationConfig -EwsEnabled $true
```

Verify the change:

```powershell
Get-OrganizationConfig | Select-Object EwsEnabled
```

### Step 4: Validate app functionality
- Re-run your app's connection test.
- Confirm mail flow, calendar sync, and free/busy lookups.
- Monitor for 24–48 hours before declaring victory.

### Step 5: Plan your migration
Re-enabling buys time — it is **not** a long-term solution. Map each EWS app to a Microsoft Graph equivalent (Graph Mail, Calendar, Contacts APIs) and set a hard migration deadline.

## Common Issues, Risks, and What You Should Know

Re-enabling EWS is a stopgap with real trade-offs. Here's what to weigh:

| Factor | Re-Enable EWS | Migrate to Graph |
|---|---|---|
| Time to fix | Minutes | Weeks–months |
| Long-term support | Deprecated | Actively supported |
| Security posture | Legacy auth concerns | Modern auth, granular scopes |
| Effort | Low | High (code changes) |
| Recommended for | Emergency bridge | Permanent solution |

**Watch out for:**
- **Throttling:** Re-enabled EWS is still subject to stricter throttling limits than before retirement. Batch operations may fail.
- **New tenants:** Some newly provisioned tenants may not have the re-enable option at all — check Message Center first.
- **Auth changes:** Basic auth is gone; ensure apps use OAuth 2.0 or they'll still fail.
- **Third-party lag:** Vendors may not have shipped Graph support yet — pressure them with a timeline.

**Alternatives to consider:** If your app only needs mail send/receive, evaluate SMTP AUTH or Graph. For calendar-heavy workflows, Graph's `calendarView` endpoint is the direct replacement.

## Frequently Asked Questions (FAQ)

### Can I re-enable EWS permanently in Exchange Online?
No. Microsoft positions the re-enable as a temporary remediation for tenants with active dependencies. EWS remains deprecated, and you should migrate to Microsoft Graph on a defined timeline.

### Why did my EWS app stop working after the retirement?
Microsoft disabled EWS by default for Exchange Online. Apps using legacy EWS calls — especially those still on basic authentication — fail with 401/403 errors until EWS is re-enabled and OAuth is configured.

### Do I need a specific license to re-enable EWS?
No special license is required. Any Exchange Online admin with the appropriate role can run `Set-OrganizationConfig -EwsEnabled $true`, provided the tenant qualifies for the re-enable path.

### What replaces EWS for mail and calendar access?
Microsoft Graph is the official replacement, covering Mail, Calendar, Contacts, and more with modern OAuth 2.0 authentication and granular permission scopes.

## Final Verdict

If a critical EWS app broke, **re-enable EWS now** using `Set-OrganizationConfig -EwsEnabled $true` to restore service — but treat it as an emergency bridge, not a destination. Immediately inventory every EWS dependency, pressure third-party vendors for Graph support, and set a firm migration deadline (90–180 days is realistic). Admins who re-enable and forget will face the same outage again when Microsoft tightens the screws. Fix it today, migrate it this quarter.