---
title: "Setting up Piwigo on Raspberry Pi"
date: 2013-04-10T23:20:00+01:00
draft: false
tags: ["blog-import", "gallery", "geek", "piwigo", "raspberry-pi"]
categories: ['Geek']
---

<div dir="ltr" style="text-align: left;" trbidi="on">
Installed the gallery software <a href="http://piwigo.org/" target="_blank">Piwigo</a> on my Raspberry Pi, screenshots below.<br />
<br />
After installing lighttpd and MySQL5 and the other <a href="http://piwigo.org/basics/requirements" target="_blank">prerequisites</a>&nbsp;you can install it using<br />
<br />
<span style="font-family: Courier New, Courier, monospace;">sudo apt-get install piwigo</span><br />
<br />
Although this is an older version, if you want the latest you'll need to go through the <a href="http://piwigo.org/basics/installation_manual" target="_blank">manual installation route</a> which is detailed on their web page.<br />
<br />
On my Ubuntu desktop, I did a trial run updating the version installed with apt-get using the Piwigo's internal upgrade option but this failed so might not be a viable option. <a href="http://piwigo.org/basics/upgrade" target="_blank">More upgrade information here.</a><br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiw91T8NxoN1abqAFuCxcjYg3yzk9Z_DgT-JReCvACYAsLrEhqXsOk4q1nejSXgOPtqGrBuZK4Gob2ySN6eyjnnSKNVQbYmV_WIeCSiPkLTIjvLwVwW-MbR9mUbwjG5FWFPf1lviXiYR98/s1600/Screenshot+from+2013-04-10+23:13:09.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="200" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiw91T8NxoN1abqAFuCxcjYg3yzk9Z_DgT-JReCvACYAsLrEhqXsOk4q1nejSXgOPtqGrBuZK4Gob2ySN6eyjnnSKNVQbYmV_WIeCSiPkLTIjvLwVwW-MbR9mUbwjG5FWFPf1lviXiYR98/s320/Screenshot+from+2013-04-10+23:13:09.png" width="320" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
Setting Up</div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhInyiCqYO9bVpKXuAdxOxgozV0ijkbRzilgoC_9Nv9FIolkkRAxd6re__rLzwXVTN7WOL-XO2CSECRf0xeUPQokRPACYg0ti6_-lQ76Nk0r9gdNoIs1DHOf8ESdcZ7KwxHkxToGmiJD-0/s1600/Screenshot+from+2013-04-10+23:15:53.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="250" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhInyiCqYO9bVpKXuAdxOxgozV0ijkbRzilgoC_9Nv9FIolkkRAxd6re__rLzwXVTN7WOL-XO2CSECRf0xeUPQokRPACYg0ti6_-lQ76Nk0r9gdNoIs1DHOf8ESdcZ7KwxHkxToGmiJD-0/s400/Screenshot+from+2013-04-10+23:15:53.png" width="400" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
External access from Internet using No-Ip, you'll need to configure your router to pass HTTP requests to the Raspberry Pi.</div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbatDU8zRc3aiCwGFc-asuCaUvCDUvbLXqhJqpBe9Yw7huOLtgyxC2nqhvFceVI5G9rcQtTWXRm6YUeUAlWwqdcnlA8BQJvFgnK32uto5AfOrlOTWPXjdcPdi9UWDCa9bEQ8SM48I9q-o/s1600/Screenshot+from+2013-04-10+23:14:33.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="200" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbatDU8zRc3aiCwGFc-asuCaUvCDUvbLXqhJqpBe9Yw7huOLtgyxC2nqhvFceVI5G9rcQtTWXRm6YUeUAlWwqdcnlA8BQJvFgnK32uto5AfOrlOTWPXjdcPdi9UWDCa9bEQ8SM48I9q-o/s320/Screenshot+from+2013-04-10+23:14:33.png" width="320" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
Local network access from Ubuntu desktop.</div>
<br />
<a href="http://meekgonkey.blogspot.com/">Doodle's Geek Monkey</a> by <a href="http://twitter.com/alastair_hm">Alastair Montgomery</a></div>
