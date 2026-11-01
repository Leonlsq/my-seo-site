---
title: "OpenAI Account Hijack: How to Check If You're at Risk"
description: "Learn how the Parameter AI team hijacked ChatGPT accounts and get a step-by-step security audit to protect your OpenAI login today."
pubDate: 2026-11-01
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## OpenAI Account Hijack: What Actually Happened and How to Secure Your Login

If you saw the headline "Do the math: How we took over ChatGPT accounts" trending on Hacker News (316 points, 157 comments), you probably want one thing: to know whether *your* account is exposed. Here's the short answer — the vulnerability Parameter AI disclosed was a **logic and authentication-flow gap**, not a password leak. That means your password was never the weak link. The attack surface was the account-linking and session layer. Below is a practical, step-by-step security audit you can run in under 15 minutes to confirm you're not exposed.

The core takeaway: **treat your OpenAI account like a financial account, not a social login.** Rotate sessions, audit connected apps, and enable the strongest MFA available.

## Step-by-Step: Audit Your OpenAI Account Security (15 Minutes)

Work through these in order. Each step maps to a class of vulnerability that account-hijack write-ups typically exploit.

### 1. Force-logout all active sessions
- Go to **ChatGPT → Settings → Data Controls → Log out of all devices** (or the equivalent session management panel).
- This invalidates any stolen session token or lingering OAuth session an attacker may hold.
- Do this **immediately** if you've clicked any unfamiliar "Sign in with OpenAI" prompt.

### 2. Enable and verify MFA
| Method | Security Level | Notes |
|---|---|---|
| SMS code | Low | Vulnerable to SIM-swap; use only as fallback |
| Authenticator app (TOTP) | High | Recommended baseline |
| Passkey / hardware key | Highest | Phishing-resistant; best against session-replay attacks |

- Go to **Settings → Security → Multi-factor authentication** and enroll a TOTP app (Google Authenticator, Authy, 1Password).
- If passkeys are offered in your region, **use them**. Passkeys defeat the exact class of redirect/session attacks that account-takeover research tends to target.

### 3. Audit connected apps and OAuth grants
- Review any third-party service you authorized via "Sign in with ChatGPT/OpenAI."
- **Revoke anything you don't recognize.** OAuth scope abuse is the most common real-world account-takeover vector.
- Check your email inbox for "new sign-in" or "app authorized" alerts from the last 90 days.

### 4. Lock down your email (the real master key)
- Your OpenAI account is only as strong as the email behind it. Enable MFA on that inbox too.
- Check for forwarding rules or filters you didn't create — attackers use these to silently intercept password resets.

### 5. Review billing and API keys
- Go to **platform.openai.com → API keys** and **revoke any key you don't actively use**.
- Check **Billing → Usage** for unexpected spikes, which indicate a compromised key being resold.

## Common Issues, Alternatives, and What You Should Know

**Was this a bug OpenAI patched, or an ongoing risk?** Disclosure write-ups like Parameter AI's typically describe a *responsibly reported* gap. Assume it's been addressed, but harden your account anyway — the same patterns recur.

**I can't find "log out of all devices."** The setting location shifts between ChatGPT web, mobile, and the API platform. If it's missing on mobile, use the **web interface** — session controls are most complete there.

**Should I switch to a different AI provider?** Not necessary for security alone. Every major LLM provider faces identical OAuth/session risks. The fix is account hygiene, not migration. That said, if you use multiple AI tools, **never reuse passwords** across them.

**Red flags you were targeted:**
- Unexpected "verify your identity" emails
- New API keys you didn't create
- Chat history containing prompts you never sent
- Billing charges for models you don't use

**Pro tip — compartmentalize:** Use a dedicated email alias for AI accounts so a breach in one service can't cascade into your primary inbox.

## Frequently Asked Questions (FAQ)

### How did the Parameter AI team take over ChatGPT accounts?
According to the disclosure, the researchers exploited a **logic/authentication-flow gap** in OpenAI's account system rather than stealing passwords. The exact technical chain is documented in their write-up at parameter.ai/labs. The practical lesson for users is that session and OAuth hygiene matters more than password complexity alone.

### Is my ChatGPT account safe right now?
If you have **MFA enabled, no unknown connected apps, and no unfamiliar API keys**, you're in good shape. Run the 5-step audit above to confirm. If you've never checked your connected apps, do it today — that's the highest-risk blind spot for most users.

### Does enabling MFA stop account hijacking?
MFA stops credential-stuffing and password theft, but **phishing-resistant methods (passkeys/hardware keys) are required** to stop session-replay and redirect-based attacks. TOTP is a strong baseline; passkeys are the gold standard.

### Do I need to change my ChatGPT password?
Changing your password is a good habit after any account-takeover news, but **revoking active sessions and connected apps is more important**. A new password won't help if a stolen session token is still valid — that's why step 1 is force-logout.

## Final Verdict

Don't panic — but don't ignore it either. The Parameter AI disclosure is a reminder that **account security lives at the session and OAuth layer**, not just the password field. Spend 15 minutes today: force-logout everywhere, enable passkeys or TOTP, revoke unknown apps, and audit your API keys. That checklist neutralizes the realistic attack surface this story highlights. Bookmark this guide and re-run the audit every 90 days — or any time a major AI account-security story breaks.