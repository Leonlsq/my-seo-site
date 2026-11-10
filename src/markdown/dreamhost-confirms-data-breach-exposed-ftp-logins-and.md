---
title: "DreamHost Breach: How to Secure FTP & Webmail Now"
description: "DreamHost breach exposed FTP and webmail logins. Follow this step-by-step guide to rotate credentials, lock down SFTP, and secure webmail today."
pubDate: 2026-11-05
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## DreamHost Breach: What Was Exposed and How to Lock Down Your Account

DreamHost confirmed that attackers accessed its File Manager platform for roughly two months and stole customers' FTP/SFTP usernames and passwords, plus webmail session data. If you host anything on DreamHost, treat every FTP and webmail credential as compromised **right now** — not "if you notice suspicious activity." The direct takeaway: rotate your FTP/SFTP passwords, force-logout all webmail sessions, enable SFTP-only access, and audit your account for unauthorized files or mail rules. This guide walks you through each step in the exact order you should do them.

### What we know about the breach

- **Attack vector:** Unauthorized access to DreamHost's File Manager platform.
- **Duration:** Approximately two months before detection and disclosure.
- **Data stolen:** FTP/SFTP usernames and passwords, plus webmail session information.
- **Why it matters:** FTP credentials are the keys to your file system. With them, an attacker can upload malware, deface sites, exfiltrate databases, or pivot to other services where you reused the same password.

## Step-by-Step: Secure Your DreamHost Account After the Breach

Do these in order. Steps 1–3 are urgent; steps 4–7 are hardening.

### Step 1: Change every FTP/SFTP password immediately

1. Log into the DreamHost panel → **Manage Websites** → select your domain → **Users** → **FTP Users**.
2. For each FTP user, click **Change Password** and set a unique 20+ character password from a password manager (Bitwarden, 1Password, KeePassXC).
3. **Do not reuse** any password that was ever stored in DreamHost's File Manager. Assume it's in an attacker's wordlist.
4. If you have multiple domains or sub-accounts, repeat for every FTP user — attackers harvest the whole list, not just your primary site.

### Step 2: Kill all active webmail sessions

Stolen webmail session tokens can let an attacker read mail without your password. Force them out:

1. In the DreamHost panel, go to **Mail** → **Manage Mail**.
2. Open each mailbox and use **Change Password** — this invalidates existing sessions tied to that account.
3. In webmail itself, check **Settings → Sessions** (Roundcube/Horde vary) and terminate unknown devices.
4. Review **mail filters and forwarding rules** for anything you didn't create. Attackers commonly add a silent forward to exfiltrate password-reset emails.

### Step 3: Audit your file system for tampering

1. Connect via **SFTP** (not plain FTP) and check your web root for unfamiliar files, especially `.php` files with obfuscated code, recently modified timestamps, or odd names like `wp-config.bak.php`.
2. Compare against a backup or your last known-good deploy.
3. Check `.htaccess` for injected redirects and `cron` entries in the panel for unauthorized scheduled tasks.

### Step 4: Disable plain FTP entirely

Plain FTP sends credentials in cleartext. Switch to SFTP or FTPS:

| Protocol | Encrypted? | Port | Recommendation |
|---|---|---|---|
| FTP | No | 21 | Disable |
| FTPS (explicit) | Yes (TLS) | 21 | Acceptable |
| SFTP (SSH) | Yes | 22 | **Best choice** |
| File Manager (web) | Yes (HTTPS) | 443 | Use with 2FA |

In the DreamHost panel, remove or restrict FTP users you don't actively need. Fewer credentials = smaller attack surface.

### Step 5: Enable two-factor authentication

Turn on 2FA for your DreamHost panel account (**Profile → Security**). This blocks panel takeover even if a password leaks, and it's the single highest-impact change you can make.

### Step 6: Rotate passwords on anything reused

If your FTP password matched your email, registrar, or database password, change those too. Credential stuffing attacks chain reused passwords across services within hours.

### Step 7: Monitor for a few weeks

Watch access logs for logins from unfamiliar IPs, unexpected file changes, and mail-forwarding rules. Set up login notifications if available.

## Common Issues and What You Should Know

- **"I can't find the FTP password field."** DreamHost moved FTP user management under **Manage Websites → Users**. Legacy panel paths differ; use the search bar in the panel.
- **"My site broke after changing the password."** Any deploy script, CI/CD pipeline, or backup tool using the old FTP credentials will fail. Update stored credentials in GitHub Actions secrets, your local FTP client, and any WordPress plugins (e.g., backup plugins) that authenticate over FTP.
- **"Was my password hashed?"** DreamHost has not publicly detailed hashing specifics for the stolen FTP credentials; assume they are usable and rotate regardless.
- **Alternatives to FTP entirely:** Consider Git-based deploys, SFTP with key-based auth, or DreamHost's SSH access — all eliminate stored passwords.
- **Cost of inaction:** A compromised FTP account can lead to site defacement, SEO poisoning, malware distribution, and Google Safe Browsing blacklisting — recovery costs far exceed the 15 minutes this guide takes.

## Frequently Asked Questions (FAQ)

### Was my DreamHost account affected by the data breach?
DreamHost has not published a per-account list, but the breach exposed FTP/SFTP credentials and webmail sessions broadly across the File Manager platform. Treat your account as affected and rotate credentials now rather than waiting for a notification email.

### Should I switch from FTP to SFTP after the DreamHost breach?
Yes. SFTP encrypts credentials and data in transit, so a future credential capture is far less damaging. Disable plain FTP users you don't need and connect over SFTP (port 22) or FTPS.

### Do I need to change my DreamHost panel password too?
Change it as a precaution, and enable two-factor authentication immediately. The confirmed exposure centers on FTP and webmail, but rotating the panel password and turning on 2FA closes the most dangerous escalation path.

### How do I know if an attacker already used my stolen FTP login?
Check your access logs for logins from unknown IPs or unusual hours, scan your web root for modified or new files, and inspect mail filters for unauthorized forwarding rules. If you find anything, restore from a clean backup and re-run the steps above.

## Final Verdict

Don't wait for DreamHost to tell you your specific account was hit — the exposure window was two months, which is more than enough time for stolen FTP credentials to be tested and weaponized. Spend the next 15 minutes rotating every FTP/SFTP password, forcing webmail session resets, and enabling 2FA. Then permanently move to SFTP with key-based auth and stop storing plain FTP credentials anywhere. The breach is the warning; your credential hygiene is the fix.