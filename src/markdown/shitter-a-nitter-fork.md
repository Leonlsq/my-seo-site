---
title: "Shitter Nitter Fork: How to Self-Host & Fix Login Issues"
description: "Learn how to self-host the Shitter Nitter fork with Docker, fix the 'No guest accounts' error, and compare it to alternative Twitter front-ends in 2026."
pubDate: 2026-10-23
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Shitter – A Nitter Fork: What It Is and How to Get It Running

If you clicked through the Hacker News thread about **Shitter** (the revived Nitter fork hosted at `codeberg.org/shitter/shitter`) and immediately wondered "how do I actually run this thing," you're in the right place. Nitter—the privacy-friendly, JavaScript-free Twitter/X front-end—was effectively killed off in early 2024 when Elon Musk's API changes broke guest account access. Shitter is a community-maintained fork that patches the breakage, adds account-pool support, and lets you self-host a working instance again.

The direct takeaway: **Shitter is not a hosted service you sign up for.** It's a Docker-deployable backend you run yourself, and the #1 stumbling block is the "No guest accounts available" error, which you fix by supplying authenticated session tokens via the `accounts_file`. Below is the full setup walkthrough, the exact config parameters that matter, and the troubleshooting fixes for the errors most users hit within the first 20 minutes.

## Step-by-Step: Self-Hosting Shitter with Docker

Before you start, confirm your prerequisites: a Linux VPS or home server with **Docker Engine 24+**, **Docker Compose v2**, at least **512 MB RAM**, and a domain name if you want TLS. Shitter is written in Nim (inherited from Nitter) and compiles to a single binary, so the Docker route is by far the easiest.

### Step 1 — Clone the repository

```bash
git clone https://codeberg.org/shitter/shitter.git
cd shitter
```

### Step 2 — Create your configuration file

Copy the sample config and edit the essentials:

```bash
cp nitter.conf.example nitter.conf
```

The parameters that actually matter for a working instance:

| Parameter | Recommended Value | Why It Matters |
|---|---|---|
| `hostname` | `your.domain.tld` | Used for absolute links and RSS feeds |
| `port` | `8080` | Internal listen port; map in Docker |
| `https` | `true` | Set `false` behind a reverse proxy |
| `enableRSS` | `true` | RSS is the main reason people self-host |
| `enableDebug` | `false` | Turn on only while troubleshooting |
| `hmacKey` | 64-char random string | Signs session cookies; **must** be unique |
| `base64Media` | `false` | Inline media bloats pages; leave off |
| `accounts_file` | `./accounts.jsonl` | **Critical** — supplies auth tokens |

Generate a strong HMAC key with `openssl rand -hex 32`.

### Step 3 — Build the accounts file (the make-or-break step)

Shitter, like late-stage Nitter, needs authenticated tokens because anonymous guest accounts are rate-limited to death. Each line in `accounts.jsonl` is a JSON object:

```json
{"username":"yourhandle","password":"yourpassword","email":"you@example.com"}
```

Use **burner accounts** only. Never put your primary X account credentials in a self-hosted front-end—the tokens are stored in plaintext on your server.

### Step 4 — Launch with Docker Compose

```yaml
services:
  shitter:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./nitter.conf:/src/nitter.conf:ro
      - ./accounts.jsonl:/src/accounts.jsonl:ro
    restart: unless-stopped
```

Run `docker compose up -d --build`, then check logs with `docker compose logs -f`. A healthy boot prints the listening port and account-pool status within ~15 seconds.

### Step 5 — Put it behind a reverse proxy

Use Caddy or Nginx with a Let's Encrypt certificate. Set `https = false` in `nitter.conf` so Shitter doesn't try to terminate TLS itself, and forward `X-Forwarded-For` so rate limiting works correctly.

## Common Issues and Fixes

- **"No guest accounts available" / blank timelines.** Your `accounts_file` is missing, malformed, or the tokens are dead. Validate JSON line-by-line with `jq -c . accounts.jsonl`. Re-authenticate accounts if X has invalidated sessions.
- **429 Too Many Requests.** You're running too few accounts for your traffic. Rough guidance: one authenticated account per ~50–100 daily active users. Add more lines to `accounts.jsonl` and restart.
- **Container exits immediately.** Usually a config parse error—Nim's config parser is strict about `key = value` spacing. Run `docker compose logs` and look for the first `Error:` line.
- **Media not loading.** Set `proxyVideos = true` and ensure your reverse proxy passes the `/pic/` and `/video/` paths without caching.
- **RSS feeds 404.** Confirm `enableRSS = true` and that you're hitting `/username/rss`, not the legacy `/rss/username` path.

### Shitter vs. the Alternatives

| Option | Self-Hosted | Guest Access | Maintenance Burden |
|---|---|---|---|
| **Shitter** | Yes (Docker) | No — needs accounts | Medium |
| Public Nitter instances | No | Mostly broken | N/A |
| Nitter (upstream) | Yes | Broken since 2024 | Abandoned |
| Official X web | No | N/A | Heavy JS/ads |

Shitter's edge is that it's actively patched against X's API churn. Its weakness is that it still depends on authenticated accounts, which X can ban. Budget for rotating burner accounts.

## Frequently Asked Questions (FAQ)

### Is Shitter safe to use with my Twitter account?
Only use throwaway accounts. Credentials sit in plaintext in `accounts.jsonl` on your server, and X may flag or suspend accounts used for automated front-end access. Never use your main handle.

### Why does Shitter need an accounts file when old Nitter didn't?
Upstream Nitter relied on anonymous guest tokens, which X disabled in 2024. Shitter's fork requires authenticated sessions to fetch timelines, so the `accounts_file` parameter is mandatory for a functional instance.

### Can I access Shitter without hosting it myself?
Not officially. There's no central Shitter service—the project is distributed as source for self-hosting. Any "public Shitter instance" you find is run by a third party with unknown logging practices, so treat it with caution.

## Final Verdict

**Shitter is worth self-hosting if you specifically need RSS feeds or a JavaScript-free Twitter reader and you're comfortable maintaining burner accounts.** The Docker setup takes about 20 minutes, and the only real friction point is the `accounts.jsonl` file. If you want zero maintenance, skip it—no fork can fully escape X's API restrictions. But for privacy-conscious users running a personal instance on a $5 VPS, Shitter is currently the most functional Nitter lineage available in 2026. Start with one account, monitor your logs for 429s, and scale the pool as your usage grows.