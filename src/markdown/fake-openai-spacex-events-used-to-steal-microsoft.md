---
title: "Fake OpenAI, SpaceX Event Phishing: How to Check if You're Hacked"
description: "Fake OpenAI, SpaceX, and Anthropic event invites are stealing Microsoft and Google accounts. Learn how to detect token theft, revoke sessions, and lock down MFA."
pubDate: 2026-11-06
tags: ['Tech', 'Guide', 'Troubleshooting', 'Cybersecurity']
---

## Fake OpenAI & SpaceX Event Phishing: How to Tell If Your Microsoft or Google Account Is Already Compromised

A wave of phishing campaigns is using fake OpenAI, SpaceX, and Anthropic "exclusive event" invitations to steal Microsoft 365 and Google Workspace credentials—and worse, the authentication session tokens that let attackers bypass your password entirely. The tell: victims often report no password change and no MFA prompt, yet their inbox, files, and calendar are already being accessed. This guide cuts past the news and gives you the exact checks, revocation steps, and hardening settings to confirm whether you're affected and close the door on token theft.

The core attack relies on **phishing-as-a-service (PhaaS)** kits that proxy the real Microsoft or Google login page in real time. When you enter your password and complete MFA, the kit captures the resulting session cookie (an `ESTSAUTH`/`ESTSAUTHPERSISTENT` cookie for Microsoft, or `SID`/`SSID` cookies for Google) and replays it from the attacker's infrastructure. That's why "I changed my password" alone does not kick them out—**you must revoke active sessions**, not just reset credentials.

## Step-by-Step: Confirm and Eject an Attacker

Work through these in order. Steps 1–3 diagnose; steps 4–7 remediate.

1. **Check Microsoft sign-in logs (Entra ID).** Go to **entra.microsoft.com → Monitoring → Sign-in logs**. Filter **Status = Success** and scan for:
   - Sign-ins from countries or IPs you don't recognize.
   - **Authentication requirement = Single-factor authentication** on accounts that should require MFA.
   - **Client app = "Browser"** with unusual user agents (e.g., `python-requests`, `curl`, headless Chrome).
   - A burst of sign-ins within seconds of each other from different geolocations (session replay signature).
2. **Check Google Workspace / personal Google activity.** Visit **myaccount.google.com → Security → Recent security activity** and **"Your devices."** Look for sessions you don't recognize, especially on devices you've never used. Personal accounts: **myaccount.google.com/deviceactivity**.
3. **Check for rogue mailbox rules and OAuth apps.** Attackers love persistence. In Microsoft 365: **Outlook → Settings → Mail → Rules** and **entra.microsoft.com → Enterprise applications → Consent**. In Google: **myaccount.google.com/permissions** for third-party access, and Gmail **Settings → Filters and Blocked Addresses**. Delete anything you didn't create—forwarding rules to external addresses are a red flag.
4. **Revoke all sessions (Microsoft).** In **entra.microsoft.com → Users → [user] → Revoke sessions**, or have the admin run:
   ```
   Revoke-AzureADUserAllRefreshToken -ObjectId <user-object-id>
   ```
   (or the Microsoft Graph equivalent `POST /users/{id}/revokeSignInSessions`). This invalidates refresh tokens so replayed cookies die.
5. **Revoke all sessions (Google).** Go to **myaccount.google.com → Security → Your devices → Manage all devices** and sign out of every session. For Workspace admins, use the Admin console to **reset sign-in cookies** for the user.
6. **Reset the password and re-enroll MFA.** Do this *after* revoking sessions, and use a fresh device if you suspect the original is infected.
7. **Scan the endpoint.** Run a full antivirus/EDR scan—PhaaS kits sometimes pair with infostealers that grab cookies locally.

### Quick Reference: Where the Evidence Lives

| Platform | Session/Token Log | Revoke Action | Persistence Check |
|---|---|---|---|
| Microsoft 365 | Entra ID → Sign-in logs | Revoke sessions / `revokeSignInSessions` | Mailbox rules, OAuth consent |
| Google Workspace | Admin console → Security → Investigation tool | Reset sign-in cookies | Gmail filters, third-party access |
| Personal Google | myaccount.google.com/deviceactivity | "Sign out of all devices" | Connected apps |

## Common Issues, Alternatives, and What You Should Know

**"I have MFA—how did they get in?"** MFA stops password-only attacks, but **adversary-in-the-middle (AiTM) phishing** proxies your MFA in real time. The session token is the prize, not the password. This is why **phishing-resistant MFA** matters: FIDO2 security keys and passkeys are bound to the real origin, so a proxy site can't replay them.

**"Password reset didn't help."** Correct—and expected. A reset kills the password but not always the refresh token. Always pair a reset with **explicit session revocation**.

**Hardening checklist that actually blocks this campaign:**
- Enforce **FIDO2/passkeys** or **number-matching** MFA; deprecate SMS.
- Enable **Conditional Access** to block legacy auth and require compliant devices.
- Turn on **token protection** (Microsoft) and **Google's Advanced Protection Program** for high-risk users.
- Deploy **link isolation** / Safe Links to detonate suspicious "event invite" URLs.
- Train staff: no legitimate OpenAI, SpaceX, or Anthropic event will ask you to log into Microsoft or Google through an emailed link.

**Alternatives to consider if you're a small team without Entra ID P1:** Microsoft 365 Business Premium includes Conditional Access basics; Google Workspace's built-in security center covers session management. Free tiers still allow manual session revocation—use it.

## Frequently Asked Questions (FAQ)

### How do I know if a fake OpenAI or SpaceX invitation compromised my account?
Check sign-in logs for unfamiliar IPs/countries, single-factor sign-ins, and bursts of activity. Then review mailbox rules and connected apps for anything you didn't create. If you see a forwarding rule to an external address or an unknown OAuth app, assume compromise and revoke sessions immediately.

### Does changing my password remove a hacker who stole my session token?
Not reliably. Session/refresh tokens can survive a password reset. You must explicitly **revoke all sessions** (Entra ID "Revoke sessions" or Google "Sign out of all devices") to invalidate the stolen cookie.

### Can MFA be bypassed by these phishing kits?
Yes—via adversary-in-the-middle proxying that captures the session cookie after you complete MFA. Phishing-resistant methods like FIDO2 security keys and passkeys are the reliable fix because they're cryptographically bound to the legitimate domain.

### What cookies do attackers steal in Microsoft and Google phishing?
For Microsoft, the `ESTSAUTH` and `ESTSAUTHPERSISTENT` authentication cookies; for Google, the `SID`, `HSID`, and `SSID` session cookies. Replaying these grants access without a password or MFA prompt.

## Final Verdict

Don't wait for a breach notification. **Right now**, open your Microsoft sign-in logs and Google device activity, revoke every session you don't recognize, and check for rogue mailbox rules and OAuth consents. Then make the structural fix: move high-value accounts to **phishing-resistant MFA (FIDO2/passkeys)** and enable Conditional Access. The fake-event lure will keep evolving—OpenAI, SpaceX, Anthropic today, something else next quarter—but token theft fails the moment your authentication can't be proxied. Treat "event invitation" emails that route you to a login page as hostile by default, and you'll neutralize this entire campaign class.