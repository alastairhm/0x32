---
title: "Ruby and RSS"
date: 2011-07-21T16:00:00+01:00
draft: false
tags: ["blog-import", "geek", "programming", "rss", "ruby"]
categories: ['Geek']
---

> **Note:** 1 of this post's 4 links are now broken — mostly dead 2008–2013 feed-syndication infrastructure (FeedBurner, Gawker, AOL's old blog network, Pheedo, Yahoo Pipes). Left as originally published.

<div dir="ltr" style="text-align: left;" trbidi="on">Started looking into access RSS from Ruby discovered it pretty much already built in as described in this article <a href="http://www.developer.com/services/article.php/3733171/Consuming-RSS-Feeds-with-Ruby.htm">Consuming RSS Feeds with Ruby</a>, full docs are available in the <a href="http://www.ruby-doc.org/stdlib/libdoc/rss/rdoc/index.html">Ruby Standard Library</a>.<br />
<br />
Accessing an RSS Feed is as simple as the following code snippet.<br />
<br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">require "rss"</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">rss_feed = "http://meekgonkey.blogspot.com/feeds/posts/default?alt=rss"</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">rss_content = ""</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">open(rss_feed) { |f|</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">rss_content = f.read</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">}</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">puts "Bytes read #{rss_content.length} from feed"</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">rss = RSS::Parser.parse(rss_content,false)</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">puts "Title: #{rss.channel.title}"</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">puts "RSS URL: #{rss.channel.link}"</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">puts "Total entries: #{rss.items.size}"</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">rss.items.each { |item|</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">puts item.title</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">puts item.link</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">puts item.date</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">puts "---"</span></span></span><br />
<span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="font-size: small;"><span style="background-color: #cccccc;">}</span></span></span><br />
<br />
Which when run produces something along the lines of;<br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Bytes read 115009 from feed</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Title: Geek Monkey</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">RSS URL: http://meekgonkey.blogspot.com/</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Total entries: 25</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Twitter from Ruby</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">http://meekgonkey.blogspot.com/2011/07/twitter-from-ruby.html</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Thu, 21 Jul 2011 13:20:00 +0100</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">---</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Github</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">http://meekgonkey.blogspot.com/2011/07/github.html</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Mon, 18 Jul 2011 13:59:00 +0100</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">---</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Google Plus</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">http://meekgonkey.blogspot.com/2011/07/google-plus.html</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Fri, 01 Jul 2011 10:50:00 +0100</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">---</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">WATIR makes a tester's life easier.</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">http://meekgonkey.blogspot.com/2011/06/watir-makes-testers-life-easier.html</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Wed, 29 Jun 2011 14:36:00 +0100</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">---</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Setting browser size and position with watir-webdriver</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">http://meekgonkey.blogspot.com/2011/06/setting-browser-size-and-position-with.html</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">Thu, 23 Jun 2011 09:22:00 +0100</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><span style="background-color: #cccccc;"><span style="background-color: white;">---</span></span></span></span><br />
<span style="font-size: x-small;"><span style="font-family: &quot;Courier New&quot;, &quot;Courier&quot;, monospace;"><br />
</span></span><br />
<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
