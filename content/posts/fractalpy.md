---
title: "Vibe Coding fractalPy with Claude"
date: 2026-08-02T15:45:00+01:00
draft: false
tags: ['tech','python','ai','claude','vibe-coding','code']
categories: ['Technical','Python']
featured_image: "python.png"

---

# Vibe coding a Mandelbrot renderer

Spent today "vibe coding" with Claude, just describing what I wanted and letting it drive, to see how far that gets you on a small self-contained project. The result is [fractalPy](https://github.com/alastairhm/fractalPy), a small Numba-accelerated Mandelbrot set renderer.

![Mandelbrot set render](https://raw.githubusercontent.com/alastairhm/fractalPy/master/docs/screenshot.png "fractalPy render")

It started as a single script — render the set to a PNG, colour it, done — using `@njit(parallel=True, fastmath=True, cache=True)` to JIT-compile the escape-time kernel so it's fast enough to iterate on interactively:

```
./fractal-env/bin/python mandelbrot_numba.py --center-x -0.743643887037151 --center-y 0.13182590420533 --zoom 1e-8 --max-iter 2000
```

From there the session turned into a normal small-project lifecycle rather than a one-shot script dump: a `benchmark.py` to time renders across zoom/iteration grids, a `precision_check.py` to visually spot where float64 arithmetic runs out of precision at deep zoom, a shared `mandelbrot_lib.py` once the kernel was duplicated across three scripts, `ruff` linting wired into GitHub Actions, and CLI args on everything instead of hardcoded constants.

What was more interesting than the code itself was the process. Every change went through its own branch and PR — six of them by the end of the afternoon — which kept each diff small enough to actually review rather than rubber-stamp. One PR was literally just documenting that git workflow in the repo's own `CLAUDE.md` so it would keep applying it consistently. It caught its own magic number (a bailout radius constant) via the lint pass and fixed it without being asked twice, which is the kind of thing that's easy to let slide in a solo throwaway project.

None of this is groundbreaking as a Mandelbrot renderer — plenty of those exist — but as a test of getting from "nothing" to a small, linted, CI-covered Python tool in an afternoon of natural-language back and forth, it held up well.
