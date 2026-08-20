---
title: "Counting up to 1023"
date: 2012-11-25T22:03:00+00:00
draft: true
tags: ["arduino", "binary", "blog-import", "electronics", "geek"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Decided in the end to wire up all 10 LEDS in the LED bar graph.<br />
Using the sketch below get the results shown in the video.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<object class="BLOGGER-youtube-video" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" data-thumbnail-src="https://ytimg.googleusercontent.com/vi/1TVgph8aZE4/0.jpg" height="266" width="320"><param name="movie" value="https://www.youtube.com/v/1TVgph8aZE4?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" /><param name="bgcolor" value="#FFFFFF" /><param name="allowFullScreen" value="true" /><embed width="320" height="266"  src="https://www.youtube.com/v/1TVgph8aZE4?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" type="application/x-shockwave-flash" allowfullscreen="true"></embed></object></div>
<br />
<br />
<pre><span style="color: #cc6600;">int</span> numLed = 10;
<span style="color: #cc6600;">int</span> ledpins[] = {
&nbsp;&nbsp;13,12,11,10,9,8,7,6,5,4};
<span style="color: #cc6600;">int</span> mask[] = {
&nbsp;&nbsp;1,2,4,8,16,32,64,128,256,512};
<span style="color: #cc6600;">int</span> counter = 0;

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>setup</b></span>() {                
&nbsp;&nbsp;<span style="color: #7e7e7e;">// initialize the digital pin as an output.</span>
&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> i=0;i&lt;numLed;i++){
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">pinMode</span>(ledpins[i], <span style="color: #006699;">OUTPUT</span>);
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(ledpins[i], <span style="color: #006699;">HIGH</span>);
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(250);
&nbsp;&nbsp;}
}

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>loop</b></span>() {

&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> i=0;i&lt;numLed;i++){
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">if</span> (counter &amp; mask[i]) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(ledpins[i], <span style="color: #006699;">HIGH</span>);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">else</span> {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(ledpins[i], <span style="color: #006699;">LOW</span>);
&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;}

&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(1000);
&nbsp;&nbsp;counter++;
}</pre>
<br />
Circuit Diagram, I used an LED Bar graph but you could use separate LEDs.<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzL-SCudRPKepzTC3NjktlWlzB6lUZZuP2mvOBUhfg8uIOKKn-ruv053tOhAsvv49Ncy0uE4FMfU3jS-A_fJ7ND8aud2ZOr5vkEtQkWlVEwBDtRsozenfFSe8SCLolnH6f0-8_fT0z9r0/s1600/ten+leds_bb.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzL-SCudRPKepzTC3NjktlWlzB6lUZZuP2mvOBUhfg8uIOKKn-ruv053tOhAsvv49Ncy0uE4FMfU3jS-A_fJ7ND8aud2ZOr5vkEtQkWlVEwBDtRsozenfFSe8SCLolnH6f0-8_fT0z9r0/s1600/ten+leds_bb.png" height="285" width="320" /></a></div>
<br /><br />
<pre>




</pre>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
