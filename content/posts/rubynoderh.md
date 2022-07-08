---
title: "Quick Tip : Installing Ruby 2.7 and Node 12 on RH8"
date: 2022-07-07T13:54:22+01:00
draft: false
featured_image: "/devops.jpg"
tags: ['devops','redhat','linux','ruby', 'node','quick tip']
---
## Installing Ruby and Node on Redhat 8

Quick tip on how to install Ruby 2.7 and Nodejs 12 on Redhat 8, as it can default to older versions.


```bash
# Enable new versions
dnf -y module reset ruby nodejs
dnf -y module enable ruby:2.7 nodejs:12

# Install
dnf install nodejs ruby

# Check installed versions
ruby --version
node --version
npm --version
```

