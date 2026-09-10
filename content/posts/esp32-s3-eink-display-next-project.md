---
title: "Next Project: ESP32-S3 and a 4.2 Inch E-Ink Display"
date: 2026-09-10T12:00:00+01:00
draft: false
tags: ['esp32','electronics','hardware','maker','eink','epaper']
categories: ['Making']
featured_image: "https://live.staticflickr.com/65535/55516411415_2feaf1e35c_c.jpg"
---

After [designing a case for my ESP32 WiFi scanner]({{< ref "esp32-wifi-scanner-case.md" >}}) I've picked up some new parts to play with: a [WeAct Studio ESP32-S3-N16R8 dev board](https://github.com/WeActStudio/WeActStudio.ESP32S3CoreBoard) — 16MB of flash and 8MB of PSRAM, dual USB-C, RGB status LED, sat in a little printed case I already had lying around — paired with a [WeAct Studio 4.2 inch e-paper module](https://github.com/WeActStudio/WeActStudio.EpaperModule), 400x300 resolution over a simple SPI header (GND, SDA, SCL, CS, D/C, RES, BUSY, VCC).

{{< flickr "ESP32-S3-N16R8 dev board"
           "The WeAct Studio ESP32-S3-N16R8 board, dual USB-C and an RGB LED, sat in an old printed case."
           "https://www.flickr.com/photos/doodle_m/55516411415"
           "https://live.staticflickr.com/65535/55516411415_2feaf1e35c_z.jpg" >}}

{{< flickr "4.2 inch e-paper module"
           "The back of the WeAct Studio 4.2 inch e-paper module, 400x300 resolution over SPI."
           "https://www.flickr.com/photos/doodle_m/55516134348"
           "https://live.staticflickr.com/65535/55516134348_e870d6d791_z.jpg" >}}

Neither part is new or exotic on its own, but I haven't built anything with e-ink before, and the combination of "plenty of processing headroom" (the S3 with that much RAM and flash) and "a screen that holds its image with zero power once drawn" opens up a different kind of project to the WiFi scanner — something that can sit on a shelf or a desk for weeks on a small battery rather than needing to be plugged in or charged constantly.

Still deciding exactly what to build first, so here's the shortlist I'm picking from:

- **E-ink weather station** — pull a forecast over WiFi, wake up every hour or so to redraw, sleep the rest of the time. The classic first e-ink project for a reason.
- **Calendar / agenda display** — pull today's events from a calendar feed and show them on the desk each morning, refreshing once rather than nagging with a backlit screen all day.
- **Dashboard for this blog** — post count, latest title, maybe a visitor stat pulled from somewhere, refreshed a few times a day.
- **Transit/departure board** — next bus or train times for a local stop, redrawn every few minutes while it's relevant and idle overnight.
- **Digital photo frame** — cycle through Flickr uploads or a folder of photos, one change a day, no backlight glare.
- **Label maker / whiteboard replacement** — a small always-on note or reminder screen that doesn't need a battery top-up every night.
- **Battery-life stress test** — before committing to any of the above, it'd be worth just measuring how long the S3 actually survives on a small LiPo with deep sleep between e-ink refreshes, to know what refresh interval is realistic.

I'll probably start with the weather station since it's the smallest scope and will tell me quickly whether the SPI wiring, the e-ink driver library and deep sleep all play nicely together before I sink time into anything more ambitious. Case design will likely follow once I've settled on which project and know what needs to fit inside, though I'm learning Autodesk Fusion at the moment so this one might end up modelled there instead of TinkerCAD.
