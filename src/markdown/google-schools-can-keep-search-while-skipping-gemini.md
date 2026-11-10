---
title: "Google Workspace for Education: Keep Search, Skip Gemini?"
description: "Google lets schools keep Search without Gemini, but AI search stays mandatory. Here's what admins can actually control and how to configure it."
pubDate: 2026-11-06
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Google Workspace for Education: What Schools Can Actually Turn Off

Google's updated Workspace for Education terms give K-12 and higher-ed admins a new toggle: you can keep classic Google Search for students while disabling Gemini app access — but the AI Overviews and AI Mode results layered *inside* Search remain non-negotiable. In plain terms, Google is offering schools a choice between "AI in Search" and "AI in Search plus the Gemini chatbot," not a choice between AI and no AI. This guide breaks down exactly which admin console settings map to which surfaces, what you can disable, and the workarounds districts are actually using in late 2026.

**The direct takeaway:** If your board or parent group wants "no generative AI in school accounts," Google Search cannot satisfy that requirement. You can turn off the Gemini app, Gemini in Classroom, and Gemini side panel — but AI Overviews and AI Mode in Search are bundled into the core Search product and are not exposed as a separate admin control.

## Which Admin Console Settings Control What

Here's the practical mapping of Google Admin console paths to the surfaces they affect, verified against the current Workspace for Education Admin help documentation:

| Surface | Admin Console Path | Can Schools Disable It? | Notes |
|---|---|---|---|
| Gemini app (chatbot) | Apps → Additional Google services → Gemini | **Yes** | Service on/off per OU; takes effect at next sign-in |
| Gemini side panel in Docs/Gmail | Apps → Additional Google services → Gemini | **Yes** | Same toggle as above |
| Gemini in Classroom | Apps → Additional Google services → Gemini | **Yes** | Follows the same OU-level service status |
| AI Overviews in Search | Not exposed | **No** | Bundled with Search; no separate kill switch |
| AI Mode (conversational Search) | Not exposed | **No** | Same — part of Search core |
| Search itself | Apps → Additional Google services → Search | **Yes** | Disabling Search also removes AI Overviews by default |

The key insight for admins: the only reliable way to remove AI Overviews from a student's experience is to disable Google Search entirely for that OU — which most districts won't do because Search is a core research tool. Everything else is a partial measure.

### Step-by-step: disable Gemini while keeping Search

1. Sign in to **admin.google.com** with a super admin account.
2. Navigate to **Apps → Additional Google services**.
3. Select the **Gemini** service card.
4. Choose the organizational unit (OU) — typically **Students** — from the left panel.
5. Set service status to **OFF** and click **Save**.
6. Repeat for any sub-OUs (e.g., Elementary, Middle, High) since settings don't cascade downward automatically in all configurations.
7. Verify by signing in as a test student account and confirming the Gemini app tile is gone from the app launcher and `gemini.google.com` returns an access-denied page.
8. Document the change in your change-management log with a timestamp — auditors and parent requests will ask for it.

Propagation typically takes **up to 24 hours** but is often immediate for new sign-ins. If a student still sees Gemini, have them sign out completely and clear the browser session; cached tokens can persist.

## Common Issues, Workarounds, and What You Should Know

**"AI Overviews still appear for students."** Expected. There is no OU-level control for AI Overviews. Your only levers are (a) disabling Search entirely, or (b) network-level filtering. Districts using content filters like GoGuardian, Lightspeed, or ContentKeeper can sometimes block the AI Overview rendering endpoint, but this is brittle and Google does not support it as a configuration method — expect breakage after Search front-end updates.

**"Parents are asking for a written guarantee."** You cannot give one that says "no AI in Search." You *can* provide a written statement that the Gemini app and Gemini in Classroom are disabled for the student OU, which is a defensible, verifiable claim.

**Cost angle.** The Gemini app toggle is free to change — there's no licensing implication for Education Fundamentals or Education Standard. Districts on Education Plus get Gemini included; turning it off doesn't reduce your per-seat cost, so there's no budget incentive either way.

**Alternatives worth evaluating if AI-free search is a hard requirement:**
- **Microsoft Bing with Copilot disabled** via tenant policy — Copilot can be turned off at the tenant level, and Bing's AI summaries have a more granular enterprise control story.
- **DuckDuckGo** — offers AI chat as an opt-in feature rather than default-on results.
- **Kiddle / SafeSearch front-ends** — limited, but some districts route elementary students through filtered front-ends that strip AI modules.

None of these replicate Google's index quality, which is why most districts are choosing to keep Search and accept AI Overviews while documenting the Gemini app shutdown.

## Frequently Asked Questions (FAQ)

### Can schools keep Google Search but disable Gemini?
Yes. In the Google Admin console, go to **Apps → Additional Google services → Gemini**, select the student OU, and set the service to OFF. Search remains fully functional for that OU. This is the exact configuration Google's updated Education terms describe.

### Are AI Overviews in Google Search optional for schools?
No. AI Overviews and AI Mode are part of the core Search product and are not exposed as a separate admin toggle. The only way to remove them via Google's own controls is to disable Search entirely for the OU.

### Does disabling Gemini affect Google Classroom or Drive?
No. Classroom assignments, Drive files, Docs, and Meet are unaffected. Only the Gemini app, Gemini side panel, and Gemini-in-Classroom features tied to that service toggle are removed.

### Is this change free for Education Fundamentals districts?
Yes. The Gemini service toggle is a configuration change with no licensing cost. Districts on Education Plus already have Gemini bundled and will not see a price reduction by disabling it.

### How long does the Gemini toggle take to apply?
Usually immediately for new sign-ins, but Google documents propagation of up to 24 hours. Force a full sign-out and clear browser sessions if students report lingering access.

## Final Verdict

If your district's goal is "no chatbot for students," the Gemini toggle delivers it cleanly and for free — flip it in the Admin console, document it, and move on. If your goal is "no generative AI in student search results," Google's current offering does not meet it, and no admin setting will get you there. In that case, your realistic options are network-level filtering (fragile), a competing search provider (lower quality), or a board-level policy conversation about what "AI-free" actually means in 2026. For most admins, the pragmatic play is: disable Gemini for student OUs today, keep Search, and put the AI Overviews limitation in writing so expectations are set before the next parent meeting.