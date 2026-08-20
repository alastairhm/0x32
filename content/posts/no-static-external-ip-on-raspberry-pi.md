---
title: "No static external IP on Raspberry Pi"
date: 2014-01-12T14:07:00+00:00
draft: false
tags: ["blog-import", "geek", "raspberry-pi", "ruby", "twitter"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
My Internet provider doesn't supply me with a static IP address with my broadband, so my Raspberry Pi external web address can wander if my router or connectigets reset. There are third party sites which will provide you with a static URL which follows your wandering IP address but its fun to do it yourself.<br />
<br />
To keep me updated on the current IP I wrote a Ruby script which I run via crontab to check and Tweet me is the IP address changes.<br />
<br />
<pre style="color: #333333; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 12px; line-height: 18px;"><div class="line" id="LC1" style="padding-left: 10px;">
<span class="c1" style="color: #999988; font-style: italic;">#!/usr/bin/ruby</span></div>
<div class="line" id="LC2" style="padding-left: 10px;">
<span class="nb" style="color: #0086b3;">require</span> <span class="s1" style="color: #dd1144;">'open-uri'</span></div>
<div class="line" id="LC3" style="padding-left: 10px;">
<span class="nb" style="color: #0086b3;">require</span> <span class="s1" style="color: #dd1144;">'twitter'</span></div>
<div class="line" id="LC4" style="padding-left: 10px;">
</div>
<div class="line" id="LC5" style="padding-left: 10px;">
<span class="n">twitDM</span> <span class="o" style="font-weight: bold;">=</span> <span class="s2" style="color: #dd1144;">"twitter_username"</span></div>
<div class="line" id="LC6" style="padding-left: 10px;">
</div>
<div class="line" id="LC7" style="padding-left: 10px;">
<span class="n">remote_ip</span> <span class="o" style="font-weight: bold;">=</span> <span class="nb" style="color: #0086b3;">open</span><span class="p">(</span><span class="s1" style="color: #dd1144;">'http://whatismyip.akamai.com'</span><span class="p">)</span><span class="o" style="font-weight: bold;">.</span><span class="n">read</span></div>
<div class="line" id="LC8" style="padding-left: 10px;">
<span class="n">old_ip</span> <span class="o" style="font-weight: bold;">=</span> <span class="no" style="color: teal;">File</span><span class="o" style="font-weight: bold;">.</span><span class="n">open</span><span class="p">(</span><span class="s1" style="color: #dd1144;">'remote_ip.txt'</span><span class="p">,</span> <span class="s1" style="color: #dd1144;">'r'</span><span class="p">)</span><span class="o" style="font-weight: bold;">.</span><span class="n">read</span></div>
<div class="line" id="LC9" style="padding-left: 10px;">
</div>
<div class="line" id="LC10" style="padding-left: 10px;">
<span class="k" style="font-weight: bold;">if</span> <span class="p">(</span><span class="n">remote_ip</span> <span class="o" style="font-weight: bold;">!=</span> <span class="n">old_ip</span><span class="p">)</span> <span class="k" style="font-weight: bold;">then</span></div>
<div class="line" id="LC11" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;<span class="no" style="color: teal;">File</span><span class="o" style="font-weight: bold;">.</span><span class="n">open</span><span class="p">(</span><span class="s1" style="color: #dd1144;">'remote_ip.txt'</span><span class="p">,</span> <span class="s2" style="color: #dd1144;">"w"</span><span class="p">)</span> <span class="p">{</span> <span class="o" style="font-weight: bold;">|</span><span class="n">file</span><span class="o" style="font-weight: bold;">|</span>  <span class="n">file</span><span class="o" style="font-weight: bold;">.</span><span class="n">write</span><span class="p">(</span><span class="n">remote_ip</span><span class="p">)}</span></div>
<div class="line" id="LC12" style="padding-left: 10px;">
</div>
<div class="line" id="LC13" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">client</span> <span class="o" style="font-weight: bold;">=</span> <span class="no" style="color: teal;">Twitter</span><span class="o" style="font-weight: bold;">::</span><span class="no" style="color: teal;">REST</span><span class="o" style="font-weight: bold;">::</span><span class="no" style="color: teal;">Client</span><span class="o" style="font-weight: bold;">.</span><span class="n">new</span> <span class="k" style="font-weight: bold;">do</span> <span class="o" style="font-weight: bold;">|</span><span class="n">config</span><span class="o" style="font-weight: bold;">|</span></div>
<div class="line" id="LC14" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config</span><span class="o" style="font-weight: bold;">.</span><span class="n">consumer_key</span>        <span class="o" style="font-weight: bold;">=</span> <span class="s2" style="color: #dd1144;">"xxxx"</span></div>
<div class="line" id="LC15" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config</span><span class="o" style="font-weight: bold;">.</span><span class="n">consumer_secret</span>     <span class="o" style="font-weight: bold;">=</span> <span class="s2" style="color: #dd1144;">"xxxx"</span></div>
<div class="line" id="LC16" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config</span><span class="o" style="font-weight: bold;">.</span><span class="n">access_token</span>        <span class="o" style="font-weight: bold;">=</span> <span class="s2" style="color: #dd1144;">"xxxx"</span></div>
<div class="line" id="LC17" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config</span><span class="o" style="font-weight: bold;">.</span><span class="n">access_token_secret</span> <span class="o" style="font-weight: bold;">=</span> <span class="s2" style="color: #dd1144;">"xxxx"</span></div>
<div class="line" id="LC18" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;<span class="k" style="font-weight: bold;">end</span></div>
<div class="line" id="LC19" style="padding-left: 10px;">
</div>
<div class="line" id="LC20" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">client</span><span class="o" style="font-weight: bold;">.</span><span class="n">update</span><span class="p">(</span><span class="s2" style="color: #dd1144;">"D </span><span class="si" style="color: #dd1144;">#{</span><span class="n">twitDM</span><span class="si" style="color: #dd1144;">}</span><span class="s2" style="color: #dd1144;"> My IP address is now </span><span class="si" style="color: #dd1144;">#{</span><span class="n">remote_ip</span><span class="si" style="color: #dd1144;">}</span><span class="s2" style="color: #dd1144;">"</span><span class="p">)</span></div>
<div class="line" id="LC21" style="padding-left: 10px;">
</div>
<div class="line" id="LC22" style="padding-left: 10px;">
<span class="k" style="font-weight: bold;">else</span></div>
<div class="line" id="LC23" style="padding-left: 10px;">
&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb" style="color: #0086b3;">puts</span> <span class="s2" style="color: #dd1144;">"IP addresses match"</span></div>
<div class="line" id="LC24" style="padding-left: 10px;">
<span class="k" style="font-weight: bold;">end</span></div>
</pre>
<br />
You can clone the script at Github&nbsp;<a href="https://github.com/alastairhm/myip">https://github.com/alastairhm/myip</a>&nbsp;it uses a Ruby Twitter API library which can be found at&nbsp;<a href="https://github.com/sferik/twitter">https://github.com/sferik/twitter</a>&nbsp;to do the direct message with the new IP.<br />
Full details about getting your Twitter API keys can be found at&nbsp;<a href="https://dev.twitter.com/">https://dev.twitter.com/</a><br />
<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
