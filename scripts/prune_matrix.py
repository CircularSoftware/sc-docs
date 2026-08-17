#!/usr/bin/env python3
"""Phase 5.2 — prune the static-embedding matrix so the browser bundle stays tiny.

DEFERRED skeleton (brief §5.2). The full model's token-embedding matrix + tokenizer.json
is far too large to ship. It's only a lookup table, so we keep just the rows the corpus
(plus the common Spanish vocabulary) can actually hit, quantize, and truncate.

Algorithm:
  1. Tokenize the entire corpus + the top ~20k Spanish tokens from a frequency list.
  2. Keep only those embedding rows; remap surviving token ids to a dense range.
  3. int8-quantize and truncate to 128 dims (same as the query encoder).
  4. Prune tokenizer.json to the surviving tokens — this is the tens-of-MB cost everyone
     forgets to measure (§5.2).
  5. Emit matrix.bin, tokens.json, meta.json {dims, scale, vocab_size}.

The CI budget gate (§5.4) then fails the build if gzip(matrix.bin) > ~2MB.

This is intentionally a skeleton: it needs the chosen model's internals and a Spanish
frequency list, both of which should be pinned when Phase 5 actually ships. Wire the real
tokenizer/matrix extraction here at that time.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "site" / "search"
FREQ_LIST = ROOT / "data" / "es-frequency-20k.txt"  # provide when Phase 5 ships
TOP_N_SPANISH = 20_000
DIMS = 128


def corpus_text() -> str:
    return "\n".join(p.read_text(encoding="utf-8") for p in DOCS.rglob("*.md"))


def main() -> None:
    try:
        import numpy as np  # noqa: F401
        from sentence_transformers import SentenceTransformer  # noqa: F401
    except ImportError:
        print("Embedding deps missing. Install: pip install -r requirements-embeddings.txt",
              file=sys.stderr)
        sys.exit(3)

    if not FREQ_LIST.exists():
        print(f"Spanish frequency list not found at {FREQ_LIST}.")
        print("Phase 5.2 is deferred: drop a top-20k es token list there when you ship "
              "semantic search, then implement the extraction steps documented in this file.")
        return

    # --- Steps 1–5 go here when Phase 5 ships (see module docstring). ---
    # 1. seen_tokens = tokenize(corpus_text()) | top_n(FREQ_LIST, TOP_N_SPANISH)
    # 2. rows, remap = keep_rows(model.embedding_matrix, seen_tokens)
    # 3. q = int8_quantize(rows[:, :DIMS])
    # 4. tokenizer = prune_tokenizer(model.tokenizer, seen_tokens)
    # 5. write matrix.bin / tokens.json / meta.json
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "meta.json").write_text(
        json.dumps({"dims": DIMS, "scale": 127, "vocab_size": 0, "status": "skeleton"}),
        encoding="utf-8",
    )
    print("prune_matrix skeleton ran — implement extraction when Phase 5 ships.")


if __name__ == "__main__":
    main()
