---
title: "Earcut vs. New Polygon Triangulation: 3.7M Polygons in 489ms"
description: "Benchmark breakdown of the 489ms map polygon triangulation technique vs earcut, plus how to apply it to your own WebGL map rendering pipeline."
pubDate: 2026-10-22
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## Why 3.7M Map Polygons in 489ms Matters for Your WebGL Pipeline

If you render maps in the browser, you already know the pain: `earcut` is the de-facto triangulation library for Mapbox GL, deck.gl, and most WebGL mapping stacks — and it chokes on large polygon counts. A recent engineering post from Globus Software claims a custom triangulation pipeline that cuts **3.7 million map polygons in 489 milliseconds**, which is roughly an order of magnitude faster than naive earcut usage on the same dataset. This guide breaks down *why* that's possible, what to change in your own pipeline, and when you should (and shouldn't) copy the approach.

The direct takeaway: the speedup does **not** come from a magic replacement for earcut. It comes from **preprocessing, batching, and avoiding per-polygon overhead** — techniques you can adopt today without rewriting your renderer.

## The Core Techniques Behind the 489ms Benchmark

The Globus write-up (and the HN discussion at item 50193170) centers on a handful of concrete optimizations. Here's the practical breakdown:

| Technique | What It Does | Typical Speedup |
|---|---|---|
| Flat typed-array input | Feed coordinates as `Float64Array`/`Float32Array` instead of nested arrays | 2–4x |
| Polygon batching | Triangulate many rings per call, amortizing JS↔WASM boundary cost | 3–8x |
| Precomputed winding & hole flags | Skip runtime orientation checks | 1.2–1.5x |
| Worker offload | Move triangulation off the main thread | Perceived 0ms jank |
| Caching by geometry hash | Reuse meshes across frames/zooms | Near-infinite on repeat |

### Step-by-Step: Applying This to Your Own Map

1. **Flatten your geometry.** Convert GeoJSON `coordinates` into a single contiguous `Float64Array` plus an index array of ring offsets. This alone often doubles throughput.
2. **Batch rings by tile.** Instead of calling `earcut(vertices)` per polygon, accumulate all rings for a tile and triangulate in one pass with an offset table.
3. **Precompute winding order.** Store a signed-area flag per ring so you never re-detect holes at runtime.
4. **Move it to a Web Worker.** Post the flat buffer with `transferable` semantics so there's zero-copy overhead.
5. **Cache meshes keyed by a geometry hash.** At 3.7M polygons you'll re-tessellate constantly on pan/zoom — a simple `Map` cache keyed by tile ID eliminates most work.

```js
// Minimal batching sketch
const verts = new Float64Array(totalVerts * 2);
const ringEnds = new Uint32Array(ringCount);
// fill verts + ringEnds during tile decode...
const triangles = earcut(verts, holes, 2); // one call per tile, not per polygon
```

## Common Issues and What You Should Know

- **Earcut is not the bottleneck in small scenes.** Below ~10k polygons, earcut is fine. The 489ms figure is about *scale*.
- **Numerical robustness.** Custom pipelines often skip earcut's robustness handling; self-intersecting or degenerate rings can produce broken meshes. Validate your data first.
- **WASM vs. JS.** The Globus approach leans on tight typed-array loops; a WASM port (e.g., via Rust `earcutr`) can push further but adds build complexity.
- **Alternatives worth benchmarking:** `earcutr` (Rust/WASM), `libtess2` (slower but handles complex holes), and `poly2tri` (constrained Delaunay). For pure speed on well-formed map data, batched earcut with flat arrays is usually the sweet spot.

## Frequently Asked Questions (FAQ)

### Is the 489ms triangulation faster than earcut?
Yes — but the gain comes from batching, flat typed arrays, and caching around earcut, not from replacing the algorithm. Naive per-polygon earcut calls are what's slow.

### Can I use this technique with Mapbox GL or deck.gl?
Partially. You can pre-tessellate and cache meshes, but you can't easily swap the internal triangulator. For custom layers and `deck.gl` `SolidPolygonLayer`, you can feed pre-triangulated data.

### Do I need WASM to hit these speeds?
No. The benchmark is achievable in plain JS with typed arrays, batching, and worker offload. WASM helps but isn't required.

## Final Verdict

Don't rip out earcut — **wrap it intelligently**. Flatten your geometry, batch per tile, precompute winding, offload to a worker, and cache aggressively. That combination gets you the bulk of the 489ms result without a rewrite. Reserve custom triangulation or WASM ports for the rare case where you're genuinely pushing millions of polygons per frame. For everyone else, the win is in the pipeline, not the library.