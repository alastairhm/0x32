---
title: "Designing and Printing a Case for My ESP32 WiFi Scanner"
date: 2026-08-31T12:00:00+01:00
draft: false
tags: ['3d-printing','bambu-lab','hardware','maker','tinkercad','cad','esp32','electronics']
categories: ['Making']
featured_image: "https://live.staticflickr.com/65535/55497437054_5760bccc0d_c.jpg"
---

After [designing my first shelf in TinkerCAD]({{< ref "tinkercad-unifi-router-shelf.md" >}}), I wanted a project that actually needed a proper enclosure rather than a mounting bracket. I'd been building a small self-contained WiFi scanner — a bare ESP32 dev board wired up to a screen and a rechargeable battery — and it had been living on my desk as a loose tangle of board, wires and cells. Time to give it a case.

I started the same way I would with pen and paper before ever opening TinkerCAD — sketching out roughly where the board, screen and battery needed to sit, and where the case would need cutouts for the screen, buttons and USB port.

{{< flickr "ESP32 Case Tinkercad"
           "The case body taking shape in TinkerCAD, worked out from the paper sketches."
           "https://www.flickr.com/photos/doodle_m/55497415338"
           "https://live.staticflickr.com/65535/55497415338_3d385feaea_z.jpg" >}}

The finished design is up on TinkerCAD if you want to poke around the model yourself: [ESP32 Case](https://www.tinkercad.com/things/fRhZlIy82JC-esp32-case).

Unlike the router shelf, this one actually has to fit around real components with real tolerances, so there was a lot more back-and-forth than my first design — printing, test-fitting the board and battery, then going back into TinkerCAD to nudge dimensions and cutouts before printing again. That's the bit I hadn't expected to enjoy as much as I did: reworking parts on the back of getting something physical in my hands, rather than just guessing dimensions upfront and hoping for the best.

{{< flickr "ESP32 case sitting on design sketches"
           "The printed case next to the original paper sketches it grew out of."
           "https://www.flickr.com/photos/doodle_m/55497437054"
           "https://live.staticflickr.com/65535/55497437054_5760bccc0d_z.jpg" >}}

The one fit issue I didn't fully solve in the model itself: the board had a little too much freedom to shift around inside the case once everything was wired in. Rather than go back and redesign the internal mounts again, I printed a small spacer to wedge it in place and hold it flat against the base. It took a few tries to get right — printing a couple of variations before landing on the version on the left that actually held the board snugly.

{{< flickr "ESP32 Box spacer designs"
           "Trying out different spacer designs for the box. The left hand one is the final model."
           "https://www.flickr.com/photos/doodle_m/55497269321"
           "https://live.staticflickr.com/65535/55497269321_8bbf5e5b94_z.jpg" >}}

{{< flickr "ESP32 Case internal"
           "The final spacer fitted, holding the board flat and in place inside the case."
           "https://www.flickr.com/photos/doodle_m/55497374728"
           "https://live.staticflickr.com/65535/55497374728_81211eac03_z.jpg" >}}

Printed on the [A1 Mini]({{< ref "bambu-lab-a1-mini.md" >}}) as usual, and good enough for a first attempt at an enclosure with actual electronics inside rather than just a static bracket. The lid on this version is just a press fit, which is fine for now but not something I'd trust long-term once it's being opened and closed regularly to charge the battery. Next revision will have the board mounts built in properly so I don't need the spacer, plus a proper way to secure the lid so it's still easily removable — either a couple of small screws into printed bosses, or embedded magnets for a cleaner look with no visible fixings.

I've also uploaded the print files to MakerWorld: [Case for ESP32 Board with 1.9 Inch Screen](https://makerworld.com/en/models/3239273-case-for-esp32-board-with-1-9-inch-screen#profileId-3669923), in case it's useful to anyone else with the same board.
