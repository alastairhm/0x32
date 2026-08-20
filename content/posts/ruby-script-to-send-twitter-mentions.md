---
title: "Ruby Script to send Twitter mentions over serial port"
date: 2013-03-19T12:00:00+00:00
draft: true
tags: ["arduino", "blog-import", "geek", "ruby", "serial-port", "twitter"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Short script to send Twitter mention messages to a serial port using Ruby and the gems twitter and serialport.<br />
<br />
<pre># Find your Twitter Mentions and send them to Arduino on Serial Port

require "rubygems"
require "twitter" #https://github.com/sferik/twitter for config details
require "serialport" #http://rubygems.org/gems/serialport
require "pp"

prevID = 0
puts "Setting Up Serial Port"
myport = SerialPort.new("/dev/ttyACM0","9600".to_i)
sleep(10)
while true
    puts "Checking for mentions"
    latestMention = Twitter.mentions(:count =&gt; 1)[0]
    if prevID != latestMention.id
        msg = latestMention.user.screen_name + " " + latestMention.text
        puts "-" + msg
        bytes = myport.write(msg)
        puts "-" + bytes.to_s
        prevID = latestMention.id
    else
        puts "-No new updates"
    end
    sleep 60
end
myport.close
</pre>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
