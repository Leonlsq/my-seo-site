---
title: "CNC Stone Carving: Is It Worth It? Cost & Setup Guide"
description: "Thinking about CNC stone carving? Get real costs, bit specs, dust control setup, and whether it beats hand carving for your project."
pubDate: 2026-10-28
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## CNC Stone Carving: What It Actually Costs and Whether It's Worth It

The Carmelite Gothic article on CNC stone carving (235 points, 79 comments on Hacker News) struck a nerve because it answers a question most makers quietly ask: **can a CNC router really cut stone, and is it worth the hassle?** Short answer: yes, but only if you accept three hard constraints — dust control is non-negotiable, your machine needs water cooling or a sealed spindle, and soft stone (soapstone, limestone, marble) is the realistic starting point. Granite will eat your bits and your budget. Below is a practical setup guide with real numbers so you can decide before you spend a dime.

## Step-by-Step: Setting Up for CNC Stone Carving

### 1. Pick the Right Stone (This Determines Everything)
| Stone | Mohs Hardness | CNC Feasibility | Notes |
|---|---|---|---|
| Soapstone | 1–2.5 | Excellent | Best beginner stone; carves like hard wood |
| Alabaster | 1.5–2 | Excellent | Dust is hazardous — respirator mandatory |
| Limestone | 3–4 | Good | Common for architectural work; affordable |
| Marble | 3–4 | Good | Slower feeds; beautiful finish |
| Granite | 6–7 | Poor | Requires diamond tooling, flood coolant, industrial rig |

### 2. Match Your Machine
- **Minimum:** a rigid CNC router (Shapeoko-class or better) with a **sealed, water-cooled spindle** — not a trim router. Stone dust kills air-cooled routers fast.
- **Better:** a gantry mill with flood or mist coolant and a steel frame.
- **Budget reality:** expect $2,000–$6,000 for a hobby-viable setup including dust extraction, versus $15k+ for production-grade stone CNC.

### 3. Tooling Specs That Work
- **Diamond-coated burrs** for marble/limestone: 6mm–12mm shank, 3–6 flutes.
- **Feed rates:** start at 400–800 mm/min with 0.5–1mm depth of cut on limestone; halve for marble.
- **Spindle speed:** 8,000–12,000 RPM for diamond burrs; higher RPMs generate heat that glazes soft stone.
- **Cooling:** mist coolant or a constant water drip at the cut point. Dry cutting soft stone is possible but generates silica dust.

### 4. Dust and Slurry Control (The Part People Skip)
- Stone dust contains **crystalline silica** — a serious respiratory hazard. You need:
  - A wet-cutting setup (slurry, not airborne dust) OR
  - A HEPA-rated extractor rated for fine particulate, plus N95/P100 respirator.
- Build a **water tray or dam** around the workpiece. Slurry is easier to contain than dust and extends bit life dramatically.

### 5. Workholding and CAM
- Stone is heavy and brittle: use a **sacrificial MDF bed** plus wedges and hot glue, not clamps that crush edges.
- In your CAM software (Fusion 360, VCarve, Carveco), use **adaptive clearing** with light radial engagement — stone hates full-width slotting.
- Leave 0.3–0.5mm for a finishing pass; diamond burrs leave visible tool marks otherwise.

## Common Issues, Alternatives, and What You Should Know

**Issue: bits overheat and glaze.** Cause: too-high RPM, no coolant, or dwelling in one spot. Fix: lower spindle speed, add mist, keep the tool moving.

**Issue: chipping at edges.** Cause: too-aggressive depth of cut or dull tooling. Fix: 0.5mm depth passes and a fresh burr for finishing.

**Issue: dust everywhere.** Cause: dry cutting. Fix: switch to wet cutting — it's cheaper than a hospital visit.

**Alternatives worth considering:**
- **Hand carving** — slower but zero capital cost and better for one-off organic shapes.
- **Sandblasting with rubber stencils** — cheaper for flat lettering and shallow relief.
- **Waterjet + hand finishing** — better for through-cuts in hard stone.
- **Hiring a stone shop** — often cheaper than buying equipment for a single project.

**Cost analysis for a first project:** machine amortization aside, expect $150–$400 in diamond tooling, $100–$300 in stone blanks, and $200+ in dust/coolant gear. If your project is one garden plaque, pay a shop. If you're doing repetitive architectural elements, the CNC pays for itself in 3–5 jobs.

## Frequently Asked Questions (FAQ)

### Can a regular CNC router cut stone?
Only soft stone (soapstone, alabaster, limestone) and only with a sealed spindle, diamond tooling, and dust or slurry control. Standard wood routers with air-cooled trim routers will fail — the dust destroys bearings and motors.

### Is CNC stone carving cheaper than hand carving?
For one-off pieces, no — equipment and tooling costs dominate. For repetitive work like balusters, plaques, or relief panels, CNC becomes cheaper after roughly 3–5 projects and delivers consistent geometry hand carving can't match.

## Final Verdict

**Worth it if:** you're producing repetitive architectural or decorative stonework and can commit to wet cutting and diamond tooling. Start with soapstone on a rigid router, budget $3,000–$5,000 all-in, and treat dust control as part of the machine cost — not an accessory. **Skip it if:** you're making a single piece or working in granite; hire a stone shop or carve by hand instead. The Carmelite Gothic write-up is right that the craft is viable — but the barrier isn't the CNC, it's the silica and the tooling budget.