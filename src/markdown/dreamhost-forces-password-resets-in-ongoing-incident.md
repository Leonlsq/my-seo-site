---
title: "DreamHost Password Reset: How to Fix Email & FTP Login Fast"
description: "DreamHost forced email and FTP/SFTP password resets after a File Manager incident. Here's how to restore access, update clients, and secure your account."
pubDate: 2026-10-27
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## DreamHost Forced a Password Reset? Here's How to Get Back Into Email and FTP

If your DreamHost email suddenly stopped syncing or your FTP client started throwing "530 Login Authentication Failed" errors, you're not alone — and you probably didn't get hacked. DreamHost has proactively forced password resets for **email and FTP/SFTP users** after an "incident" that disrupted connections to the File Manager interface. The company reset credentials as a precaution, which means your old password is now dead everywhere it was saved.

The direct takeaway: **you must set a new password once, then update every device and app that stored the old one.** This guide walks you through the fix in order — webmail, email clients, FTP/SFTP tools, and the security steps most users skip.

## Step-by-Step: Restore Access After the DreamHost Reset

Work through these steps in order. Skipping ahead to your FTP client before resetting the password in the panel will just loop you through auth failures.

### Step 1: Reset the password in the DreamHost panel
1. Log in at **panel.dreamhost.com** using your *account* (dashboard) credentials — these are separate from your mailbox passwords.
2. Go to **Manage Users** (or **Mailboxes** under the Mail menu) for email addresses, or **Manage Users → FTP/SFTP** for file access users.
3. Select the affected user and click **Change Password**.
4. Generate a strong, unique password — 16+ characters, mixed case, numbers, symbols. Do **not** reuse your old one.
5. Save it in a password manager immediately. DreamHost will not email you the new password.

### Step 2: Update your email clients
The reset breaks the saved credential in every mail app. Update each one:

| Client | Where to change the password |
|---|---|
| Apple Mail (macOS/iOS) | Settings → Mail → Accounts → [account] → Password |
| Outlook (desktop) | File → Account Settings → double-click account → Password field |
| Gmail app (IMAP) | Settings → Add account → re-enter credentials |
| Thunderbird | Right-click account → Settings → Server Settings → password prompt |

**Server settings to confirm while you're in there:**
- **IMAP:** `imap.dreamhost.com`, port **993**, SSL/TLS
- **POP3:** `pop.dreamhost.com`, port **995**, SSL/TLS
- **SMTP:** `smtp.dreamhost.com`, port **465** (SSL) or **587** (STARTTLS)
- **Username:** your **full email address** (e.g., `you@yourdomain.com`), not just the mailbox name

### Step 3: Fix FTP/SFTP clients
For SFTP users, the host is typically `yourdomain.com` or the server hostname shown in the panel, port **22**. For FTPS, port **21** with explicit TLS. Update the stored password in:

- **FileZilla:** Site Manager → select site → Edit → update password → reconnect.
- **Cyberduck:** Bookmark → Edit → Password field.
- **WinSCP:** Session → Stored sessions → Edit → Password.
- **VS Code SFTP extensions:** update the `sftp.json` config or the extension's credential store.

If you still get `530 Login incorrect` after updating, delete the saved site profile entirely and recreate it — cached credentials sometimes survive an edit.

### Step 4: Re-authenticate connected apps and scripts
Anything that authenticates with your mailbox or FTP credentials will fail silently until updated:
- WordPress SMTP plugins (WP Mail SMTP, etc.)
- Backup plugins that push via SFTP
- Contact forms using authenticated SMTP
- Cron jobs or deployment scripts with hardcoded credentials — **move these to environment variables** while you're fixing them

## Common Issues and What You Should Know

**"My password reset link doesn't work."** DreamHost's reset flow is initiated from the panel, not via email link for mailbox users. If you're locked out of the *panel* itself, use the account recovery flow on the login page.

**"Email still won't sync after updating."** Force a re-sync: remove and re-add the account on mobile, or rebuild the profile in desktop clients. Some clients cache OAuth tokens that need clearing.

**"Was my data compromised?"** DreamHost framed this as a precautionary reset tied to an incident affecting File Manager connectivity. Treat your old password as exposed regardless — if you reused it anywhere (banking, social, shopping), change it there too. This is the single most important step.

**Enable 2FA now.** Go to **Panel → Security → Two-Factor Authentication**. A forced reset is the perfect moment to lock the account down properly.

**Alternatives if you're rethinking providers:** If repeated forced resets are a dealbreaker, compare against **SiteGround** (stronger default mail security tooling) or **Cloudflare Email Routing** (free forwarding, no mailbox passwords to leak). For pure FTP/SFTP workflows, most hosts now push SFTP-only — verify yours supports it before migrating.

## Frequently Asked Questions (FAQ)

### Why did DreamHost force a password reset for email and FTP users?
DreamHost reset email and FTP/SFTP credentials as a precautionary security measure after an incident that disrupted File Manager connections. The reset invalidates potentially exposed credentials, which is why all saved passwords stopped working at once.

### How do I fix "530 Login Authentication Failed" on DreamHost FTP?
Reset the password in the DreamHost panel under Manage Users → FTP/SFTP, then delete and recreate the saved site in your FTP client (FileZilla, Cyberduck, WinSCP) with the new password. Confirm you're using the full username and port 22 for SFTP.

### Do I need to change my DreamHost panel (dashboard) password too?
Not necessarily — the forced reset targets mailbox and FTP/SFTP users. However, if you reused the old password on your dashboard account, change it immediately and enable two-factor authentication under Panel → Security.

### Will my email be deleted after the password reset?
No. The reset only invalidates credentials; your stored mail, folders, and settings remain intact. Once you enter the new password in your mail client, messages sync normally.

## Final Verdict

Don't panic — this is a **credential reset, not a data loss event**. The fastest path back online is: reset in the panel → update mail clients → update FTP/SFTP tools → purge any hardcoded credentials from scripts. Budget 15–20 minutes if you have one mailbox and one FTP site; longer if you run multiple domains or WordPress installs with SMTP plugins.

The non-negotiable follow-up: **change the old password anywhere you reused it and turn on 2FA today.** A forced reset is a warning shot — treat it like one.