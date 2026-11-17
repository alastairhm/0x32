---
title: "A BBC Owner's Mandelbrot on the Commodore 64"
date: 2026-11-17T19:00:00+00:00
draft: false
tags: ['tech','fractals','mandelbrot','c64','commodore','basic','retro','claude','ai','vibe-coding']
categories: ['Technical']
featured_image: "/c64-mandelbrot/mandel.png"
---

After [the BBC Micro Mandelbrots]({{< ref "bbc-micro-mandelbrot.md" >}}) the obvious next stop was the machine on the other side of the playground. I never had a Commodore 64. I was a BBC kid, so the C64 was something I saw at friends' houses, loading games off tape while we argued about which was better. Writing a program for one feels like visiting a foreign country where I don't speak the language.

So I had Claude be my guide. It drove the [VICE](https://vice-emu.sourceforge.io/) emulator through its remote monitor, typing the program in at the `READY.` prompt while I watched the window, just like it did with the BBC.

![The C64 start-up screen: 38911 BASIC bytes free](/c64-mandelbrot/ready.png)

The programs are in the `c64/` folder of my [fractals](https://github.com/alastairhm/fractals) repo, as listings and on a 1541 disk image.

## No MODE 2 here

On the BBC you type `MODE 2` and you've got a cleared graphics screen in eight colours. Then `GCOL` and `PLOT` draw on it, and the OS works out which byte of screen memory that means.

Commodore BASIC V2 has none of that. It's essentially Microsoft's BASIC from 1977, with disk commands bolted on, and it has no graphics commands at all (no sound commands either). Everything goes through `POKE`:

- `POKE 53265,59` turns on bitmap mode in the VIC-II video chip.
- `POKE 53270,216` turns on multicolour mode.
- `POKE 53272,24` points the chip at a bitmap in memory at 8192.

Those numbers are to C64 people what `VDU 23` is to BBC people: half-remembered magic.

Multicolour mode gives 160×200 pixels, wide like MODE 2's, but only four colours in each 4×8 pixel cell. One of them is the background colour for the whole screen, and the other three come from screen RAM and colour RAM for that cell. To plot a pixel you have to work out which byte it's in yourself. The bitmap is laid out in 8×8 character cells rather than scan lines, so it's

```basic
8192 + INT(Y/8)*320 + INT(X/4)*8 + (Y AND 7)
```

and then you OR the pixel's two bits into the right place in that byte. The BBC listing reads like the maths. Half the C64 listing is memory-map arithmetic.

## Getting lost in translation

The first attempt to type it in went badly:

![A screen full of ?SYNTAX ERROR](/c64-mandelbrot/syntax-errors.png)

That one was our fault, not the C64's. VICE's monitor command for typing into the keyboard buffer takes everything after it literally, so the quotes around each line got typed too. There was also a C64 rule we hadn't allowed for: a program line can't be longer than two screen lines, which is 80 characters. One line had to be split in two.

Other things that felt foreign coming from BBC BASIC:

- There's no `REPEAT`/`UNTIL`, no procedures, no `ELSE` and no `MOD`.
- The iteration loop uses a C64 trick instead of `REPEAT`. It's one line ending `IF A+B<F THEN NEXT`. While the point hasn't escaped, the `NEXT` goes round again. When it escapes, the `IF` fails, the rest of the line is skipped, and the loop counter is the escape count.
- BASIC V2 finds variables by searching through them in the order they were created, so the ones used most are defined first. It also re-reads a number like `4` from its digits every time it meets one, so constants live in variables.
- `TI` is a jiffy clock counting 60ths of a second, which made timing easy.

## MANDEL: the same picture, the C64 way

`MANDEL` draws the same set as the BBC version: 32 iterations, filling in from the top and bottom edges towards the middle, since the set is symmetric. It skips the main cardioid and the big bulb with a direct formula, as before.

![MANDEL part-way through, filling in from the edges](/c64-mandelbrot/mandel-progress.png)

![MANDEL finished: the Mandelbrot set in blue, light blue and white](/c64-mandelbrot/mandel.png)

I asked whether that was the best the C64 could do for colour. It isn't. The C64 has 16 colours, and each cell can have its own three. `MANDEL` just uses the same three everywhere. Choosing them per cell means fighting the C64's version of colour clash, where a cell crossing more than three colour bands has to lose one. That could be a good `MANDEL3`.

## Clearing the screen

On the BBC, `MODE 2` clears the screen for you. On the C64, the bitmap is full of whatever was in memory, so `MANDEL` clears it with 8000 `POKE`s:

```basic
90 FOR I=8192 TO 16191:POKE I,0:NEXT
```

That takes **32½ seconds**, watching garbage slowly being wiped. Is there no easier way? Not in BASIC. The C64 answer is a little machine code: 22 bytes, `POKE`d in from `DATA` statements and run with `SYS 49152`. `MANDEL2` does exactly that, and the screen is clear before you can blink.

```basic
90 FOR I=0 TO 21:READ D:POKE 49152+I,D:NEXT:SYS 49152
280 DATA 169,32,133,252,169,0,133,251,168,162,32
290 DATA 145,251,200,208,251,230,252,202,208,246,96
```

It also turns out the clear isn't really needed. Every byte of the bitmap gets drawn, so the program could build each byte up from its four pixels and `POKE` it whole, without `PEEK`ing first. That's a tweak for another day.

## How long?

Claude used VICE's warp mode to get to the end, but the `TI` clock runs on the C64's time, so the timings are what real hardware would take:

| Program   | Machine                    | Time to draw    |
| --------- | -------------------------- | --------------- |
| BBC `MANDEL` | BBC Model B, 2 MHz      | about 39 min    |
| C64 `MANDEL`  | Commodore 64 (PAL), 0.985 MHz | about 67½ min, plus 32½ s to clear |
| C64 `MANDEL2` | Commodore 64 (PAL), 0.985 MHz | about 68¼ min, and the clear is instant |

The surprise is that `MANDEL2` is slower overall. The clear is 32½ seconds quicker, but the drawing is 40 seconds slower. The culprit is the `D` in `READ D`. It's a new variable, created before the drawing starts, and BASIC V2 looks variables up by searching them in the order they were made. So every variable made after it, including `Y`, `Q`, `V` and `O`, which get used for every pixel, is one step further down the list. One extra variable costs 40 seconds. Welcome to the C64.

The BBC wins this one comfortably. The C64's processor runs at half the speed, BASIC V2's floating point is slower than BBC BASIC's, and every pixel costs extra BASIC just to find its address. That was the playground argument all along: BBC BASIC was the better language, and the C64 was the better games machine, with its sprites and SID chip. Neither of those helps with a Mandelbrot.

## Trying it yourself

Grab `c64/mandel.d64` from the [repo](https://github.com/alastairhm/fractals/tree/main/c64), attach it to drive 8 in [VICE](https://vice-emu.sourceforge.io/) or any other C64 emulator, and type:

```basic
LOAD"MANDEL",8
RUN
```

Then go and make a cup of tea. Or several. Press any key when it's finished and it tells you how long it took.
