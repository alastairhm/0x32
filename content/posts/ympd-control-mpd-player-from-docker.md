---
title: "ympd - Control MPD player from a Docker Image"
date: 2016-04-28T12:24:00+01:00
draft: true
tags: ["blog-import", "docker", "geek", "mp3", "mpd", "music", "radio"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
After setting up a Streaming radio instance of MPD/Icecast2 running in a <a href="https://hub.docker.com/r/alastairhm/docker-icecast/" target="_blank">Docker image</a>&nbsp;I was looking for a nice front end to control it.<br />
<br />
I found <a href="https://www.ympd.org/" target="_blank">ympd</a> a MPD web GUI written in C, so created a Docker image to run it,&nbsp;<a href="https://hub.docker.com/r/alastairhm/docker-icecast/">https://hub.docker.com/r/alastairhm/docker-icecast/</a>&nbsp;it uses Alpine Linux so the image is only 6mb is size.<br />
<br />
You run it linking to your Docker image which is running MPD.<br />
<br />
<span style="background-color: #eaeef3; color: #333333; font-family: Consolas, 'Liberation Mono', Courier, monospace; font-size: 16px; line-height: 24px; white-space: pre;">docker run --name my-ympd -d -p 8080:8080 --link your_mpd_container:mpdhost alastair/docker-ympd</span><br />
<br />
Then browse to http://localhost:8080/<br />
<br />
For more info checkout this <a href="https://github.com/alastairhm/docker-ympd/blob/master/docker-compose.yml" target="_blank">Docker compose</a> file which runs both my icecast and ympd images.<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
