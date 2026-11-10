---
title: "DOOMFORMER Explained: How to Run a Transformer in DOOM"
description: "Learn how DOOMFORMER turns DOOM into a transformer. Step-by-step setup, performance benchmarks, and why it is 65,000x slower than NumPy."
pubDate: 2026-10-30
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## DOOMFORMER Explained: What It Is and How to Try It

DOOMFORMER is a project that uses DOOM game mechanics—including voodoo dolls and DOOM's Turing-complete logic—to perform the matrix math behind a transformer neural network. Instead of running DOOM on a neural net, the creator ran the neural net *on DOOM*. The result is a working (if extremely slow) alternative to NumPy that can classify MNIST digits, generate maps, and even play DOOM itself. This guide breaks down what DOOMFORMER actually does, how to set it up, what hardware you need, and whether it is worth your time in 2026.

The direct takeaway: DOOMFORMER is a brilliant technical flex and a fun weekend project, but it is roughly **65,000x slower than NumPy**. Use it to learn how transformers work at the lowest level, not for any production workload.

## DOOMFORMER Setup: Step-by-Step Guide

Because DOOMFORMER is a hobby/research project rather than a polished app, setup requires a specific toolchain. Here is the practical path to getting it running.

### Prerequisites
- **A DOOM source port** that supports scripting and voodoo doll mechanics (the project relies on classic DOOM engine behavior).
- **A WAD editor** (e.g., SLADE or Doom Builder) to load the generated maps.
- **Python 3.10+** for the glue scripts that translate tensor operations into DOOM map geometry.
- **A modern CPU** — GPU acceleration does not apply here; everything runs through the DOOM engine loop.

### Setup Steps
1. **Clone the repository** and read the README fully — the build process is non-standard.
2. **Install dependencies** listed in the project's requirements file (NumPy is ironically still needed for comparison benchmarks).
3. **Build the WAD files** that encode the transformer weights as map geometry.
4. **Launch your DOOM port** and load the generated WAD.
5. **Run the MNIST demo first** — it is the simplest test case and confirms your pipeline works.
6. **Scale up** to the map-generation and self-play demos once MNIST classification succeeds.

### What DOOMFORMER Can Actually Do
| Capability | Description | Practical Use |
|---|---|---|
| MNIST classification | Recognizes handwritten digits, even when drawn on the map itself | Learning demo |
| Text generation | "Talks" (kinda) via token prediction | Novelty |
| Decision-making | Plays DOOM by controlling the marine's "mind" | Research curiosity |
| Map generation | DOOMFORMER generates maps that DOOM then plays on | Experimental |

## Performance Reality Check: DOOMFORMER vs NumPy

The headline number matters: DOOMFORMER is about **65,000x slower** than NumPy for equivalent operations. Here is what that means in practice.

- **A single forward pass** that takes milliseconds in NumPy can take minutes in DOOMFORMER.
- **MNIST classification** of one digit is feasible; training from scratch is not.
- **Map generation** is the most practical demo because it tolerates long runtimes.
- **Memory** is constrained by DOOM engine limits, not your RAM.

If you want to understand *why* it is slow, the answer is architectural: every arithmetic operation is encoded as a DOOM game mechanic (voodoo doll movement, monster behavior, sector triggers) rather than a CPU instruction. That is the whole point—and the whole cost.

## Common Issues and What You Should Know

- **"It won't load my WAD."** Verify your source port matches the one the project targets; voodoo doll behavior differs between ports.
- **"The demo hangs."** Long runtimes are expected. Let MNIST classification run for several minutes before assuming a crash.
- **"Can I use this for real ML work?"** No. Treat DOOMFORMER as an educational artifact, not a framework.
- **Alternatives:** If you want fast transformer math, use PyTorch or NumPy. If you want DOOM-based computing curiosities, explore other Turing-complete-in-DOOM projects.

## Frequently Asked Questions (FAQ)

### What is DOOMFORMER?
DOOMFORMER is a project that implements a transformer neural network using DOOM game mechanics, including voodoo dolls, to perform the required math. It is an alternative to NumPy that is roughly 65,000x slower.

### Is DOOM really Turing complete?
Yes. DOOM's logic and map mechanics are Turing complete, which is exactly what makes DOOMFORMER possible—the engine can simulate arbitrary computation.

### Can DOOMFORMER play DOOM by itself?
Yes. One demo lets DOOMFORMER make decisions that control the marine, effectively playing DOOM on maps that DOOMFORMER itself generated.

### How slow is DOOMFORMER compared to NumPy?
Approximately 65,000x slower. It is a proof of concept, not a performance tool.

## Final Verdict

DOOMFORMER is not something you install to get work done—it is something you install to *understand* work at its most absurd and fundamental level. If you are a developer curious about transformers, DOOM internals, or Turing-complete game engines, it is absolutely worth a weekend. If you need actual ML performance in 2026, stick with PyTorch and NumPy, and enjoy DOOMFORMER as the brilliant flex it is.