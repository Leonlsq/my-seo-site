---
title: "How to Run the 'Ram Altman' Linux Script Safely"
description: "Learn how to install, configure, and safely run the 'Ram Altman' Linux script that emails Sam Altman a daily report of your PC's unused RAM."
pubDate: 2026-11-08
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What Is the "Ram Altman" Script and Should You Actually Run It?

The "Ram Altman" script is a viral Linux shell utility that detects how much unused RAM your machine has and automatically emails a daily report to Sam Altman's inbox. It's a joke about OpenAI's aggressive memory demands, but it's also a real, functional script that touches your SMTP credentials, cron scheduler, and outbound network traffic. If you want to run it for fun, you need to understand exactly what it does before you hand it your email password. This guide gives you a safe, sandboxed setup, a full configuration walkthrough, and the troubleshooting steps most tutorials skip.

The short answer: yes, you can run it, but **never use your primary email account**, and **always test it with a dry-run flag first**. Below is the exact process.

## Step-by-Step: Installing and Configuring "Ram Altman" Safely

### Step 1: Inspect the Script Before Running It

Never pipe a viral script straight into `bash`. Download it first and read the source.

```bash
git clone https://github.com/<repo>/ram-altman.git
cd ram-altman
cat ram_altman.sh
```

Look for three things: the SMTP host it connects to, the recipient address (it should be a placeholder you edit, not a hardcoded address), and any `curl`/`wget` calls that exfiltrate data elsewhere.

### Step 2: Create a Throwaway Email Account

Use a dedicated mailbox — a fresh Gmail, ProtonMail, or a self-hosted address. For Gmail, you must generate an **App Password** (Google Account → Security → 2-Step Verification → App Passwords). Your normal password will not work with SMTP.

### Step 3: Configure the Environment File

The script reads from a `.env` file. Populate it with these values:

| Variable | Example Value | Notes |
|---|---|---|
| `SMTP_HOST` | `smtp.gmail.com` | Use port 587 with STARTTLS |
| `SMTP_PORT` | `587` | 465 for implicit TLS |
| `SMTP_USER` | `yourthrowaway@gmail.com` | App Password required |
| `SMTP_PASS` | `abcd efgh ijkl mnop` | Never commit this file |
| `RECIPIENT` | `sam@openai.com` | Verify the current public address |
| `DRY_RUN` | `true` | Set to `false` only after testing |

Lock down permissions immediately:

```bash
chmod 600 .env
```

### Step 4: Run a Dry-Run Test

```bash
DRY_RUN=true ./ram_altman.sh
```

The dry run prints the RAM report to stdout without sending mail. Confirm the RAM figure matches `free -h` output before proceeding.

### Step 5: Schedule It with Cron

```bash
crontab -e
```

Add one line for a daily 9 AM report:

```
0 9 * * * /home/user/ram-altman/ram_altman.sh >> /home/user/ram-altman/ram.log 2>&1
```

### Step 6: Verify Delivery

Check `ram.log` for a `250 OK` SMTP response. If you see `535 Authentication Failed`, your App Password is wrong or 2FA isn't enabled.

## Common Issues, Security Risks, and Better Alternatives

**Issue 1: `smtp: command not found`.** The script depends on `msmtp` or `sendmail`. Install with `sudo apt install msmtp msmtp-mta` (Debian/Ubuntu) or `sudo dnf install msmtp` (Fedora).

**Issue 2: Gmail blocks the connection.** Google flags automated logins from unknown IPs. If you're on a VPS, use a transactional provider like Mailgun or SendGrid's free tier instead.

**Issue 3: The script reports wrong RAM.** It likely parses `free -m` and ignores buffers/cache. The accurate command is `free -h` or `awk '/MemAvailable/{print $2}' /proc/meminfo` — the latter is the true "unused" figure Linux admins trust.

**Security reality check:** You are storing SMTP credentials in plaintext on disk and granting a third-party script outbound mail access. A compromised repo could silently change the recipient or add a BCC. Mitigations:

- Run it inside a container with `--network` restricted to your SMTP host.
- Use a dedicated low-privilege user account, not root.
- Audit the script's git history before every `git pull`.

**Alternatives if you just want the joke without the risk:**

- **Manual one-liner:** `free -h | mail -s "RAM report" sam@openai.com` — no third-party code.
- **A local dashboard:** Grafana + Prometheus gives you real RAM telemetry without emailing anyone.
- **A satirical cron job:** Print the report to your terminal with `watch -n 60 'free -h'` — zero credentials, zero risk.

## Frequently Asked Questions (FAQ)

### Is the "Ram Altman" script safe to run on my main Linux machine?
It's safe *only* if you use a throwaway email account, verify the source code, and run it as a non-root user. The core risk is credential exposure, not the RAM-reading logic itself.

### Does the script actually email Sam Altman, and will he read it?
The script sends mail to whatever address you configure. Whether it reaches a monitored inbox depends on OpenAI's spam filters — realistically, automated mail to a public figure is filtered or ignored. Treat it as a novelty, not a communication channel.

### How do I uninstall the "Ram Altman" script completely?
Remove the cron entry with `crontab -e`, delete the cloned directory with `rm -rf ram-altman`, and revoke the App Password in your email provider's security settings. Also delete the `.env` file — it holds your credentials.

### Why does the script report more unused RAM than `free -h` shows?
It probably reads only `MemFree` and ignores `MemAvailable` (which includes reclaimable cache). Use `grep MemAvailable /proc/meminfo` for the accurate figure.

## Final Verdict

Run the "Ram Altman" script for the meme, but run it **sandboxed, with a throwaway mailbox, and a dry-run first**. If you want the same joke with none of the credential risk, the one-line `free -h | mail` command delivers 90% of the fun. The real takeaway is practical: learn how `MemAvailable` works, set up a proper monitoring stack, and stop trusting viral scripts with your SMTP password.