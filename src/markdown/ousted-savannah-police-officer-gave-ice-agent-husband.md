---
title: "Flock Safety Audit: How to Check Who Accessed Your Data"
description: "Learn how to audit Flock Safety camera access logs, spot unauthorized sharing, and harden your ALPR deployment after the Savannah access scandal."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Audit Flock Safety Access Logs After the Savannah Scandal

The Savannah Police Department incident—where an ousted officer allegedly gave her ICE agent husband access to the city's Flock Safety license plate reader (LPR) system—has triggered a wave of audits across agencies and neighborhoods running automated license plate recognition (ALPR) cameras. If you're a city IT admin, a police records supervisor, or a neighborhood HOA board member, the question you're now Googling is simple: **how do I check who has accessed our Flock data, and how do I lock it down?**

The short answer: Flock Safety logs every login, search, and data-share event, but the logs are only useful if someone actually reviews them. Below is a concrete, step-by-step audit workflow you can run today, plus the access-control settings that would have blocked the Savannah scenario in the first place.

## Step-by-Step: Auditing Flock Access and Sharing Permissions

Flock's platform (the "Flock Portal" / FlockOS) is role-based. Auditing means checking three surfaces: **users, shares, and search history.**

### Step 1 — Pull the active user roster
1. Log in to the Flock Portal with an **admin-level account** (not a standard operator).
2. Navigate to **Settings → User Management** (labeling varies slightly by contract version).
3. Export the full user list. For each account, record:
   - Name and email
   - Role (Admin, Operator, Viewer)
   - Last login timestamp
   - MFA status (enabled/disabled)

**Red flag:** any account with Admin rights that isn't a named, current employee. In the Savannah case, the core failure was an *external* person (a federal agent) gaining access through a credentialed insider.

### Step 2 — Review data-sharing agreements
Flock allows agencies to share camera feeds and search access with partner agencies. Audit this under **Settings → Sharing / Network**.
- List every agency your system shares with.
- Confirm each share has a **written MOU (memorandum of understanding)** on file.
- Check whether sharing is **bidirectional** (they can search your data) or **one-way** (you only see theirs).

### Step 3 — Export the search/audit log
1. Go to the **Audit Log** or **Search History** section.
2. Set the date range to the last 90 days (or full contract term).
3. Export to CSV. Filter for:
   - Searches run by accounts outside your agency
   - Searches outside normal shift hours
   - Bulk or repeated queries on the same plate

### Step 4 — Reconcile against HR records
Cross-reference every admin/operator account against your current personnel roster. **Terminated employees must have accounts deactivated the same day**—this is the exact gap that let an ousted officer retain or hand off access.

### Step 5 — Enforce MFA and least privilege
- Require **multi-factor authentication** for all accounts (Flock supports MFA; enforce it org-wide).
- Downgrade anyone who doesn't need Admin to **Operator** or **Viewer**.
- Remove dormant accounts (no login in 60+ days).

## Common Issues, Alternatives, and What You Should Know

### The "insider handoff" problem
No vendor can fully prevent a credentialed user from sharing a password or screen-sharing a live session. The Savannah incident is a **policy and monitoring failure**, not necessarily a software bug. Mitigations:

| Control | What It Stops | Effort |
|---|---|---|
| MFA enforcement | Password sharing / credential theft | Low |
| Per-user audit logs | Unattributed searches | Low |
| IP/device allowlisting | Off-site logins | Medium |
| Quarterly access reviews | Dormant/rogue accounts | Medium |
| Contractual MOU checks | Unauthorized agency sharing | High |

### Questions to ask your Flock rep
- Does our contract log **who searched what, when, and from which IP**?
- Can we restrict logins to a **specific IP range** (e.g., department network only)?
- Are **federal agencies** able to query our data by default, or only via an explicit share?
- What's the **retention period** on audit logs?

### Alternatives to consider if trust is the issue
- **Axon Fusus** and **Motorola** offer ALPR with tighter integration to existing evidence systems.
- **Open-source / self-hosted LPR** (e.g., OpenALPR derivatives) gives you full log ownership but shifts all security burden to your team.
- **Contract renegotiation** is often cheaper than switching: demand audit-log export rights and MFA as contractual terms.

### For HOAs and private neighborhoods
If your community runs Flock cameras, you typically **don't** have portal access—the partnering police department does. Request a written summary of who can access your cameras and under what sharing terms, and ask for the audit log on a quarterly basis.

## Frequently Asked Questions (FAQ)

### Can a police officer give a family member access to Flock cameras?
No—Flock accounts are individually credentialed and tied to an agency. Sharing login credentials or granting an unauthorized person access violates most agency policies and the vendor's terms of service, and can constitute a criminal or administrative offense. The Savannah case is under investigation precisely because this is prohibited.

### How do I check who has accessed my Flock Safety data?
Admins can export the **audit log / search history** from the Flock Portal, which records user, timestamp, and query details. Cross-reference it against your current user roster and any external sharing agreements. If you lack admin access, request the export from the agency or account owner in writing.

### Does Flock Safety share data with ICE or federal agencies?
Flock does not automatically hand data to federal agencies. Sharing happens through **agency-to-agency agreements** configured by the local agency. Whether federal agents can query your data depends entirely on the shares your department has authorized—so audit the Sharing settings, not just the vendor's marketing.

### What is the retention period for Flock ALPR data?
Flock's default retention is typically **30 days** for plate reads, though this is configurable by contract (some agencies set 7, 14, or 60 days). Audit logs may be retained longer. Confirm your specific retention window with your account representative, since shorter retention limits exposure but also limits investigations.

### How often should agencies audit Flock access?
Best practice is a **quarterly access review** plus an **immediate review after any personnel termination**. High-risk agencies (those sharing with multiple partners) should review monthly.

## Final Verdict

The Savannah incident is a wake-up call, not a reason to rip out every camera. **If you run Flock—or any ALPR—treat access auditing as a mandatory quarterly task, not a one-time setup.** Enforce MFA, enforce least privilege, deactivate terminated accounts the same day, and demand audit-log export rights in your contract. For HOAs and private users, get written confirmation of who can access your feeds. The technology isn't the weak link here—the access controls around it are, and those are fixable in an afternoon.