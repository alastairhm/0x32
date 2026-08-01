# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the Hugo source for Alastair Montgomery's personal blog, published at https://blog.0x32.co.uk/ (baseURL in `config.toml`) and mirrored at http://0x32.uk/. There is no application code — this repo is Hugo content, a vendored theme, and deployment config.

## Setup

The theme is a git submodule and must be initialized before building:

```bash
git submodule update --init themes/ananke
```

## Commands

```bash
hugo                 # build static site into public/
hugo server -D       # local dev server with drafts, live reload
make build-blog       # hugo (build)
make deploy-blog       # hugo deploy (pushes to S3 target defined in config.toml)
make build-docker      # build blog, then docker build -t 0x32 .
make run-docker        # build-docker, then run it on localhost:8000
```

There is no test suite, linter, or package manager in this repo — it's static content, so validate changes by building with `hugo` and checking `hugo server` output.

## Architecture

- `content/posts/*.md` — blog posts. Front matter uses `title`, `date`, `draft`, `tags`, `categories`, `featured_image`.
- `content/links/` and `content/_index.md` — the links page and homepage content.
- `archetypes/default.md` — template used by `hugo new` for new posts (draft: true by default).
- `themes/ananke` — vendored theme (git submodule, do not edit in place; submodule points at `theNewDynamic/gohugo-theme-ananke`).
- `layouts/` — site-specific overrides layered on top of the theme:
  - `layouts/shortcodes/` — custom shortcodes (`flickr`, `flickralbum`, `lbry`) used inline in post markdown for embedding Flickr photos/albums and LBRY videos.
  - `layouts/taxonomy/tag.html` — override for the tag taxonomy listing page.
- `static/` — images and static assets referenced directly by posts (e.g. `![alt](/logo.png)`).
- `config.toml` — Hugo site config: theme selection, social network params under `[params.ananke.social.*]`, taxonomies (`categories`, `tags`), and the `[deployment]` block (S3 target `s3://blog.0x32.co.uk`, cache-control/gzip matchers per file type). `markup.goldmark.renderer.unsafe = true` allows raw HTML in markdown content.
- `Dockerfile` — multi-stage build: builds the site with `ghcr.io/alastairhm/docker-hugo:main`, then serves `public/` via `ghcr.io/alastairhm/alpine-lighttpd:latest`.

## Deployment

Two independent, parallel deploy paths triggered on push to `master`:

- `.github/workflows/main.yml` — builds with `reuixiy/hugo-deploy` and pushes the built site to the `build` branch of the separate `alastairhm/alastairhm.github.io` repo (GitHub Pages mirror).
- `.github/workflows/s3.yaml` — builds with `alastairhm/deploy-hugo-to-s3-action` (pinned Hugo `0.139.0`) and deploys directly to S3 (`blog.0x32.co.uk`), which serves the primary site via CloudFront.

`hugo deploy` (via `make deploy-blog`) performs the same S3 deploy locally using the `[deployment]` config in `config.toml`, and requires AWS credentials in the environment.

## Writing posts

New posts go in `content/posts/`. Use `hugo new posts/my-post.md` to scaffold from the archetype, then set `draft: false` when ready to publish. Existing posts show recurring tag/category conventions (e.g. `inktober*` posts for the annual drawing challenge series) — check a similar existing post for front matter conventions before adding a new one.
