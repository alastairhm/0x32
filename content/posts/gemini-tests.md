---
title: "Gemini Tests"
date: 2026-08-04T18:00:00+01:00
draft: false
tags: ['tech','ai','claude','gemini','antigravity','cli','vibe-coding']
categories: ['Technical']
featured_image: "/antigravity-logo.png"

---

# Taking Antigravity for a spin

Been using Claude Code as my daily driver for a few days now, so when Google's Antigravity CLI showed up I figured it was worth a proper look rather than just reading the launch blog post. Ran it side by side with Claude Code on the same kind of day-to-day work — repo exploration, small fixes, the usual — to see how the two actually compare in practice rather than on paper.

First impression: the feature set overlaps a lot more than I expected. Tool use, file editing, running shell commands, planning steps before touching code — it's clearly playing in the same space as Claude Code, and for the most part it gets the job done.

A few things stood out:

- **Verbosity.** Out of the box, Antigravity is a lot chattier than Claude Code's default setup. More narration, more restating what it's about to do before doing it. Not wrong, just noisier — I ended up wanting to dial it back, which I haven't needed to do with Claude Code.
- **Rule-following.** A couple of times it just didn't stick to instructions I'd given it earlier in the session — not catastrophically, but enough that I noticed and had to correct it. Claude Code hasn't been perfect on this either, but it's been more consistent about it in my experience so far.
- **Everything else** — the core loop of "understand the task, make a plan, execute it, check the result" — felt broadly comparable between the two.

None of this is a final verdict, more a snapshot from a few days of poking at it. Still very much a work in progress trying to find my happy place in all these AI coding tools — there's enough overlap between them now that the differences are mostly in the edges: how much they talk, how well they hold onto context and rules, and how much friction there is in actually getting work done. More to follow as I keep testing.
