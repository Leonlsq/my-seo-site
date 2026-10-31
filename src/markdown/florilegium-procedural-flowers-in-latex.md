---
title: "Florilegium LaTeX: How to Generate Procedural Flowers (Setup Guide)"
description: "Learn how to install and use Florilegium, the procedural flower generator for LaTeX. Step-by-step setup, TikZ parameters, and troubleshooting tips."
pubDate: 2026-10-31
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## What Is Florilegium and How Do You Actually Use It?

Florilegium is a procedural flower generator built on top of LaTeX and TikZ that lets you create unique, mathematically generated botanical illustrations directly in your documents. Instead of manually drawing petals with TikZ paths, you define a handful of parameters—petal count, rotation, color palette, stem curvature—and Florilegium handles the geometry. The project hit the front page of Hacker News with 238 points and 43 comments, which tells you one thing: a lot of people want to try it but aren't sure where to start. This guide walks you through installation, a working minimal example, the parameters that matter, and the errors you'll hit on a fresh TeX Live install.

The core appeal is reproducibility. Every flower is deterministic from its seed value, so you can version-control your illustrations alongside your source. That's a meaningful upgrade over exporting PNGs from Illustrator.

## Step-by-Step Setup and Parameter Reference

### Step 1: Verify Your TeX Distribution

Florilegium requires a reasonably modern TeX distribution because it relies on `pgf` (TikZ) features and `l3keys`. Check your versions first:

```bash
pdflatex --version
kpsewhich tikz.sty
```

You want **TeX Live 2022 or newer** (or MiKTeX 22.x+). Older distributions will fail on `expl3` syntax. If you're on TeX Live 2020 or earlier, run `tlmgr update --self --all` before proceeding.

### Step 2: Clone and Install the Package

```bash
git clone https://github.com/kevinraymond/florilegium.git
cd florilegium
```

Copy the `.sty` file into your local texmf tree so it's available to all projects:

```bash
mkdir -p ~/texmf/tex/latex/florilegium
cp florilegium.sty ~/texmf/tex/latex/florilegium/
texhash ~/texmf
```

On Windows with MiKTeX, use `%USERPROFILE%\texmf\tex\latex\florilegium` and refresh the file name database from the MiKTeX Console.

### Step 3: A Minimal Working Document

```latex
\documentclass{article}
\usepackage{florilegium}
\begin{document}
\begin{florilegium}[
  petals=8,
  seed=42,
  hue=340,
  stem=curved
]
\end{florilegium}
\end{document}
```

Compile with `pdflatex`. If you see a flower, you're done. If not, jump to the troubleshooting section below.

### Key Parameters Worth Knowing

| Parameter | Type | Default | Effect |
|---|---|---|---|
| `petals` | integer | 6 | Number of petal instances around the center |
| `seed` | integer | 0 | Deterministic random seed; same seed = same flower |
| `hue` | 0–360 | 200 | Base hue in HSL space |
| `saturation` | 0–100 | 60 | Color intensity |
| `stem` | `straight`/`curved` | `straight` | Stem path style |
| `layers` | integer | 1 | Concentric petal rings |
| `scale` | float | 1.0 | Overall size multiplier |

The `seed` parameter is the most important one for practical use. Because generation is deterministic, you can iterate on a seed until you get a flower you like, then lock it in. A common workflow is to generate a contact sheet of 20 seeds in a grid, pick the best, and hardcode it.

## Common Issues, Alternatives, and What You Should Know

**Compilation fails with `Undefined control sequence \florilegiumsetup`.** This almost always means the `.sty` file wasn't found. Run `kpsewhich florilegium.sty`—if it returns nothing, your texmf copy failed or you skipped `texhash`.

**Flowers render but colors look washed out.** Florilegium outputs colors in the `cmyk` model by default for print compatibility. If you're producing screen PDFs, pass `rgb` as a package option: `\usepackage[rgb]{florilegium}`. The hue values will shift noticeably—expect to re-tune your palette.

**Generation is slow in large documents.** Each flower instance runs the procedural geometry at compile time. Ten flowers in one document is fine; a hundred will add noticeable seconds. Cache the output as a standalone PDF and `\includegraphics` it if you need volume.

**Alternatives to consider.** If you want hand-tuned botanical accuracy, the `tikz-botany` style packages or direct `pgfplots` polar plots give you more control at the cost of more code. If you want photo-realistic output, LaTeX is the wrong tool—use Blender's geometry nodes or a procedural SVG generator and import the result. Florilegium's niche is clean, vector, reproducible line-and-fill illustrations that match your document's typography.

**One gotcha for arXiv submissions.** Procedural generation means your PDF is not byte-reproducible across TeX Live versions if the package updates its geometry code. Pin the `.sty` file version in your repository if you're submitting to venues with reproducibility requirements.

## Frequently Asked Questions (FAQ)

### Is Florilegium free to use in commercial documents?

Check the repository's license file before publishing. The project is open source, but LaTeX package licenses vary—LPPL and MIT have different redistribution implications. For a commercial book, verify the license permits your use case rather than assuming.

### Does Florilegium work with LuaLaTeX and XeLaTeX?

Yes, the TikZ backend is engine-agnostic. However, font handling differences mean you should test your specific font setup. If you hit `l3keys` errors under XeLaTeX, update your `l3kernel` package first.

### Can I export a Florilegium flower as SVG?

Not directly. Compile to PDF, then convert with `pdftocairo -svg output.pdf flower.svg` (part of poppler-utils). The result preserves vector paths and is suitable for web use.

### Why does my flower look different from the README screenshots?

The README examples were generated with specific seeds and parameter combinations. Copy the exact parameter blocks from the examples rather than starting from defaults—small changes to `seed` produce completely different geometry.

## Final Verdict

Florilegium is worth installing if you produce technical documents, papers, or books that need decorative vector botanicals without leaving your LaTeX workflow. The deterministic seed system is genuinely useful for version control, and the parameter set is small enough to learn in an afternoon. Skip it if you need photorealistic art or if you're on a TeX distribution older than 2022—the upgrade friction isn't worth it for a decorative package. Start with the minimal example above, generate a seed grid to find a flower you like, and pin your package version before submitting anything to a reproducibility-sensitive venue.