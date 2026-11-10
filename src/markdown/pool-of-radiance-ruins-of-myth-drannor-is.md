---
title: "Pool of Radiance: Ruins of Myth Drannor GOG vs Steam: Best Setup"
description: "Pool of Radiance: Ruins of Myth Drannor is back on GOG and Steam. Compare versions, fix crashes, and apply the best widescreen and patch settings."
pubDate: 2026-11-08
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Pool of Radiance: Ruins of Myth Drannor Is Back — Here's How to Actually Make It Run

After two decades in licensing limbo, *Pool of Radiance: Ruins of Myth Drannor* (the 2001 Gold Box successor from Stormfront Studios, not the 1988 SSI classic) has finally returned to digital storefronts via GOG and Steam. Reddit user /u/Fritolex flagged the Steam listing, and the nostalgia wave is real. But here's the catch nobody tells you in the news post: **the re-release ships as a near-verbatim 2001 build**, which means the same crash-on-save bugs, the same uninstaller that could nuke your `system32` folder (yes, really), and the same DirectX 8 rendering path that modern GPUs hate.

This guide cuts through the hype. Below you'll find a direct GOG vs Steam comparison, the exact patch and compatibility steps to get the game stable, and the community fixes that turn a broken 2001 launch into a playable dungeon crawl. If you're searching "Ruins of Myth Drannor crash fix" or "GOG vs Steam Pool of Radiance," you're in the right place.

## GOG vs Steam: Which Version Should You Buy?

Both storefronts sell the same core game at roughly the same price, but the packaging differs in ways that matter for a 24-year-old title.

| Feature | GOG Version | Steam Version |
|---|---|---|
| **DRM** | DRM-free, offline installer | Steam client required |
| **Pre-patched** | Ships with official v1.4 patch applied | Verify: check build number in main menu |
| **Cloud saves** | GOG Galaxy optional | Steam Cloud supported |
| **Community patch pre-bundled** | Often includes fan fixes in extras | Manual install required |
| **Refund window** | 30 days | 2 hours / 14 days |
| **Best for** | Preservationists, offline play, modders | Achievement hunters, Steam Deck users |

**My recommendation:** Buy on **GOG** if you want a clean, patchable install you can back up and mod without a launcher fighting you. Buy on **Steam** only if you want the convenience of Steam Deck's Proton layer (which handles the game surprisingly well) or you're collecting the library.

### Step-by-Step: Getting the Game Stable on Modern Windows

The vanilla build crashes frequently on Windows 10/11. Follow this sequence exactly:

1. **Install to a short path.** Use `C:\Games\PoR` — not `Program Files`. The 2001 engine chokes on long paths and permission-locked folders.
2. **Apply the official v1.4 patch** if your storefront build shows anything lower. Check the version number in the bottom-right of the main menu.
3. **Install the community "Ruins of Myth Drannor Fix Pack"** (hosted on ModDB and the GOG forums). This resolves the infamous save-corruption bug and the broken uninstaller.
4. **Set compatibility mode:** Right-click `POR.exe` → Properties → Compatibility → Windows XP (Service Pack 3), and check "Run as administrator."
5. **Force windowed mode** by editing `config.ini` and setting `Fullscreen=0`. The engine renders more reliably in a window; use Borderless Gaming to fake fullscreen.
6. **Cap the framerate at 60 FPS** via your GPU control panel. The game logic ties to frame timing and runs at 2x speed on high-refresh monitors.

### Widescreen and Resolution Fixes

The game natively caps at 1024x768. For modern displays:

- Use **dgVoodoo2** to wrap the old DirectX 8 calls into DirectX 11 — this alone fixes most black-screen and texture-corruption issues on AMD and Intel GPUs.
- Apply the **widescreen hex edit** (documented on the GOG community forums) to unlock 1920x1080. Note: UI elements stretch, so 1600x900 is the sweet spot.
- On Steam Deck, launch with Proton Experimental and set the in-game resolution to 1280x800.

## Common Issues and What You Should Know

**The uninstaller trap.** The original 2001 uninstaller had a notorious bug that could delete the contents of your Windows directory. The re-releases *should* have this patched, but **never run the uninstaller without first verifying the fix pack is installed**. Back up your save folder (`Documents\Pool of Radiance`) before uninstalling.

**Save corruption.** The game auto-saves aggressively and corrupts saves if you quit mid-combat. Manually copy your save folder after every major dungeon.

**Steam Deck performance.** Expect 60 FPS locked with Proton, but the touchpad and on-screen keyboard are clunky for the game's dense inventory UI. A Bluetooth mouse is strongly recommended.

**Alternatives worth knowing:** If you bounced off Ruins of Myth Drannor's real-time-with-pause combat, the *Baldur's Gate: Enhanced Edition* trilogy and *Neverwinter Nights: Enhanced Edition* deliver the same D&D 3rd Edition-era feel with modern stability. For the original 1988 *Pool of Radiance*, GOG's Gold Box bundle is the cleaner purchase.

## Frequently Asked Questions (FAQ)

### Is Pool of Radiance: Ruins of Myth Drannor the same as the 1988 game?
No. The 1988 *Pool of Radiance* is an SSI Gold Box tactical RPG. The 2001 *Ruins of Myth Drannor* is a separate real-time-with-pause dungeon crawler set in the Forgotten Realms city of Myth Drannor. They share a name and setting lineage but are entirely different games.

### Does the GOG or Steam version include the official patches?
GOG typically ships the game pre-patched to v1.4 with fan fixes in the extras folder. Steam versions have varied by build — check the version number in the main menu and apply the v1.4 patch manually if it reads lower.

### Can I play Ruins of Myth Drannor on Steam Deck?
Yes. It runs under Proton Experimental at a locked 60 FPS. Use a Bluetooth mouse for the inventory screens, and apply the community fix pack via desktop mode before launching.

### Why does the game crash when I save?
The vanilla build has a save-corruption bug tied to auto-saves during combat. Install the community Fix Pack, disable auto-save in the options menu, and manually back up your save folder after each session.

## Final Verdict

**Buy it on GOG.** The DRM-free installer, pre-applied patches, and 30-day refund window make it the safer bet for a game this old and this fragile. Then immediately install the community Fix Pack, force windowed mode, and cap your framerate — that trio of steps turns a crash-prone 2001 relic into a genuinely playable nostalgia trip. If you're on Steam Deck, the Steam version's Proton compatibility is a legitimate reason to go the other way, but budget 20 minutes for manual patching. Either way, don't launch it blind — the vanilla build will punish you.