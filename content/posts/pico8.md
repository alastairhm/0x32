---
title: "TFT Display ST7735 MicroPython"
date: 2023-02-17T16:31:44Z
draft: false
tags: ['tech','code','electronics','pico','raspberrypi','python']
categories: ['Geek','Python','RaspberryPi']
featured_image: "https://live.staticflickr.com/65535/52644510266_a694023ca0_z.jpg"
---

I got a cheap SPI TFT ST7735 Display module with SD Card reader off ebay, it had an unusual number of pins on the back.

{{< flickr "Numbers"
           "Numbers"
           "https://www.flickr.com/photos/doodle_m/52700051851"
           "https://live.staticflickr.com/65535/52700051851_da6a2aab59_c.jpg">}}

It took a while searching about on the internet and some head scratching to find a library and work out what connected to what on the Pico.

This is what I found, and worked out.

|TFT Board	| Raspberry Pi Pin |
|-|-|
|LED	|3v3(Out)|
|SCK	|GP10|
|SDA	|GP11|
|AO/DC	|GP16|
|Reset	|GP17|
|CS	|GP18|
|GND	|GND|
|VCC	|VBUS 5V|

Using that information I was able to put together this library based on a few others I found and a few test programs.

[https://github.com/alastairhm/micropython-st7735](https://github.com/alastairhm/micropython-st7735)

Based on the work from;

* [Guy Carver](https://github.com/GuyCarver)
* [boochow](https://github.com/boochow)


{{< flickralbum "Inktober 2020"
           "https://www.flickr.com/photos/doodle_m/albums/72177720306846081"
           "https://live.staticflickr.com/65535/52680439866_2ac726e570_c.jpg" >}}

I have yet to try the SD Card functionality on the board, something to play with later.           




