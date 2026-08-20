---
title: "Sainsmart LCD Shield Test"
date: 2013-03-06T22:35:00+00:00
draft: false
tags: ["arduino", "blog-import", "geek", "lcd"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Testing my Sainsmart LCD Shield.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<object width="320" height="266" class="BLOGGER-youtube-video" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" data-thumbnail-src="http://i.ytimg.com/vi/xx7y3yGC76A/0.jpg"><param name="movie" value="http://www.youtube.com/v/xx7y3yGC76A?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" /><param name="bgcolor" value="#FFFFFF" /><param name="allowFullScreen" value="true" /><embed width="320" height="266"  src="http://www.youtube.com/v/xx7y3yGC76A?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" type="application/x-shockwave-flash" allowfullscreen="true"></embed></object></div>
<br />
<br />
<pre><span style="color: #7e7e7e;">/*</span>
<span style="color: #7e7e7e;">&nbsp;&nbsp;LiquidCrystal&nbsp;Library&nbsp;-&nbsp;Hello&nbsp;World</span>
<span style="color: #7e7e7e;">&nbsp;</span>
<span style="color: #7e7e7e;">&nbsp;Demonstrates&nbsp;the&nbsp;use&nbsp;a&nbsp;16x2&nbsp;LCD&nbsp;display.&nbsp;&nbsp;The&nbsp;LiquidCrystal</span>
<span style="color: #7e7e7e;">&nbsp;library&nbsp;works&nbsp;with&nbsp;all&nbsp;LCD&nbsp;displays&nbsp;that&nbsp;are&nbsp;compatible&nbsp;with&nbsp;the&nbsp;</span>
<span style="color: #7e7e7e;">&nbsp;Hitachi&nbsp;HD44780&nbsp;driver.&nbsp;There&nbsp;are&nbsp;many&nbsp;of&nbsp;them&nbsp;out&nbsp;there,&nbsp;and&nbsp;you</span>
<span style="color: #7e7e7e;">&nbsp;can&nbsp;usually&nbsp;tell&nbsp;them&nbsp;by&nbsp;the&nbsp;16-pin&nbsp;interface.</span>
<span style="color: #7e7e7e;">&nbsp;</span>
<span style="color: #7e7e7e;">&nbsp;This&nbsp;sketch&nbsp;prints&nbsp;"Hello&nbsp;World!"&nbsp;to&nbsp;the&nbsp;LCD</span>
<span style="color: #7e7e7e;">&nbsp;and&nbsp;shows&nbsp;the&nbsp;time.</span>
<span style="color: #7e7e7e;">&nbsp;</span>
<span style="color: #7e7e7e;">&nbsp;&nbsp;The&nbsp;circuit:</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;LCD&nbsp;RS&nbsp;pin&nbsp;to&nbsp;digital&nbsp;pin&nbsp;12</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;LCD&nbsp;Enable&nbsp;pin&nbsp;to&nbsp;digital&nbsp;pin&nbsp;11</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;LCD&nbsp;D4&nbsp;pin&nbsp;to&nbsp;digital&nbsp;pin&nbsp;5</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;LCD&nbsp;D5&nbsp;pin&nbsp;to&nbsp;digital&nbsp;pin&nbsp;4</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;LCD&nbsp;D6&nbsp;pin&nbsp;to&nbsp;digital&nbsp;pin&nbsp;3</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;LCD&nbsp;D7&nbsp;pin&nbsp;to&nbsp;digital&nbsp;pin&nbsp;2</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;LCD&nbsp;R/W&nbsp;pin&nbsp;to&nbsp;ground</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;10K&nbsp;resistor:</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;ends&nbsp;to&nbsp;+5V&nbsp;and&nbsp;ground</span>
<span style="color: #7e7e7e;">&nbsp;*&nbsp;wiper&nbsp;to&nbsp;LCD&nbsp;VO&nbsp;pin&nbsp;(pin&nbsp;3)</span>
<span style="color: #7e7e7e;">&nbsp;</span>
<span style="color: #7e7e7e;">&nbsp;Library&nbsp;originally&nbsp;added&nbsp;18&nbsp;Apr&nbsp;2008</span>
<span style="color: #7e7e7e;">&nbsp;by&nbsp;David&nbsp;A.&nbsp;Mellis</span>
<span style="color: #7e7e7e;">&nbsp;library&nbsp;modified&nbsp;5&nbsp;Jul&nbsp;2009</span>
<span style="color: #7e7e7e;">&nbsp;by&nbsp;Limor&nbsp;Fried&nbsp;(http://www.ladyada.net)</span>
<span style="color: #7e7e7e;">&nbsp;example&nbsp;added&nbsp;9&nbsp;Jul&nbsp;2009</span>
<span style="color: #7e7e7e;">&nbsp;by&nbsp;Tom&nbsp;Igoe</span>
<span style="color: #7e7e7e;">&nbsp;modified&nbsp;22&nbsp;Nov&nbsp;2010</span>
<span style="color: #7e7e7e;">&nbsp;by&nbsp;Tom&nbsp;Igoe</span>
<span style="color: #7e7e7e;">&nbsp;</span>
<span style="color: #7e7e7e;">&nbsp;This&nbsp;example&nbsp;code&nbsp;is&nbsp;in&nbsp;the&nbsp;public&nbsp;domain.</span>

<span style="color: #7e7e7e;">&nbsp;http://www.arduino.cc/en/Tutorial/LiquidCrystal</span>
<span style="color: #7e7e7e;">&nbsp;*/</span>

<span style="color: #7e7e7e;">//&nbsp;include&nbsp;the&nbsp;library&nbsp;code:</span>
#include&nbsp;&lt;<span style="color: #cc6600;">LiquidCrystal</span>.h&gt;

<span style="color: #7e7e7e;">//&nbsp;initialize&nbsp;the&nbsp;library&nbsp;with&nbsp;the&nbsp;numbers&nbsp;of&nbsp;the&nbsp;interface&nbsp;pins</span>
<span style="color: #7e7e7e;">//LiquidCrystal&nbsp;lcd(12,&nbsp;11,&nbsp;5,&nbsp;4,&nbsp;3,&nbsp;2);</span>
<span style="color: #cc6600;">LiquidCrystal</span> lcd(8, 9, 4, 5, 6, 7);

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>setup</b></span>() {
&nbsp;&nbsp;<span style="color: #7e7e7e;">// set up the LCD's number of columns and rows: </span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">begin</span>(16, 2);
&nbsp;&nbsp;<span style="color: #7e7e7e;">// Print a message to the LCD.</span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">print</span>(<span style="color: #006699;">"hello, world!"</span>);
}

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>loop</b></span>() {
&nbsp;&nbsp;<span style="color: #7e7e7e;">// set the cursor to column 0, line 1</span>
&nbsp;&nbsp;<span style="color: #7e7e7e;">// (note: line 1 is the second row, since counting begins with 0):</span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">setCursor</span>(0, 1);
&nbsp;&nbsp;<span style="color: #7e7e7e;">// print the number of seconds since reset:</span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">print</span>(<span style="color: #cc6600;">millis</span>()/1000);
}

</pre>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
