---
title: "How to Make Any Website Printable: 5 Fixes for Cluttered Pages"
description: "Learn how to make websites printable using reader mode, CSS print styles, and browser tweaks. Fix cluttered pages and save clean PDFs in minutes."
pubDate: 2026-10-26
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why Websites Should Be Printable (And How to Fix the Ones That Aren't)

A developer's essay arguing that "websites should be printable" recently hit the front page of Hacker News, racking up 218 points and 156 comments—and for good reason. Anyone who has tried to print a recipe, a return policy, or a technical tutorial has watched in horror as navigation bars, cookie banners, and sticky ads devour half the page while the actual content gets chopped mid-sentence.

The core argument is simple: the web's print medium is broken by default, and it doesn't have to be. Whether you're a frustrated user trying to save a clean PDF or a developer who wants to ship print-friendly pages, this guide gives you concrete fixes. Below you'll find browser-level workarounds you can use in under 60 seconds, plus the exact CSS a site owner needs to make printing work properly.

**The direct takeaway:** Most "unprintable" pages can be tamed with Reader Mode or a print stylesheet. If you control the site, a 20-line `@media print` block solves 90% of the problem.

## Step-by-Step Fixes: Make Any Website Printable

### Fix 1: Use Reader Mode (Fastest, No Extensions)

Every major browser now ships a distraction-free reader view that strips navigation, ads, and sidebars before printing.

1. **Firefox:** Click the document icon in the address bar (or press `Ctrl+Alt+R` / `Cmd+Alt+R`). Then `Ctrl+P` to print.
2. **Safari:** Click the **Reader** button (or press `Shift+Cmd+R`), then `Cmd+P`.
3. **Edge:** Click the book icon in the address bar, then `Ctrl+P`.
4. **Chrome:** Reader Mode is hidden. Go to `chrome://flags`, search **"Reader Mode"**, enable it, and relaunch. A book icon will appear on supported pages.

Reader Mode works on article-style pages (blogs, news, docs) but fails on app-like pages, forums, and e-commerce product grids.

### Fix 2: Toggle "Simplify Page" in the Print Dialog

In Edge and Chrome, the print preview itself offers cleanup:

- **Edge:** In the print preview, toggle **Simplify page** on. It re-renders the page without clutter.
- **Chrome:** No native toggle, but selecting **"Save as PDF"** as the destination and unchecking **Headers and footers** removes URL/date junk.
- **Firefox:** In the print dialog, check **Simplify Page** to apply reader styling automatically.

### Fix 3: Use a Print-Cleanup Extension

If you print regularly, install a dedicated tool:

| Extension | Browser | What It Does | Free? |
|---|---|---|---|
| Print Friendly & PDF | Chrome, Firefox, Edge | Delete elements by clicking them, adjust font size, save PDF | Yes |
| Just Read | Chrome | Customizable reader mode with print support | Yes |
| Reader View | Firefox (built-in) | One-click clean view | Yes |

Print Friendly is the standout: it lets you click any element (ads, sidebars, footers) to delete it before printing, and it auto-removes common junk.

### Fix 4: For Developers — Add a `@media print` Stylesheet

This is the real fix the Hacker News thread was arguing for. Add this block to your site's CSS:

```css
@media print {
  /* Hide non-essential UI */
  nav, footer, aside, .sidebar, .cookie-banner,
  .ad, .newsletter-signup, .social-share, video, iframe {
    display: none !important;
  }

  /* Clean typography for paper */
  body {
    font-size: 12pt;
    color: #000;
    background: #fff;
    line-height: 1.5;
  }

  /* Show link URLs after link text */
  a[href]::after {
    content: " (" attr(href) ")";
    font-size: 9pt;
    color: #555;
  }

  /* Prevent awkward page breaks */
  h1, h2, h3 { page-break-after: avoid; }
  img, table, pre { page-break-inside: avoid; }
  img { max-width: 100% !important; }

  /* Remove shadows and backgrounds that waste ink */
  * { box-shadow: none !important; text-shadow: none !important; }
}
```

**Why each rule matters:**

- `display: none` on `nav`, `footer`, and `.cookie-banner` eliminates the biggest offenders.
- `a[href]::after` prints the URL, so a printed article remains useful offline.
- `page-break-inside: avoid` on images and tables stops content from splitting across pages.
- `font-size: 12pt` is the standard print body size; `pt` units map correctly to paper.

### Fix 5: Test and Debug Your Print Styles

1. Open Chrome DevTools (`F12`).
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P`) and type **"Show Rendering"**.
3. In the Rendering panel, set **Emulate CSS media** to **print**.

You'll see exactly what the printer sees, live. Iterate on your `@media print` rules until the layout is clean.

## Common Issues, Alternatives, and What You Should Know

**"My print preview is blank."** This usually means the page relies on JavaScript-rendered content that doesn't fire in print mode, or a `@media print { display: none }` rule is hiding the wrong container. Check DevTools' print emulation (Fix 5) to isolate the culprit.

**"Images are cut off."** Add `img { max-width: 100% !important; height: auto; }` and `page-break-inside: avoid` to your print CSS.

**"Dark mode prints as a black page."** Many sites invert colors for dark mode but don't reset them for print. Force `background: #fff !important; color: #000 !important;` inside your `@media print` block.

**Alternatives to printing:** If you just need offline access, "Save as PDF" via the browser's print dialog is often cleaner than a physical print. For long reads, Pocket and Instapaper both strip clutter and export to PDF or e-reader formats.

**The cost angle:** Printing full-color pages with ad banners can waste 30–50% more ink than a clean print. Reader Mode or a print stylesheet isn't just tidier—it's cheaper.

## Frequently Asked Questions (FAQ)

### How do I print a website without ads and menus?
Use Reader Mode in Firefox, Safari, or Edge (book/document icon in the address bar), or install the Print Friendly & PDF extension in Chrome. Both strip navigation, ads, and sidebars before the print dialog opens.

### How do I make my own website print-friendly?
Add an `@media print` CSS block that hides `nav`, `footer`, `aside`, and ad containers with `display: none`, sets body text to `12pt` black-on-white, and uses `page-break-inside: avoid` on images and tables. Test it with Chrome DevTools' "Emulate CSS media: print" setting.

### Why does a website print as a blank page?
Usually the content is rendered by JavaScript that doesn't execute in print mode, or a print stylesheet hides the main container by mistake. Open DevTools, emulate print media, and inspect which element is being hidden.

### Is Reader Mode available in Chrome?
Not by default. Enable it via `chrome://flags` by searching "Reader Mode" and setting it to Enabled, then relaunch Chrome. A book icon will appear in the address bar on supported article pages.

## Final Verdict

The "websites should be printable" argument is correct, but you don't have to wait for site owners to fix it. **For everyday users:** Reader Mode plus Print Friendly covers nearly every scenario in under a minute. **For developers:** the 20-line `@media print` block above is the single highest-value accessibility fix you can ship this week—it costs almost nothing and makes your content genuinely useful offline. Start with the link-URL rule and the `page-break-inside: avoid` rule; those two alone transform printed output from unusable to professional.