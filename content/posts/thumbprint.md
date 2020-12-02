---
title: "CA Thumbprint from Python"
date: 2020-12-02T13:29:00Z
draft: false
tags: ['tech','python','aws','oidc','eks']
categories: ['Technical']
featured_image: "python.png"
---

Recently had a need to get the CA Thumbprint from the Root certificate of a domain. This was for creating OIDC provider for an AWS EKS cluster.

This is the solution I came up with.

{{< gist alastairhm  a2b1b5e6adde9d9626d84e531adf39ed >}}

