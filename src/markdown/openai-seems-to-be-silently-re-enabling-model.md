---
title: "Codex Data Sharing Re-Enabled? How to Check & Turn It Off"
description: "OpenAI silently re-enabled 'Improve the model for everyone' in Codex. Here's how to check your data controls, disable training, and lock it down."
pubDate: 2026-11-04
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## OpenAI Re-Enabled Codex Model Training on Your Chats — Here's How to Turn It Off

If you disabled data sharing in Codex to protect company IP, you need to re-check your settings **right now**. Multiple users — including entire engineering teams — have reported that the "Improve the model for everyone" toggle was silently flipped back on without their consent. This means your Codex prompts, code snippets, and chat history may have been eligible for model training again. This guide gives you the exact steps to verify your current status, disable training across every OpenAI surface, and prevent it from silently re-enabling in the future.

## Step-by-Step: Check and Disable Codex Data Sharing

The problem is that OpenAI has **multiple, disconnected privacy toggles** across different products and URLs. Disabling one does not disable the others. Here's how to audit all of them.

### Step 1: Check the ChatGPT/Codex Data Controls Page
1. Go to `https://chatgpt.com/settings/data-controls`.
2. Locate the toggle labeled **"Improve the model for everyone."**
3. If it is **ON**, toggle it **OFF**. This is the setting users report being silently re-enabled.
4. Refresh the page and confirm the toggle stayed off.

### Step 2: Check the Privacy Portal (Second Toggle)
Many users don't know a second control exists on a completely different domain:
1. Go to `https://privacy.openai.com/policies?modal=take-control`.
2. Sign in with the same account.
3. Review the data-sharing / model-training consent options and opt out where prompted.

### Step 3: Audit Organization-Level Settings
If you're on a **Team, Business, or Enterprise** plan, individual toggles may be overridden by workspace admin settings:
- Have your workspace admin open the **Admin Console → Workspace Settings → Data Controls**.
- Confirm that "Improve the model for everyone" is disabled at the **organization level**, not just per-user.
- Note: Enterprise and API data are contractually excluded from training by default, but **ChatGPT Team/Business and consumer Codex usage may not be** — verify your specific plan.

### Step 4: Verify and Document
- Take a **timestamped screenshot** of each setting showing it disabled. This is your paper trail if IP leakage ever becomes a legal question.
- Set a recurring calendar reminder (weekly or monthly) to re-check, since the re-enable appears to happen silently.

| Setting Location | URL | What It Controls |
|---|---|---|
| ChatGPT Data Controls | `chatgpt.com/settings/data-controls` | "Improve the model for everyone" toggle |
| OpenAI Privacy Portal | `privacy.openai.com/policies?modal=take-control` | Secondary consent / training opt-out |
| Admin Console (Team/Enterprise) | Admin → Workspace Settings | Org-wide training policy |
| API Platform | `platform.openai.com` | API data (excluded by default) |

## Why This Matters for IP Protection (And What You Should Know)

For companies paranoid about leaking intellectual property to frontier labs, a silently re-enabled toggle is a serious compliance risk. Here's the practical context:

- **The re-enable appears widespread, not isolated.** The original report on Hacker News (465+ points, 144 comments) plus a prior thread (`news.ycombinator.com/item?id=49643556`) confirm multiple independent users saw the same behavior. Treat it as systemic.
- **"Off" is not sticky.** The core lesson: never assume a privacy toggle you set months ago is still set. OpenAI's consent flows have changed across product updates, and toggles can reset during account migrations or UI changes.
- **Consumer vs. business data differ.** API and Enterprise data are excluded from training by contract. Consumer ChatGPT and Codex chats are **not** — they depend entirely on these toggles.
- **Competitor comparison:** Claude Code and GitHub Copilot have their own separate data-sharing controls. If your team uses multiple tools, audit each one — a fix in Codex does nothing for Claude or Copilot.

### Workarounds if You Can't Trust the Toggle
- **Use the API instead of the chat UI** for sensitive code — API data is excluded from training by default.
- **Use an Enterprise workspace** where training is contractually off.
- **Redact secrets before prompting** — never paste credentials, keys, or proprietary algorithms into any chat interface.
- **Route through a local model** (e.g., self-hosted open-weight models) for the most sensitive work.

## Frequently Asked Questions (FAQ)

### Did OpenAI really re-enable model training on Codex chats without permission?
Multiple users report the "Improve the model for everyone" setting was silently turned back on without their action. OpenAI has not issued a clear public statement confirming intent, so treat it as an unexplained reset and verify your own settings manually.

### How do I turn off data sharing for Codex?
Go to `chatgpt.com/settings/data-controls` and toggle off "Improve the model for everyone." Then also visit `privacy.openai.com/policies?modal=take-control` to opt out on the secondary consent page. Team/Enterprise admins should disable it at the workspace level too.

### Is my Codex code used for training if the toggle is off?
If the toggle is genuinely off and your plan excludes training (API/Enterprise), your data should not be used. But because the toggle has been observed resetting, verify it frequently and keep screenshots as documentation.

### Does disabling data sharing in ChatGPT also disable it for Codex?
Not necessarily — the settings are spread across multiple URLs and product surfaces. You must check each location independently; there is no single master switch.

## Final Verdict

**Check your settings today — do not assume your previous opt-out held.** The evidence points to a widespread, silent re-enable of model training on Codex chats, and for anyone handling proprietary code, that's an unacceptable default. The fix takes two minutes: disable the toggle at `chatgpt.com/settings/data-controls`, opt out again at the privacy portal, and have your admin lock it down at the org level. Then set a monthly reminder to re-verify, and move your most sensitive work to the API or a local model. Treat every privacy toggle as temporary until proven otherwise.