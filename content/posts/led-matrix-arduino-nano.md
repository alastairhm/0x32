---
title: "LED Matrix Arduino Nano"
date: 2015-01-28T08:42:00+00:00
draft: true
tags: ["arduino", "blog-import", "geek", "led", "max7219"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<iframe allowfullscreen="" frameborder="0" height="270" src="https://www.youtube.com/embed/IYBRyIQGTh0" width="480"></iframe><br />
<br />
<br />
<br />
<br />
<br />
Testing a LCD Max7219 Matrix with an Arduino Nano, thank to&nbsp;<a href="http://tronixstuff.com/2013/10/11/tutorial-arduino-max7219-led-display-driver-ic/" target="_blank">http://tronixstuff.com/2013/10/11/tutorial-arduino-max7219-led-display-driver-ic/</a><br />
<br />
<br />
<br />
<pre>#include&nbsp;&lt;<span style="color: #cc6600;">LedControl</span>.h&gt;

<span style="color: #cc6600;">LedControl</span> lc=<span style="color: #cc6600;">LedControl</span>(12,11,10,1);
<span style="color: #7e7e7e;">//&nbsp;pin&nbsp;12&nbsp;is&nbsp;connected&nbsp;to&nbsp;the&nbsp;MAX7219&nbsp;pin&nbsp;1</span>
<span style="color: #7e7e7e;">//&nbsp;pin&nbsp;11&nbsp;is&nbsp;connected&nbsp;to&nbsp;the&nbsp;CLK&nbsp;pin&nbsp;13</span>
<span style="color: #7e7e7e;">//&nbsp;pin&nbsp;10&nbsp;is&nbsp;connected&nbsp;to&nbsp;LOAD&nbsp;pin&nbsp;12</span>
<span style="color: #7e7e7e;">//&nbsp;1&nbsp;as&nbsp;we&nbsp;are&nbsp;only&nbsp;using&nbsp;1&nbsp;MAX7219</span>

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>setup</b></span>(){
&nbsp;&nbsp;lc.<span style="color: #cc6600;">shutdown</span>(0,<span style="color: #cc6600;">false</span>);
&nbsp;&nbsp;lc.<span style="color: #cc6600;">setIntensity</span>(0,8);
&nbsp;&nbsp;lc.<span style="color: #cc6600;">clearDisplay</span>(0); 
}

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><b>loop</b></span>(){
&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> row=0; row&lt;8; row++)
&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> col=0; col&lt;8; col++)
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lc.setLed(0,col,row,<span style="color: #cc6600;">true</span>);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lc.setLed(1,col,row,<span style="color: #cc6600;">false</span>);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(25);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;}

&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> row=0; row&lt;8; row++)
&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">for</span> (<span style="color: #cc6600;">int</span> col=0; col&lt;8; col++)
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lc.setLed(0,col,row,<span style="color: #cc6600;">false</span>);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lc.setLed(1,col,row,<span style="color: #cc6600;">true</span>);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #cc6600;">delay</span>(25);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;}&nbsp;&nbsp;
}


</pre>
</div>
