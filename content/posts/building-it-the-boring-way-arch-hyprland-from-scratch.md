---
title: "Building It the Boring Way: Arch + Hyprland From Scratch"
date: 2026-09-21T21:00:00+01:00
draft: true
tags: ['linux','arch','hyprland','how-to']
categories: ['Geek']
featured_image: "https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png"
---

Follow-up to [The Politics I Never Noticed Were There]({{< ref "the-politics-i-never-noticed-were-there.md" >}}) — this one's the practical half. After all the reading about Omarchy's baggage, I landed on the least dramatic option available: a plain Arch install, built up by hand, with someone else's dotfiles layered on top rather than baked in.

The machine is an old Lenovo laptop that's been kicking around doing not much — Intel i5-4300M, 16GB RAM, and (crucially) an SSD I fitted before starting, which turned out to remove basically every hardware worry from the list. The dotfiles are [LinuxBeginnings/Hyprland-Dots](https://github.com/LinuxBeginnings/Hyprland-Dots) — the community-maintained continuation of the well-regarded JaKooLit dotfiles, handed off cleanly in early 2026.

## The plan, step by step

Roughly 2–2.5 hours of actual hands-on time, going in with the SSD already in place:

1. **Arch ISO → USB.** Download, verify the checksum, write it with `dd` (or Rufus/Ventoy if I'm feeling lazy). ~15–20 min.
2. **Boot the USB, get online.** `iwctl` for WiFi if there's no cable handy. ~5–10 min.
3. **`archinstall`.** The guided TUI installer does the heavy lifting — partitioning, filesystem, bootloader, locale — set to a minimal profile with no desktop environment. Fast on an SSD, maybe 15–20 min.
4. **First boot, full update.** `pacman -Syu` to bring everything current. ~10–15 min.
5. **GPU drivers.** The i5-4300M's integrated graphics (Intel HD 4600) has solid, mature open-source support — just `mesa`, `vulkan-intel`, `intel-media-driver`. No proprietary driver hunting required, which is one less thing to go wrong. ~10 min.
6. **Audio.** `pipewire`, `pipewire-pulse`, `pipewire-alsa`, `wireplumber`, enabled as user services. ~10 min.
7. **Hyprland itself.** Plus the core Wayland bits it needs — `xdg-desktop-portal-hyprland`, `polkit-kde-agent`. ~10 min.
8. **Login manager.** `sddm`, or skip it entirely and launch from a TTY. ~10–15 min.
9. **Checkpoint reboot.** Confirm a bare, un-decorated Hyprland session actually boots before touching any dotfiles — cheap insurance against debugging two things at once. ~5 min.
10. **Dotfiles prerequisites.** Waybar, rofi/wofi, a terminal emulator, a notification daemon, fonts — whatever the LinuxBeginnings README says it expects. ~15–20 min.
11. **Run the install script.** Clone the repo, run `Distro-Hyprland.sh`, let it do its thing. ~10–15 min, mostly hands-off.
12. **Reboot and fix whatever broke.** Keybinds, waybar modules, wallpaper theming (wallust) — this is the one step with real variance, anywhere from 20 minutes to an hour depending on how cleanly it all lands.

## Why the long way round

I did seriously consider the shortcuts — CachyOS for its performance tuning, or just staying on EndeavourOS. Neither made sense here. CachyOS's whole pitch is CPU-specific optimised builds, which is wasted on a decade-old Haswell chip; I'd get the extra complexity without the payoff. Vanilla Arch, by contrast, means nothing sits between me and the actual system — every package is a deliberate choice, not an inherited default.

Given I already run a pyinfra provisioning script for other boxes and a k3s cluster held together with my own scripts, this felt like the natural extension: build it myself, know exactly what's in it, and don't inherit anyone else's opinions about what my desktop should look like — political or otherwise.

## What I'm expecting to go wrong

If past experience with "just run the install script" projects is any guide, it won't be steps 1–9 that bite — it'll be step 12. Waybar modules that assume a package I didn't install, a wallpaper script that wants a directory that doesn't exist yet, a keybind clash with something Hyprland ships by default. Nothing that a bit of patience and the LinuxBeginnings wiki won't sort out.

I'll follow this up once it's actually running — properly, with screenshots, not just a plan on paper.
