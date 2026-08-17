# sc-docs — Notion → MkDocs → Pagefind → Cloudflare Pages

Spanish help-center pipeline. Editors write in a Notion database; CI turns it into a static
MkDocs (Material) site with Pagefind search and deploys to Cloudflare Pages. A semantic
search fallback (browser) and bot retrieval are scaffolded but **deferred** until there are
real articles and query logs.

## Status by phase

| Phase | What | State |
|-------|------|-------|
| 1 | Notion as source of truth | DB exists & token has access — **schema not yet created** (see below) |
| 2 | Repo scaffold | ✅ done |
| 3 | Deterministic sync script | ✅ done + unit-tested (`tests/test_convert.py`) |
| 4 | Build / Pagefind / Cloudflare deploy / Slack alert | ✅ wired — **needs CI secrets to deploy** |
| 5 | Browser semantic fallback | scaffolded, deferred (`scripts/build_embeddings.py`, `scripts/prune_matrix.py`) |
| 6 | Bot retrieval | scaffolded, deferred (same encode pass emits `bot/`) |
| 7 | Weekly alias loop | process, owned by support |

## Two things block a live site

1. **Notion schema.** The `Docs` database currently has only a `Name` (title) property and
   no rows. Add the Phase 1.1 properties before content can flow:

   | Property | Type | Notes |
   |----------|------|-------|
   | `Name`/`Title` | Title | already present |
   | `Slug` | Text | **immutable**, lowercase-hyphen-no-accents |
   | `Category` | Select | becomes the folder + nav group |
   | `Order` | Number | gaps of 10 |
   | `Status` | Select | `Draft` / `Published` — only `Published` exports |
   | `Aliases` | Text | real customer phrasings, comma-separated |
   | `Updated` | Last edited time | staleness / incremental sync |

   The sync integration is **read-only by design** (it never writes back), so this schema
   is created by a human in Notion — not by the pipeline.

2. **Cloudflare + Slack CI secrets** (GitHub → repo → Settings → Secrets → Actions):
   `NOTION_API_TOKEN`, `NOTION_DATABASE_ID`, `CLOUDFLARE_API_TOKEN`,
   `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_PROJECT_NAME`, `SLACK_WEBHOOK_URL`.
   Create the Cloudflare Pages project once (`wrangler pages project create <name>`), then
   the workflow deploys `site/` on every run.

## Local development

```bash
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
cp .env.example .env          # fill in NOTION_API_TOKEN
./.venv/bin/python tests/test_convert.py     # offline unit tests
./.venv/bin/python scripts/sync_notion.py    # Notion -> docs/
./.venv/bin/mkdocs serve                     # preview at http://127.0.0.1:8000
```

Full build (what CI runs):

```bash
python scripts/sync_notion.py
mkdocs build --strict          # broken internal links fail the build
npx -y pagefind --site site
python scripts/emit_cloudflare.py
```

## How the sync behaves (`scripts/sync_notion.py`)

- **Deterministic**: same Notion state in → byte-identical tree out. Ordering is stable;
  image files are content-addressed on the *unsigned* URL so signatures don't churn diffs.
- **Images** are downloaded and rehosted under `docs/assets/<slug>/` (Notion URLs expire
  in ~1h).
- **Sanity gates** (exit 2, refuse to publish): duplicate slug, empty published body,
  a changed slug on an existing page, or a >20% drop in article count.
- **Removals** delete the file and append a never-shrinking entry to `redirects.yml`.
- `manifest.json` (committed) maps `page_id → {slug, path}` and drives the diff.

## The generated `docs/` tree is committed on purpose

It gives a readable diff of what editors changed and lets a bad sync be reverted with
`git revert`. Do not hand-edit files under `docs/<category>/` — they are overwritten.
`docs/index.md` and `docs/assets/stylesheets/` are static and safe to edit.

## Search note (Phase 4 → 5)

Right now Material's built-in Spanish search is the live UI, and Pagefind builds its index
alongside it. The Pagefind-UI swap (dropping the built-in index) is done together with the
Phase 5 semantic fallback, because the fallback wraps Pagefind's "no results" callback — so
the search override is written once, not twice. Until then the site ships two small indexes;
harmless at this corpus size.

## Deferred phases 5–6

Do not start until ~30 articles + a month of query logs exist (brief §5). Then:

```bash
pip install -r requirements-embeddings.txt
python scripts/build_embeddings.py    # emits site/search/* (browser) and bot/* (assistant)
python scripts/prune_matrix.py        # trims the shipped matrix; wire in the frequency list
```

A CI budget gate must fail the build if `gzip(site/search/matrix.bin) > ~2MB` (brief §5.4).
