---
title: "The Politics I Never Noticed Were There"
date: 2026-09-21T20:55:46+01:00
draft: false
tags: ['linux','foss','hyprland','reflection']
categories: ['Geek']
featured_image: "https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png"
---

This follows on from [my post about the Omarchy/DHH controversy]({{< ref "omarchy-linux-dhh-controversy.md" >}}) — I went down a much longer rabbit hole than I expected.

I went looking for a Linux distro. I came back with a headache and a much longer reading list.

It started simply enough. I'd been eyeing my old Lenovo laptop — an i5-4300M, 16GB RAM, nothing special — as a candidate for a proper Arch + Hyprland setup. Omarchy kept coming up: slick, popular, well-documented, built by David Heinemeier Hansson (DHH), the guy behind Ruby on Rails. Obvious choice, right?

Then people on Mastodon started pointing me toward something I hadn't clocked at all — mentions of DHH that weren't about Rails or Basecamp, but about him personally. Curious, I asked, almost as an afterthought: is the creator of this thing actually a bigot?

I did not expect that question to open the door it opened.

## The rabbit hole

What followed wasn't a single scandal — it was layers. DHH has published essays that read, depending who you ask, as either hard-edged immigration commentary or textbook white-nationalist rhetoric: praising a Tommy Robinson "remigration" march, comparing Romani people to wolves in a piece an AI model reportedly refused to translate because it was too dehumanizing. There's a 2022 incident where DHH banned political discussion at his own company and a third of the staff walked out. There's a Ruby community petition — small, maybe 140 people — trying to "hard fork" Rails away from him entirely. There's a RubyGems governance fight that spun out of the same tension. There's Omarchy itself: an Arch Linux spin that's pulled in something like $18 million from a roster of tech executives — Shopify, Stripe, Dell, Cloudflare, 1Password — funding that no other FOSS project gets anywhere close to.

And then there's the other side, because there always is one: DHH calling the backlash a cancellation attempt, framing himself as a casualty of ideological capture in tech, backed by a real contingent of developers who think the criticism is overblown or beside the point — "the focus is software excellence," as one defender put it. A protest site (stopomarchy.org) makes the maximalist case that this is organized fascism dressed up as a Linux distro; DHH's defenders call that same site hysterical. Somewhere in the middle is the actual, unglamorous truth: most people using Omarchy have absolutely no idea any of this is happening. They just wanted a nice-looking desktop.

I ended up settling on a plan that sidesteps the whole thing rather than making a statement out of it: a plain Arch install from scratch, with a separate set of dotfiles — JaKooLit's Hyprland-Dots, now maintained by a community successor called LinuxBeginnings — layered on top, rather than reaching for Omarchy's all-in-one install. Not really a boycott, more that going bare-Arch-plus-dotfiles turned out to be the right technical call anyway, once I looked past the marketing: full control, no vendor lock-in, and none of the baggage riding along with it. But the choosing wasn't really the interesting part anymore. The interesting part was realizing how much I'd been treating "which Linux distro" as a purely technical decision, when for a lot of people — maintainers, contributors, whole communities — it plainly isn't.

## It's bigger than one guy

Once I started pulling that thread, I found out this isn't an isolated flare-up. 2026 has apparently been a genuinely rough year for open source, on multiple fronts I'd never paid attention to:

**The fork wars.** Forks used to be open source's escape valve — don't like where a project's going, take the code and go build your own. Now, apparently, they're the opening move in drawn-out legal fights where whoever has the bigger litigation budget wins, not whoever's technically right. OnlyOffice is reportedly leaning on an AGPL clause against Nextcloud. IBM's HashiCorp has been grinding down OpenTofu — the community fork that sprang up after HashiCorp yanked Terraform out of open source in the first place. There's even a report of someone allegedly using an AI model to launder an LGPL-licensed library into a permissive MIT license. That last one stopped me — I hadn't considered that AI tooling could be used to quietly erase a license's obligations.

**AI is making some projects go closed.** Cal.com — a genuinely big open-source project — closed its source entirely this year. Their reasoning: publishing your code now is like handing out the blueprint to a bank vault to a hundred times more attackers, because AI models can now find exploitable bugs at real scale. Apparently one model found a 27-year-old bug in OpenBSD and a 17-year-old flaw in FreeBSD. That's a genuinely new kind of pressure on the whole "open by default" assumption I'd never really questioned.

The counterargument is decent too — that open source might actually be *more* defensible in this era, because a whole community can spend effort auditing code together, which a closed-source vendor has to pay for alone. And the doom narrative doesn't hold up in the data either: 98% of organizations kept or grew their open-source use this year. So it's not death, exactly. It's more like... open source figuring out what it's for, again, under new pressure.

## What actually changed for me

None of this makes me an expert, and I'm wary of pretending I've "solved" any of it — the DHH situation especially is genuinely contested, and I don't think picking a side from the outside, based on a few evenings of reading, is something I'm owed the confidence to do.

But the blinkers are off in a specific, useful way: I used to think of "which tool do I use" as a purely engineering question — performance, compatibility, community size, documentation quality. I still think those matter most of the time. What I hadn't clocked is how often the *people* question — who's funding this, who's leading it, what's the culture around it — sits quietly underneath the technical one, waiting to matter the moment you actually look.

I don't think that means auditing every dependency's maintainer before I `pip install` anything. That way lies paralysis. But it does mean I'll probably ask the question a bit more often than "does it work" from here on — even if, most of the time, the honest answer turns out to be that it's just a config file, and none of this touches it at all.
