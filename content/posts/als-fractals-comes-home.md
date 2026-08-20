---
title: "The Old Blogs Come Home"
date: 2026-08-20T20:00:00+01:00
draft: false
tags: ['blog','meta','blogger-import','archive']
categories: ['General']
featured_image: "/contextfree-fractal-tree.png"
---

Something I've been meaning to do for years, finally done: my old Blogger blogs are moving in here, one by one.

Before this blog, and running alongside it for years without me really thinking of them as related, I kept separate Blogger sites for whatever I was into at the time — fractal art, tech links, photography. They mostly went dormant, but they never got deleted, and every so often I'd think "I should really pull that lot into 0x32 someday." Google Takeout finally made "someday" easy: it exports a Blogger blog as an Atom feed with every post's original title, HTML body, labels, and publish timestamp intact, so nothing needs backdating by hand. A [Claude Code](https://claude.com/claude-code) session parsed each export, converted the posts into Hugo front matter with their real dates, and mapped Blogger's labels onto tags — three separate imports, one per blog.

## Al's Fractals

[Al's Fractals](https://alsfractals.blogspot.com/) started in March 2008 as a dumping ground for whatever I'd rendered that week — [gnofract4d](https://fract4d.github.io/gnofract4d/) parameter files, [Ultra Fractal](https://www.ultrafractal.com/) exports, [Context Free](https://www.contextfreeart.org/) grammars, the occasional [XaoS](https://xaos-project.github.io/) zoom. It ran on and off for about a decade, drifting later into IFTTT reposts of fractal art I'd found on Pinterest, before going dormant.

148 posts came out of the export. 31 embedded images hosted on Photobucket, which killed free hotlinking [years ago](https://en.wikipedia.org/wiki/Photobucket#2017_hotlinking_controversy) — those got dropped rather than published broken. The remaining **117 are live now**, spanning 2008 to 2017, tagged `blogger-import` and `fractal`.

## Geek Monkey

[Geek Monkey](https://meekgonkey.blogspot.com/) was more of a linkblog — Linux distros, Raspberry Pi and Arduino projects, browser oddities, a lot of "10 free things you should bookmark" roundups, much of it reposted via feed aggregators from sites that don't exist anymore.

218 posts came out of the export. This time I ran a full link-rot check across all 2,205 outbound links first: 54% were dead, almost all of it dead 2008–2013 feed-syndication infrastructure (FeedBurner, Gawker, AOL's old blog network, a defunct ad service called Pheedo, Yahoo Pipes). Three posts had no surviving links at all and got dropped; the other 101 kept their content with a note added up top flagging what's broken and why. **215 posts are queued** — tagged `blogger-import` and `geek` — pending merge.

## Alastair's Doodles

[Alastair's Doodles](https://doodlem.blogspot.com/) is the big one: mostly single-photo posts, a lot of them auto-reposted from Instagram and Flickr via IFTTT with nothing but a hashtag caption, spanning 2006 to 2020 — overlapping this blog's entire existence.

2,383 posts came out of the export, roughly ten times either of the other two. **They're imported and staged**, tagged `blogger-import` and `photography`, but still sitting as drafts pending the same link-rot treatment Geek Monkey got — a lot of the images point at old `farmN.static.flickr.com` URLs that Flickr deprecated years ago, so I'd expect a similar hit rate before any of it goes live.

## So far

Two blogs' worth of history folded in, a third queued up. It's a fun read back if you're into that sort of nostalgia — software I'd completely forgotten existed, a lot of enthusiasm for the maths of pretty pictures, and a reminder that this is at least the fourth blog I've run over the years. [0x32](/) is just the one that stuck, and now it gets to be all of them.
