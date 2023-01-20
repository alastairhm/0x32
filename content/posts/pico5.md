---
title: "Raspberry Pi Pico W LED Matrix"
date: 2023-01-20T09:56:40Z
draft: false
tags: ['tech','code','electronics','pico','raspberrypi','python']
categories: ['Geek','Python','RaspberryPi']
featured_image: "raspberry-pi-logo.jpg"
---

Found a LED Matrix with a Max7219 in my parts bin (box of random electronics in the garage) so looked into getting it working with the Pico and MicroPython.

This is an example why I love open source.
The original library I found was functional but sparse, last committed to 4 years ago.
There were a few forks, most not much activity.
One had been active recently and had some major improvements in functionality so switched over to that fork.
[https://github.com/enchant97/micropython-max7219](https://github.com/enchant97/micropython-max7219)

This is the LED Matrix test code I wrote [led_matrix.py](https://github.com/alastairhm/pico_w/blob/main/led_matrix.py) you have to upload the max7219 library to your Pico first.

It is wired up like;
![LED Matrix Wiring](https://live.staticflickr.com/65535/52637590357_b73d564a08_c.jpg)

These are the results,


{{< flickr "Matrix"
           "LED Matrix"
           "https://www.flickr.com/photos/doodle_m/52637095996"
           "https://live.staticflickr.com/65535/52637590357_b73d564a08_w.jpg" >}}

I did find this useful resource to generate custom characters which could be displayed as a glyph in the fork of the library.

[LED Matrix Tool](https://gurgleapps.com/tools/matrix)


