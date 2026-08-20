---
title: "Setting browser size and position with watir-webdriver"
date: 2011-06-23T09:22:00+01:00
draft: true
tags: ["blog-import", "geek", "ruby", "watir", "web-testing", "webdriver"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">In working on my automated web app test using <a href="https://github.com/jarib">watir-webdriver</a> I need to change the window size and move it on the screen.<br />
<br />
From asking the question at <a href="http://stackoverflow.com/questions/6126311/setting-browser-window-size-in-watir-webdriver">StackOverFlow.com</a> you can do this with the following commands;<br />
<br />
<span class="Apple-style-span" style="background-color: #999999; border-collapse: collapse; font-size: 14px; line-height: 18px;"><span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;"></span></span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">browser = Watir::Browser.new(:firefox)</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">browser.execute_script('window.resizeTo(800,600)')</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">browser.execute_script('window.moveTo(0,0)')</span><br />
<br />
<br />
<div dir="ltr" style="text-align: left;" trbidi="on"><a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div></div>
