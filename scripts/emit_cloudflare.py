#!/usr/bin/env python3
"""Emit Cloudflare Pages control files into the built site/ (run after `mkdocs build`).

  site/_redirects  from redirects.yml — keeps old WhatsApp links alive (brief §3.5).
  site/_headers    long-cache the content-addressed assets for speed (the reason we
                   chose Cloudflare Pages). Only files whose name carries their hash are
                   safe to mark immutable; HTML and the hand-written css/js stay
                   short-lived so edits show up.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
REDIRECTS = ROOT / "redirects.yml"


# A filename is content-addressed when it carries a hash: our rehosted images are
# `<sha12>.webp`, and the theme and Pagefind emit `name.<hash>.ext`.
HASHED_NAME = re.compile(r"^([0-9a-f]{8,}|.+\.[0-9a-f]{8,})\.[A-Za-z0-9_]+$")


def is_content_addressed(d: Path) -> bool:
    """True when every file under `d` carries its own hash, so freezing them is safe."""
    files = [p for p in d.rglob("*") if p.is_file()]
    return bool(files) and all(HASHED_NAME.match(p.name) for p in files)


def main() -> None:
    if not SITE.exists():
        raise SystemExit("site/ not found — run `mkdocs build` first.")

    redirects = {}
    if REDIRECTS.exists():
        redirects = yaml.safe_load(REDIRECTS.read_text(encoding="utf-8")) or {}
    lines = [f"{src}  {dst}  301" for src, dst in sorted(redirects.items())]
    (SITE / "_redirects").write_text(("\n".join(lines) + "\n") if lines else "", encoding="utf-8")
    print(f"wrote site/_redirects ({len(lines)} rule(s))")

    # NOTE: Cloudflare _headers COMBINES (does not override) Cache-Control across all
    # matching rules, so the rules must not overlap. Pages are served at trailing-slash
    # directory URLs (/, /catalogo/slug/); asset files never end in "/". So scope the
    # revalidate rule to trailing-slash paths and emit one disjoint rule per asset dir.
    IMMUTABLE = "public, max-age=31536000, immutable"
    REVALIDATE = "public, max-age=0, must-revalidate"

    lines = [
        '# HTML pages (directory URLs end in "/") revalidate so edits appear quickly.',
        "/", f"  Cache-Control: {REVALIDATE}",
        "/*/", f"  Cache-Control: {REVALIDATE}",
        "",
        "# One rule per asset directory: immutable only where every filename carries its",
        "# own hash. A blanket /assets/* would also freeze extra.css and the js, which have",
        "# stable names — a year of visitors would keep the stylesheet they first saw.",
    ]
    for top in ("assets", "pagefind"):
        root = SITE / top
        if not root.exists():
            continue
        for d in sorted(p for p in root.iterdir() if p.is_dir()):
            policy = IMMUTABLE if is_content_addressed(d) else REVALIDATE
            lines += [f"/{top}/{d.name}/*", f"  Cache-Control: {policy}"]
        loose = sorted(p for p in root.iterdir() if p.is_file())
        for f in loose:
            policy = IMMUTABLE if HASHED_NAME.match(f.name) else REVALIDATE
            lines += [f"/{top}/{f.name}", f"  Cache-Control: {policy}"]

    (SITE / "_headers").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote site/_headers ({sum(1 for l in lines if l.startswith('/'))} rule(s))")


if __name__ == "__main__":
    main()
