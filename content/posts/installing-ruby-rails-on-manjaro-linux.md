---
title: "Installing Ruby Rails on Manjaro Linux"
date: 2014-02-28T12:08:00+00:00
draft: false
tags: ["blog-import", "geek", "linux", "manjaro", "rails", "ruby"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Thought I'd give Rails another go on my newly created Manjaro Linux VM.<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAY-9P0iuvGBpUXG9-rrKgREuzE-j2CqdrKToThQTsoovZWMp4GYUe205L03o9LH5VwJsI4zV6Hk9wY_5_ps_m3THhr2vHkWs5-fYcOgWHcBqEuv_IuvWkhVrWts656Yd3omDC6UsPylY/s1600/Manjaro+Rails.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAY-9P0iuvGBpUXG9-rrKgREuzE-j2CqdrKToThQTsoovZWMp4GYUe205L03o9LH5VwJsI4zV6Hk9wY_5_ps_m3THhr2vHkWs5-fYcOgWHcBqEuv_IuvWkhVrWts656Yd3omDC6UsPylY/s1600/Manjaro+Rails.png" height="184" width="320" /></a></div>
<br />
<br />
<br />
<br />
<br />
After filling in a couple of required packages the above screenshot shows it firing through the Rails install.<br />
<br />
To get to this stage I did the following;<br />
<br />
<ul style="text-align: left;">
<li><span style="font-family: &quot;Courier New&quot;,Courier,monospace;">sudo pacman -S base-devel ruby sqlite3 nodejs</span></li>
<li>Added <span style="font-family: &quot;Courier New&quot;,Courier,monospace;">/home/alastair/.gem/ruby/2.1.0/bin</span> to my path in .bashrc </li>
<li><span style="font-family: &quot;Courier New&quot;,Courier,monospace;">gem install rails</span></li>
<li><span style="font-family: &quot;Courier New&quot;,Courier,monospace;">gem install execjs </span></li>
</ul>
After a few minutes got the following successful install<br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1tm8RGzy6qE1OkPDK9KenjY3ltDKGDgRrgOTTPNqCrHw1-47CqdgaQBuyZr_uL24ON5NFxP4YkNjm4AsVr931CPMR2G2morv8ybd58tJkC2U83DbKc7UMt2RW7M8A8X4LOtckwpT_0Bo/s1600/Manjaro+Rails2.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1tm8RGzy6qE1OkPDK9KenjY3ltDKGDgRrgOTTPNqCrHw1-47CqdgaQBuyZr_uL24ON5NFxP4YkNjm4AsVr931CPMR2G2morv8ybd58tJkC2U83DbKc7UMt2RW7M8A8X4LOtckwpT_0Bo/s1600/Manjaro+Rails2.png" height="184" width="320" /></a></div>
<br />
<br />
<br />
Now to dig out that Rails tutorial I was working through.<br />
<br />
<b>Update</b>,<br />
Turns out can't start a rails server do it a missing JavaScript Runtime, bit more searching require.<br />
<br />
<b>Update2</b>,<br />
Found the answer on the Arch Linux Wiki which worked updated the instructions above.<br />
<ul style="text-align: left;">
<li><span style="font-family: &quot;Courier New&quot;, Courier, monospace;">sudo pacman -S nodejs</span><b>&nbsp;</b> </li>
</ul>
Success<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjC_jMQgtCeY4Fv0_6ghJMGdqbTSPv2MZQdmVgfiZ8sVh5ZEb9mLW1gaKCb0RcRxB-TRHc3iWEyMOjFX2p8QvR7xWGllo5RKRUiMLaKtYLb7nGTS72nUu6jci2iPJXa-VHYXCLK91OaGQc/s1600/Manjaro+Rails3.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjC_jMQgtCeY4Fv0_6ghJMGdqbTSPv2MZQdmVgfiZ8sVh5ZEb9mLW1gaKCb0RcRxB-TRHc3iWEyMOjFX2p8QvR7xWGllo5RKRUiMLaKtYLb7nGTS72nUu6jci2iPJXa-VHYXCLK91OaGQc/s1600/Manjaro+Rails3.png" height="184" width="320" /></a></div>
<br />
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
