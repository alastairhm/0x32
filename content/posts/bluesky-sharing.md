---
title: "New Posts Now Announce Themselves on Bluesky"
date: 2026-10-17T13:00:00+01:00
draft: false
tags: ['tech','hugo','blog','bluesky','automation','workflow','githubactions']
categories: ['Technical']
featured_image: "hugo-logo.png"
---

New posts on this blog now get announced on [Bluesky](https://bsky.app/profile/alastair-hm.bsky.social) automatically, alongside the Mastodon toots that were already going out. If you're reading this via a Bluesky link card, that's the thing working.

It went live on 16 October, with the Inktober "Gangly" post being the first one through, and it's been quietly doing its job since.

## How it works

The whole thing is a GitHub Actions workflow plus a small Python script, with no third-party service in the middle.

**1. Wait for the site to actually be live.** The workflow doesn't run on a push. It runs when the *Hugo Build and Deploy to S3* workflow finishes, and only if that deploy succeeded on `master`. That way the announcement never points at a page that isn't there yet. Pull-request build checks don't trigger it.

**2. Work out what's new.** It diffs the commits that were just deployed and looks for *newly added* files under `content/posts/`. Edits to existing posts, theme tweaks and workflow changes find nothing and exit quietly. Drafts are skipped, and if one merge somehow adds several posts, only the latest by front-matter date gets announced, so nobody gets a burst of posts at once.

**3. Build the post.** The script reads the post's front matter and pulls out:

- the **title**
- a short **description**: the first plain line of the body, with markdown links and emphasis stripped
- **hashtags** from the post's `tags` (falling back to `categories`)
- the **featured image**

These are squeezed into Bluesky's 300-character limit, trimming the description if needed. The hashtags are added as proper rich-text "facets", so they're real clickable tags on Bluesky rather than just text with a `#` in front.

**4. Attach a link card.** The post gets an external embed: the URL, title, description and a thumbnail. The featured image is fetched (from Flickr for the Inktober drawings, or from `static/` for local images), resized with Pillow and re-compressed until it fits under Bluesky's 1MB blob limit, then uploaded. If the image can't be loaded, the post still goes out, just without a thumbnail.

**5. Post it.** It logs in using an app password stored as a GitHub secret (never the main account password), uploads the thumbnail, and creates the post through the AT Protocol API. The run log prints the new post's `at://` URI, which makes it easy to check it worked.

There's also a manual trigger that takes a specific post file, for re-announcing something or recovering from a failed run, and it refuses to post drafts.

## Why bother

Mostly because publishing here has got so low-friction that the sharing step was the last bit still done by hand, and it was the bit most likely to get forgotten. Now merging a post is the whole job: deploy, toot, post to Bluesky, done.
