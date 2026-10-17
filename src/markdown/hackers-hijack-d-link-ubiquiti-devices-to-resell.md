---
title: "Is Your Router Hijacked? How to Check & Stop Proxyjacking"
description: "Hackers are hijacking D-Link and Ubiquiti routers to resell your bandwidth. Learn how to check your device, remove proxyjacking malware, and lock it down."
pubDate: 2026-10-17
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Is Your D-Link or Ubiquiti Router Secretly Selling Your Bandwidth?

A proxyjacking campaign has quietly compromised routers and IoT devices across **34 countries**, turning them into nodes on a commercial residential proxy network — and the operators are pocketing the profits from *your* internet connection. Unlike ransomware, there's no lock screen, no ransom note, and no obvious symptom. Your D-Link or Ubiquiti device just keeps working while silently routing strangers' traffic through your IP address. The direct takeaway: **you need to check your router today**, because proxyjacking is designed to be invisible, and the longer it runs, the more your IP gets tied to sketchy activity you didn't commit.

This guide gives you a concrete, step-by-step way to detect, remove, and prevent proxyjacking on D-Link and Ubiquiti hardware — plus the exact settings that close the doors attackers are walking through.

## How Proxyjacking Works (and Why D-Link/Ubiquiti)

Proxyjacking malware installs a lightweight proxy client on a compromised device, then registers that device with a **residential proxy marketplace**. Buyers pay per gigabyte to route web scraping, ad fraud, or credential-stuffing traffic through residential IPs — because residential IPs look trustworthy to anti-bot systems. The victim pays the bandwidth bill and absorbs the legal risk.

D-Link and Ubiquiti gear is targeted for three reasons:

- **Default or weak credentials** — many D-Link models shipped with admin/admin or similar, and Ubiquiti devices with default `ubnt` logins are still out there.
- **Exposed management interfaces** — routers with WAN-side admin access or UPnP enabled are remotely reachable.
- **Known CVEs and end-of-life firmware** — older D-Link DIR series and Ubiquiti EdgeRouter/AirOS devices with unpatched vulnerabilities are low-hanging fruit.

## Step-by-Step: Check and Clean Your Router

### 1. Look for the telltale signs
- **Unexplained bandwidth usage** — check your ISP data dashboard or router traffic graphs during idle hours (e.g., 2–5 AM). Steady upload traffic with no devices active is a red flag.
- **Unknown processes or cron jobs** — on Ubiquiti EdgeOS, run `ps aux` and `crontab -l` via SSH. Look for unfamiliar binaries, especially anything referencing proxy, socks, or tunnel.
- **Open ports you didn't open** — scan your WAN IP with an external tool like ShieldsUP or a port scanner. A listening SOCKS proxy port (often 1080, 8080, or random high ports) is a strong indicator.
- **Slow speeds and high latency** — a saturated uplink from proxy traffic degrades your connection.

### 2. Isolate and inspect
1. Log into your router's admin panel (usually `192.168.0.1` for D-Link, `192.168.1.1` for Ubiquiti).
2. Check **connected clients** and **DHCP leases** for unknown devices.
3. Review **port forwarding, UPnP mappings, and remote management** settings for entries you didn't create.
4. On Ubiquiti, SSH in and review `/etc/cron.*`, startup scripts, and recently modified files.

### 3. Remove the infection
- **Best option: factory reset.** Hold the reset button 10–30 seconds, then reconfigure from scratch. Do *not* restore an old backup — it may contain the malicious config.
- **Update firmware immediately** after reset, before reconnecting to the internet if possible.
- **Change the admin password** to a long, unique passphrase and disable WAN-side admin access.

### 4. Lock it down (the settings that matter)

| Setting | Action | Why |
|---|---|---|
| Admin password | Unique 16+ char passphrase | Blocks credential-based takeover |
| Remote/WAN management | **Disable** | Removes internet-facing attack surface |
| UPnP | **Disable** unless required | Prevents silent port mapping |
| Firmware | Enable auto-update / check monthly | Patches known CVEs |
| Guest/IoT network | Separate VLAN or SSID | Contains a future compromise |
| DNS | Use a filtering resolver (e.g., Quad9) | Blocks proxy C2 domains |

## What You Should Know Before You Panic

- **Not every slow connection is proxyjacking.** Run the checks above before assuming compromise.
- **Check EOL status.** Several D-Link DIR models and older Ubiquiti AirOS devices are end-of-life and no longer receive patches — if yours is EOL, replacement is the real fix, not another reset.
- **Your IP reputation may already be tainted.** After cleanup, check your IP against abuse databases (e.g., AbuseIPDB) and request delisting if flagged.
- **Report it.** File a report with your ISP and, in the US, with the FBI's IC3 — residential proxy abuse is increasingly prosecuted.

## Frequently Asked Questions (FAQ)

### How do I know if my D-Link router is hijacked by proxyjacking?
Check for idle-time upload traffic, unknown cron jobs or processes (via SSH), unexpected open ports on your WAN IP, and port-forwarding rules you didn't create. A factory reset plus firmware update is the safest remediation.

### Can proxyjacking malware survive a router reboot?
Yes. Most proxyjacking implants persist via cron jobs, startup scripts, or modified firmware configs, so a simple reboot won't remove them. You need a factory reset and fresh firmware.

### Does proxyjacking steal my personal data?
Not directly — it monetizes your bandwidth and IP address. But because your IP routes others' traffic, you could be implicated in abuse complaints, and any device on your network remains at risk if the initial access vector isn't closed.

## Final Verdict

Treat any D-Link or Ubiquiti device with default credentials, WAN management enabled, or end-of-life firmware as **already compromised until proven otherwise**. Do the factory reset, disable remote management and UPnP, and update firmware today. If your hardware is end-of-life and no longer patched, stop resetting it and replace it — a $60–$120 modern router is far cheaper than the bandwidth theft, ISP throttling, and IP reputation damage a hijacked device will cost you.