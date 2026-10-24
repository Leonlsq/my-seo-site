---
title: "Torchlight 2 Controller Support Beta: How to Opt In & Fix Crashes"
description: "Enable Torchlight 2 controller support via the Steam beta branch, map your gamepad, and fix the crashes the new patch introduces. Step-by-step."
pubDate: 2026-10-24
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Torchlight II Controller Support Beta: How to Opt In and Fix the New Crashes

Runic Games' Torchlight II just got a surprise beta patch on Steam that finally adds native controller support — plus a batch of crash fixes. The catch? It's an **opt-in beta branch**, it's unpolished, and a chunk of players are reporting fresh crashes the moment they plug in a gamepad. This guide shows you exactly how to switch to the beta, get your controller recognized, and work around the known crash triggers so you can actually play.

Here's the short version: open Steam → right-click **Torchlight II** → **Properties** → **Betas** → select the controller-support branch → let it download → launch with your controller connected *before* the game starts. If it crashes, the fixes are below.

## Step-by-Step: Enabling the Beta & Controller Support

### 1. Opt into the beta branch
1. Open **Steam** and go to your **Library**.
2. Right-click **Torchlight II** → **Properties**.
3. Open the **Betas** tab.
4. In the dropdown, select the controller-support beta branch (the exact name appears as a `beta -` entry; pick the newest one listed).
5. Click **Check Code** only if the developer posted a password — otherwise leave it blank.
6. Close the window and let Steam download the patch. Wait for it to finish **before** launching.

### 2. Connect and configure your controller
- **Connect the controller before launching the game.** Torchlight II reads input devices at startup; hot-plugging mid-session is the #1 cause of "controller not detected."
- For **Xbox / PlayStation pads**, Steam Input handles mapping automatically. If buttons feel wrong, open **Steam → Settings → Controller** and enable **Steam Input** for the game.
- For **generic / third-party pads**, use **Steam Input's template browser** and pick a community layout, or map manually via **Controller → Edit Layout**.

### 3. Verify it's working
- Move the left stick — the cursor/character should respond.
- Open the inventory with the mapped button (defaults vary; check the in-game **Options → Controls** menu).
- If the game still shows keyboard prompts, the controller wasn't detected at launch — fully close the game and relaunch.

### Quick Reference: Beta Setup Checklist

| Step | Action | Common Failure |
|------|--------|----------------|
| 1 | Select beta branch in Steam Properties | Forgetting to click **Check Code** if required |
| 2 | Wait for full download | Launching mid-download → version mismatch crash |
| 3 | Connect controller **before** launch | Hot-plugging → not detected |
| 4 | Enable Steam Input | Double-mapping → stuck buttons |
| 5 | Test in Options → Controls | Skipping → confusion over prompts |

## Common Issues & Crash Fixes

The beta is genuinely beta. Here's what players are hitting and how to get around it:

- **Crash on launch after opting in.** Verify game files: right-click the game → **Properties → Installed Files → Verify integrity of game files**. A partial beta download is the usual culprit.
- **Crash when a controller is connected.** Disconnect the controller, launch the game with keyboard/mouse, then reconnect once you're at the main menu. This sidesteps the input-init crash on some hardware.
- **Controller detected but buttons are dead.** Disable any third-party mapper (DS4Windows, reWASD, x360ce) — running them *alongside* Steam Input causes double-input conflicts.
- **Save file concerns.** Beta branches can change save formatting. **Back up your save** first: it lives in `Documents\My Games\Runic Games\Torchlight 2\save`. Copy that folder somewhere safe before you opt in.
- **Reverting to stable.** Same Betas tab → select **None**. Your backed-up save protects you if the beta touched anything.

**What you should know before committing:** beta branches don't always carry forward cleanly, and multiplayer between beta and stable clients may not connect. If you play co-op with friends on the stable build, keep a second install or coordinate everyone onto the same branch.

## Frequently Asked Questions (FAQ)

### Does Torchlight II have official controller support now?
Only through the **Steam beta branch** as of this patch. The stable build still relies on keyboard/mouse or third-party mapping tools. Native support is being tested before a wider rollout.

### Why does Torchlight II crash when I connect my controller?
The beta initializes input devices at launch, and some drivers conflict with that handshake. Launch the game first, then connect the controller at the main menu — or disable third-party mappers like DS4Windows so only Steam Input is active.

### Can I lose my save by joining the beta?
Possibly, if the beta alters save formatting. Always copy the `save` folder under `Documents\My Games\Runic Games\Torchlight 2\` before opting in, and revert to the **None** branch if anything breaks.

### How do I leave the beta and go back to normal?
Steam → right-click Torchlight II → **Properties → Betas** → select **None**. Steam will re-download the stable build.

## Final Verdict

If you've been waiting to play Torchlight II from the couch, **opt into the beta — but back up your saves first and connect your controller before launch.** It's a real step toward native gamepad support, and the crash fixes are welcome, but this is still a test branch with rough edges. Casual keyboard/mouse players and co-op groups on the stable build should sit this one out until it graduates to the main branch. For everyone else: follow the checklist above, keep Steam Input as your only mapper, and you'll be dungeon-crawling with a controller in about five minutes.