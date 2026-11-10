---
title: "OpenSSH + musl-libc Flaw: How to Patch Alpine Linux Now"
description: "Fix the combined OpenSSH and musl-libc auth bypass on Alpine Linux. Step-by-step patch commands, detection checks, and hardening tips inside."
pubDate: 2026-11-06
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## The OpenSSH + musl-libc Auth Bypass: What Actually Happened and How to Fix It

If you run Alpine Linux (or any musl-based distro) with OpenSSH exposed to the internet, you need to act today. A chained vulnerability—one flaw in OpenSSH's authentication handling combined with a memory-handling bug in musl-libc's `strlen`/comparison path—allows a remote attacker to bypass password authentication entirely by submitting a password string longer than 256 characters. In practice: **type anything over 256 characters as the password, and you're in as `root`** (assuming root password auth is enabled). This guide gives you the exact commands to detect exposure, patch, and lock down the box before someone else finds it.

> **TL;DR:** Run `apk update && apk upgrade openssh musl`, restart `sshd`, and disable `PasswordAuthentication` / `PermitRootLogin` as a belt-and-suspenders mitigation. Details below.

## Step-by-Step Fix: Patch and Harden Alpine Linux in 6 Steps

The root cause is a **stack-based buffer over-read** in musl's string handling that OpenSSH's password comparison routine trusts without a length bound. When the supplied password exceeds 256 bytes, the comparison returns a false "match." The fix lands in two packages, so you must upgrade **both**.

### Step 1 — Confirm you're affected

Check your distro and package versions:

```bash
cat /etc/os-release
apk info -v openssh-server musl | head
```

You are vulnerable if:
- You run **Alpine Linux** (any release before the patched `musl` build) or another musl-based distro (e.g., some Void/embedded builds).
- `openssh-server` is installed **and** `PasswordAuthentication yes` is set in `/etc/ssh/sshd_config`.
- `sshd` is reachable from untrusted networks.

### Step 2 — Back up your config

```bash
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak.$(date +%F)
```

### Step 3 — Upgrade the vulnerable packages

```bash
apk update
apk upgrade openssh openssh-server musl
# verify the new versions:
apk info -v openssh-server musl
```

If your mirror hasn't synced the patched build yet, pin to the `edge` repo temporarily:

```bash
apk add --repository https://dl-cdn.alpinelinux.org/alpine/edge/main --upgrade openssh-server musl
```

### Step 4 — Restart the daemon (not just reload)

A full restart is required because the musl library is loaded into the running process:

```bash
rc-service sshd restart
# or on systemd-based musl distros:
systemctl restart sshd
```

### Step 5 — Apply the interim mitigation (works even before patching)

Even unpatched, you can neutralize the attack by disabling password auth. Edit `/etc/ssh/sshd_config`:

```
PasswordAuthentication no
PermitRootLogin prohibit-password
KbdInteractiveAuthentication no
MaxAuthTries 3
```

Then reload: `rc-service sshd reload`. Switch to **key-based auth** immediately if you haven't already.

### Step 6 — Verify the fix

```bash
# Should now reject a 300-char password:
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no \
    root@your-host "$(printf 'A%.0s' {1..300})"
# Expected: Permission denied (publickey,password).
```

## Common Issues, Detection, and What You Should Know

### How to tell if you were already exploited

Because the bypass logs in as a *valid* user with a *valid* auth event, it can look legitimate. Check for:

- `auth.log` / `messages` entries with unusually long or binary-garbage password attempts.
- Successful `Accepted password for root` lines you can't attribute.
- New `authorized_keys` entries, cron jobs (`/etc/cron.*`, `crontab -l`), or systemd/OpenRC service additions.

```bash
grep -Ei 'Accepted (password|keyboard)' /var/log/messages
lastlog | grep -v 'Never'
find / -name authorized_keys -newer /etc/ssh/sshd_config 2>/dev/null
```

### Mitigation vs. patch — which do you need?

| Action | Stops the attack? | Effort | Recommended? |
|---|---|---|---|
| Disable `PasswordAuthentication` | ✅ Yes (kills the vector) | Low | ✅ Always |
| Upgrade `openssh` + `musl` | ✅ Yes (fixes root cause) | Low | ✅ Always |
| Firewall/allowlist SSH | ⚠️ Partial | Medium | ✅ Defense-in-depth |
| Change root password | ❌ No | Low | ❌ Pointless here |

### Why "just change your password" doesn't help

The bypass doesn't guess or crack a password—it exploits the length comparison. A stronger password provides **zero** protection. Only disabling password auth or patching the library closes the hole.

### Affected vs. unaffected stacks

- **Affected:** Alpine Linux, and any distro linking OpenSSH against musl-libc.
- **Not affected:** glibc-based distros (Debian, Ubuntu, RHEL, Fedora) — the vulnerable code path lives in musl's string routines, so standard OpenSSH on glibc is not exposed to this specific chain.

## Frequently Asked Questions (FAQ)

### Is my Ubuntu or Debian server vulnerable to the OpenSSH musl-libc flaw?
No. The chained bug depends on **musl-libc**, which Debian/Ubuntu/RHEL do not use (they ship glibc). Only musl-based systems like Alpine Linux are exposed to this specific authentication bypass.

### Does disabling password authentication fix the Alpine OpenSSH bug without upgrading?
Yes—disabling `PasswordAuthentication` removes the vulnerable code path from being reachable, so it's a valid emergency mitigation. However, you should still upgrade `openssh` and `musl` to fix the underlying flaw and any related issues.

### How do I know if my Alpine box was already breached via this flaw?
Look for `Accepted password` logins you can't explain, unexpected `authorized_keys` files, new cron jobs, and recently modified binaries. Because the attack authenticates as a real user, treat any suspicious successful login as a compromise and rebuild the host.

### Does a longer or stronger root password protect me?
No. The flaw is triggered by *length* (>256 characters), not by password strength. Changing the password does nothing; you must patch or disable password auth.

## Final Verdict

Treat this as a **patch-today** issue, not a wait-and-see. The combination of an OpenSSH auth-handling flaw and a musl-libc memory bug creates a trivial, unauthenticated root login on exposed Alpine systems—and "change your password" advice is actively wrong here. Do three things right now: **(1)** run `apk upgrade openssh openssh-server musl` and restart `sshd`, **(2)** set `PasswordAuthentication no` and move to SSH keys, and **(3)** audit logs for any `Accepted password` events you can't account for. If you find evidence of compromise, don't clean it—rebuild the host from a known-good image. Patch first, harden second, and verify with the 300-character test above.