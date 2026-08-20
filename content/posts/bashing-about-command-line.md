---
title: "Bashing about the command line"
date: 2012-10-24T14:59:00+01:00
draft: false
tags: ["bash", "blog-import", "geek", "linux"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Sometimes the best solution is the quickest one, sure I could have written a Ruby script to format the results of the find but a few bash commands achieved the same result.<br />
<br />



<br />
<div class="MsoNormal">
<span style="color: #1f497d; font-family: &quot;Courier New&quot;;">find
/svn/repos -name "authz" -exec grep dev {} ";" | grep -v
@dev | cut -d"=" -f 2|sed 's/,/\n/g'|sed 's/ //g'|sort|uniq &gt;
/tmp/dev.txt</span></div>
<br /><br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
