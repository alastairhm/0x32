---
title: "10 PRINT"
date: 2020-09-04T16:08:20+01:00
draft: false
tags: ['tech','retro','basic','8bit','video','lbry']
categories: ['Retro']
featured_image: "/invader.jpg"
---

BBC Micro take on [C64 10 Print](https://10print.org/) one line random pattern generator.

```text
10 MODE 0
20 N=RND(1):IF N > 0.5 THEN PRINT "/"; ELSE PRINT "\";
30 GOTO 20
RUN
```

{{< tweet 1301899318203383811 >}}