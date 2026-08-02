---
title: "Blowing the Cobwebs Off This Blog with Claude Code"
date: 2026-08-02T17:10:00+01:00
draft: false
tags: ['tech','hugo','blog','claude','ai','vibe-coding','code']
categories: ['Technical']
featured_image: "hugo-logo.png"

---

# A Hugo repo hadn't been looked at properly in a while

This blog is just Hugo content and a vendored theme — no app code, nothing exciting — which is exactly the kind of repo that quietly accumulates small rot nobody notices because nothing ever actually breaks the build. Spent a session pointing Claude Code at it to find and fix that rot.

Started with a straight status check: a couple of generated CSS cache files showing as deleted (build artifacts that shouldn't have been tracked in the first place) and a stray uncommitted edit sitting inside the `ananke` theme submodule from as far back as November 2024. Both restored/reverted to get back to a clean tree before touching anything else.

From there it turned into a small punch list, each one its own branch and PR:

- **A broken RSS follow-icon link** — the theme's default `rss` social network entry has an empty `profile` template and expects a username that was never configured, so Hugo's `printf` was emitting Go's literal `%!(EXTRA <nil>)` error text straight into the link. Fixed by setting `profilelink` explicitly, the same pattern already used for the Mastodon entry.
- **A dead ko-fi button image** — `www.ko-fi.com/img/...` 404s; the same asset is served fine without the `www.`.
- **A dead outbound link** — an old Commodore Plus/4 archive site in a 2020 post had gone unreachable (timed out over both HTTP and HTTPS). Pointed the links at Wayback Machine snapshots instead of just deleting them.
- **No favicon or site logo** — both params existed in the theme but were empty, and there was no square branding asset anywhere in `static/`. Generated a simple "0x32" mark and wordmark with Pillow rather than invent something by hand.
- **No analytics at all** — despite the theme having a Google Analytics hook, nothing was wired up, so there was no way to actually know if any of this mattered. Wired in [GoatCounter](https://www.goatcounter.com/) instead — no cookies, no tracking baggage — through the theme's own empty `head-additions.html` override point, gated to production builds so local dev traffic doesn't get counted.
- **Hugo version drift** — the local `asdf` install was on 0.136.2 while the S3 deploy workflow pins 0.139.0. Pinned the repo to 0.139.0 via `.tool-versions` so local builds match what actually ships.

None of this was individually hard, which is sort of the point — it's the kind of maintenance that's easy to keep deferring on a low-traffic personal blog because nothing forces your hand. Having something else drive the "notice, branch, fix, PR, merge" loop end-to-end made it cheap enough to just do.

Still on the list: the `ananke` theme submodule itself is pinned to a commit from late 2024, about a year and a half behind upstream. That one's a bigger, riskier chunk of work — happy to leave the cobwebs there a little longer.
