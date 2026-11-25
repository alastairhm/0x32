---
title: "Mazes, Maps, Glyphs and a Space City"
date: 2026-11-25T20:00:00+00:00
draft: false
tags: ['tech','fractals','mandelbrot','generative-art','python','art','claude','ai','vibe-coding']
categories: ['Technical']
featured_image: "/generative-art/space-city.png"
---

After [the Commodore 64]({{< ref "c64-mandelbrot.md" >}}) it's back to this century. A pile of Python scripts had been building up in my Google Drive, some drawing fractals and some not. I had Claude fetch them, sort out which were older copies of things already in my [fractals](https://github.com/alastairhm/fractals) repo, install the packages they needed, run them and write them up in the README.

Most of them aren't fractals at all, so the repo's name is now a bit of a fib. What they share is the **seed**: give a script the same number and you get the same picture, or leave it out and see what turns up.

## Mazes

`maze.py` draws maze posters. Every maze is "perfect", meaning there's exactly one route between any two cells. You can pick how it's carved:

- **Backtracker** wanders at random and backs up when it gets stuck, giving long, twisty corridors.
- **Aldous-Broder** wanders purely at random and carves a passage the first time it visits each cell. It's unbiased, but slow.
- **Wilson** uses random walks with the loops erased. It's also unbiased, and quicker.

<table>
<tr>
<td><img src="/generative-art/maze-backtracker.png" alt="Backtracker maze poster coloured by distance"></td>
<td><img src="/generative-art/maze-aldous.png" alt="Aldous-Broder maze poster coloured by distance"></td>
<td><img src="/generative-art/maze-wilson.png" alt="Wilson maze poster coloured by distance"></td>
</tr>
<tr><td align="center">Backtracker</td><td align="center">Aldous-Broder</td><td align="center">Wilson</td></tr>
</table>

The colours show how far each cell is from the entrance, and the dark line is the solution. There's a plainer style too, with just the walls and the way through:

![Backtracker maze drawn as lines on a dark background, with the solution in yellow](/generative-art/maze-lines.png)

## Cats

`cat_maze.py` is less use for getting anywhere. It's a pattern of thick right-angled meanders with blocky black cats hidden in it, sitting, lying down and hanging upside down. There are 13 cats in this one:

![Black cats hidden in a meander pattern](/generative-art/cat-maze.png)

It works on a grid. Every free point is a black square, and joining two neighbours fills the gap between them. The white channels are the gaps that never get joined, so they're all the same width, which gives it a lino-cut look.

## City maps

`citymap.py` makes minimalist map posters of cities that don't exist, with rivers, railways, parks and street grids that don't quite line up. It makes up a name if you don't give it one.

<table>
<tr>
<td><img src="/generative-art/city.png" alt="Map poster of an imaginary Dishforth"></td>
<td><img src="/generative-art/city-night.png" alt="Map poster of an imaginary Ravenhythe in night colours"></td>
</tr>
<tr><td align="center">Not the real Dishforth</td><td align="center">The night palette</td></tr>
</table>

## Alien handwriting

`glyphs.py` draws sheets of an imaginary script. Each glyph is split into columns, and each column is stacked with bars, blocks and ovals. Everything is wobbled, with white streaks like a felt-tip running dry.

![Twelve coloured glyphs on ruled paper](/generative-art/glyphs.png)

It can also draw just the outlines:

![Twelve glyphs in outline](/generative-art/glyphs-outline.png)

## Space city

And `space_city.py` draws a pen-and-ink city of enormous radial hubs, with solar panels, shuttles and a space station drifting past in the corner of the sky. If you don't give it a seed it uses the date and time, so every second has its own city.

![Black and white space city of radial hubs](/generative-art/space-city.png)

## And some fractals

The repo does still do fractals. There are four new scripts.

`pixel_resolve.py` makes a video that starts as one giant pixel and splits into 4, 16, 64 and so on up to 1024×1024, in 16 colours. It's the same idea as [`MANDEL2` on the BBC Micro]({{< ref "bbc-micro-mandelbrot.md" >}}), but each block is the average of everything under it rather than the colour of its corner. In quadtree mode, only blocks that still hide some detail get split. By the last level of this one, that's 62,048 of the million or so pixels.

<table>
<tr>
<td><img src="/generative-art/pixel-resolve.gif" alt="Mandelbrot set resolving from one pixel"></td>
<td><img src="/generative-art/pixel-resolve-quadtree.gif" alt="Mandelbrot set resolving, splitting only the detailed blocks"></td>
</tr>
<tr><td align="center">Grid</td><td align="center">Quadtree</td></tr>
</table>

`fractal_tile.py` turns a view of the set into an STL file for a 3D printer, as a terraced relief, raised line art or a lithophane to hold up to the light. These are its height maps of the spot [the zoom video]({{< ref "fractal-zoom-video-script.md" >}}) dives into, where brighter is taller:

<table>
<tr>
<td><img src="/generative-art/tile-relief.png" alt="Relief height map: a ring of spirals"></td>
<td><img src="/generative-art/tile-lines.png" alt="Line art height map"></td>
<td><img src="/generative-art/tile-litho.png" alt="Lithophane height map"></td>
</tr>
<tr><td align="center">Relief</td><td align="center">Lines</td><td align="center">Lithophane</td></tr>
</table>

`triangle_flake.py` joins the [Koch curves, Pythagoras trees and attractors]({{< ref "more-fractals-explorer-and-python.md" >}}). Each triangle sprouts a smaller one from the middle of each side, and so on down.

![Amber triangle flake](/generative-art/flake.png)

Last is `mandelbrot_numba.py`, a short script that renders the whole set at 1920×1080.

## Trying it yourself

Everything is in the [repo](https://github.com/alastairhm/fractals), and the README lists all the options:

```sh
git clone https://github.com/alastairhm/fractals
cd fractals
python3 -m venv python/.venv
source python/.venv/bin/activate
pip install -r python/requirements.txt

python mazes/maze.py --algo all --seed 3
python mazes/cat_maze.py -o cats.png
python "City Map Generator/citymap.py"
python glyphs/glyphs.py --lines --png glyphs.png
python space_city/space_city.py
```

`pixel_resolve.py` also needs `ffmpeg`, and you may need a C compiler and the `cairo` library for the space city.
