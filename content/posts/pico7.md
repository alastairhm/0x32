---
title: "Small LED Matrix Numbers"
date: 2023-01-26T15:16:16Z
draft: false
tags: ['tech','code','electronics','pico','raspberrypi','python']
categories: ['Geek','Python','RaspberryPi']
featured_image: "https://live.staticflickr.com/65535/52644510266_a694023ca0_z.jpg"
---

Something I did a few (8) years ago on the Arduino to display two-digit numbers on a 8x8 LED matrix, this is an update to do the same in Micropthon.

Numbers have been defined to 3x5 pixels, so for a two-digit number it fits into 8x5 LED grid with spacing, saving some LED Matrix space.

{{< flickr "Numbers"
           "Numbers"
           "https://www.flickr.com/photos/doodle_m/52650530060"
           "https://live.staticflickr.com/65535/52650530060_6ca8331919_w.jpg">}}

The code for this can be found here [numbers.py](https://github.com/alastairhm/pico_w/blob/main/numbers.py)

This original Arduino code is [here](https://github.com/alastairhm/arduino/blob/master/lmnumbers/lmnumbers.ino).
