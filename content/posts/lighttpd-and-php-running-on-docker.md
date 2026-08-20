---
title: "Lighttpd and PHP running on Docker Example"
date: 2016-04-18T10:46:00+01:00
draft: true
tags: ["blog-import", "docker", "geek", "lighttpd", "php"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Here is a low resource Lighttpd with PHP Docker image running on Alpine Linux, only ~37MB image.<br />
<br />
Github = <a href="https://github.com/alastairhm/alpine-lighttpd-php">https://github.com/alastairhm/alpine-lighttpd-php</a><br />
Docker Hub = <a href="https://hub.docker.com/r/alastairhm/alpine-lighttpd-php/">https://hub.docker.com/r/alastairhm/alpine-lighttpd-php/</a><br />
<br />
Create an example PHP file in your local directory<br />
<br />
<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">echo "<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;"><span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">&lt;</span></span>?php phpinfo(); ?<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">&gt;</span>" &gt;&gt; index.php</span><br />
<br />
Then start the Docker image;<br />
<br />
<span style="font-family: &quot;courier new&quot; , &quot;courier&quot; , monospace;">docker run --name "my-lighttpd-php" -p 8000:80 -v $(pwd):/var/www alastairhm/alpine-lighttpd-php</span><br />
<br />
Browse to <a href="http://localhost:8000/">http://localhost:8000/</a><br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYWIck0V67HWxjgOpScXap5OEx2vv1gBjwCgyvR6BLSFY6UyA9KmMkeljWAO1qYnEBfaLGbzGRqyNlYZ0EIJ32tlzMwcGqmdowivbjtawBEZDlxGBQ27AgmsnDVKpHsp3A3Ej5fhdmykU/s1600/Screenshot%252B2016-04-18%252B10.44.29.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="227" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYWIck0V67HWxjgOpScXap5OEx2vv1gBjwCgyvR6BLSFY6UyA9KmMkeljWAO1qYnEBfaLGbzGRqyNlYZ0EIJ32tlzMwcGqmdowivbjtawBEZDlxGBQ27AgmsnDVKpHsp3A3Ej5fhdmykU/s320/Screenshot%252B2016-04-18%252B10.44.29.png" width="320" /></a></div>
<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
