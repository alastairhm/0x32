---
title: "Sending Arduino messages over serial port"
date: 2013-03-14T08:52:00+00:00
draft: true
tags: ["arduino", "blog-import", "geek", "lcd", "ruby", "sainsmart", "twitter"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<div style="text-align: left;">
<span style="background-color: white;"><span style="color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;">Video of sending a message to the Arduino over the serial port which then gets scrolled on a SainSmart LCD shield.</span></span></div>
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;"><br /></span>
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;">Idea was to use it to display tweets, just need to write the Ruby code to get the tweet and send it over the serial port now.</span><br />
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;"><br /></span>
<br />
<div class="separator" style="clear: both; text-align: center;">
<object class="BLOGGER-youtube-video" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" data-thumbnail-src="http://i.ytimg.com/vi/1xrbyvgB7L0/0.jpg" height="266" width="320"><param name="movie" value="http://www.youtube.com/v/1xrbyvgB7L0?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" /><param name="bgcolor" value="#FFFFFF" /><param name="allowFullScreen" value="true" /><embed width="320" height="266"  src="http://www.youtube.com/v/1xrbyvgB7L0?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" type="application/x-shockwave-flash" allowfullscreen="true"></embed></object></div>
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;"><br /></span>
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;"><br /></span>
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;">Here is the first version of the sketch uploaded to the Arduino.</span><br />
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;">All code can be found at<a href="http://www.blogger.com/goog_1929310187">&nbsp;</a></span><span style="color: #333333; font-family: arial, sans-serif; font-size: x-small;"><span style="line-height: 17px;"><a href="https://github.com/alastairhm/arduino.git">https://github.com/alastairhm/arduino.git</a></span></span><br />
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;"><br /></span>
<span style="background-color: white; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;"><br /></span>
<br />
<span style="background-color: #f6f6f6; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;"><br /></span>
<span style="background-color: #f6f6f6; color: #333333; font-family: arial, sans-serif; font-size: 13px; line-height: 17px;"><br /></span>
<br />
<pre><span style="color: #7e7e7e;">//&nbsp;Auto&nbsp;scroll&nbsp;a&nbsp;message&nbsp;on&nbsp;the&nbsp;LCD&nbsp;and&nbsp;receive&nbsp;new&nbsp;messages&nbsp;via&nbsp;Serial&nbsp;port.</span>
<span style="color: #7e7e7e;">//&nbsp;Alastair&nbsp;Montgomery&nbsp;(c)&nbsp;2013</span>
<span style="color: #7e7e7e;">//&nbsp;Version&nbsp;1.00</span>
&nbsp;
<span style="color: #7e7e7e;">//&nbsp;include&nbsp;the&nbsp;library&nbsp;code:</span>
#include&nbsp;&lt;<span style="color: #cc6600;">LiquidCrystal</span>.h&gt;
#include&nbsp;&lt;string.h&gt;

<span style="color: #7e7e7e;">//&nbsp;initialize&nbsp;the&nbsp;library&nbsp;with&nbsp;the&nbsp;numbers&nbsp;of&nbsp;the&nbsp;interface&nbsp;pins</span>
<span style="color: #7e7e7e;">//&nbsp;below&nbsp;for&nbsp;SainSmart&nbsp;LCD&nbsp;Shield</span>
<span style="color: #cc6600;">LiquidCrystal</span> lcd(8, 9, 4, 5, 6, 7);

<span style="color: #7e7e7e;">//Default&nbsp;Message</span>
<span style="color: #cc6600;">char</span> msg[256] = <span style="color: #006699;">"I'm afraid I can't do that Dave."</span>;
<span style="color: #cc6600;">char</span> buffer[256];
<span style="color: #cc6600;">int</span> newMsg = <span style="color: #cc6600;">true</span>;
<span style="color: #cc6600;">int</span> scrollAmount = 0;

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>setup</b></span>() {
&nbsp;&nbsp;<span style="color: #7e7e7e;">// set up the LCD's number of columns and rows: </span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">begin</span>(16,2);
&nbsp;&nbsp;<span style="color: #cc6600;"><b>Serial</b></span>.<span style="color: #cc6600;">begin</span>(9600);
}

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>loop</b></span>() {
&nbsp;&nbsp;
&nbsp;&nbsp;<span style="color: #7e7e7e;">//Read serial</span>
&nbsp;&nbsp;<span style="color: #cc6600;">if</span> (<span style="color: #cc6600;"><b>Serial</b></span>.<span style="color: #cc6600;">available</span>()){
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(100);
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">int</span> i = 0;
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">while</span> (<span style="color: #cc6600;"><b>Serial</b></span>.<span style="color: #cc6600;">available</span>() &gt; 0 &amp;&amp; i&lt;254){
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;buffer[i++]&nbsp;=&nbsp;<span style="color: #cc6600;"><b>Serial</b></span>.<span style="color: #cc6600;">read</span>();
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;buffer[i]&nbsp;=&nbsp;<span style="color: #006699;">'\0'</span>;
&nbsp;&nbsp;&nbsp;&nbsp;strcpy(msg,buffer);

&nbsp;&nbsp;&nbsp;&nbsp;newMsg&nbsp;=&nbsp;<span style="color: #cc6600;">true</span>;
&nbsp;&nbsp;}
&nbsp;
&nbsp;&nbsp;<span style="color: #cc6600;">if</span> (newMsg){
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">noAutoscroll</span>();
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">clear</span>();
&nbsp;&nbsp;&nbsp;&nbsp;scrollAmount&nbsp;=&nbsp;strlen(msg)-16;
&nbsp;&nbsp;&nbsp;&nbsp;newMsg&nbsp;=&nbsp;<span style="color: #cc6600;">false</span>;
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">setCursor</span>(0, 0);  
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">print</span>(<span style="color: #006699;">"***New Message***"</span>);    
&nbsp;&nbsp;}
&nbsp;&nbsp;
&nbsp;&nbsp;<span style="color: #7e7e7e;">// set the cursor to (0,1):</span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">setCursor</span>(0, 1);  
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">print</span>(msg);
&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(500);

&nbsp;&nbsp;<span style="color: #7e7e7e;">// set the cursor to (16,1):</span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">setCursor</span>(16,0);
&nbsp;&nbsp;<span style="color: #7e7e7e;">// set the display to automatically scroll:;</span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">autoscroll</span>();
&nbsp;&nbsp;<span style="color: #7e7e7e;">//lcd.noAutoscroll();</span>
&nbsp;&nbsp;<span style="color: #7e7e7e;">// print from 0 to 9:</span>
&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> thisChar = 0; thisChar &lt; scrollAmount+16; thisChar++) {
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">print</span>(<span style="color: #006699;">" "</span>);
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(700);
&nbsp;&nbsp;}
&nbsp;&nbsp;
&nbsp;&nbsp;<span style="color: #7e7e7e;">// turn off automatic scrolling</span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">noAutoscroll</span>();  
&nbsp;&nbsp;<span style="color: #7e7e7e;">// clear screen for the next loop:</span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">clear</span>();
}

</pre>
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
