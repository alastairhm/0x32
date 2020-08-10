---
title: "Automation"
tags: ['tech','Travis CI','CI/CD']
categories: ['Technical']
date: 2020-08-10T11:00:49+01:00
draft: false
---

## Automate publishing

To make the publishing of new content easily I am using Travis CI to publish changes.

I did try installing Hugo from source but this took longer and was producing errors so it was easier to download the binary.

Using this as the Travis CI pipline yaml.

### Travis CI Pipeline

```yaml
# Auto deploy repo from Github to Amazon S3 bucket via Travis CI
# * Set env vars for ACCESS_KEY_ID, BUCKET_NAME and SECRET_ACCESS_KEY on Travis
# * Update `bucket.name` in `sync` command
# * Assumes your `publishDir` is the default (`public`) - if not update `sync` command

language: go
before_install:
addons:
  apt:
    packages:
    - libcurl4-openssl-dev # required to avoid SSL errors
install:
  - curl -LO https://github.com/gohugoio/hugo/releases/download/v0.74.3/hugo_0.74.3_Linux-64bit.deb
  - sudo dpkg -i hugo_0.74.3_Linux-64bit.deb
before_script:
  - python --version
  - sudo pip install s3cmd
script:
  - hugo
after_success:
  - s3cmd sync -v --delete-removed --no-preserve --access_key=$ACCESS_KEY_ID --secret_key=$SECRET_ACCESS_KEY -r public/ s3://$BUCKET_NAME
notifications:
    email: true
```

