# 0x32

Hugo source for my personal blog, published at [blog.0x32.co.uk](https://blog.0x32.co.uk/) (served from S3 via CloudFront) and mirrored at [0x32.uk](http://0x32.uk/) via [GitHub Pages](https://github.com/alastairhm/alastairhm.github.io).

## Layout

- `content/posts/` — blog posts.
- `content/links/` and `content/_index.md` — the links page and homepage content.
- `archetypes/default.md` — template used by `hugo new` for new posts.
- `themes/ananke` — vendored theme (git submodule), with site-specific overrides in `layouts/`.
- `static/` — images and other static assets referenced directly by posts.
- `config.toml` — Hugo site config, including the `[deployment]` block used by `hugo deploy`.

## Requirements

- [Hugo](https://gohugo.io/) (extended, with `withdeploy` support for `hugo deploy`)
- The theme is a git submodule and must be initialized before building:

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

There's no test suite or linter — it's static content, so changes are validated by building with `hugo` and checking `hugo server` output.

## Writing a post

```bash
hugo new posts/my-post.md
```

This scaffolds a draft from `archetypes/default.md`; set `draft: false` in the front matter when it's ready to publish.

## Deployment

Two independent workflows run on every push to `master`:

- `.github/workflows/main.yml` — builds the site and pushes it to the `build` branch of [`alastairhm/alastairhm.github.io`](https://github.com/alastairhm/alastairhm.github.io) (GitHub Pages mirror).
- `.github/workflows/s3.yaml` — builds the site and deploys it directly to the `blog.0x32.co.uk` S3 bucket, served via CloudFront (the primary site).

`make deploy-blog` performs the same S3 deploy locally, and requires AWS credentials in the environment.

## License

[MIT](LICENSE)
