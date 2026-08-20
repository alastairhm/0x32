---
title: "Owncloud running on Docker"
date: 2016-04-09T16:37:00+01:00
draft: false
tags: ["blog-import", "devops", "docker", "geek", "owncloud"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8RKV82q4iv9LCHFP4oHyi9dmec8GCOJnOA0TxCxG0wjYYRpm2zwhXNBe-ju8bxF_LDf1PzbK80bCqLX6QyCrgxxuWlCFaGGt4Qj1vob0N2OSF7SfbqZmIUlgGUflSnYVkVUcQrxqU1bg/s1600/Screenshot%252B2016-04-09%252B04.33.41.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="194" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8RKV82q4iv9LCHFP4oHyi9dmec8GCOJnOA0TxCxG0wjYYRpm2zwhXNBe-ju8bxF_LDf1PzbK80bCqLX6QyCrgxxuWlCFaGGt4Qj1vob0N2OSF7SfbqZmIUlgGUflSnYVkVUcQrxqU1bg/s320/Screenshot%252B2016-04-09%252B04.33.41.png" width="320" /></a></div>
<h1>
&nbsp;Owncloud Running on Docker</h1>
Just a quick test getting ownCloud to run on Docker<br />


<h2>
<a class="anchor" href="https://github.com/alastairhm/owncloud#refences" id="user-content-refences"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Refences</h2>
<ul>
<li>Owncloud Docker information : <a href="https://hub.docker.com/r/library/owncloud/">https://hub.docker.com/r/library/owncloud/</a></li>
<li>mySQL Docker information : <a href="https://hub.docker.com/_/mysql/">https://hub.docker.com/_/mysql/</a></li>
</ul>
<h2>
<a class="anchor" href="https://github.com/alastairhm/owncloud#setup-the-database-connection" id="user-content-setup-the-database-connection"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Setup the database connection</h2>
Enter details as follows (as setup in the compose file);<br />


<ul>
<li>Choose MySQL/MariaDB</li>
<li>Database user : owncloud</li>
<li>Database password : password</li>
<li>Database name : owncloud</li>
<li>Host : mysql</li>
</ul>
<h2>
<a class="anchor" href="https://github.com/alastairhm/owncloud#local-volume" id="user-content-local-volume"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Local Volume</h2>
Create a local directory for your ownCloud files /var/www/owncloud<br />


<h2>
<a class="anchor" href="https://github.com/alastairhm/owncloud#running" id="user-content-running"><svg class="octicon octicon-link" height="16" viewbox="0 0 16 16" width="16"><path d="M4 9h1v1h-1c-1.5 0-3-1.69-3-3.5s1.55-3.5 3-3.5h4c1.45 0 3 1.69 3 3.5 0 1.41-0.91 2.72-2 3.25v-1.16c0.58-0.45 1-1.27 1-2.09 0-1.28-1.02-2.5-2-2.5H4c-0.98 0-2 1.22-2 2.5s1 2.5 2 2.5z m9-3h-1v1h1c1 0 2 1.22 2 2.5s-1.02 2.5-2 2.5H9c-0.98 0-2-1.22-2-2.5 0-0.83 0.42-1.64 1-2.09v-1.16c-1.09 0.53-2 1.84-2 3.25 0 1.81 1.55 3.5 3 3.5h4c1.45 0 3-1.69 3-3.5s-1.5-3.5-3-3.5z"></path></svg></a>Running</h2>
Clone the <a href="https://github.com/alastairhm/owncloud" target="_blank">repo</a> then run the following in the directory<br />


docker-compose -d up<br />


then browse to http://localhost/<br />
<br />
<a href="https://github.com/alastairhm/owncloud">https://github.com/alastairhm/owncloud</a><br />
<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
