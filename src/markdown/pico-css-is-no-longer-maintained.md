---
title: "Pico CSS Unmaintained? Best Alternatives to Migrate in 2026"
description: "Pico CSS is no longer maintained. Compare Bulma, Water.css, MVP.css and Tailwind, plus a step-by-step migration guide to keep your classless CSS site working."
pubDate: 2026-10-30
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Pico CSS Is No Longer Maintained: What Do You Do Now?

The maintainers of Pico CSS have confirmed in a pinned GitHub discussion (picocss/pico #754) that the project is **no longer actively maintained**. If you're one of the thousands of developers who shipped a site with `<link href="https://cdn.jsdelivr.net/npm/@picocss/pico">` and zero custom classes, you're now facing a fork in the road: freeze your dependency, self-host, or migrate to a maintained alternative.

The good news: Pico is a **classless CSS framework with a tiny API surface**. That means migration is usually a matter of swapping one stylesheet link and adjusting a handful of CSS variables — not a rewrite. This guide gives you the exact decision matrix, step-by-step migration instructions, and a comparison of the four best replacements so you can pick the right one in under an hour.

**Direct takeaway:** If your site is stable, pin your version and self-host — you can safely run Pico for years. If you need active security patches, new components, or accessibility fixes, migrate to **Bulma (class-based)** or **MVP.css / Water.css (classless drop-ins)**.

## Step-by-Step: How to Migrate Off Pico CSS

### Step 1 — Audit how deeply you use Pico

Run a quick grep across your templates to see whether you rely on Pico's utility classes or only its classless defaults:

```bash
# Find Pico-specific classes in your templates
grep -rE "(role=|\.container|\.grid|\.outline|\.contrast|data-theme)" ./src
```

- **Zero or near-zero matches** → you're using Pico purely classless. Migration to another classless framework is a 5-minute job.
- **Heavy matches** (`role="button"`, `.grid`, `.container`, `data-theme="dark"`) → you're using Pico's component layer. Prefer **Bulma** or **Tailwind**, which have equivalents.

### Step 2 — Pin and self-host your current version (safety net)

Before changing anything, lock the version you're running so a CDN update can't break your layout:

```html
<!-- Before: floating version risk -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">

<!-- After: pinned + local copy -->
<link rel="stylesheet" href="/assets/css/pico.min.css">
```

Download `pico.min.css` from the last release on npm (`npm pack @picocss/pico`) and commit it to your repo. This alone buys you **years of stability** since CSS has no runtime security surface.

### Step 3 — Swap the stylesheet for your chosen alternative

Replace the single `<link>` tag. For classless frameworks, no HTML changes are required:

```html
<!-- MVP.css (classless) -->
<link rel="stylesheet" href="https://unpkg.com/mvp.css">

<!-- Water.css (classless, auto dark mode) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
```

### Step 4 — Port your CSS custom properties

Pico exposes variables like `--pico-primary`, `--pico-font-family`, and `--pico-border-radius`. Map them to your new framework's tokens in a small override file:

```css
:root {
  --pico-primary: #0d6efd;   /* old Pico token */
  --brand: #0d6efd;          /* new token */
}
```

### Step 5 — Test dark mode and form controls

Pico auto-styled `<input>`, `<select>`, `<button>`, and `data-theme="dark"`. Verify these render correctly in your new framework — form controls are where 80% of migration bugs appear.

## Pico CSS Alternatives Compared (2026)

| Framework | Type | Maintained? | Size (min) | Best For |
|---|---|---|---|---|
| **Pico CSS** | Classless | ❌ No | ~40 KB | Legacy sites, freeze & self-host |
| **MVP.css** | Classless | ✅ Yes | ~10 KB | Minimal blogs, docs |
| **Water.css** | Classless | ✅ Yes | ~9 KB | Quick prototypes, auto dark mode |
| **Bulma** | Class-based | ✅ Yes | ~200 KB | Full component libraries |
| **Tailwind CSS** | Utility | ✅ Yes | ~10 KB (JIT) | Custom design systems |

**Key differences to weigh:**

- **MVP.css and Water.css** are the closest drop-in replacements for Pico's classless philosophy — you change one line and you're done.
- **Bulma** gives you the `.container`, `.grid`, and button classes Pico users often reach for, but requires adding class names to your HTML.
- **Tailwind** is the most future-proof but demands a build step and a mindset shift from "classless" to "utility-first."

## What You Should Know Before Migrating

- **Security risk is near zero.** CSS frameworks don't execute code. A frozen Pico build is safe to run indefinitely; the "unmaintained" label matters mainly for *feature* stagnation and browser-quirk fixes.
- **Browser drift is slow.** Expect Pico to render fine for **3–5 years** before new browser defaults cause visible issues.
- **Fork it if you're ambitious.** Pico is MIT-licensed — a community fork is plausible, so check for active forks before committing to a full migration.
- **Don't migrate mid-sprint.** If your site works today, schedule the swap for a low-traffic window and diff your screenshots with a tool like Playwright.

## Frequently Asked Questions (FAQ)

### Is Pico CSS safe to keep using now that it's unmaintained?
Yes. CSS has no executable attack surface, so a pinned, self-hosted Pico build is safe. The real risk is slow visual drift as browsers evolve, not security.

### What is the best drop-in replacement for Pico CSS?
For classless sites, **MVP.css** or **Water.css** are the closest matches — swap one `<link>` tag and your HTML stays untouched. For component-heavy sites, use **Bulma**.

### Will Pico CSS stop working on the CDN?
No. jsDelivr and unpkg serve existing versions indefinitely. However, pinning the exact version (`@picocss/pico@2.x.x`) prevents surprise breakage from future tag changes.

### Should I migrate to Tailwind instead?
Only if you want a custom design system and can adopt a build step. For simple content sites, Tailwind is overkill compared to a classless framework.

## Final Verdict

**Don't panic-migrate.** If your Pico site works, pin the version, self-host the CSS file, and keep shipping — you have years of runway. If you want active maintenance and new features, the smartest move in 2026 is a **one-line swap to MVP.css or Water.css** for classless projects, or **Bulma** if you depend on Pico's component classes. Reserve Tailwind for greenfield builds where you control the design from day one. Either way, the migration is measured in minutes, not weeks — the "unmaintained" headline is far scarier than the actual work.