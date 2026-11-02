---
title: "HackerBooks: How to Use HN's 16.5k Book Index (2026 Guide)"
description: "Learn how to search, filter, and export HackerBooks' 16.5k book index from Hacker News comments. Step-by-step guide, data tips, and fixes for bad matches."
pubDate: 2026-11-02
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## HackerBooks: What It Is and How to Actually Use It

HackerBooks is a searchable index of roughly **16,500 books** that were mentioned by at least two different Hacker News commenters between 2007 and today. Each book entry links back to the original HN comments that referenced it, and the full dataset is downloadable from the site's About page. It was built as a "HackerTube for books" — a direct nod to Andrej Karpathy's HackerTube project — with Claude (Opus 5.5) writing almost all of the code, including the data pipeline and the front end.

The catch you need to know before you start clicking: **the index counts mentions, not sentiment.** A book that gets praised 40 times and trashed 40 times ranks the same as one that gets 80 genuine recommendations. That single design decision shapes how you should use the tool, and this guide shows you how to get real value out of it without being misled by raw mention counts.

## Step-by-Step: Getting Useful Results from HackerBooks

### 1. Start with the About page, not the homepage

Before searching, open the About page and grab the downloadable dataset. Having the raw data locally lets you sort, filter, and cross-reference in ways the web UI may not support. If the export is CSV or JSON, load it into a spreadsheet or a quick SQLite table — 16.5k rows is trivial for either.

### 2. Search by exact title, then by author

The matching is automated, so title collisions are common. Search the exact title first. If you get a wrong match (for example, a programming book matched to a novel with a similar name), search the author's last name plus a keyword instead. This is the fastest workaround for the mis-matching problem the creator openly acknowledges.

### 3. Read the linked comments, not the rank

This is the most important habit. Because mentions are counted without sentiment analysis, a high rank means "frequently discussed," not "frequently recommended." Click through to the comment threads and skim for context. A book with 30 mentions where 20 are "this book is overrated" is a very different signal than 30 straight endorsements.

### 4. Cross-reference with a second source

Treat HackerBooks as a discovery layer, not a review aggregator. Once a book surfaces, check Goodreads or Amazon ratings for a sanity check on general reception. HN skews toward systems programming, startups, and classic computer science texts, so expect the index to over-represent those categories and under-represent fiction and niche domains.

### 5. Use it for "what should I read next" queries

The strongest use case is topical discovery. Search a technology or concept (e.g., "distributed systems," "compilers," "product management") and scan which books recur across many different threads. Books that appear in *unrelated* discussions are usually the genuinely canonical ones.

### 6. Report bad matches

If your favorite book is missing or mapped to the wrong edition or title, the creator explicitly asks users to report it. Include the book title, author, and the HN comment URL where it was mentioned. Reports are the only way the index improves.

## What You Should Know Before Relying on It

**Mention counting is sentiment-blind.** This is the single biggest limitation. Plan your reading decisions around comment context, not the number next to the title.

**Two-mention threshold filters noise but also hides gems.** A book mentioned once by a single insightful commenter won't appear. If you're hunting obscure recommendations, supplement HackerBooks with direct HN search (Algolia-powered) using `site:news.ycombinator.com` queries.

**Coverage is HN-shaped.** Expect heavy representation of:
- Classic CS texts (SICP, TAOCP, CLRS)
- Startup and management books (Zero to One, The Hard Thing About Hard Things)
- Systems and networking references
- Productivity and thinking frameworks

Expect thin coverage of fiction, poetry, and non-English works.

**Data freshness depends on pipeline reruns.** The dataset spans 2007 to the present, but new comments only appear after the pipeline is re-run. Check the About page for the last-updated date before assuming recency.

**It's a solo, AI-built project.** Claude wrote nearly all the code; the human steered, made product calls, and bought the domain. That means the site is functional and honest about its limits, but don't expect enterprise-grade uptime or support.

### Comparison: HackerBooks vs. Alternatives

| Tool | Scope | Sentiment-aware? | Exportable? |
|---|---|---|---|
| HackerBooks | ~16.5k books, 2+ HN mentions | No | Yes (About page) |
| HN Algolia Search | All HN comments | No (raw text) | No |
| Goodreads | Millions of books | Yes (ratings) | No |
| HackerTube | Videos mentioned on HN | No | N/A |

## Frequently Asked Questions (FAQ)

### How many books are in HackerBooks and what's the date range?
Approximately **16,500 books**, each mentioned by at least two distinct Hacker News commenters, covering comments from **2007 through the present**.

### Can I download the HackerBooks dataset?
Yes. The full dataset is downloadable from the **About page** on the site. It's the best way to do custom sorting and filtering that the web interface may not expose.

### Why does a bad book rank highly on HackerBooks?
Because the index **counts mentions without sentiment analysis**. A book that is frequently criticized ranks just as high as one that is frequently praised. Always click through to the linked comments to judge context.

### Who built HackerBooks and how?
It was built by a Hacker News user who wanted a "HackerTube for books." **Claude (Opus 5.5) wrote almost all of the code**, including the data pipeline and the site itself; the human steered the project and handled product decisions.

### What should I do if a book is missing or matched incorrectly?
Report it to the creator with the **book title, author, and the HN comment URL** where it was mentioned. The creator explicitly requests these reports to improve matching accuracy.

## Final Verdict

HackerBooks is genuinely useful as a **discovery and cross-referencing tool** — not as a ranking or review site. Use it to find which books the HN community keeps circling back to, then verify each candidate by reading the linked comment threads and checking a ratings site. Download the dataset if you want to do serious filtering. And if you spot a bad match, report it — the project's accuracy depends entirely on user feedback, and the creator has been upfront that the mention-counting model is imperfect by design.