---
title: "GLM-5.3 KV Cache Exposure: How to Fix & Secure Workers AI"
description: "Cloudflare patched a cross-request KV cache leak in GLM-5.3 Workers AI. Here's how to audit your Worker, rotate keys, and prevent cache bleed."
pubDate: 2026-10-27
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## GLM-5.3 KV Cache Exposure: What Happened and How to Fix It

Cloudflare disclosed a cross-request KV cache exposure affecting the **GLM-5.3 model on Workers AI**, where cached key-value tensors from one request could leak into another user's inference session. If you run a Cloudflare Worker that calls `@cf/zhipu/glm-5.3` (or any GLM-family model), this guide gives you the exact remediation steps, an audit checklist, and the config changes needed to eliminate cache bleed. The short takeaway: **Cloudflare has already patched the platform layer**, but your Worker code, cache keys, and API tokens still need a manual review — and most teams haven't done it yet.

## Step-by-Step Remediation Guide

The exposure stemmed from how the inference runtime scoped KV cache entries. Under concurrent load, a cache key collision could return a previously computed attention cache from a *different* request. That means prompt fragments, system instructions, or partial completions from another tenant could theoretically surface in a response. Here's how to lock down your deployment.

### Step 1: Confirm Your Runtime Version
1. Open your `wrangler.toml` (or `wrangler.jsonc`).
2. Check the `compatibility_date`. Anything **before 2026-10-20** may run on the pre-patch inference path.
3. Bump it explicitly:
   ```toml
   compatibility_date = "2026-10-27"
   ```
4. Redeploy with `npx wrangler deploy` and verify the version in the dashboard under **Workers & Pages → your-worker → Deployments**.

### Step 2: Audit Every GLM-5.3 Call Site
Search your codebase for all model invocations and confirm each one passes an explicit, unique session identifier:

```js
const response = await env.AI.run("@cf/zhipu/glm-5.3", {
  messages: [...],
  // REQUIRED post-patch: bind cache scope to the request
  headers: { "x-session-id": crypto.randomUUID() },
});
```

**Red flags to grep for:**
- Hardcoded `sessionId`, `cacheKey`, or `conversationId` values.
- Shared module-level variables holding conversation state across requests.
- Missing `x-session-id` headers on any GLM call.

### Step 3: Rotate Credentials
If your Worker logged raw prompts or responses during the exposure window, treat those logs as potentially contaminated.
- Rotate your **Workers AI API token** in the Cloudflare dashboard.
- Invalidate any downstream session tokens derived from model output.
- Purge Worker logs older than the patch date if they contain user PII.

### Step 4: Add a Cache-Scoping Guardrail
Wrap your inference calls in a helper that enforces isolation:

```js
async function safeInfer(env, messages, userId) {
  if (!userId) throw new Error("Missing user scope");
  return env.AI.run("@cf/zhipu/glm-5.3", {
    messages,
    headers: { "x-session-id": `${userId}:${crypto.randomUUID()}` },
  });
}
```

### Step 5: Verify With a Concurrency Test
Fire 50+ simultaneous requests with distinct system prompts and assert no response contains another request's marker string. A simple loop with `Promise.all` and a unique token per prompt is enough to catch residual bleed.

## Common Issues, Alternatives, and What You Should Know

| Concern | Status After Patch | Your Action |
|---|---|---|
| Platform-level cache collision | Fixed by Cloudflare | Update `compatibility_date` |
| App-level shared session state | **Still your responsibility** | Audit + refactor |
| Logged contaminated prompts | Not auto-purged | Rotate + purge logs |
| Other GLM-family models | Assessed, no exposure reported | Monitor changelog |

**Alternatives if you need stricter isolation today:**
- **Per-tenant model instances** — route each customer to a dedicated Worker with its own binding, eliminating shared cache scope entirely.
- **Stateless prompting** — resend full context each call instead of relying on server-side conversation caching (higher token cost, zero cache risk).
- **Switch models** — Llama or Mistral endpoints on Workers AI were unaffected, but you lose GLM-5.3's multilingual strengths.

**Cost note:** Stateless prompting can raise token spend 2–4× on long conversations. For most apps, the session-ID fix is the better tradeoff.

## Frequently Asked Questions (FAQ)

### Was my data actually exposed by the GLM-5.3 KV cache bug?
Only if you ran GLM-5.3 on Workers AI with concurrent traffic and shared or missing session identifiers **before the October 2026 patch**. Cloudflare states the window was limited, but you should assume any un-scoped call was at risk and rotate credentials.

### Do I need to change my code after Cloudflare's fix?
Yes. The platform patch stops the runtime-level collision, but Workers that reuse module-level conversation state or hardcoded cache keys can still bleed data between requests. Add a unique `x-session-id` per request and redeploy with `compatibility_date = "2026-10-27"`.

### Is GLM-5.3 still safe to use on Workers AI?
Yes — post-patch it's safe **provided** you scope sessions correctly. The model itself wasn't compromised; the issue was cache key scoping in the inference layer, which is now fixed.

### How do I test whether my Worker still leaks cache data?
Run a concurrency test: send 50+ parallel requests, each with a unique marker string in the system prompt, then scan all responses for foreign markers. Any hit means your session scoping is still broken.

## Final Verdict

**Update your `compatibility_date`, add per-request session IDs, and rotate tokens today.** Cloudflare's patch closes the platform hole, but the majority of real-world risk now lives in application code that shares cache state across users. The fix takes under an hour for a typical Worker and eliminates the entire class of cross-request exposure. If you maintain a high-traffic or multi-tenant GLM-5.3 deployment, go further: add the concurrency test to CI so any future regression fails the build before it reaches production.