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

    headers = """\
# Default: every page revalidates so edits appear quickly. This MUST use /* (not
# /*.html) because pages are served at directory URLs like /catalogo/slug/ that don't
# end in .html. The immutable asset rules below are more specific and override this.
/*
  Cache-Control: public, max-age=0, must-revalidate

# Content-addressed images never change under a given URL -> cache hard.
/assets/*
  Cache-Control: public, max-age=31536000, immutable

# Pagefind index + search assets: hashed, safe to cache long.
/pagefind/*
  Cache-Control: public, max-age=31536000, immutable
"""
    (SITE / "_headers").write_text(headers, encoding="utf-8")
    print("wrote site/_headers")


if __name__ == "__main__":
    main()
