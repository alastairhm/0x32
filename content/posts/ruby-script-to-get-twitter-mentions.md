---
title: "Ruby Script to get Twitter mentions"
date: 2013-03-14T14:15:00+00:00
draft: false
tags: ["blog-import", "geek", "ruby", "twitter"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<div style="text-align: left;">
Here is a short Ruby script to check for mentions on Twitter, it uses the <a href="https://github.com/sferik/twitter" target="_blank">Twitter Gem</a>.</div>
<div style="text-align: left;">
Plan to use this to <a href="http://meekgonkey.blogspot.co.uk/2013/03/sending-arduino-messages-over-serial.html" target="_blank">send messages to my Arduino</a>, looking for a good Ruby Serial Port Gem now.</div>
<pre>&nbsp;</pre>
<pre>&nbsp;</pre>
<pre># Find your Twitter Mentions

require "rubygems"
require "twitter" #https://github.com/sferik/twitter for config details
require "pp"

prevID = 0
while true
 latestMention = Twitter.mentions(:count =&gt; 1)[0]
 if prevID != latestMention.id
  msg = latestMention.user.screen_name + " " + latestMention.text 
  #puts msg.size
  puts msg
  prevID = latestMention.id
 else
  puts "No new updates"
 end
 sleep 60
end

</pre>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
