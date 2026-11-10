---
title: "Vibe Coding Mandelbrots in Pascal"
date: 2026-11-10T21:30:00+00:00
draft: false
tags: ['tech','fractals','mandelbrot','pascal','free-pascal','claude','ai','vibe-coding','terminal']
categories: ['Technical']
featured_image: "/pascal-fractals/mandelbrot4-seahorse.png"
---

A bit of evening fun: I wanted to see how far a quick vibe coding session could take a Mandelbrot renderer in [Free Pascal](https://www.freepascal.org/), drawing straight into the terminal. Pascal was one of the first languages I used, and the Mandelbrot set is the classic "hello world" of fractals, so it seemed like a good pairing.

The result is [alastairhm/fractals](https://github.com/alastairhm/fractals): four small programs, each one building on the one before, going from plain ASCII art up to truecolor half-block graphics.

| Program       | Output                       | What it adds                                                   |
| ------------- | ---------------------------- | -------------------------------------------------------------- |
| `mandelbrot`  | Plain ASCII                  | The basic escape-time algorithm; characters cycle by iteration |
| `mandelbrot2` | ASCII gradient               | Log-scaled character gradient, separate interior character     |
| `mandelbrot3` | Coloured ASCII (24-bit ANSI) | Smooth (fractional) escape count and a cosine colour gradient  |
| `mandelbrot4` | Truecolor half blocks (`▀`)  | Two square pixels per cell, auto contrast, pan and zoom        |

## Where it started: plain ASCII

`./mandelbrot 100 36`

![mandelbrot plain ASCII output](/pascal-fractals/mandelbrot.png)

The simplest version. Each character is a point *c* in the complex plane; repeat *z ← z² + c* from *z = 0*, and if it hasn't escaped after the iteration limit, it's in the set. Otherwise the number of steps it took picks the character.

## An ASCII gradient

`./mandelbrot2 100 36`

![mandelbrot2 ASCII gradient output](/pascal-fractals/mandelbrot2.png)

Spreading `ln(iterations)` across the character palette gives a smooth gradient instead of the characters wrapping round.

## Adding colour

`./mandelbrot3 100 36 500`

![mandelbrot3 coloured ASCII output](/pascal-fractals/mandelbrot3.png)

With 24-bit ANSI colour, a large escape radius and the fractional escape count `n + 1 − log₂(log|z|)`, the colour bands disappear.

## Truecolor half blocks

`./mandelbrot4 120 36 1000`

![mandelbrot4 showing the whole set](/pascal-fractals/mandelbrot4.png)

The final version uses the `▀` half-block character with separate foreground and background colours, so each terminal cell becomes two square pixels. It works out every pixel first and then stretches the gradient between the lowest and highest values on screen, so zoomed-in views keep their contrast. It also takes a centre point and zoom level, so you can go exploring:

`./mandelbrot4 120 36 2000 -0.7436 0.1318 200`, zoomed into Seahorse Valley:

![mandelbrot4 zoomed into Seahorse Valley](/pascal-fractals/mandelbrot4-seahorse.png)

## Trying it yourself

You just need Free Pascal 3.x and a terminal with 24-bit colour (kitty, alacritty, foot, wezterm and so on):

```sh
git clone https://github.com/alastairhm/fractals.git
cd fractals
for f in mandelbrot*.pas; do fpc -O2 "$f"; done
./mandelbrot4 $(tput cols) $(($(tput lines)-1)) 1000    # fill the terminal
./mandelbrot4 160 50 3000 -0.1011 0.9563 300            # spiral near the top bulb
```

Deep zooms need a higher iteration limit to bring out detail near the edge of the set. The screenshots above are the programs' real output, rendered to PNG by a small `tools/ansi2png.py` script in the repo.

It was a fun way to spend an evening, and a nice reminder that you don't need a GPU or a fancy graphics library to make pretty fractals, just a terminal and a few lines of Pascal.
