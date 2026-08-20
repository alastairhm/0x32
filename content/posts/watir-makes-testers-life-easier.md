---
title: "WATIR makes a tester's life easier."
date: 2011-06-29T14:36:00+01:00
draft: true
tags: ["blog-import", "geek", "ruby", "watir", "web-testing", "webdriver"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">I am constantly amazed that <a href="http://watir.com/">Watir</a> and <a href="http://www.ruby-lang.org/en/">Ruby</a> make software testing a web application so easy.<br />
For example finding all the links in a table based on their text starting with a string.<br />
<br />
<span class="Apple-style-span" style="background-color: #cccccc;"><span></span>stub = "0 Text"</span><br />
<span class="Apple-style-span" style="background-color: #cccccc;">browser.table(:id,"myTable").links(:text,/#{stub}/).each { |link| puts link.text }</span><br />
<span class="Apple-style-span" style="background-color: #cccccc;"><br />
</span><br />
This will return all the links in the table "myTable" with text starting with "0 Text"<br />
<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
