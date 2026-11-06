---
title: "Axiom Math AI Proofs: How to Verify Math Without Slop"
description: "How to use Axiom Math's formal verification agents to check AI-generated proofs, avoid math slop, and set up Lean 4 verification workflows."
pubDate: 2026-11-06
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Keep AI Slop Out of Your Math: A Practical Verification Workflow

AI models now generate mathematical proofs faster than any human can read them—and a disturbing share of those proofs are subtly wrong. Axiom Math's recent milestone, where its AI agents formally verified the entire Stacks Project (one of algebraic geometry's largest and most cited libraries), signals a turning point: verification is becoming the bottleneck, not generation. This guide shows you exactly how to set up a formal verification pipeline so you can use AI proof assistants without letting slop into your work. The takeaway up front: never trust a natural-language proof from an LLM—route every claim through a proof checker like Lean 4, and treat Axiom-style agent verification as your quality gate.

## Step-by-Step: Building a Verification-First Math Workflow

Here is a concrete pipeline you can run today, modeled on how Axiom Math's agents approach large libraries.

### Step 1 — Choose your proof assistant
| Tool | Best For | Learning Curve | Ecosystem |
|------|----------|----------------|-----------|
| Lean 4 + Mathlib | Research math, large libraries | Steep | Huge, active |
| Coq/Rocq | Type theory, CS proofs | Steep | Mature |
| Isabelle/HOL | Automation-heavy proofs | Moderate | Strong |
| Agda | Dependent types | Very steep | Niche |

For most users chasing the Axiom Math workflow, **Lean 4 with Mathlib** is the default—it is the same ecosystem where formal verification of large corpora like the Stacks Project is meaningful.

### Step 2 — Generate, then immediately formalize
1. Ask your LLM for the proof **and** a Lean 4 skeleton simultaneously.
2. Paste the skeleton into a `.lean` file.
3. Run `lake build` to type-check. Any `sorry` placeholder is a red flag—it means the proof is incomplete.
4. Count `sorry`s with: `grep -r "sorry" ./YourFile.lean | wc -l`. Zero is the only acceptable target.

### Step 3 — Run an automated checker
- Use `lean --make` or the Mathlib CI pipeline.
- For agent-style batch verification, script a loop that compiles each theorem file independently and logs failures.
- Reject any proof that compiles only with `admit`, `sorry`, or `axiom` injections—these are the formal equivalent of AI slop.

### Step 4 — Audit assumptions
Even a compiling proof can be wrong if it smuggles in a false axiom. Run:
- `#print axioms your_theorem` in Lean to list every axiom a proof depends on.
- Confirm nothing beyond `propext`, `Classical.choice`, and `Quot.sound` (the standard Lean axioms) appears.

### Step 5 — Log and version
Keep a verification log per theorem: model used, prompt, compile result, axiom audit. This is exactly the discipline Axiom Math's agents apply at scale across the Stacks Project.

## Common Issues, Alternatives, and What You Should Know

**Issue: The proof compiles but is meaningless.** A theorem can be vacuously true (e.g., `False → anything`). Always check the *statement*, not just the proof. Have a second model restate the theorem in plain English and compare.

**Issue: Hallucinated lemmas.** LLMs invent lemma names that don't exist in Mathlib. Fix: run `#check lemma_name` before trusting any citation. If it errors, the lemma is fake.

**Issue: Version drift.** Mathlib changes fast; a proof that compiled last month may break. Pin your toolchain with `lean-toolchain` and update deliberately.

**Alternatives to Axiom-style agent verification:**
- **Manual peer review** — accurate but slow, the exact bottleneck Axiom is trying to solve.
- **Informal LLM self-critique** — cheap but unreliable; models confidently approve their own errors.
- **Hybrid** — agent generates, formal checker validates, human audits axioms. This is the current best practice.

**Cost reality check:** Formal verification is compute-heavy. Batch-verifying a large library can take hours of CI time. Budget for it—cheap generation plus expensive verification is still far cheaper than publishing a wrong theorem.

## Frequently Asked Questions (FAQ)

### What is Axiom Math and why does formal verification matter?
Axiom Math is a startup building AI agents that formally verify mathematical proofs. Its agents recently verified the Stacks Project, a massive algebraic geometry library, demonstrating that automated checking can scale to real research mathematics—filtering out unchecked AI-generated "slop."

### Can I verify AI-generated proofs for free?
Yes. Lean 4, Mathlib, and Coq are open-source and free. The main cost is compute time and the learning curve. You can run a local Lean toolchain and type-check proofs at zero licensing cost.

### How do I know if an AI math proof is wrong?
Run it through a proof assistant. If it fails to compile, contains `sorry`/`admit`, or depends on non-standard axioms (check with `#print axioms`), treat it as unverified. Natural-language plausibility is not evidence of correctness.

### What is the Stacks Project and why is verifying it a big deal?
The Stacks Project is one of the largest open libraries of algebraic geometry, spanning thousands of pages. Formally verifying it end-to-end is a landmark because it proves automated agents can handle library-scale mathematics, not just toy problems.

## Final Verdict

If you use AI for mathematics, adopt a verification-first workflow today: generate with an LLM, but gate every result through Lean 4 or Coq, audit your axioms, and log everything. Axiom Math's Stacks Project milestone proves the tooling is ready—the discipline is now on you. Never publish or rely on an unverified AI proof; in math, "looks right" and "is right" are worlds apart, and formal verification is the only reliable bridge between them.