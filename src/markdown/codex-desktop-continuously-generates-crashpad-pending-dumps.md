---
title: "Codex Desktop Crashpad Dumps: How to Fix Pending Crash Reports"
description: "Stop Codex Desktop from flooding your disk with Crashpad pending dumps. Step-by-step fixes, cleanup commands, and workarounds for the GitHub issue #25921 bug."
pubDate: 2026-10-18
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Codex Desktop Crashpad Dumps: What's Actually Happening (and How to Stop It)

If you've noticed your disk filling up with gigabytes of `pending` and `completed` crash dump files inside a `Crashpad` folder while running OpenAI's Codex Desktop app, you're not alone. This is the exact symptom reported in [GitHub issue #25921](https://github.com/openai/codex/issues/25921), where Codex Desktop's bundled Crashpad handler (Chromium's crash-reporting subsystem) continuously writes dump files even when the app appears to be running normally. The direct takeaway: this is a **reporting/logging bug, not a crash loop** — your app isn't actually crashing, but the handler is misclassifying events and dumping memory snapshots. Below are the concrete fixes, ordered from quickest to most thorough.

## Step-by-Step Guide: Fixing Continuous Crashpad Pending Dumps

### Step 1: Confirm the Dumps Are Real and Locate Them
Before changing anything, verify the disk usage. Crashpad stores reports in a per-user directory:

- **Windows:** `%LOCALAPPDATA%\Codex\Crashpad\reports\` (also check `%LOCALAPPDATA%\Temp\`)
- **macOS:** `~/Library/Application Support/Codex/Crashpad/reports/` (and `~/Library/Logs/DiagnosticReports/`)
- **Linux:** `~/.config/Codex/Crashpad/reports/` or `~/.local/share/Codex/`

Run a size check:
```bash
# macOS / Linux
du -sh ~/.config/Codex/Crashpad/reports/ 2>/dev/null
find ~/.config/Codex/Crashpad/reports/ -name '*.dmp' | wc -l
```
```powershell
# Windows PowerShell
Get-ChildItem "$env:LOCALAPPDATA\Codex\Crashpad\reports" -Recurse | Measure-Object -Property Length -Sum
```
If you see hundreds of `.dmp` files with timestamps minutes apart, you've reproduced the bug.

### Step 2: Disable Crash Reporting in the App Config
Codex Desktop reads a local settings file. Disabling telemetry/crash upload stops the *upload* loop but not always the *dump* creation — however, in most reports it dramatically reduces frequency.

1. Fully quit Codex Desktop (check Task Manager / Activity Monitor for `Codex` and `crashpad_handler` processes).
2. Open the config directory (`~/.config/Codex/` or `%APPDATA%\Codex\`).
3. Edit `settings.json` (create it if missing) and add:
```json
{
  "telemetry": { "enabled": false },
  "crashReporting": { "enabled": false }
}
```
4. Save and relaunch.

### Step 3: Kill and Block the Orphaned Handler
The dump loop often persists because a `crashpad_handler` child process outlives the parent app. Terminate it:

```bash
# macOS / Linux
pkill -f crashpad_handler
```
```powershell
# Windows
Stop-Process -Name "crashpad_handler" -Force -ErrorAction SilentlyContinue
```
If the process respawns immediately, the parent app is still running — close it fully first.

### Step 4: Clean Up the Existing Dumps Safely
Once reporting is disabled, delete the accumulated files to reclaim space:

```bash
# macOS / Linux — remove dumps older than 1 day
find ~/.config/Codex/Crashpad/reports/ -name '*.dmp' -mtime +1 -delete
```
```powershell
# Windows
Get-ChildItem "$env:LOCALAPPDATA\Codex\Crashpad\reports" -Filter *.dmp | Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-1)} | Remove-Item -Force
```

### Step 5: Update or Pin to a Patched Build
Check the [issue thread](https://github.com/openai/codex/issues/25921) and the Codex release notes for a fixed version. If a patch exists, update. If not, pin to the last known-good build and watch the issue for a maintainer response. The HN discussion ([item #50133231](https://news.ycombinator.com/item?id=50133231)) has community-reported version numbers worth cross-referencing.

## Common Issues, Workarounds, and What You Should Know

**Why does this happen?** Crashpad's handler is designed to catch native crashes. A bug in how Codex Desktop signals "clean shutdown" to the handler causes it to treat normal exits (or even idle periods) as abnormal terminations, generating a dump each time. It's a **false-positive crash classification**, which is why the app "works fine" while your disk doesn't.

**Workaround comparison table:**

| Method | Effort | Effectiveness | Side Effects |
|---|---|---|---|
| Disable crashReporting in config | Low | High | No automatic crash telemetry |
| Kill crashpad_handler | Low | Temporary (respawns) | None |
| Delete dumps manually | Low | Reclaims space only | None |
| Pin to older build | Medium | High | Misses new features |
| Filesystem read-only on reports dir | High | Total block | May log errors |

**Advanced workaround — make the reports folder read-only** (Linux/macOS) to hard-block writes:
```bash
chmod 500 ~/.config/Codex/Crashpad/reports
```
Undo with `chmod 700` when a fix ships.

**Don't confuse this with real crashes.** If Codex Desktop actually closes unexpectedly, check `codex.log` for stack traces before dismissing the dumps — some users in the HN thread reported a mix of false positives and one genuine GPU-driver crash.

## Frequently Asked Questions (FAQ)

### Is the Codex Desktop Crashpad dump bug dangerous or just annoying?
It's primarily a disk-space and privacy concern, not a security vulnerability. The dumps can contain memory snapshots, so if you work with sensitive code, disable reporting and delete existing dumps promptly.

### Does disabling crash reporting break Codex Desktop features?
No. Crash reporting is telemetry-only. Disabling it does not affect code generation, the editor, or any core functionality — you simply stop sending crash data to OpenAI.

### How much disk space do the pending dumps use?
Community reports range from a few hundred MB to multiple GB depending on uptime. Each `.dmp` can be tens of MB; a loop generating one every few minutes can consume gigabytes per day.

### Will uninstalling and reinstalling fix it?
Usually not — the bug lives in the app build, so a reinstall of the same version reproduces it. Reinstalling only helps if you install a version where the issue is patched.

## Final Verdict

This is a **logging bug, not a broken app** — treat it as a housekeeping problem. The fastest reliable fix is **Step 2 + Step 3** (disable crash reporting in config, then kill the orphaned `crashpad_handler`), followed by cleanup. Watch GitHub issue #25921 for the official patch and upgrade the moment it lands. Until then, set a reminder to purge the `reports` folder weekly so a false-positive crash loop never eats your disk.