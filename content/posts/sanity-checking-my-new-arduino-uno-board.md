---
title: "Sanity Checking my new Arduino Uno Board"
date: 2012-11-22T22:13:00+00:00
draft: true
tags: ["arduino", "binary", "blog-import", "electronics", "geek"]
categories: ['Geek']
---

Quick sanity check of my new Arduino board using a LED Bar Graph.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<object width="320" height="266" class="BLOGGER-youtube-video" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" data-thumbnail-src="https://ytimg.googleusercontent.com/vi/L7ri5PBrsQU/0.jpg"><param name="movie" value="https://www.youtube.com/v/L7ri5PBrsQU?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" /><param name="bgcolor" value="#FFFFFF" /><param name="allowFullScreen" value="true" /><embed width="320" height="266"  src="https://www.youtube.com/v/L7ri5PBrsQU?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" type="application/x-shockwave-flash" allowfullscreen="true"></embed></object></div>
<br />
<br />
Here is the sketch I will be using.<br />
<br />
<pre><span style="color: #cc6600;">int</span> led1 = 8;
<span style="color: #cc6600;">int</span> led2 = 9;
<span style="color: #cc6600;">int</span> counter = 0;

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>setup</b></span>() {                
&nbsp;&nbsp;<span style="color: #7e7e7e;">// initialize the digital pin as an output.</span>
&nbsp;&nbsp;<span style="color: #cc6600;">pinMode</span>(led1, <span style="color: #006699;">OUTPUT</span>);
&nbsp;&nbsp;<span style="color: #cc6600;">pinMode</span>(led2, <span style="color: #006699;">OUTPUT</span>);  
}

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>loop</b></span>() {

&nbsp;&nbsp;<span style="color: #cc6600;">if</span> (counter &amp; 1) {
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(led1, <span style="color: #006699;">HIGH</span>);
&nbsp;&nbsp;}
&nbsp;&nbsp;<span style="color: #cc6600;">else</span> {
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(led1, <span style="color: #006699;">LOW</span>);
&nbsp;&nbsp;}

&nbsp;&nbsp;<span style="color: #cc6600;">if</span> (counter &amp; 2) {
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(led2, <span style="color: #006699;">HIGH</span>);
&nbsp;&nbsp;}
&nbsp;&nbsp;<span style="color: #cc6600;">else</span> {
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">digitalWrite</span>(led2, <span style="color: #006699;">LOW</span>);
&nbsp;&nbsp;}
&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(1000);
&nbsp;&nbsp;counter++;

}


</pre>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a>
