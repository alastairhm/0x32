---
title: "Docker Doku Wiki"
date: 2016-04-20T15:27:00+01:00
draft: true
tags: ["blog-import", "docker", "doku", "geek", "lighttpd", "wiki"]
categories: ['Geek']
---

> **Note:** 1 of this post's 13 links are now broken — mostly dead 2008–2013 feed-syndication infrastructure (FeedBurner, Gawker, AOL's old blog network, Pheedo, Yahoo Pipes). Left as originally published.

<div dir="ltr" style="text-align: left;" trbidi="on">
Created a small footprint (less than 50mb) Docker image running the <a href="https://www.dokuwiki.org/dokuwiki#" target="_blank">Doku Wiki</a> on <a href="https://www.lighttpd.net/" target="_blank">Lighttpd</a> under <a href="http://alpinelinux.org/" target="_blank">Alpine Linux</a>.<br />
<br />
Git Hub =<a href="https://github.com/alastairhm/alpine-doku" target="_blank"> https://github.com/alastairhm/alpine-doku</a><br />
Docker Hub = <a href="https://hub.docker.com/r/alastairhm/alpine-doku/">https://hub.docker.com/r/alastairhm/alpine-doku/</a><br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOQqssteAzmQ_iIC6ubMWW4s5I1ICmrst2qqksT3EFREyjq8NvZDIIhDbj4xDqxBcTe0exnWCzg5dGVDUBORJJQqd6DTlVcutgelKuGjqrJmuQxXrmcxI5a0l74a1V1nvb_0OwRA7elV0/s1600/Screenshot%252B2016-04-20%252B03.24.18.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="177" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOQqssteAzmQ_iIC6ubMWW4s5I1ICmrst2qqksT3EFREyjq8NvZDIIhDbj4xDqxBcTe0exnWCzg5dGVDUBORJJQqd6DTlVcutgelKuGjqrJmuQxXrmcxI5a0l74a1V1nvb_0OwRA7elV0/s320/Screenshot%252B2016-04-20%252B03.24.18.png" width="320" /></a></div>
<h2>
Running</h2>
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;,Courier,monospace;">docker run --name "my-wiki" -d -p 80:80 alastairhm/alpine-doku</span></span><br />
<br />


Browse to install page <a href="http://localhost/install.php">http://localhost/install.php</a><br />
<br />


<h2>
<a class="anchor" href="https://github.com/alastairhm/alpine-doku#data-persistence" id="user-content-data-persistence"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Data Persistence</h2>
<br />
You can use volume mounts to persist your data outside the container for example<br />
<br />


<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;,Courier,monospace;">docker run --name "my-wiki" -d -p 80:80 -v $(pwd)/data:/var/doku/data -v $(pwd)/conf:/var/doku/conf alastairhm/alpine-doku</span></span><br />


<br />
this will create the data/ conf directories in your local directory.<br />


<br />
There is an issue with file permissions when using the volume mounts on a Mac so;<br />


<h3>
<a class="anchor" href="https://github.com/alastairhm/alpine-doku#backup" id="user-content-backup"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Backup</h3>
You can copy your Wiki out of your container with<br />


<div class="highlight highlight-source-shell">
<pre>docker cp my-wiki:/var/doku/data ./
docker cp my-wiki:/var/doku/conf ./</pre>
</div>
<h3>
<a class="anchor" href="https://github.com/alastairhm/alpine-doku#restore" id="user-content-restore"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Restore</h3>
Startup a new instance of your Doku container then<br />


<div class="highlight highlight-source-shell">
<pre>docker cp data my-wiki:/var/doku/
docker cp conf my-wiki:/var/doku/
docker my-wiki stop
docker my-wiki start</pre>
</div>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
