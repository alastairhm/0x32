---
title: "Trying Omarchy Linux on an Old Laptop"
date: 2026-09-20T11:25:45+01:00
draft: false
tags: ['linux','omarchy','hyprland','arch-linux','distro','laptop']
categories: ['Geek']
featured_image: "https://live.staticflickr.com/65535/55539542540_6ef2325713_c.jpg"
---

I had an old laptop sitting around doing nothing, so instead of letting it gather dust I decided to put [Omarchy](https://omarchy.org/) on it and see how it held up.

{{< flickr "omarchy linux"
           "Trying out Omarchy Linux on an old laptop"
           "https://www.flickr.com/photos/doodle_m/55539542540"
           "https://live.staticflickr.com/65535/55539542540_6ef2325713_z.jpg" >}}

Omarchy is DHH's opinionated Arch Linux + Hyprland setup — essentially Arch with all the tedious post-install decisions already made for you: a tiling window manager, a curated set of themes, and a sensible default toolset out of the box rather than a blank Arch install you have to build up from scratch yourself.

Putting it on hardware this old felt like a reasonable stress test. If a tiling, GPU-accelerated Wayland compositor is going to fall over anywhere, it's on a laptop that's long past its best. Install itself was painless — the installer does the Arch base install and drops you straight into a configured Hyprland desktop, no manual partitioning dance or fumbling through `pacstrap` required.

Once it was up, the laptop actually felt more usable than it had in years. Hyprland's tiling means no wrestling with sluggish window compositing, and the reduced overhead compared to a heavier desktop environment goes a long way on older, weaker hardware. It's not going to turn a decade-old machine into something snappy, but it strips away enough of the fat that what performance is left actually gets used.

Worth a try if you've got old hardware kicking around and fancy giving it a second life rather than a trip to the recycling centre.
