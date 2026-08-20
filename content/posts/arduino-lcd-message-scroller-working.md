---
title: "Arduino LCD Message Scroller working"
date: 2013-03-19T10:13:00+00:00
draft: false
tags: ["arduino", "blog-import", "geek", "lcd", "sainsmart", "scrolling"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Got my Arduino LCD message scroller working last night, will post a video later when I do an end to end test with my Twitter mentions.<br />
<div class="separator" style="clear: both; text-align: center;">
<object width="320" height="266" class="BLOGGER-youtube-video" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" data-thumbnail-src="https://ytimg.googleusercontent.com/vi/g2Ql86wt8dI/0.jpg"><param name="movie" value="https://www.youtube.com/v/g2Ql86wt8dI?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" /><param name="bgcolor" value="#FFFFFF" /><param name="allowFullScreen" value="true" /><embed width="320" height="266"  src="https://www.youtube.com/v/g2Ql86wt8dI?version=3&f=user_uploads&c=google-webdrive-0&app=youtube_gdata" type="application/x-shockwave-flash" allowfullscreen="true"></embed></object></div>
<br />
Here is the code (also at GitHub <a href="https://github.com/alastairhm/arduino.git">https://github.com/alastairhm/arduino.git</a>)<br />
<br />
<pre><span style="color: #7e7e7e;">//&nbsp;Auto&nbsp;scroll&nbsp;a&nbsp;message&nbsp;on&nbsp;the&nbsp;LCD&nbsp;and&nbsp;receive&nbsp;new&nbsp;messages&nbsp;via&nbsp;Serial&nbsp;port.</span>
<span style="color: #7e7e7e;">//&nbsp;Alastair&nbsp;Montgomery&nbsp;(c)&nbsp;2013</span>
<span style="color: #7e7e7e;">//&nbsp;Version&nbsp;1.02</span>
&nbsp;
<span style="color: #7e7e7e;">//&nbsp;include&nbsp;the&nbsp;library&nbsp;code:</span>
#include&nbsp;&lt;<span style="color: #cc6600;">LiquidCrystal</span>.h&gt;
#include&nbsp;&lt;string.h&gt;

<span style="color: #7e7e7e;">//&nbsp;initialize&nbsp;the&nbsp;library&nbsp;with&nbsp;the&nbsp;numbers&nbsp;of&nbsp;the&nbsp;interface&nbsp;pins</span>
<span style="color: #7e7e7e;">//&nbsp;below&nbsp;for&nbsp;SainSmart&nbsp;LCD&nbsp;Shield</span>
<span style="color: #cc6600;">LiquidCrystal</span> lcd(8, 9, 4, 5, 6, 7);

<span style="color: #cc6600;">const</span> <span style="color: #cc6600;">int</span> ledWidth = 16;
<span style="color: #cc6600;">const</span> <span style="color: #cc6600;">int</span> ledDepth = 2;

<span style="color: #7e7e7e;">//Default&nbsp;Message</span>
<span style="color: #cc6600;">char</span> msg[256] = <span style="color: #006699;">"Serial Message Version 1.02"</span>;
<span style="color: #cc6600;">char</span> buffer[256];
<span style="color: #cc6600;">int</span> newMsg = <span style="color: #cc6600;">true</span>;
<span style="color: #cc6600;">int</span> previous = 0;
<span style="color: #cc6600;">int</span> pos = 0;

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>setup</b></span>() {
&nbsp;&nbsp;<span style="color: #7e7e7e;">// set up the LCD's number of columns and rows: </span>
&nbsp;&nbsp;lcd.<span style="color: #cc6600;">begin</span>(ledWidth,ledDepth);
&nbsp;&nbsp;<span style="color: #cc6600;"><b>Serial</b></span>.<span style="color: #cc6600;">begin</span>(9600);
}

<span style="color: #cc6600;">void</span> printLine(<span style="color: #cc6600;">int</span> refreshSeconds, <span style="color: #cc6600;">int</span> lineNum){
&nbsp;&nbsp;<span style="color: #7e7e7e;">//Check if the current second since restart is a mod of refresh seconds , </span>
&nbsp;&nbsp;<span style="color: #7e7e7e;">//if it is then update the display , it must also not equal the previously </span>
&nbsp;&nbsp;<span style="color: #7e7e7e;">//stored value to prevent duplicate refreshes</span>
&nbsp;&nbsp;<span style="color: #cc6600;">if</span>((<span style="color: #cc6600;">millis</span>()/1000) % refreshSeconds == 0 &amp;&amp; previous != (<span style="color: #cc6600;">millis</span>()/1000)){
&nbsp;&nbsp;&nbsp;&nbsp;previous&nbsp;=&nbsp;&nbsp;(<span style="color: #cc6600;">millis</span>()/1000);  <span style="color: #7e7e7e;">//Store the current time we entered for comparison on the next cycle</span>
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">setCursor</span>(0, lineNum);    <span style="color: #7e7e7e;">//Set our draw position , set second param to 0 to use the top line</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">char</span> lcdTop[ledWidth];              <span style="color: #7e7e7e;">//Create a char array to store the text for the line</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">int</span> copySize = ledWidth;            <span style="color: #7e7e7e;">// What is the size of our screen , this could probably be moved outside the loop but its more dynamic like this</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">if</span>(strlen(msg) &lt; copySize)
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #7e7e7e;">//if the msg is smaller than the current buffer use its length instead;</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;copySize&nbsp;=&nbsp;strlen(msg);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #7e7e7e;">//Store the current position temporarily and invert its sign if its negative since we are going in reverse</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">int</span> tempPos = pos;
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">if</span>(tempPos &lt; 0)
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tempPos&nbsp;=&nbsp;-(tempPos);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #7e7e7e;">//Build the lcd text by copying the required text out of our template msg variable </span>
&nbsp;&nbsp;&nbsp;&nbsp;memcpy(&amp;lcdTop[0],&amp;msg[tempPos],copySize);
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">print</span>(lcdTop);            <span style="color: #7e7e7e;">//Print it from position 0</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #7e7e7e;">//Increase the current position and check if the position + 16 (screen size) would be larger than the msg length , if it is go in reverse by inverting the sign.</span>
&nbsp;&nbsp;&nbsp;&nbsp;pos&nbsp;+=&nbsp;1;
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">if</span>(pos +copySize &gt;= strlen(msg))
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pos&nbsp;=&nbsp;-(pos);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">setCursor</span>(0, 0);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">print</span>(<span style="color: #006699;">"           "</span>);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;}
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
&nbsp;&nbsp;&nbsp;&nbsp;pos&nbsp;=&nbsp;0;
&nbsp;&nbsp;}
&nbsp;
&nbsp;&nbsp;<span style="color: #cc6600;">if</span> (newMsg){
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">noAutoscroll</span>();
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">clear</span>();
&nbsp;&nbsp;&nbsp;&nbsp;newMsg&nbsp;=&nbsp;<span style="color: #cc6600;">false</span>;
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">setCursor</span>(0, 0);  
&nbsp;&nbsp;&nbsp;&nbsp;lcd.<span style="color: #cc6600;">print</span>(<span style="color: #006699;">"New Message"</span>);    
&nbsp;&nbsp;}
&nbsp;
&nbsp;&nbsp;printLine(1,1);
}&nbsp;</pre>
<pre></pre>
<pre>Still a few rough edges to smooth out but its almost there.</pre>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
