---
title: "Hugo Lbry Shortcode"
date: 2020-08-13T13:50:32+01:00
draft: false
categories: ['Technical']
tags: ['tech','Hugo','blog','dev','lbry']
featured_image: "/hugo-logo.png"
---

One thing I like about Hugo is how easy it is to expand its functionality with your own code.

For example was able to create a [shortcode](https://gohugo.io/content-management/shortcodes/) to embed [Lbry.tv](https://lbry.tv/) videos into a post in around five minutes.

First I created an empty file `layouts/shortcodes/lbry.html` which I pasted the basic embed code take from the share button on one of their videos.

![Share button](/lbry_embed.jpg)

```html
<iframe id="lbry-iframe" width="560" height="315" src="https://lbry.tv/$/embed/this-new-fedora-powered-thinkpad-p53-is/097106eb68aebc90b33d83bb053467af942a8e20" allowfullscreen></iframe>
```

Then parameterized this so that the src url can be changed.

```html
<iframe id="lbry-iframe" width="560" height="315" src="{{.Get 0 }}" allowfullscreen></iframe>
```

You can then call this with a shortcode like the following to embed the video.

![Shortcode example](/short_example.jpg)

Which will appear like this

{{< lbry "https://lbry.tv/$/embed/this-new-fedora-powered-thinkpad-p53-is/097106eb68aebc90b33d83bb053467af942a8e20" >}}

The possibilities are endless creating shortcodes to do custom HTML in posts.