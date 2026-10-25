---
title: "Shogun 2 Complete Edition Broken? How to Fix & What to Avoid"
description: "Shogun 2 Complete Edition is a mess after the external partner release. Here's how to fix crashes, missing content, and whether to buy it."
pubDate: 2026-10-24
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Shogun 2 Complete Edition Is Broken — Here's How to Fix It (or Avoid It)

If you bought the **Total War: Shogun 2 Complete Edition** expecting a definitive, all-in-one package, you've probably already hit a wall. The collection launched in a rough state — missing DLC, broken launcher behavior, save incompatibilities, and crash-on-startup reports. Creative Assembly's boss has publicly stated this was **not a Creative Assembly-developed release**, pointing the finger at an external partner who handled the packaging. That context matters, because it tells you where the fixes actually live: in your Steam library configuration, not in a CA patch.

This guide gives you the concrete workarounds to get Shogun 2 running properly, plus a clear buying verdict if you haven't pulled the trigger yet.

## Step-by-Step: Fixing the Shogun 2 Complete Edition

Work through these in order. Most users solve their problem within the first three steps.

### 1. Verify Your Game Files (Fixes ~60% of Cases)
1. Open **Steam** → right-click **Total War: SHOGUN 2** → **Properties**.
2. Go to **Installed Files** → click **Verify integrity of game files**.
3. Wait for the scan. Steam will re-download any missing DLC `.pack` files that the Complete Edition bundle failed to install correctly.

### 2. Manually Confirm DLC Ownership
The most common complaint is DLC appearing "owned" but not active in-game. Check this:

1. In Steam, go to **Library** → **SHOGUN 2** → scroll to **DLC** on the right panel.
2. Confirm each item shows as installed: *Rise of the Samurai*, *Fall of the Samurai*, *Blood Pack*, *Ikko-Ikki*, *Sengoku Jidai Unit Pack*, *Hattori*, *Oda*, *Otomo*, *Saint & Hero*.
3. If any are missing, **uncheck and re-check** them to force a re-sync, then restart Steam entirely.

### 3. Bypass the Broken Launcher
If the game crashes immediately after the launcher appears:
- Navigate to your install folder (typically `steamapps\common\Total War SHOGUN 2`).
- Launch `Shogun2.exe` **directly** as administrator.
- If that works, create a desktop shortcut to the `.exe` and skip the launcher permanently.

### 4. Clear the Scripts and Preferences Cache
Corrupted config files from a previous install cause black screens and infinite loading:

1. Go to `%AppData%\The Creative Assembly\Shogun2\scripts`.
2. **Back up** the folder, then delete its contents.
3. Also delete `preferences.script.txt` in the same directory tree.
4. Relaunch — the game regenerates clean defaults.

### 5. Fix Save Incompatibility
Complete Edition saves are **not** always backward-compatible with older standalone installs. If your old campaign won't load:
- Start a **new campaign** to confirm the game itself works.
- Old saves tied to a different DLC configuration generally cannot be recovered — this is a packaging limitation, not a bug you can patch.

## Common Issues, Alternatives, and What You Should Know

| Issue | Likely Cause | Fix |
|---|---|---|
| Crash on launch | Launcher conflict | Run `Shogun2.exe` directly |
| DLC missing in-game | Incomplete bundle install | Verify files + re-check DLC |
| Black screen / infinite load | Corrupt scripts cache | Delete `scripts` folder |
| Old saves won't load | DLC config mismatch | New campaign required |
| Missing Blood Pack | Regional rating restriction | Check store region settings |

**Should you buy it?** If you already own base Shogun 2 plus DLC, **do not** buy the Complete Edition — you gain nothing and risk breaking a working install. If you're a new player, the safer route is buying **Shogun 2 base + Fall of the Samurai separately** during a sale, which avoids the packaging problems entirely. The Complete Edition's only real advantage is a single-click install, and right now that install is unreliable.

**Information gain worth noting:** because CA did not develop this package, don't expect an official hotfix on the base game's normal patch cadence. Community fixes (Steam Workshop mods, the manual `.pack` verification method above) are your realistic support path.

## Frequently Asked Questions (FAQ)

### Is the Shogun 2 Complete Edition worth buying in 2026?
Only if it's heavily discounted and you're a brand-new player. Existing owners should skip it. The packaging issues mean you may spend more time troubleshooting than playing.

### Why is my Shogun 2 Complete Edition missing DLC?
The external partner's bundle installer sometimes fails to register individual DLC. Verifying game files in Steam and manually re-checking the DLC list usually resolves it.

### Did Creative Assembly develop the Shogun 2 Complete Edition?
No. CA's leadership confirmed an external partner handled this release. That's why fixes come from Steam-side verification rather than official CA patches.

### Can I get a refund if the Complete Edition won't launch?
Yes — Steam's refund policy covers games that fail to run, provided you're within the playtime and purchase window. Document the crash before requesting.

## Final Verdict

**Don't buy the Complete Edition blindly, and don't panic if you already did.** Run the five-step fix above first — file verification, DLC re-sync, direct `.exe` launch, and cache clearing solve the overwhelming majority of reported problems. If you're still deciding, buy **base Shogun 2 plus Fall of the Samurai** separately instead. You get the same content with far fewer headaches, and you're not gambling on a third-party bundle that CA itself has distanced from.