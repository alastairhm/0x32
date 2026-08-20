---
title: "Some Debug Required"
date: 2013-03-17T21:51:00+00:00
draft: false
tags: ["arduino", "blog-import", "geek", "lcd", "ruby", "sainsmart", "serial-port", "twitter"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
First test of Twitter updates getting written to the Arduino from Ruby didn't go quite right as seen from the video below, some debugging required.<br />
<br />
Testing writing the same message from the Arduino IDE gives the same results so looks like problem is in the Arduino code. Maybe the message is too long for the LCD's buffer?<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<object class="BLOGGER-youtube-video" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" data-thumbnail-src="http://i.ytimg.com/vi/g2Ql86wt8dI/0.jpg" height="266" width="320"><param name="movie" value="http://www.youtube.com/v/g2Ql86wt8dI?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" /><param name="bgcolor" value="#FFFFFF" /><param name="allowFullScreen" value="true" /><embed width="320" height="266"  src="http://www.youtube.com/v/g2Ql86wt8dI?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" type="application/x-shockwave-flash" allowfullscreen="true"></embed></object></div>
<br />
<br />
The Twitter to Serial port Ruby script can be found at&nbsp;<a href="https://github.com/alastairhm/arduino/tree/master/SerialMessage">https://github.com/alastairhm/arduino/tree/master/SerialMessage</a><br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
