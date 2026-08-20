---
title: "Arduino Binary second counter"
date: 2012-11-23T14:46:00+00:00
draft: false
tags: ["arduino", "binary", "blog-import", "electronics", "geek"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Next step with my Arduino is to set up a binary second counter.<br />
Basic using the LED Bar Graph or six single LEDs to count seconds in binary<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNmgs8Izk2utl30ZAVCskDyYVZ2wMyj97vYfOIO-uxLJk1cOgJ_ZaY-_LZmbyjDATFZWzCzKZQVxI7P1Y1obG7oL9eIb0x5no0MF79yfG4KTp3ruXU9Xn-ZY-ZUMVihaNaLlNvoxhBcW8/s1600/six+leds_bb.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="290" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNmgs8Izk2utl30ZAVCskDyYVZ2wMyj97vYfOIO-uxLJk1cOgJ_ZaY-_LZmbyjDATFZWzCzKZQVxI7P1Y1obG7oL9eIb0x5no0MF79yfG4KTp3ruXU9Xn-ZY-ZUMVihaNaLlNvoxhBcW8/s320/six+leds_bb.png" width="320" /></a></div>
<br /><br />
<br />
<pre><span style="color: #7e7e7e;">/*</span>
<span style="color: #7e7e7e;">Binary&nbsp;Second&nbsp;Counter</span>
<span style="color: #7e7e7e;">&nbsp;</span>
<span style="color: #7e7e7e;">&nbsp;Created&nbsp;Alastair&nbsp;Montgomery&nbsp;22/11/2012</span>
<span style="color: #7e7e7e;">&nbsp;</span>
<span style="color: #7e7e7e;">&nbsp;*/</span>

<span style="color: #cc6600;">int</span> ledPins[] = {
&nbsp;&nbsp;7,8,9,10,11,12};
<span style="color: #cc6600;">int</span> mask[] = {
&nbsp;&nbsp;1,2,4,8,16,32};
<span style="color: #cc6600;">int</span> ledCount = 6;

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>setup</b></span>() {
&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> thisPin =0; thisPin &lt; ledCount; thisPin++) {
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">pinMode</span>(ledPins[thisPin], <span style="color: #006699;">OUTPUT</span>);
&nbsp;&nbsp;}
}

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>loop</b></span>() {
&nbsp;&nbsp;<span style="color: #cc6600;">int</span> seconds = 0;
&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> thisPin =0; thisPin &lt; ledCount; thisPin++){
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">if</span> (seconds &amp; mask[thisPin]) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(ledPins[thisPin], <span style="color: #006699;">HIGH</span>);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">else</span> {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(ledPins[thisPin], <span style="color: #006699;">LOW</span>);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;}
&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(1000);
&nbsp;&nbsp;seconds++;
&nbsp;&nbsp;<span style="color: #cc6600;">if</span> (seconds &gt;= 60) seconds = 0;
}


</pre>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
