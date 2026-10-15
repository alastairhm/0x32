#!/usr/bin/env python3
"""Announce a blog post on Bluesky as a link card with the featured image.

Usage: bluesky_post.py content/posts/foo.md

Env: BLUESKY_HANDLE, BLUESKY_APP_PASSWORD, BASE_URL, optional DRY_RUN=1.
"""
import io
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

PDS = "https://bsky.social/xrpc"
MAX_GRAPHEMES = 300
MAX_BLOB_BYTES = 1_000_000
THUMB_SIZE = (800, 600)


def xrpc(method, body=None, token=None, content_type="application/json"):
    data = body
    if content_type == "application/json" and body is not None:
        data = json.dumps(body).encode()
    req = urllib.request.Request(f"{PDS}/{method}", data=data, method="POST")
    req.add_header("Content-Type", content_type)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} failed: {e.code} {e.read().decode(errors='replace')}")


def parse_post(path):
    text = Path(path).read_text(encoding="utf-8")
    parts = text.split("\n---", 2)
    front, body = parts[0], parts[1] if len(parts) > 1 else ""

    def field(name):
        m = re.search(rf"^{name}:\s*(.*)$", front, re.M)
        return m.group(1).strip().strip("\"'") if m else ""

    def list_field(name):
        m = re.search(rf"^{name}:\s*\[(.*)\]\s*$", front, re.M)
        if not m:
            return []
        items = [re.sub(r"[^\w]", "", t.strip().strip("\"'")) for t in m.group(1).split(",")]
        return [t for t in items if t]

    # Same description rule as the Mastodon workflow: first non-blank body
    # line without a shortcode, with markdown links/emphasis/code stripped.
    desc = ""
    for line in body.split("\n")[1:]:
        if line.strip() and "{{<" not in line:
            desc = line.strip()
            break
    desc = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", desc)
    desc = re.sub(r"\*\*([^*]+)\*\*", r"\1", desc)
    desc = re.sub(r"\*([^*]+)\*", r"\1", desc)
    desc = re.sub(r"`([^`]+)`", r"\1", desc)

    return {
        "title": field("title"),
        "image": field("featured_image"),
        "tags": list_field("tags") or list_field("categories"),
        "desc": desc,
    }


def load_image(ref, post_path):
    if not ref:
        return None
    try:
        if re.match(r"https?://", ref):
            req = urllib.request.Request(ref, headers={"User-Agent": "blog.0x32.co.uk bluesky poster"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        # Site-relative images live in static/; also allow page-bundle siblings.
        for candidate in (Path("static") / ref.lstrip("/"), Path(post_path).parent / ref):
            if candidate.is_file():
                return candidate.read_bytes()
    except Exception as e:  # a missing image shouldn't block the announcement
        print(f"Could not load featured image {ref}: {e}", file=sys.stderr)
        return None
    print(f"Featured image not found: {ref}", file=sys.stderr)
    return None


def shrink(raw):
    img = Image.open(io.BytesIO(raw))
    img.thumbnail(THUMB_SIZE)
    if img.mode != "RGB":
        bg = Image.new("RGB", img.size, "white")
        img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1])
        img = bg
    for quality in (85, 75, 65, 50):
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=quality, optimize=True)
        if buf.tell() <= MAX_BLOB_BYTES:
            return buf.getvalue()
    return None


def build_text(title, desc, tags):
    """Title, description and hashtags, with tag facets (byte offsets)."""
    hashtags = " ".join(f"#{t}" for t in tags)
    budget = MAX_GRAPHEMES - len(title) - len(hashtags) - 4  # 2x "\n\n"
    if len(desc) > budget:
        desc = desc[: max(budget - 1, 0)].rstrip() + "…" if budget > 1 else ""
    head = f"{title}\n\n{desc}\n\n" if desc else f"{title}\n\n"
    text = head + hashtags

    facets = []
    pos = len(head.encode())
    for t in tags:
        tag = f"#{t}"
        end = pos + len(tag.encode())
        facets.append({
            "index": {"byteStart": pos, "byteEnd": end},
            "features": [{"$type": "app.bsky.richtext.facet#tag", "tag": t}],
        })
        pos = end + 1
    return text, facets


def main():
    post_path = sys.argv[1]
    post = parse_post(post_path)
    if not post["tags"]:
        sys.exit(f"No tags or categories found on {post_path}; refusing to post without a hashtag.")

    url = f"{os.environ['BASE_URL']}/posts/{Path(post_path).stem}/"
    text, facets = build_text(post["title"], post["desc"], post["tags"])

    thumb_bytes = None
    raw = load_image(post["image"], post_path)
    if raw:
        thumb_bytes = shrink(raw)

    if os.environ.get("DRY_RUN"):
        print(text)
        print(json.dumps(facets, indent=2))
        print(f"link: {url}, thumb: {len(thumb_bytes) if thumb_bytes else 'none'} bytes")
        return

    session = xrpc("com.atproto.server.createSession", {
        "identifier": os.environ["BLUESKY_HANDLE"],
        "password": os.environ["BLUESKY_APP_PASSWORD"],
    })
    token = session["accessJwt"]

    external = {"uri": url, "title": post["title"], "description": post["desc"]}
    if thumb_bytes:
        blob = xrpc("com.atproto.repo.uploadBlob", thumb_bytes, token, "image/jpeg")
        external["thumb"] = blob["blob"]

    record = {
        "$type": "app.bsky.feed.post",
        "text": text,
        "facets": facets,
        "createdAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "langs": ["en"],
        "embed": {"$type": "app.bsky.embed.external", "external": external},
    }
    print(f"Posting to Bluesky: {post['title']} ({url})")
    result = xrpc("com.atproto.repo.createRecord", {
        "repo": session["did"],
        "collection": "app.bsky.feed.post",
        "record": record,
    }, token)
    print(f"Posted: {result['uri']}")


if __name__ == "__main__":
    main()
