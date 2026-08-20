---
title: "Ubuntu 10.10 RC"
date: 2010-10-05T11:22:00+01:00
draft: false
tags: ["blog-import", "geek", "linux", "ubuntu", "virtual-machine"]
categories: ['Geek']
---

<div style="float: right; margin-left: 10px; margin-bottom: 10px;"><a href="http://www.flickr.com/photos/doodle_m/5054061920/" title="photo sharing"><img src="http://farm5.static.flickr.com/4112/5054061920_0db0c419e1_m.jpg" alt="" style="border: 2px solid rgb(0, 0, 0);" /></a><br /><span style="margin-top: 0px;font-size:0.9em;" ><a href="http://www.flickr.com/photos/doodle_m/5054061920/">Ubuntu 10.10 RC</a><br />Originally uploaded by <a href="http://www.flickr.com/people/doodle_m/">Alastair Montgomery</a></span></div>The Ubuntu 10.10 release candidate running on VirtualBox.<br /><br />Need to work out how to install the guest additions so I can get a proper screen resolution.<br /><br />Found a solution,<br /><br />Solution to VirtualBox guest problem<br />1. Open terminal and enter the following command:<br /><span style="font-family:courier new;">    sudo apt-get update</span><br /><span style="font-family:courier new;">    sudo apt-get install build-essential linux-headers-$(uname -r)</span><br /><span style="font-family:courier new;">    sudo apt-get install virtualbox-ose-guest-x11</span><br />2. Once installation is finished, restart your virtualBox machine.<br />3. Go to System -->Preferences -->Monitors and change the resolution of your screen.<br /><br /><a href="http://www.flickr.com/photos/doodle_m/5054098502/" title="Ubuntu 10.10 Release Candidate by Alastair Montgomery, on Flickr"><img src="http://farm5.static.flickr.com/4150/5054098502_658ed58331.jpg" width="500" height="311" alt="Ubuntu 10.10 Release Candidate" /></a>
