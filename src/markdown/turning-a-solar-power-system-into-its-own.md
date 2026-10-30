---
title: "Solar Backup Power: Run Your Plant on Stored Heat or Combustion"
description: "How to turn a solar thermal plant into its own backup using stored heat or combustion. Step-by-step hybrid design, sizing tables, and troubleshooting tips."
pubDate: 2026-10-30
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## How to Turn a Solar Thermal Plant Into Its Own Backup (Stored Heat + Combustion)

Most solar plants go dark the moment clouds roll in or the sun sets — because they were never designed to run without direct sunlight. The fix isn't a bigger battery bank. It's a **hybrid dispatch design** where the plant runs on either stored solar heat *or* combustion, so it never depends on the sun being out. This guide walks you through the exact components, sizing math, and switching logic to make a solar thermal system self-backing, plus the failure points that trip up most DIY and small-commercial builds.

## Step-by-Step: Designing a Dual-Source Backup Plant

The core idea: capture solar heat into a thermal store (molten salt, thermal oil, or a water/steam accumulator), then add a combustion backup (biogas, natural gas, or biomass) that feeds the *same* steam or heat loop. One turbine, one generator, two heat sources.

### Step 1 — Size the thermal store for your target backup window

Thermal storage is the heart of "stored solar heat" backup. Use this rule of thumb for a steam-cycle plant:

| Storage Medium | Temp Range | Energy Density | Best For |
|---|---|---|---|
| Molten salt (nitrate) | 290–565 °C | ~250 kWh/tonne usable | Utility-scale, 4–12 hr backup |
| Thermal oil | 200–400 °C | ~120 kWh/tonne | Small commercial, 2–6 hr |
| Pressurized water | 100–180 °C | ~60 kWh/tonne | Micro plants, <2 hr |
| Concrete/rock bed | 200–400 °C | ~80 kWh/tonne | Low-cost retrofits |

**Sizing formula:** `Store capacity (kWh) = Plant output (kW) × backup hours ÷ cycle efficiency (0.25–0.35)`. A 100 kW plant needing 6 hours of backup needs roughly `100 × 6 ÷ 0.3 = 2,000 kWh` of usable thermal energy — about 8 tonnes of molten salt.

### Step 2 — Add the combustion backup on a shared loop

- **Biogas/biomass boiler:** feeds the same steam drum as the solar receiver. Lowest retrofit cost if you already have a boiler house.
- **Natural gas burner:** fastest ramp (under 5 min), but check local emissions rules.
- **Dual-fuel burner:** runs on biogas normally, switches to gas when the store drops below threshold.

Plumb the combustion source *downstream* of the thermal store so both feed the turbine through one control valve. This is what lets the plant "run on either" without a second generator.

### Step 3 — Wire the switching logic

Set a simple three-tier controller:

1. **Solar surplus (store > 80%):** charge store, turbine on solar only.
2. **Store 30–80%:** turbine draws from store; combustion on standby.
3. **Store < 30% or no solar input for 2 hr:** combustion kicks in automatically.

Use a PLC or a Raspberry Pi + Modbus setup for micro plants; industrial plants use a DCS with a deadband of ±5% to avoid burner chatter.

### Step 4 — Commission and test the failover

Run a **black-start test**: cut solar input, force the store to 25%, and confirm combustion ramps within your design time (target <10 min for gas, <30 min for biomass). Log the switchover.

## Common Issues, Alternatives, and What You Should Know

**Issue 1 — Store temperature stratification collapse.** If your molten salt tank mixes, you lose usable capacity fast. Fix: install a diffuser plate and keep flow rates under 1.5 m/s.

**Issue 2 — Combustion fouling the solar loop.** Biomass ash can coat heat exchanger tubes. Fix: isolate the combustion loop with a separate HX and add a soot blower.

**Issue 3 — Controller oscillation.** The burner short-cycles when the store hovers near threshold. Fix: widen the deadband and add a 15-minute minimum run time.

**Cost reality check:** A combustion backup adds roughly **$400–$900/kW** for gas and **$700–$1,400/kW** for biomass, versus **$150–$400/kWh** for lithium batteries. For backup windows over 4 hours, thermal + combustion wins on cost-per-kWh delivered — often by 3–5×. Batteries still win for sub-1-hour, fast-response needs.

**Alternative:** If you can't add combustion (permitting, fuel supply), a larger thermal store plus a small battery for parasitic loads gets you 60–70% of the way there.

## Frequently Asked Questions (FAQ)

### Can a solar thermal plant really run on stored heat alone overnight?
Yes — molten-salt plants routinely run 8–12 hours after sunset. The limit is store size and insulation, not the technology. Add combustion and you remove the time limit entirely.

### What's cheaper: combustion backup or more thermal storage?
For backup beyond ~4 hours, combustion is usually cheaper per kWh delivered. For 1–3 hours, extra storage often wins. Run the cost-per-kWh math for your specific fuel price before deciding.

### Do I need a second generator for the combustion backup?
No. The whole point of a shared-loop design is one turbine and one generator fed by two heat sources. A second generator only makes sense if you need true N+1 redundancy.

## Final Verdict

If you want a solar plant that never goes dark, **build the dual-source design from day one**: size the thermal store for your realistic backup window, plumb combustion into the same steam loop, and automate the three-tier switchover. Skip the second generator — spend that budget on storage insulation and a reliable controller instead. For plants under 100 kW, start with a pressurized-water store and a biogas boiler; for anything larger, molten salt plus a dual-fuel burner is the proven, cost-effective path.