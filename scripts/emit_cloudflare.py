#!/usr/bin/env python3
"""Emit Cloudflare Pages control files into the built site/ (run after `mkdocs build`).

  site/_redirects  from redirects.yml — keeps old WhatsApp links alive (brief §3.5).
  site/_headers    long-cache the content-addressed assets for speed (the reason we
                   chose Cloudflare Pages). Image filenames are sha256-hashed, so they
                   are safe to mark immutable; HTML stays short-lived so edits show up.
"""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
REDIRECTS = ROOT / "redirects.yml"


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
    # matching rules, so the HTML and asset rules must not overlap. Pages are served at
    # trailing-slash directory URLs (/, /catalogo/slug/); asset files never end in "/".
    # So scope the revalidate rule to trailing-slash paths and immutable to the asset dirs.
    headers = """\
# HTML pages (directory URLs end in "/") revalidate so edits appear quickly.
/
  Cache-Control: public, max-age=0, must-revalidate
/*/
  Cache-Control: public, max-age=0, must-revalidate

# Content-addressed / hashed files: safe to cache forever (never end in "/").
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/pagefind/*
  Cache-Control: public, max-age=31536000, immutable
"""
    (SITE / "_headers").write_text(headers, encoding="utf-8")
    print("wrote site/_headers")


if __name__ == "__main__":
    main()
