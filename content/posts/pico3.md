---
title: "Raspberry Pi Pico W Temperature"
date: 2023-01-17T12:29:22Z
draft: false
tags: ['tech','code','electronics','pico','raspberrypi','python']
categories: ['Geek','Python','RaspberryPi']
featured_image: "raspberry-pi-logo.jpg"
---

Have been tinkering with temperature measurement using the Raspberry Pi Pico.

First with the internal temperature sensor and then using a TMP36 temperature sensor externally.

I wrote two classes to access these and return the reading.

* [Internal Temperature](https://github.com/alastairhm/pico_w/blob/main/library/internal_temp.py)
* [External Temperature](https://github.com/alastairhm/pico_w/blob/main/library/tmp36.py)

Here is an example using the two sensors together [temps.py](https://github.com/alastairhm/pico_w/blob/main/temps.py)

You will need to upload the two classes to the Pico first in a `library` sub-directory.

Here is how you would wire it up on a breadboard [tmp36.fzz](https://github.com/alastairhm/pico_w/blob/main/circuits/tmp36.fzz)

![TMP36 Wiring](https://live.staticflickr.com/65535/52632604331_e3fb371877_c.jpg)

Taking this further I hooked up the OLED [oled_tmp36.fzz](https://github.com/alastairhm/pico_w/blob/main/circuits/oled_tmp36.fzz)

![OLED TMP36](https://live.staticflickr.com/65535/52633049290_638dfd7830_c.jpg)

Then used this code to update the OLED with the temperature readings.
[temp_oled.py](https://github.com/alastairhm/pico_w/blob/main/temp_oled.py)

![Temp on OLED](https://live.staticflickr.com/65535/52633067160_ec52d30b29_c.jpg)

