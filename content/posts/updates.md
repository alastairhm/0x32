---
title: "Cascading Updates"
date: 2024-11-19T09:36:00Z
draft: false
categories: ['Technical']
tags: ['tech','Hugo','blog','dev','lbry']
featured_image: "/hugo-logo.png"
---

Having been a bit lazy in not updating my Hugo version since I started which was recently breaking one of my Github actions, I decided do do that.

This lead to an cascading update cycle.

* Updating Hugo version broke the theme I was using.
* Updating the theme broke the Tweet shortcode, no longer on Twitter so edited those post which referenced my old Twitter account.
* Updating the Hugo version, broke the Github Action which was building and uploaded to S3. This was due to newer versions of Hugo now having an "extended" and "with_deploy" versions.
* Raised a PR against the Github action to update to use the "with_deploy" version.

Still a couple of deprecated warning and fixing background and social icon links to sort out but at least now running against the latest version of Hugo.

Lesson to keep up to date more often.
