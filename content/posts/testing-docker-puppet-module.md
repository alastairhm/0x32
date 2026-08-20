---
title: "Testing Docker Puppet Module"
date: 2015-02-04T14:59:00+00:00
draft: false
tags: ["blog-import", "docker", "geek", "puppet", "vagrant"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
This module <a href="https://github.com/garethr/garethr-docker">https://github.com/garethr/garethr-docker</a>&nbsp;lets you install and control Docker using Puppet.<br />
<br />
For example this <a href="https://github.com/alastairhm/docker.git" target="_blank">Vagrant setup</a> spins up an Ubuntu VM and then using the Docker module spins up a Jenkins build server Docker container with a few simple commands;<br />
<br />
<pre>include docker
docker::image { 'jenkins': }

docker::run { 'some-jenkins':
  image =&gt; 'jenkins',
  ports =&gt; '8080:8080',
  volumes =&gt; '/vagrant/jenkins',
  use_name =&gt; true,
}</pre>
<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
