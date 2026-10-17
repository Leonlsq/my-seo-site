---
title: "Home Assistant Integration Scanning Secrets: How to Audit & Block It"
description: "Worried an integration is scanning your secrets? Learn how to audit Home Assistant integrations, restrict secret access, and block unauthorized scans."
pubDate: 2026-10-17
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Your Home Assistant Integration Might Be Scanning More Than It Should

A firestorm erupted on GitHub (issue #49314) and Hacker News when users discovered that certain Home Assistant integrations can access configuration data—including API keys, tokens, and passwords stored in `secrets.yaml`—without explicit, granular authorization. The core complaint: **"I never authorized an integration that scans my secrets."** If you run Home Assistant, this is your wake-up call. This guide gives you a concrete audit-and-lockdown procedure so you can verify which integrations touch your secrets and restrict them before anything leaks.

The short version: Home Assistant's integration model is powerful but permissive. Integrations run inside the same process and can read config entries and, in some cases, the filesystem where `secrets.yaml` lives. You must treat every third-party or HACS integration as code with your credentials in reach.

## Step-by-Step: Audit and Restrict Secret Access in Home Assistant

Follow these steps in order. Each one closes a specific gap.

### 1. Inventory every installed integration
- Go to **Settings → Devices & Services → Integrations**.
- Export the list (screenshot or copy names). Flag anything from **HACS**, custom repositories, or unknown authors in red.
- Cross-check against `config/.storage/core.config_entries` to see the raw entries, including which ones store credentials.

### 2. Find what touches `secrets.yaml`
- Open `configuration.yaml` and search for `!secret` references.
- Run a filesystem check from the HA host:
  ```bash
  grep -rn "secrets.yaml" /config --include="*.py" --include="*.yaml"
  ```
- Any integration directory referencing `secrets.yaml` directly deserves scrutiny. Built-in integrations rarely do; custom ones often do.

### 3. Lock down file permissions
Restrict `secrets.yaml` so only the HA process user can read it:
```bash
chmod 600 /config/secrets.yaml
chown homeassistant:homeassistant /config/secrets.yaml
```
This won't stop in-process integrations, but it blocks other containers and add-ons from reading it.

### 4. Rotate exposed credentials
If you suspect an integration already read your secrets, rotate **every** token it could reach:
- Long-lived access tokens (Profile → Security → Tokens)
- Cloud API keys (Nabu Casa, Google, Alexa)
- Third-party service tokens (MQTT, Zigbee2MQTT, database passwords)

### 5. Sandbox risky integrations
- Run untrusted integrations in a **separate container** or use the **Home Assistant Container** deployment instead of Supervised/OS where add-ons share the host.
- Prefer integrations that support **OAuth** over raw token storage—OAuth tokens are scoped and revocable.

### 6. Enable audit logging
Add to `configuration.yaml`:
```yaml
logger:
  default: warning
  logs:
    homeassistant.components: info
```
Then monitor `home-assistant.log` for unexpected file reads or outbound calls from integrations you don't recognize.

## What You Should Know: Limits, Risks, and Alternatives

Home Assistant's architecture does **not** provide per-integration secret isolation out of the box. That's the root of the controversy—there is no permission prompt saying "This integration wants to read your secrets." Here's the practical reality:

| Risk | Mitigation | Effort |
|------|-----------|--------|
| Custom/HACS integration reads `secrets.yaml` | Audit code, sandbox, rotate tokens | Medium |
| Add-on accesses host filesystem | Use container deployment, restrict mounts | High |
| Long-lived token leaked | Switch to OAuth, short expiry | Low |
| Malicious update in a custom repo | Pin versions, review diffs | Medium |

**Alternatives worth considering:**
- **Vault/secrets manager** (e.g., HashiCorp Vault, SOPS) with HA fetching secrets at runtime instead of storing them in plaintext.
- **Environment variables** passed to the container rather than `secrets.yaml`.
- **Read-only config mounts** for integrations that shouldn't write back.

The community discussion makes one thing clear: until Home Assistant ships a formal permission model for secret access, **you are the permission layer**. Treat integration installs like installing browser extensions—review, pin, and revoke.

## Frequently Asked Questions (FAQ)

### Can a Home Assistant integration read my secrets.yaml without permission?
Yes. Integrations run in the same Python process as Home Assistant and can access config entries and, in many deployments, the filesystem path where `secrets.yaml` is stored. There is no built-in per-integration permission prompt for secret access, which is exactly what GitHub issue #49314 raised.

### How do I know if an integration is scanning my secrets?
There's no single "secret access" log. Instead, audit integration source code (especially custom/HACS ones), grep for `secrets.yaml` references, monitor `home-assistant.log`, and watch for unexpected outbound network calls. Rotating tokens and checking for unauthorized API usage is the most reliable detection method.

### Does this affect built-in integrations or only custom ones?
Built-in integrations are reviewed and generally follow stricter practices, but the architectural risk applies to all integrations. Custom and HACS integrations carry the highest risk because they aren't vetted by the core team and can change on update.

### Should I stop using HACS because of this?
No—but pin your versions, review updates before applying, and prefer well-maintained repositories with visible source. HACS itself isn't the problem; unreviewed code with access to your credentials is.

## Final Verdict

The "unauthorized secret scan" controversy isn't a bug you patch once—it's a structural gap in Home Assistant's integration model. **Do the audit today**: inventory your integrations, lock down `secrets.yaml` permissions, rotate any token an untrusted integration could have touched, and move to OAuth where possible. If you run custom integrations, sandbox them and pin versions. Until Home Assistant introduces granular secret permissions, assume every integration can read everything—and secure your setup accordingly.