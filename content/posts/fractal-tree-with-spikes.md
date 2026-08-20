---
title: "Fractal tree with spikes"
date: 2009-11-20T14:09:00+00:00
draft: true
tags: ["blogger-import", "context-free", "fractal-images"]
categories: ['Creative']
---

<style type="text/css">.flickr-photo { border: solid 2px #000000; }.flickr-yourcomment { }.flickr-frame { text-align: left; padding: 3px; }.flickr-caption { font-size: 0.8em; margin-top: 0px; }</style><div class="flickr-frame"> <a href="http://www.flickr.com/photos/doodle_m/4119139089/" title="photo sharing"><img src="http://farm3.static.flickr.com/2583/4119139089_fbd5d53089.jpg" class="flickr-photo" alt="" /></a><br /><span class="flickr-caption"><a href="http://www.flickr.com/photos/doodle_m/4119139089/">Fractal tree with spikes</a>, originally uploaded by <a href="http://www.flickr.com/people/doodle_m/">Alastair Montgomery</a>.</span></div>    <p class="flickr-yourcomment"> Fractal tree created in <a href="http://www.contextfreeart.org/">Context Free</a> using the script below.</p><br /><br /><code><br />startshape trees<br /><br />rule trees {<br />tree {hue =1 sat =0.8016 b =0.9502}<br />}<br /><br />rule tree {<br />spike {}<br />tree {y 2 s 0.7 r 30 hue +5}<br />tree {y 2 s 0.7 r -30 hue +5}<br />}<br /><br />rule spike {<br />point {}<br />}<br /><br />rule point {<br />CIRCLE {}<br />point { y 0.1 s 0.96 sat -0.005 }<br />}<br /></code>
