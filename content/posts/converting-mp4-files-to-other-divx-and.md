---
title: "Converting MP4 files to other divX and mp3 formats"
date: 2010-01-20T12:00:00+00:00
draft: true
tags: ["blog-import", "divx", "ffmpeg", "geek", "linux", "mencoder", "mp3", "mp4", "script", "video"]
categories: ['Geek']
---

I find myself often converting <a href="http://en.wikipedia.org/wiki/MPEG-4">MP4 video files</a> to <a href="http://www.divx.com/">divX</a> and <a href="http://en.wikipedia.org/wiki/MP3">mp3</a> format to play on my <a href="http://www.lge.com/products/model/detail/kc910.jhtml">LG phone</a>.<div>I used to do this with <a href="http://www.videolan.org/vlc/index.html">VLC</a> application but this required too much button poking on my part.</div><div><br /></div><div>So after reading up on the Linux command line <a href="http://ffmpeg.org/">ffmpeg</a> and <a href="http://www.mplayerhq.hu/">mencoder</a> utilities I've created this basic shell script to do it automatically. </div><div><br /><code><br />#!/bin/bash<br />echo "MP4 Conversion"<br />for f in *.mp4;<br />do<br /> echo "...Processing $f file..."<br /> ffmpeg -i "$f" -vn -ac 2 -acodec libmp3lame -ab 128k `echo $f|cut -d. -f1`.mp3 > /dev/null 2>&amp;1<br /> mencoder "$f" -ovc lavc -lavcopts vcodec=mpeg4:vpass=1 -oac mp3lame -lameopts vbr=3 -o `echo $f|cut -d. -f1`.divx > /dev/null 2>&amp;1<br />done<br /></code><br /></div><div>This will convert all the mp4 files in the local directory to both divx and mp3 format ready to be transferred to my phone. Obviously you need to have the ffmpeg, mencoder and lame mp3 encoder installed on your Linux machine for this too work.</div><div><br /><a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
