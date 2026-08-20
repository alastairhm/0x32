---
title: "Context Free Spikes"
date: 2009-11-20T11:51:00+00:00
draft: true
tags: ["blogger-import", "context-free", "fractal", "fractal-images"]
categories: ['Creative']
---

More <a href="http://www.contextfreeart.org/">context free</a> art<br /><br /><a href="http://www.flickr.com/photos/doodle_m/4118942337/" title="Spikes 4 by Alastair Montgomery, on Flickr"><img src="http://farm3.static.flickr.com/2548/4118942337_5f0c115213.jpg" width="394" height="500" alt="Spikes 4" /></a><br /><a href="http://www.flickr.com/photos/doodle_m/4119716944/" title="Spikes 4 version 2 by Alastair Montgomery, on Flickr"><img src="http://farm3.static.flickr.com/2802/4119716944_6b692ca419.jpg" width="500" height="460" alt="Spikes 4 version 2" /></a><br /><br />Here is the script, just change the "r -40" to "r 40" to generate the other image.<br /><br /><code><br />startshape spin2<br /><br />rule spin2 {<br />spin {}<br />spin2 { r -40 x 1.5 y 1 s 0.9}<br />}<br /><br />rule spin {<br />spikes {}<br />}<br /><br />rule spikes { spike {hue =1 sat =0.8016 b =0.9502} }<br /><br />rule spike { point {  } spike { r 10 s 0.95 hue +1 } }<br /><br />rule point { CIRCLE{} point { y 0.1 s 0.96 sat -0.005 }}<br /></code><br /><br /><br /><p><span style="font-size:85%;">Alastair's Fractals <a href="http://alsfractals.blogspot.com/">Main Page</a>,<br /><a href="http://www.cafepress.com/alastair_hm">My Shop at CafePress</a>, <a href="http://www.zazzle.com/doodle_m*">My Shop at Zazzle</a> <a href="http://tinyurl.com/28ufx8">Sign My Guestbook</a><br /><a href="http://tinyurl.com/yofz2a"><img src="http://tinyurl.com/ysfcth" alt="In association with Zazzle.com" border="0" height="57" width="141" /></a></span></p><p>© Alastair Montgomery 2008</p>
