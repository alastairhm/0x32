---
title: "Generative Art with Context Free"
date: 2026-08-19T15:30:00+01:00
draft: false
tags: ['tech','art','generative-art','code','docker']
categories: ['Creative','Technical']
featured_image: "/contextfree-fractal-tree.png"
---

I've got a small repo, [ContextFree](https://github.com/alastairhm/ContextFree), that I keep coming back to whenever I want the specific kind of fun that comes from writing a handful of lines of code and having something unexpectedly pretty fall out the other end. It's a collection of [Context Free Art](https://www.contextfreeart.org/index.html) scripts — a tiny grammar for describing images as recursive drawing rules — plus a Docker image wrapping the [`cfdg`](https://github.com/MtnViewJohn/context-free) renderer so I can run them without installing anything locally.

The appeal is the mix. It's programming — rules, recursion, parameters, a build pipeline — in service of something purely creative, with no functional requirement other than "does this look good". That's a nice change of pace from the day job.

## The idea

A `.cfdg` script is just a `startshape` and a set of `rule`s. Each rule draws a primitive shape and then calls itself (or other rules) again with a transform applied — shift it, shrink it, rotate it, nudge the hue. Recurse a few hundred times and you get a fractal. Here's the whole of `fractal_tree.cfdg`:

```
startshape trees

rule trees {
tree {hue 1 sat 0.8016 b 0.9502}
}

rule tree {
spike {}
tree {y 2 s 0.7 r 30 hue +5}
tree {y 2 s 0.7 r -30 hue +5}
}

rule spike {
point {}
}

rule point {
CIRCLE {}
point { y 0.1 s 0.96 sat -0.005 }
}
```

`tree` draws a spike, then calls itself twice — once rotated 30° left, once 30° right, each time 70% the size of the parent and nudged a few degrees round the colour wheel. That's it. That's the entire tree:

![Fractal tree render, orange and yellow branching shape](/contextfree-fractal-tree.png)

Swap `CIRCLE` for `SQUARE`, change the transform from a rotating branch into a spiral, and the same handful of ideas produces something completely different — a crystalline diamond built from squares shrinking and stepping inward:

![Crystal2 render, green crystalline spiral on black background](/contextfree-crystal2.png)

Or a four-armed spiral of shrinking, fading circles that reads as a starfish:

![Starfish render, orange and yellow spiral shape](/contextfree-starfish.png)

What I like about it is how little code it takes to get somewhere interesting, and how much of the result is *discovered* rather than designed. You write four short rules, run the renderer, and get something you didn't quite picture in your head — then you nudge one number (a rotation, a scale factor, a colour delta) and the whole image transforms. It's closer to tweaking a synth patch than to normal programming: small, legible causes with genuinely surprising effects.

Drop the colour entirely and add some randomness to the branch angle instead of a fixed 30°, and the same "draw a spike, recurse twice" idea stops looking like a fractal and starts looking like an actual plant:

![mtree2 render, black branching tree structure on white background](/contextfree-mtree2.png)

or a whole different rule set, `tree grey.cfdg`, layers squares and rotations into something closer to a stained-glass kaleidoscope than anything botanical:

![tree grey render, black and white kaleidoscope pattern of nested squares](/contextfree-tree-grey.png)

Not everything in the repo is fractal, either. A `hearts.cfdg` builds a spiral of hearts out of a triangle and two circles per "petal":

![Hearts render, red heart spiral on white background](/contextfree-hearts.png)

and `cards.cfdg` reuses that same heart-drawing rule, flipped and combined with triangles, to build the four playing card suits:

![Cards render, heart diamond and spade suit symbols](/contextfree-cards.png)

which is a good example of the other satisfying bit — once you have a rule like `drawheart`, it's just a function. Reuse it, transform it, compose it into something new.

## The plumbing

The creative side is the point, but I still ended up doing normal software things around it, because that's the itch I can't leave unscratched. The repo has:

- `scripts/*.cfdg` — the grammar files, one per image.
- `Examples/*.png` — matching rendered output, filename-paired with the script that produced it.
- `docker_image/` — a multi-stage Dockerfile that compiles `cfdg` from source in a build stage and copies only the binary and its runtime libs into the final image, which took the image from ~700MB down to ~140MB.
- `draw.sh` — a one-line wrapper so rendering a script is just `./draw.sh 1024 fractal_tree`.

None of that is necessary to enjoy Context Free Art — the tool has its own bundled editor — but wrapping it in Docker means I can render from any machine without an install step, and keeping scripts and their rendered PNGs paired in git gives me a visual diff of sorts: change a rule, re-render, see exactly what moved.

A few more from the collection, because it's hard to stop once you start nudging parameters — the same handful of tricks (recurse, transform, shift the hue) keeps producing things that don't look related to each other at all:

![Spikes render, red and orange spiky spiral shape](/contextfree-spikes.png)

![starfish2 render, pink and magenta four-armed spiral](/contextfree-starfish2.png)

![ctree curl render, red orange and green scale-like curling pattern](/contextfree-ctree-curl.png)

![hearts2 render, dense four-armed spiral of red hearts](/contextfree-hearts2.png)

![tenree render, simple black branching tree on white background](/contextfree-tenree.png)

Between the tiny recursive grammar and the small pile of build tooling around it, ContextFree is a good reminder that "programming" and "making something creative" aren't really different activities for me — just the same instinct pointed at a different kind of output.
