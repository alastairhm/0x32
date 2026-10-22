---
title: "Patching php2shell in My Alpine Lighttpd PHP Docker Image"
date: 2026-10-22T10:00:00+01:00
draft: false
tags: ['tech','docker','php','alpine','lighttpd','security','githubactions']
categories: ['Technical']
---

If you use my [alpine-lighttpd-php](https://github.com/alastairhm/alpine-lighttpd-php) Docker image, please pull `:latest` again and recreate your container. The image now runs **PHP 8.4.27**, which fixes the php2shell vulnerabilities.

```bash
docker pull alastairhm/alpine-lighttpd-php:latest
# or
docker pull ghcr.io/alastairhm/alpine-lighttpd-php:latest
```

## What is php2shell?

php2shell is the name for two PHP vulnerabilities, **CVE-2026-109618** and **CVE-2026-109619**. Both are critical, and both allow remote code execution with no authentication. Anyone who can send a request to a PHP page could run their own code on the server. The fixes are in the latest PHP point releases, which for the 8.4 branch is 8.4.27.

You can reduce the risk by setting `session.upload_progress.enabled = 0`, but the PHP team says no setting fully closes the hole. The real fix is to upgrade.

## How I found out

A user of the image, [@gmanic](https://github.com/gmanic), opened [issue #5](https://github.com/alastairhm/alpine-lighttpd-php/issues/5) asking whether I'd rebuild the image. I'm glad they did. The `:latest` image was shipping PHP 8.4.16, so it was vulnerable.

## Why a rebuild wasn't enough

Normally this image just installs PHP from Alpine's package repositories, so a security fix means a rebuild once Alpine publishes new packages. This time the Alpine 3.23 mirrors were still serving `php84` 8.4.21, and I didn't want to leave a publicly downloadable image exposed to an unauthenticated RCE until they caught up.

## The fix: build PHP from Alpine's own recipe

Rather than compile PHP from scratch, I added a temporary build stage to the `Dockerfile`. It builds `php84` with Alpine's own 3.23 APKBUILD, with only the version number changed. That way the packages match what Alpine will eventually ship, with the same configure flags, file layout and package split.

The `php-build` stage:

1. Starts from `alpine:3.23` with `alpine-sdk`, and creates a `builder` user and a signing key for `abuild`.
2. Does a shallow, sparse clone of [aports](https://github.com/alpinelinux/aports) on the `3.23-stable` branch, fetching only `community/php84`.
3. Changes `pkgver` in the APKBUILD to 8.4.27 and resets `pkgrel`.
4. Downloads the source tarball and checks it against the **SHA-256 published on php.net** before building. If the checksum doesn't match, the build fails.
5. Runs `abuild -r` to produce the `.apk` packages.

```dockerfile
RUN sed -i \
        -e "s/^pkgver=.*/pkgver=$PHP_VERSION/" \
        -e "s/^pkgrel=.*/pkgrel=0\noptions=\"!check\"/" \
        APKBUILD && \
    abuild checksum && \
    echo "$PHP_SHA256  /var/cache/distfiles/php-$PHP_VERSION.tar.xz" | sha256sum -c - && \
    abuild -r
```

The final stage, still on top of my [alpine-lighttpd](https://github.com/alastairhm/alpine-lighttpd) base image, copies those packages and the signing key in and installs from a local repository. The build then checks that it got what it expected:

```dockerfile
php-cgi84 -v | grep -q "^PHP $PHP_VERSION " && \
! apk info -v | grep '^php84-' | grep -v -- "-$PHP_VERSION-" && \
```

If `php-cgi84` isn't 8.4.27, or any installed `php84-*` package came from somewhere else, the image doesn't build. I'd rather have a failed build than one that quietly falls back to the vulnerable version.

The downside is build time. Alpine's APKBUILD compiles PHP twice, once for the Apache module and once for the other SAPIs, so a full build now takes about 20 minutes instead of seconds. That's fine for a stopgap. Once Alpine 3.23 ships `php84` 8.4.27 or later, I'll remove the stage and go back to a plain `apk add`.

## Things I found along the way

Looking closely at the package list turned up a couple of other problems:

- **`php-imap` never worked.** The unversioned `php-imap` package installed the PHP 8.3 extension, which the PHP 8.4 runtime never loaded. Alpine has no `php84-imap`, so I removed it.
- **`php-json` was redundant.** JSON is built into PHP 8.4.
- **A suggested quick fix wouldn't have worked here.** Another commenter on the issue posted a one-line `docker exec` that finds a PHP `conf.d` directory and writes the mitigation setting into it. On this image it could pick `/etc/php83/conf.d/`, which PHP 8.4 doesn't read, so it would look like it worked without protecting anything. If you apply the mitigation by hand, use `/etc/php84/conf.d/`.

This release also includes some earlier fixes from [PR #4](https://github.com/alastairhm/alpine-lighttpd-php/pull/4). lighttpd and the `php-cgi` workers now run as the base image's `lighttpd` user. Dotfiles like `.git` and `.env` are blocked again. The examples now mount a dedicated `html/` directory instead of the current directory.

## A CI slip

The GitHub Actions workflow ran with `push: true` on pull requests as well as on `master`. That meant the unmerged PR build for the fix was pushed straight to `ghcr.io/alastairhm/alpine-lighttpd-php:latest` before I'd merged it. This time it was the fixed image, so no harm done, but it shouldn't happen. [PR #7](https://github.com/alastairhm/alpine-lighttpd-php/pull/7) changed it so pull requests only build, tagged `pr-<number>`, without logging in or pushing. Only pushes to `master` publish `:latest`.

## Testing

Before merging I built the image locally and checked that:

- `php-cgi84 -v` reports 8.4.27, and every `php84-*` package is `8.4.27-r0`
- all the extensions the image provided before still load (iconv, gd, curl, xml, SimpleXML, pgsql, pdo_pgsql, soap, ldap, dom and so on)
- the container stays up, `index.php` renders `phpinfo()`, and raw `.php` source is never served
- static files return 200 and `/.git/config` returns 403

The patched image went out on Docker Hub first, then ghcr.io, and it's tagged as release [3.23.5](https://github.com/alastairhm/alpine-lighttpd-php/releases/tag/3.23.5). gmanic confirmed their pod updated without problems.

Thanks again to gmanic for raising it. If you run anything PHP-based in containers, it's worth checking which PHP version your images ship, because a rebuild only helps once the distro has the fix.
