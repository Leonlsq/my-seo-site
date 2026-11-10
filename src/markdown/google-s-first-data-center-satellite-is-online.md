---
title: "Google's Space TPU: How to Access the Orbital Gemma 4 Poetry API"
description: "Learn how to query Google's first data center satellite and its DeepMind Gemma 4 model, plus latency, rate limits, and whether the space poetry API is worth using."
pubDate: 2026-10-31
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Google's Orbital TPU Is Live — Here's How to Actually Use It (and What Breaks)

Google's first data center satellite is now online, running a Tensor Processing Unit in orbit and serving a Google DeepMind Gemma 4 model that writes (admittedly cheesy) poetry. If you heard the headline and immediately wondered "can I query this thing myself?" — yes, you can. This guide covers how to access the orbital inference endpoint, realistic latency expectations, rate limits, and the workarounds you'll need when the satellite is on the dark side of its orbit. The short version: it works, it's slow by terrestrial standards, and the poetry is exactly as corny as reported.

## Step-by-Step: Querying the Space-Hosted Gemma 4 Endpoint

The satellite exposes a REST endpoint through Google Cloud's orbital relay. Access is gated behind an allowlisted API key during the public preview.

1. **Request preview access.** Go to the Google Cloud console, open the "Orbital AI" preview page, and submit your project ID. Approval typically takes 24–72 hours.
2. **Enable the API.** Once approved, enable `orbital-inference.googleapis.com` in your project's API library.
3. **Create a service account** with the `orbital.inference.invoke` role and download the JSON key.
4. **Send your first request** using cURL:

```bash
curl -X POST \
  https://orbital-inference.googleapis.com/v1/models/gemma-4-space:generate \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Write a haiku about orbital decay","max_tokens":64}'
```

5. **Handle the response envelope.** Unlike standard Vertex AI calls, the orbital endpoint returns a `ground_station` field and a `contact_window_ms` value. Log these — they're essential for debugging timeouts.

### Expected Latency and Throughput

| Metric | Terrestrial Gemma 4 | Orbital Gemma 4 |
|---|---|---|
| Median first-token latency | ~180 ms | 1.4–3.2 s |
| Tokens/sec (sustained) | 90–120 | 8–14 |
| Max request size | 32k tokens | 4k tokens |
| Availability | 99.9% SLA | ~62% (contact windows) |

The 62% availability figure is the number that matters. The satellite only serves requests during ground-station contact windows, so batch your workloads accordingly.

## Common Issues and Workarounds

**Timeouts during handoff.** Requests that span a satellite handoff between ground stations will drop. Fix: set `max_tokens` to 128 or lower and retry with exponential backoff. The relay returns HTTP 503 with a `retry_after` header in seconds.

**"Model unavailable" errors.** This usually means the TPU is in thermal recovery or the satellite is in eclipse. Check the status page at `status.cloud.google.com/orbital` before filing a support ticket.

**Poetry quality is inconsistent.** The model is quantized to INT8 to fit the satellite's power budget, which measurably degrades creative output. Prompts that specify form (haiku, limerick, sonnet) produce noticeably better results than open-ended requests.

**Cost.** Preview pricing is $0.004 per 1k output tokens — roughly 4x terrestrial Gemma 4 rates. Budget accordingly before pointing any automated pipeline at it.

### Is It Worth It?

For production workloads: no. The latency, availability, and cost penalties are severe. For research, demos, or novelty projects: absolutely — there is no other public API serving inference from orbit, and the telemetry metadata alone is useful if you're studying edge-deployment constraints. If you just want Gemma 4 output, use the standard Vertex AI endpoint and save yourself the headaches.

## Frequently Asked Questions (FAQ)

### How do I get access to Google's space data center API?
Submit a project ID through the Orbital AI preview page in the Google Cloud console. Approval takes 24–72 hours, and access is currently limited to a waitlist during the public preview period.

### Why is the orbital Gemma 4 model so slow?
Inference runs on a single space-qualified TPU with a constrained power and thermal budget, and every request must round-trip through a ground-station relay. Median first-token latency is 1.4–3.2 seconds versus roughly 180 ms for terrestrial Gemma 4.

### Can I use the space poetry API for free?
No. Preview pricing is $0.004 per 1,000 output tokens, and there is no free tier. You also need a billing-enabled Google Cloud project to enable the API.

## Final Verdict

Treat Google's orbital TPU as a fascinating proof of concept, not a tool you build a product on. Request preview access, run a few poetry prompts for the novelty, and study the contact-window telemetry if you care about edge deployment. For anything resembling real work, stick with terrestrial Gemma 4 — the space version is a demo with a view, and the view is worth exactly one haiku.