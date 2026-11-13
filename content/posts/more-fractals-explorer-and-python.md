---
title: "More Fractals: An Interactive Explorer and Some Python"
date: 2026-11-13T22:00:00+00:00
draft: false
tags: ['tech','fractals','mandelbrot','pascal','free-pascal','python','claude','ai','vibe-coding','terminal']
categories: ['Technical']
featured_image: "/fractals-update/attractor-sheet.png"
---

The [fractals](https://github.com/alastairhm/fractals) repo from my [Pascal Mandelbrot post]({{< ref "vibe-coding-pascal-fractals.md" >}}) didn't stay still for long. There's a fifth Pascal program you can explore with, and some Python scripts that draw other kinds of fractals in a retro style.

## mandelbrot5: an interactive explorer

`mandelbrot4` could pan and zoom, but only by rerunning it with new numbers. `mandelbrot5` turns it into an explorer you drive with the keyboard. It fills the terminal and follows it when you resize it, and every frame is redrawn in place.

| Key               | Action                                      |
| ----------------- | ------------------------------------------- |
| arrows, `h j k l` | pan by a tenth of the view                  |
| `+` / `-`         | zoom in / out (×1.5)                        |
| `]` / `[`         | more / fewer iterations                     |
| `s`               | save the view as a PNG                      |
| `r`               | reset to the whole set                      |
| `q`               | quit                                        |

The status line shows where you are, the zoom, the iteration limit and how long the last frame took. It warns you once you've zoomed so deep that double precision can't tell neighbouring pixels apart. When you quit, it prints the command line that reopens the same view.

`./mandelbrot5 120 36 3000 -0.1011 0.9563 300 | cat`, the branching filaments near the top bulb:

![mandelbrot5 showing branching filaments near the top bulb](/fractals-update/mandelbrot5-filaments.png)

It's also much quicker. It shares the rows out across a pool of threads, one per CPU, and it uses a direct formula to spot points in the main cardioid and the big bulb to its left. Those points never escape, so they're the most expensive pixels to iterate, and now they're skipped. On my 2-core/4-thread laptop, a 400×120 frame of the whole set at 20,000 iterations went from about 2.4 seconds with `mandelbrot4` to about 0.35 seconds.

Pressing `s` sends the frame on screen through the same `ansi2png.py` script that made the screenshots, so saving a view you like is one key press. These two were saved that way:

![A Mandelbrot view saved from mandelbrot5](/fractals-update/mandelbrot-20261110-220117.png)

![The whole Mandelbrot set saved from mandelbrot5](/fractals-update/mandelbrot-20261110-220136.png)

There's also a Makefile now. `make check` runs every program's `--help` and a tiny render, and checks that a frame from `mandelbrot5` matches `mandelbrot4` byte for byte, so the speed-ups can't quietly change the picture. A `todo.md` lists what's next: mouse support and a Julia set mode for a `mandelbrot6`, deeper zooms, and faster interior pixels.

## Python fractals

All the Pascal code now lives in `pascal/`, alongside a new `python/` folder with three scripts. Each one takes a **seed**, a number or any bit of text, which picks the shape, depth and colour palette (amber CRT, green phosphor, ice and so on). The same seed always gives the same picture. Single images are drawn at a third of the size and scaled up, which gives them a chunky low-res look.

Each script has the same options: `--gif` animates the fractal growing, `--sheet` lays out a 3×3 contact sheet of seeds, and `--size` sets the output size.

### koch_riff.py

Koch curves drawn round a polygon with 3 to 8 sides. The bumps can be the classic triangle, the Cesàro shape or squares, and each one is flipped in or out at random.

`python3 python/koch_riff.py --size 720 17`, a pentagon with square bumps:

![Koch riff seed 17, a green pentagon with square bumps](/fractals-update/koch.png)

`python3 python/koch_riff.py --sheet 1 2 3 4 5 6 7 8 9`:

![Contact sheet of Koch riffs for seeds 1 to 9](/fractals-update/koch-sheet.png)

### pythagoras_tree.py

Pythagoras trees built from squares and right triangles, with the branch angle, wobble and lean varied by the seed.

`python3 python/pythagoras_tree.py --size 720 6`:

![Pink Pythagoras tree for seed 6](/fractals-update/tree.png)

With `--gif`, it grows one level at a time:

![Animated blue Pythagoras tree for seed 9 growing level by level](/fractals-update/tree-grow.gif)

### attractor.py

My favourite of the three. It draws Clifford and de Jong strange attractors, simple maps such as

*x′ = sin(a·y) − cos(b·x)*, *y′ = sin(c·x) − cos(d·y)*

that are run from 20,000 random starting points for 300 steps each. It counts how many points land in each pixel, then colours those counts on a log scale, which gives the wispy, glowing look. Parameters that collapse down to a few dots are thrown away and picked again.

`python3 python/attractor.py --size 720 14`:

![Amber de Jong attractor for seed 14](/fractals-update/attractor.png)

`python3 python/attractor.py --sheet --size 720 11 13 14 15 17 18 2 5 6`:

![Contact sheet of nine Clifford and de Jong attractors](/fractals-update/attractor-sheet.png)

And with `--gif`, the points pile up:

![Animated magenta de Jong attractor for seed 11 filling in](/fractals-update/attractor-grow.gif)

## Trying it yourself

The Pascal side needs Free Pascal 3.x and a terminal with 24-bit colour, and `mandelbrot5` is Linux only. The Python scripts need Pillow, and `attractor.py` needs NumPy as well.

```sh
git clone https://github.com/alastairhm/fractals.git
cd fractals/pascal
make
./mandelbrot5                                # explore from the whole set
./mandelbrot5 0 0 2000 -0.7436 0.1318 200    # start in Seahorse Valley
cd ..
python3 python/attractor.py --gif 42         # attractor_42.gif
python3 python/pythagoras_tree.py --sheet    # 9 random trees
```

Try your own name as a seed and see what you get.
