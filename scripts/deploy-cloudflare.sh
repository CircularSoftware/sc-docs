#!/usr/bin/env bash
# Manual/local deploy to Cloudflare Pages. CI does this automatically (publish.yml);
# this is for a first deploy or an ad-hoc one from your machine.
#
# Needs, in .env (gitignored) or the environment:
#   CLOUDFLARE_API_TOKEN     scoped token with "Account > Cloudflare Pages > Edit"
#   CLOUDFLARE_ACCOUNT_ID    from the Cloudflare dashboard sidebar
#   CLOUDFLARE_PROJECT_NAME  optional, defaults to sc-docs
set -euo pipefail
cd "$(dirname "$0")/.."

# Load .env without echoing secrets.
[ -f .env ] && { set -a; . ./.env; set +a; }
# Accept either CLOUDFLARE_API_TOKEN (canonical, what wrangler reads) or CLOUDFLARE_TOKEN.
: "${CLOUDFLARE_API_TOKEN:=${CLOUDFLARE_TOKEN:-}}"
export CLOUDFLARE_API_TOKEN
: "${CLOUDFLARE_API_TOKEN:?missing — add CLOUDFLARE_API_TOKEN (or CLOUDFLARE_TOKEN) to .env}"
: "${CLOUDFLARE_ACCOUNT_ID:?missing — add CLOUDFLARE_ACCOUNT_ID to .env}"
PROJECT="${CLOUDFLARE_PROJECT_NAME:-sc-docs}"

PY=./.venv/bin/python;  [ -x "$PY" ] || PY=python
MK=./.venv/bin/mkdocs;  [ -x "$MK" ] || MK=mkdocs

# Rebuild fresh (sync is best-effort; skip if no Notion token locally).
"$PY" scripts/sync_notion.py || echo "(sync skipped/failed — building current docs/ tree)"
"$MK" build --strict
npx -y pagefind --site site
"$PY" scripts/emit_cloudflare.py

# Create the Pages project on first run (no-op if it already exists).
npx -y wrangler pages project create "$PROJECT" --production-branch main 2>/dev/null \
  || echo "(project '$PROJECT' already exists — deploying)"

npx -y wrangler pages deploy site --project-name "$PROJECT"
echo "Done. Live at https://${PROJECT}.pages.dev (custom domain configured separately)."
