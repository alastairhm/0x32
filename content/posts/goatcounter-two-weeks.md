---
title: "Two Weeks of GoatCounter Data"
date: 2026-08-15T18:00:00+01:00
draft: false
tags: ['tech','blog','goatcounter','analytics']
categories: ['Technical']
---

Back when I [wired GoatCounter into this blog]({{< ref "claude-code-blog-cleanup.md" >}}), the honest answer to "does any of this actually get read" was a shrug — no analytics meant no way to know. It's been running for a couple of weeks now, so pulled the first export and had a proper look.

Rather than paste a wall of numbers, here's the breakdown as an actual chart — daily pageviews, top pages, referrers, and where the hits are coming from:

<iframe id="traffic-report-frame" src="/charts/0x32-traffic-report.html" style="width:100%;border:0;display:block;border-radius:8px;" title="0x32 blog traffic report, 2 to 15 August 2026" loading="lazy"></iframe>
<script>
(function () {
  var f = document.getElementById('traffic-report-frame');
  function resize() {
    try { f.style.height = f.contentWindow.document.documentElement.scrollHeight + 'px'; } catch (e) {}
  }
  f.addEventListener('load', function () {
    resize();
    setTimeout(resize, 300);
  });
  window.addEventListener('resize', resize);
})();
</script>

The headline: 36 pageviews over 14 days, and the split is a good reminder to sanity-check your own analytics before getting excited — 27 of those hits are Great Britain on Firefox, which is almost certainly just me checking the site loaded properly after a deploy. Strip that out and it's closer to 8-10 genuine visitors, mostly arriving direct or via the GitHub link on the [ST7735 MicroPython post]({{< ref "pico8.md" >}}), plus one organic Google hit.

Not exactly viral, but it's real signal rather than none, and it's the first time this blog has ever had any idea who's reading it. Planning to pull another export in a few weeks once there's enough data to actually trend against.
