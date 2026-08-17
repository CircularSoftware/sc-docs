#!/usr/bin/env python3
"""Phase 5/6 — chunk the generated docs and embed them.

DEFERRED: run this only once real articles exist (~30) and you have a month of query
logs (brief §5, §6). It is wired and correct, but tuning it against an empty corpus is
pointless. Nothing in Phases 1–4 depends on it.

Deps live in requirements-embeddings.txt (heavy: torch + sentence-transformers), NOT in
the fast docs build. Install them first:  pip install -r requirements-embeddings.txt

Emits two artifact sets from ONE encode pass:
  Browser fallback (§5.1)  site/search/vectors.bin   int8, 128-dim (MRL-truncated)
                           site/search/chunks.json   [{slug, heading, url, preview}]
  Bot retrieval (§6)       bot/embeddings.f32.bin     float32, 256-dim
                           bot/chunks.jsonl           chunk text + metadata + raw markdown

Run:  python scripts/build_embeddings.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE_SEARCH = ROOT / "site" / "search"
BOT = ROOT / "bot"

MODEL_NAME = "sentence-transformers/static-similarity-mrl-multilingual-v1"
BROWSER_DIMS = 128   # MRL truncation for the shipped browser matrix
BOT_DIMS = 256       # richer vectors for the bot (no download budget)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    import yaml

    _, fm, body = text.split("---", 2)
    return (yaml.safe_load(fm) or {}), body.lstrip("\n")


def url_for(relpath: str) -> str:
    # docs/<category>/<slug>.md -> /<category>/<slug>/
    p = re.sub(r"\.md$", "/", relpath)
    p = re.sub(r"index/$", "", p)
    return "/" + p


def chunk_article(fm: dict, body: str, relpath: str) -> list[dict]:
    """Split on h2/h3 boundaries (~200–400 tokens), prepend the title to each chunk."""
    title = fm.get("title", "")
    aliases = fm.get("aliases", "")
    slug = fm.get("slug", "")
    url = url_for(relpath)

    # Split at ## / ### headings while keeping the heading with its section.
    parts = re.split(r"(?m)^(#{2,3}\s.*)$", body)
    sections: list[tuple[str, str]] = []
    # parts = [pre, heading, text, heading, text, ...]
    lead = parts[0].strip()
    if lead:
        sections.append(("", lead))
    for i in range(1, len(parts), 2):
        heading = re.sub(r"^#{2,3}\s", "", parts[i]).strip()
        text = parts[i + 1].strip() if i + 1 < len(parts) else ""
        sections.append((heading, text))

    chunks = []
    for heading, text in sections:
        # strip hidden alias block from body text
        text = re.sub(r'<p class="doc-aliases".*?</p>', "", text, flags=re.S).strip()
        if not text:
            continue
        preview = re.sub(r"\s+", " ", re.sub(r"[#>*`\[\]]", "", text))[:180]
        chunks.append(
            {
                "slug": slug,
                "title": title,
                "heading": heading,
                "url": url + (f"#{_anchor(heading)}" if heading else ""),
                "aliases": aliases,
                "body": text,
                "preview": preview,
            }
        )
    return chunks


def _anchor(heading: str) -> str:
    a = heading.lower()
    a = re.sub(r"[^\w\s-]", "", a)
    return re.sub(r"\s+", "-", a).strip("-")


def collect_chunks() -> list[dict]:
    chunks = []
    for md in sorted(DOCS.rglob("*.md")):
        if md.name == "index.md" and md.parent == DOCS:
            continue
        fm, body = parse_frontmatter(md.read_text(encoding="utf-8"))
        if not fm.get("slug"):
            continue
        chunks.extend(chunk_article(fm, body, str(md.relative_to(DOCS))))
    return chunks


def main() -> None:
    chunks = collect_chunks()
    if not chunks:
        print("No article chunks found — nothing to embed yet. (Phase 5 is deferred "
              "until real articles exist.)")
        return

    try:
        import numpy as np
        from sentence_transformers import SentenceTransformer
    except ImportError:
        print("Embedding deps missing. Install: pip install -r requirements-embeddings.txt",
              file=sys.stderr)
        sys.exit(3)

    print(f"Embedding {len(chunks)} chunk(s) with {MODEL_NAME} ...")
    model = SentenceTransformer(MODEL_NAME)
    # Include aliases in the embedded text — the single highest-recall line here (§5.1).
    texts = [f"{c['title']}\n{c['aliases']}\n{c['body']}" for c in chunks]
    full = model.encode(texts, normalize_embeddings=True)

    # ---- Browser artifacts: int8, 128-dim ----
    SITE_SEARCH.mkdir(parents=True, exist_ok=True)
    vecs = full[:, :BROWSER_DIMS]
    vecs = np.round(vecs / (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9) * 127)
    vecs.astype(np.int8).tofile(SITE_SEARCH / "vectors.bin")
    (SITE_SEARCH / "chunks.json").write_text(
        json.dumps(
            [{"slug": c["slug"], "heading": c["heading"], "url": c["url"], "preview": c["preview"]}
             for c in chunks],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (SITE_SEARCH / "meta.json").write_text(
        json.dumps({"dims": BROWSER_DIMS, "scale": 127, "count": len(chunks)}), encoding="utf-8"
    )
    print(f"  browser: {SITE_SEARCH/'vectors.bin'} ({len(chunks)}x{BROWSER_DIMS} int8)")

    # ---- Bot artifacts: float32, 256-dim + raw text (§6) ----
    BOT.mkdir(parents=True, exist_ok=True)
    full[:, :BOT_DIMS].astype("float32").tofile(BOT / "embeddings.f32.bin")
    with (BOT / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"  bot: {BOT/'embeddings.f32.bin'} ({len(chunks)}x{BOT_DIMS} float32)")


if __name__ == "__main__":
    main()
