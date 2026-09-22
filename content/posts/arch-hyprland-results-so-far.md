---
title: "Arch + Hyprland: Results So Far"
date: 2026-09-22T08:00:10+01:00
draft: false
tags: ['linux','arch','hyprland','archbtw','laptop']
categories: ['Geek']
featured_image: "https://live.staticflickr.com/65535/55542039423_2b7624e059_z.jpg"
---

Follow-up to [Building It the Boring Way: Arch + Hyprland From Scratch]({{< ref "building-it-the-boring-way-arch-hyprland-from-scratch.md" >}}) — turned out easier than I thought, once I got past one annoying snag right at the start.

{{< flickr "ArchBTW desktop"
           "Arch + Hyprland up and running on the old laptop"
           "https://www.flickr.com/photos/doodle_m/55542039423"
           "https://live.staticflickr.com/65535/55542039423_2b7624e059_z.jpg" >}}

The only real hiccup was WiFi from the Arch install ISO — `iwctl` didn't want to cooperate at first, so getting the installer online took longer than every other step combined. Once that was sorted, the rest of the plan went pretty much exactly as laid out: `archinstall` for the base system, then Hyprland and the usual Wayland bits on top.

For the actual desktop setup I ended up using [LinuxBeginnings/Arch-Hyprland](https://github.com/LinuxBeginnings/Arch-Hyprland) rather than hand-rolling every dotfile myself — it handles Waybar, theming, and all the little pieces that would otherwise have eaten up an evening of fiddling.

{{< flickr "ArchBTW waybar and terminal"
           "Waybar and a terminal running under Hyprland"
           "https://www.flickr.com/photos/doodle_m/55540901807"
           "https://live.staticflickr.com/65535/55540901807_a460e0dbbd_z.jpg" >}}

{{< flickr "ArchBTW tiling"
           "Tiling windows working as expected"
           "https://www.flickr.com/photos/doodle_m/55541928996"
           "https://live.staticflickr.com/65535/55541928996_5897d05ee6_z.jpg" >}}

Still a few rough edges to sort out, but it's a proper usable Hyprland desktop on hardware that's been sitting idle for years. More to follow once I've had longer to live in it day to day.
