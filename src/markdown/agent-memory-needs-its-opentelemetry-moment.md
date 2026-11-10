---
title: "Open Agent Memory Format: How to Adopt It (Setup Guide)"
description: "Step-by-step guide to the Open Agent Memory Format from LoreKit: schema, migration, and OTel-style tracing for AI agent memory. Includes code and pitfalls."
pubDate: 2026-11-08
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What Is the Open Agent Memory Format (and Why Should You Care)?

The "Agent memory needs its OpenTelemetry moment" debate—sparked by LoreKit's Open Agent Memory Format proposal and a 127-point Hacker News thread—boils down to one practical problem: **every AI agent framework stores memory differently, so you can't inspect, migrate, or debug it across tools.** The Open Agent Memory Format (OAMF) is an attempt to standardize how agents persist facts, episodes, and embeddings into a portable, traceable schema—much like OpenTelemetry standardized observability.

Here's the direct takeaway: **you don't need to wait for industry consensus to benefit.** You can adopt the core ideas today—a normalized memory record schema plus trace IDs on every write—and get cross-framework portability and debuggability in a single afternoon. This guide walks you through the schema, a migration script, and the pitfalls that will bite you if you skip validation.

## Step-by-Step: Adopting a Portable Agent Memory Schema

The OAMF concept centers on a **memory record** with a stable, framework-agnostic shape. Below is a practical schema you can implement immediately, followed by migration steps.

### Step 1: Define the normalized memory record

Every memory entry should be self-describing. Use this minimum viable schema:

| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| `memory_id` | UUIDv7 | Yes | Sortable, globally unique ID |
| `agent_id` | string | Yes | Which agent wrote it |
| `session_id` | string | Yes | Conversation/run grouping |
| `trace_id` | string (W3C) | Yes | Links memory to an OTel span |
| `kind` | enum | Yes | `fact`, `episode`, `preference`, `summary` |
| `content` | text | Yes | Human-readable payload |
| `embedding` | float[] | No | Vector for retrieval |
| `source_ref` | URI | No | Provenance (doc, URL, message ID) |
| `created_at` | RFC 3339 | Yes | Timestamp with timezone |
| `ttl_seconds` | int | No | Expiry for ephemeral memory |
| `confidence` | float 0–1 | No | Extraction reliability score |

The `trace_id` field is the "OpenTelemetry moment" in practice: it lets you join a memory write to the exact LLM call, tool invocation, or user message that produced it.

### Step 2: Instrument writes with trace context

Wrap your memory store's `write()` behind a helper that pulls the active span context:

```python
from opentelemetry import trace
import uuid, datetime

def write_memory(store, agent_id, session_id, kind, content, **kw):
    span = trace.get_current_span()
    ctx = span.get_span_context()
    record = {
        "memory_id": str(uuid.uuid7()),
        "agent_id": agent_id,
        "session_id": session_id,
        "trace_id": format(ctx.trace_id, "032x"),
        "kind": kind,
        "content": content,
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        **kw,
    }
    store.upsert(record)
    return record["memory_id"]
```

If your framework lacks UUIDv7, use `uuid4()` now and backfill ordering via `created_at`—but note UUIDv7 gives you time-ordered pagination for free.

### Step 3: Migrate existing memory

1. **Export** your current store (Mem0, LangChain `VectorStore`, custom JSON, etc.) to NDJSON.
2. **Map** fields: `user_id` → `agent_id`, `timestamp` → `created_at`, free-text → `content` with `kind: "fact"` as default.
3. **Backfill `trace_id`** with a sentinel like `00000000000000000000000000000000` for legacy records, then flag them `legacy: true`.
4. **Validate** with a JSON Schema check before re-importing—reject records missing `memory_id`, `agent_id`, or `created_at`.
5. **Dual-write** for one release cycle: write to both old and new stores, diff counts nightly, then cut over.

### Step 4: Add retrieval-time tracing

Log the `memory_id`s returned by each retrieval call as span attributes (`memory.retrieved_ids`). This is the highest-value payoff: when an agent gives a wrong answer, you can trace backward from the response span to the exact memories that influenced it.

## Common Pitfalls, Alternatives, and What You Should Know

**Pitfall 1: Treating embeddings as portable.** Vectors from different models are not comparable. Store `embedding_model` alongside `embedding` or you'll silently corrupt retrieval after a model swap.

**Pitfall 2: Unbounded `content` growth.** Summaries of summaries bloat fast. Enforce a `content` byte cap (e.g., 8 KB) and route longer material to `source_ref`.

**Pitfall 3: TTL collisions.** Agents writing `ttl_seconds: 0` meaning "never expire" vs. "expire now" is a classic ambiguity—define `null` as permanent, `0` as invalid.

**Alternatives to a full OAMF rollout:**

- **Mem0 / Zep native schemas** — faster to start, but lock you into one vendor's retrieval semantics.
- **LangGraph checkpointers** — great for state, weak for long-term facts.
- **Raw Postgres + pgvector** — maximum control, but you own the schema discipline yourself.

**Cost note:** adding a `trace_id` column and span attributes is effectively free at the storage layer; the real cost is OTel backend ingestion (typically $0.10–$0.30 per GB at hosted vendors). Sample 10–20% of spans if volume is a concern.

## Frequently Asked Questions (FAQ)

### What is the Open Agent Memory Format?
It's a proposed portable schema for AI agent memory—normalizing facts, episodes, and embeddings with trace IDs so memory can be inspected, migrated, and debugged across frameworks, analogous to how OpenTelemetry standardized traces and metrics.

### Is the Open Agent Memory Format an official standard yet?
No. As of the LoreKit proposal and the associated Hacker News discussion, it's a community specification draft, not a ratified standard. Adopt the schema ideas now, but version your records (`schema_version` field) to survive breaking changes.

### How is this different from just using OpenTelemetry?
OTel defines telemetry signals (traces, metrics, logs) but says nothing about memory record structure. OAMF borrows OTel's trace-context discipline and applies it to memory payloads—the two are complementary, not competing.

### Can I use this with LangChain or Mem0?
Yes, via an adapter layer: map their internal records to the normalized schema on write and back on read. Dual-write during migration to avoid data loss.

## Final Verdict

Don't wait for a ratified standard—**adopt the three highest-leverage pieces of the Open Agent Memory Format today**: a normalized record schema, W3C `trace_id` on every memory write, and retrieval-time span logging. That combination alone will cut your agent debugging time dramatically and make future migration to whatever standard wins nearly painless. If you're on a single framework with low stakes, a lightweight adapter is enough; if you run multi-agent systems in production, invest in the full schema plus validation now—your future self, staring at a wrong answer with no trace, will thank you.