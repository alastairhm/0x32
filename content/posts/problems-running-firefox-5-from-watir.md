---
title: "Problems running Firefox 5 from watir-webdriver on Mac OS 10.5"
date: 2011-07-29T14:15:00+01:00
draft: true
tags: ["blog-import", "firefox", "geek", "watir", "web-testing", "webdriver", "workaround"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">Finally decided it was time to update my watir-webdriver development environment to the latest version of Firefox. I have been happily using Firefox 3.6.19 on my 64bit Intel Mac 10.5 and yesterday made the jump to Firefox 5.<br />
<br />
To my horror there is a bug in Firefox 4 and 5 which causes problems when attempting to start Firefox from the command line (basically what watir-webdriver does).<br />
<br />
Thankfully with the help of <a href="https://github.com/jarib">Jarib Bakken</a> I was able to use the workaround detailed on this <a href="http://asqueella.blogspot.com/2010/12/dyld-unknown-required-load-command.html">blog post</a>.<br />
<br />
The work around is to strip the x86_64 part from firefox-bin using ditto:<br />
<br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;">cd /Applications/Firefox.app/Contents/MacOS</span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;">mv firefox-bin firefox-bin.original</span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;">ditto --arch i386 firefox-bin.original firefox-bin</span>&nbsp;</span><br />
<br />
This will solve the problem until we can upgrade to a later version of Mac Os.<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
