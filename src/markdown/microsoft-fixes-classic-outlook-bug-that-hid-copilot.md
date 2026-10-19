---
title: "Copilot Buttons Missing in Classic Outlook? How to Fix It"
description: "Copilot buttons vanished from classic Outlook on Windows? Microsoft's fix is rolling out. Here's how to restore them fast, plus fallback workarounds that work."
pubDate: 2026-10-19
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Copilot Buttons Missing in Classic Outlook? Here's the Fix (and What to Do If It's Not Working Yet)

If you opened the classic Outlook desktop client on Windows and noticed the **Copilot Chat and Copilot buttons had vanished** from the ribbon or toolbar, you weren't imagining it—and you weren't alone. Microsoft confirmed a known issue that removed these Copilot entry points for some Windows users in the classic Outlook mail client. The good news: **Microsoft has shipped a server-side fix**, and most affected users will see the buttons return automatically after restarting Outlook. The bad news: if you're reading this because the buttons *still* aren't back, the fix isn't instant for everyone. This guide walks you through exactly how to force the fix through, verify your Copilot eligibility, and what to do if you're stuck waiting.

## Step-by-Step: How to Restore Your Copilot Buttons

Work through these steps in order. Most users will be fixed by step 3.

### 1. Fully restart Outlook (not just close the window)
A quick X-click often leaves Outlook running in the background, which means the updated configuration never loads.

1. Press `Ctrl + Shift + Esc` to open **Task Manager**.
2. Find **Outlook (Microsoft Outlook)** under Processes.
3. Right-click → **End task**.
4. Relaunch Outlook from the Start menu.

### 2. Check for Office updates
The fix is primarily server-side, but the client needs a recent build to render the Copilot controls correctly.

1. Open any Office app → **File → Account**.
2. Click **Update Options → Update Now**.
3. Wait for the update to complete, then restart Outlook.

### 3. Confirm your Copilot license and channel
Copilot in classic Outlook requires a **Microsoft 365 Copilot license** (the add-on, not just a standard M365 subscription). Verify:

- **File → Account** shows your subscription and license type.
- Your organization hasn't disabled Copilot via policy (check with IT if this is a work account).
- You're signed in with the **correct account**—a common cause of "missing" buttons is being signed into a personal account while the Copilot license sits on the work account.

### 4. Reset the ribbon and toolbar
If the buttons are back in the code but hidden in your layout:

1. Go to **File → Options → Customize Ribbon**.
2. Click **Reset → Reset all customizations**.
3. Click **OK** and restart Outlook.

### 5. Clear the Office cache (last resort before reinstall)
Corrupted cached config can mask the fix:

1. Close Outlook completely.
2. Navigate to `%localappdata%\Microsoft\Office\16.0\OfficeFileCache`.
3. Rename the folder to `OfficeFileCache_old`.
4. Relaunch Outlook—it rebuilds the cache fresh.

| Symptom | Most Likely Cause | Fastest Fix |
|---|---|---|
| Buttons gone after an update | Server-side config bug | Restart Outlook + check updates |
| Buttons never appeared | No Copilot license / wrong account | Verify license in File → Account |
| Buttons appear then vanish | Corrupted Office cache | Clear OfficeFileCache |
| Buttons hidden in layout | Ribbon customization | Reset ribbon |

## Common Issues, Workarounds, and What You Should Know

**The fix is staged, not universal.** Microsoft rolls out server-side fixes in waves. If your colleague has the buttons back and you don't, that's normal—give it 24–72 hours and re-check after a full restart.

**Classic vs. new Outlook matters.** The bug specifically affected the **classic Outlook desktop client**. If you've switched to the new Outlook for Windows, Copilot behavior and placement differ. You can toggle back via the **"Try the new Outlook"** switch in the top-right of the client.

**Web fallback works now.** While you wait, Copilot Chat is available at **outlook.com** and via the **Microsoft 365 Copilot web app**—same underlying assistant, different surface. For quick drafting and summarization, this covers most workflows.

**Don't reinstall Office as a first move.** Reinstalling is slow, wipes customizations, and rarely fixes a server-side issue. Exhaust the steps above first.

**Watch for policy blocks.** In managed environments, admins can disable Copilot via the Microsoft 365 admin center. If buttons are missing org-wide, it's a policy issue, not the bug—escalate to IT.

## Frequently Asked Questions (FAQ)

### Why did my Copilot buttons disappear from classic Outlook?
Microsoft confirmed a known issue that removed the Copilot Chat and Copilot buttons for some Windows users in classic Outlook. It was a configuration bug, not a change to your license or settings. Microsoft has since deployed a fix.

### Do I need to do anything to get the fix?
Usually not—the fix is server-side and applies automatically. A **full restart of Outlook** (via Task Manager) and an **Office update check** are enough for most users. If buttons are still missing after 72 hours, verify your Copilot license and account sign-in.

### Is Copilot in classic Outlook free?
No. Copilot in classic Outlook requires a **Microsoft 365 Copilot add-on license**. A standard Microsoft 365 Personal or Family subscription does not include it. Some Copilot Chat features may be available through other surfaces depending on your plan.

### Will switching to the new Outlook bring the buttons back?
Possibly, but it's a different client with different Copilot integration. If you rely on classic Outlook's layout, the better path is to wait for the staged fix and confirm your license—switching clients is a workaround, not a repair.

## Final Verdict

**Don't panic and don't reinstall.** This was a Microsoft-side bug, and the fix is already rolling out. Your action plan: **fully restart Outlook, run an Office update, and verify your Copilot license and account**—that resolves the vast majority of cases. If the buttons are still gone after three days, clear the Office cache and check whether your organization has a Copilot policy in place. In the meantime, the Copilot web app is a solid stopgap. The buttons are coming back—you just may need to nudge your client to notice.