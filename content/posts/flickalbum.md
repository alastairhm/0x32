---
title: "Flickr album Short Code"
date: 2020-10-13T09:28:23+01:00
draft: false
tags: ['photo','art','blog','hugo']
categories: ['Creative']
featured_image: "https://live.staticflickr.com/65535/50403951781_ba272345ab_z.jpg"
---

Short code for embedding Flickr albums easily.
Here demonstrated with my Inkotober 2020 album.

{{< flickralbum "Inktober 2020"
           "https://www.flickr.com/photos/doodle_m/albums/72157716205953681"
           "https://live.staticflickr.com/65535/50403951781_ba272345ab_z.jpg" >}}

Short code defined like this

```html
<a data-flickr-embed="true" data-header="true" data-footer="true"
href="{{ index .Params 1 }}"
title="{{ index .Params 0 }}">
<img src="{{ index .Params 2 }}"
width="800" height="600"
alt="{{ index .Params 0 }}">
</a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
```

First parameter is the album title.
Second parameter is the album URL.
Third parameter is a URL to an image to use for the album.
