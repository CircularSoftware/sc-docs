#!/usr/bin/env python3
"""Sync a Notion `Docs` database into a byte-deterministic MkDocs tree.

Contract (brief §3): same Notion state in => byte-identical tree out. Non-determinism
here turns git history into noise and hides real edits, so every ordering is stable and
image filenames are content-addressed on the *unsigned* URL.

Env:
  NOTION_API_TOKEN     Notion internal integration token (read-only). From .env or CI.
  NOTION_DATABASE_ID   The Docs database id (dashless or dashed). Required (env / CI secret).

Exit codes:
  0  success
  2  a sanity gate failed — DO NOT PUBLISH (brief §3.6)
  3  configuration / network error
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import unicodedata
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import requests
import yaml

# --------------------------------------------------------------------------------------
# Paths & config
# --------------------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
ASSETS_ROOT = DOCS / "assets"
MANIFEST_PATH = ROOT / "manifest.json"
REDIRECTS_PATH = ROOT / "redirects.yml"
HOMEPAGE_CONFIG = ROOT / "homepage.yml"
FAQ_HUB = "preguntas-frecuentes.md"  # generated hub; FAQ articles have no page of their own

NOTION_VERSION = "2022-06-28"
API = "https://api.notion.com/v1"
# The Docs database id comes from NOTION_DATABASE_ID (env / CI secret) — never hardcoded.

# Article-count drop that trips the safety gate (brief §3.6): a broken filter / revoked
# token can silently wipe the site, so refuse to publish a >20% shrink.
COUNT_DROP_GATE = 0.20

warnings: list[str] = []


def warn(msg: str) -> None:
    warnings.append(msg)


def die(msg: str, code: int = 3) -> "None":
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


# --------------------------------------------------------------------------------------
# .env loader (no extra dependency; real env vars always win)
# --------------------------------------------------------------------------------------
def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        os.environ.setdefault(key, val)


def normalize_db_id(raw: str) -> str:
    s = re.sub(r"[^0-9a-fA-F]", "", raw)
    if len(s) != 32:
        return raw  # let the API reject it with a clear error
    return f"{s[0:8]}-{s[8:12]}-{s[12:16]}-{s[16:20]}-{s[20:32]}"


# --------------------------------------------------------------------------------------
# Notion HTTP client: rate-limited (~3 req/s) with 429/5xx retry
# --------------------------------------------------------------------------------------
class Notion:
    def __init__(self, token: str):
        self.s = requests.Session()
        self.s.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Notion-Version": NOTION_VERSION,
                "Content-Type": "application/json",
            }
        )
        self._last = 0.0
        self._min_interval = 0.34  # ~3 req/s

    def _throttle(self) -> None:
        wait = self._min_interval - (time.monotonic() - self._last)
        if wait > 0:
            time.sleep(wait)
        self._last = time.monotonic()

    def _request(self, method: str, path: str, **kw) -> dict:
        url = f"{API}{path}"
        for attempt in range(6):
            self._throttle()
            resp = self.s.request(method, url, timeout=30, **kw)
            if resp.status_code == 429:
                retry = float(resp.headers.get("Retry-After", "1"))
                time.sleep(retry)
                continue
            if resp.status_code >= 500:
                time.sleep(min(2**attempt, 8))
                continue
            if resp.status_code >= 400:
                die(
                    f"Notion {method} {path} -> {resp.status_code}: {resp.text[:400]}",
                    code=3,
                )
            return resp.json()
        die(f"Notion {method} {path} kept failing after retries", code=3)
        return {}

    def query_database(self, db_id: str) -> list[dict]:
        results, cursor = [], None
        while True:
            body: dict = {"page_size": 100}
            if cursor:
                body["start_cursor"] = cursor
            data = self._request("POST", f"/databases/{db_id}/query", json=body)
            results.extend(data.get("results", []))
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")
        return results

    def block_children(self, block_id: str) -> list[dict]:
        results, cursor = [], None
        while True:
            q = f"?page_size=100" + (f"&start_cursor={cursor}" if cursor else "")
            data = self._request("GET", f"/blocks/{block_id}/children{q}")
            results.extend(data.get("results", []))
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")
        return results


# --------------------------------------------------------------------------------------
# Property extraction
# --------------------------------------------------------------------------------------
def plain(rich: list[dict]) -> str:
    return "".join(r.get("plain_text", "") for r in rich or [])


def prop_of_type(props: dict, wanted_type: str) -> dict | None:
    for p in props.values():
        if p.get("type") == wanted_type:
            return p
    return None


def get_prop(props: dict, name: str) -> dict | None:
    return props.get(name)


def read_select(p: dict | None) -> str:
    if not p:
        return ""
    t = p.get("type")
    v = p.get(t)
    if isinstance(v, dict):
        return (v or {}).get("name", "") or ""
    return ""


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "general"


def extract_article(page: dict) -> dict | None:
    props = page.get("properties", {})

    title_prop = get_prop(props, "Title") or prop_of_type(props, "title")
    title = plain((title_prop or {}).get("title", [])) if title_prop else ""

    slug_prop = get_prop(props, "Slug")
    slug = plain((slug_prop or {}).get("rich_text", [])).strip() if slug_prop else ""

    category = read_select(get_prop(props, "Category")) or "General"

    order_prop = get_prop(props, "Order")
    order = (order_prop or {}).get("number") if order_prop else None
    if order is None:
        order = 1000  # unsorted articles sink to the bottom, deterministically

    status = read_select(get_prop(props, "Status"))

    aliases_prop = get_prop(props, "Aliases")
    aliases = plain((aliases_prop or {}).get("rich_text", [])).strip() if aliases_prop else ""

    typ = read_select(get_prop(props, "Type")) or "Guía"

    updated = ""
    up = get_prop(props, "Updated")
    if up and up.get("type") == "last_edited_time":
        updated = up.get("last_edited_time", "")
    updated = updated or page.get("last_edited_time", "")

    return {
        "page_id": page["id"],
        "title": title.strip(),
        "slug": slug,
        "category": category.strip(),
        "category_slug": slugify(category),
        "order": order,
        "status": status,
        "aliases": aliases,
        "type": typ,
        "updated": updated,
    }


# --------------------------------------------------------------------------------------
# Rich text + block -> markdown
# --------------------------------------------------------------------------------------
def rich_to_md(rich: list[dict]) -> str:
    out = []
    for r in rich or []:
        t = r.get("plain_text", "")
        if t == "":
            continue
        ann = r.get("annotations", {})
        href = r.get("href")
        if ann.get("code"):
            t = f"`{t}`"
        if ann.get("bold"):
            t = f"**{t}**"
        if ann.get("italic"):
            t = f"*{t}*"
        if ann.get("strikethrough"):
            t = f"~~{t}~~"
        if href:
            t = f"[{t}]({href})"
        out.append(t)
    return "".join(out)


# blocks whose children hold recoverable content even though the block type itself is
# "unsupported" per the editor contract — flatten instead of losing text silently.
FLATTEN_CHILDREN = {"column_list", "column", "synced_block", "toggle"}
# truly unsupported: dropped with a warning (brief editor contract §1.3)
SKIP_BLOCKS = {"child_database", "embed", "bookmark", "link_preview", "button", "unsupported"}


class BlockConverter:
    """Walks Notion blocks into markdown, collecting image URLs to rehost."""

    def __init__(self, notion: Notion):
        self.n = notion
        self.image_jobs: list[tuple[str, str]] = []  # (original_url, alt)

    def convert(self, blocks: list[dict], indent: int = 0) -> list[str]:
        lines: list[str] = []
        for b in blocks:
            lines.extend(self._block(b, indent))
        return lines

    def _children(self, block: dict) -> list[dict]:
        if not block.get("has_children"):
            return []
        return self.n.block_children(block["id"])

    def _block(self, b: dict, indent: int) -> list[str]:
        bt = b.get("type", "")
        data = b.get(bt, {}) or {}
        pad = "    " * indent
        out: list[str] = []

        if bt in SKIP_BLOCKS:
            warn(f"skipped unsupported block '{bt}' ({b.get('id')})")
            return out

        if bt in FLATTEN_CHILDREN:
            if bt == "toggle":
                txt = rich_to_md(data.get("rich_text", []))
                if txt:
                    out.append(f"{pad}{txt}")
                    out.append("")
            out.extend(self.convert(self._children(b), indent))
            return out

        if bt == "paragraph":
            txt = rich_to_md(data.get("rich_text", []))
            out.append(f"{pad}{txt}" if txt else "")
            out.append("")
        elif bt in ("heading_1", "heading_2", "heading_3"):
            # Page H1 is the frontmatter title; shift Notion headings down one level so the
            # document has exactly one H1 (a11y/SEO) and phase-5 chunking sits on h2/h3.
            level = {"heading_1": 2, "heading_2": 3, "heading_3": 4}[bt]
            out.append(f"{'#' * level} {rich_to_md(data.get('rich_text', []))}")
            out.append("")
        elif bt == "bulleted_list_item":
            out.append(f"{pad}- {rich_to_md(data.get('rich_text', []))}")
            out.extend(self.convert(self._children(b), indent + 1))
        elif bt == "numbered_list_item":
            out.append(f"{pad}1. {rich_to_md(data.get('rich_text', []))}")
            out.extend(self.convert(self._children(b), indent + 1))
        elif bt == "to_do":
            box = "[x]" if data.get("checked") else "[ ]"
            out.append(f"{pad}- {box} {rich_to_md(data.get('rich_text', []))}")
            out.extend(self.convert(self._children(b), indent + 1))
        elif bt == "quote":
            for ln in rich_to_md(data.get("rich_text", [])).split("\n"):
                out.append(f"> {ln}")
            out.append("")
        elif bt == "callout":
            icon = (data.get("icon") or {}).get("emoji", "")
            body = rich_to_md(data.get("rich_text", []))
            title = f'"{icon} Nota"' if icon else '"Nota"'
            out.append(f"!!! note {title}")
            out.append(f"    {body}")
            for child in self.convert(self._children(b), 0):
                out.append(f"    {child}" if child else "")
            out.append("")
        elif bt == "code":
            lang = data.get("language", "") or "text"
            lang = {"plain text": "text"}.get(lang, lang).replace(" ", "-")
            out.append(f"```{lang}")
            out.extend(plain(data.get("rich_text", [])).split("\n"))
            out.append("```")
            out.append("")
        elif bt == "divider":
            out.append("---")
            out.append("")
        elif bt == "image":
            url, alt = self._image(data)
            if url:
                self.image_jobs.append((url, alt))
                out.append(f"![{alt}]({url})")
                out.append("")
        elif bt == "table":
            out.extend(self._table(b, data))
            out.append("")
        else:
            # Unknown but possibly-text block: try rich_text, else warn.
            txt = rich_to_md(data.get("rich_text", []))
            if txt:
                out.append(f"{pad}{txt}")
                out.append("")
            else:
                warn(f"unhandled block type '{bt}' ({b.get('id')})")
        return out

    def _image(self, data: dict) -> tuple[str, str]:
        kind = data.get("type")
        url = ((data.get(kind) or {}).get("url", "")) if kind else ""
        alt = plain(data.get("caption", []))
        return url, alt

    def _table(self, block: dict, data: dict) -> list[str]:
        rows = self.n.block_children(block["id"])
        has_header = data.get("has_column_header", False)
        md: list[str] = []
        for i, row in enumerate(rows):
            cells = row.get("table_row", {}).get("cells", [])
            rendered = [rich_to_md(c).replace("|", "\\|") or " " for c in cells]
            md.append("| " + " | ".join(rendered) + " |")
            if i == 0:
                sep = ["---"] * len(rendered)
                md.append("| " + " | ".join(sep) + " |")
                if not has_header:
                    # markdown needs a header row; keep the first row as header anyway.
                    pass
        return md


# --------------------------------------------------------------------------------------
# Image rehosting (brief §3.3) — content-addressed on the UNSIGNED url
# --------------------------------------------------------------------------------------
def url_without_query(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def guess_ext(url: str) -> str:
    path = urlsplit(url).path
    m = re.search(r"(\.[A-Za-z0-9]{2,5})$", path)
    return m.group(1).lower() if m else ""


def rehost_images(md: str, slug: str, jobs: list[tuple[str, str]], session: requests.Session) -> str:
    for url, _alt in jobs:
        if url not in md:
            continue
        digest = hashlib.sha256(url_without_query(url).encode()).hexdigest()[:12]
        ext = guess_ext(url) or ".png"
        rel = f"assets/{slug}/{digest}{ext}"
        dest = DOCS / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            try:
                r = session.get(url, timeout=60)
                r.raise_for_status()
                dest.write_bytes(r.content)
            except Exception as e:  # noqa: BLE001
                warn(f"image download failed for {slug} ({e}); keeping original url")
                continue
        md = md.replace(url, f"/{rel}")
    return md


# --------------------------------------------------------------------------------------
# File emission
# --------------------------------------------------------------------------------------
def render_markdown(art: dict, body: str) -> str:
    fm = {
        "title": art["title"],
        "slug": art["slug"],
        "order": art["order"],
        "type": art.get("type", "Guía"),
        "aliases": art["aliases"],
    }
    front = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    parts = [f"---\n{front}\n---", "", f"# {art['title']}", "", body.rstrip()]
    if art["aliases"]:
        # Hidden synonyms so Pagefind (phase 4) indexes real customer phrasings now.
        parts += ["", f'<p class="doc-aliases" markdown>Términos relacionados: {art["aliases"]}</p>']
    return "\n".join(parts).rstrip() + "\n"


def collapse_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def generate_homepage() -> None:
    """Regenerate docs/index.md: hero + one card per category that actually has content.

    Data-driven from the docs tree + editor copy in homepage.yml, so cards never link to
    a page that doesn't exist (keeps `mkdocs build --strict` green even with no content).
    """
    cfg = {}
    if HOMEPAGE_CONFIG.exists():
        cfg = yaml.safe_load(HOMEPAGE_CONFIG.read_text(encoding="utf-8")) or {}
    hero = cfg.get("hero", {}) or {}
    title = hero.get("title", "¿En qué podemos ayudarte?")
    subtitle = hero.get("subtitle", "")
    cat_cfg = cfg.get("categories", {}) or {}
    default_emoji = cfg.get("default_emoji", "📄")

    cards = []
    for cat_dir in sorted(p for p in DOCS.iterdir() if p.is_dir() and p.name != "assets"):
        pages_file = cat_dir / ".pages"
        if not pages_file.exists():
            continue
        meta = yaml.safe_load(pages_file.read_text(encoding="utf-8")) or {}
        nav = meta.get("nav") or []
        if not nav:
            continue
        cat_title = meta.get("title", cat_dir.name)
        url = f"{cat_dir.name}/{nav[0]}"  # .md link; mkdocs rewrites to the directory URL
        c = cat_cfg.get(cat_title, {}) or {}
        cards.append((c.get("emoji", default_emoji), cat_title, c.get("description", ""), url))

    L = [
        "---", "title: Centro de Ayuda", "hide:", "  - navigation", "  - toc", "---", "",
        '<div class="sc-hero">',
        f'  <h1 class="sc-hero__title">{title}</h1>',
        f'  <p class="sc-hero__subtitle">{subtitle}</p>',
        '  <button class="sc-hero__search" type="button" aria-label="Buscar" tabindex="0">',
        '    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"></circle>'
        '<line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
        '    <span class="sc-hero__search-text">Busca tu pregunta…</span>',
        "    <kbd>/</kbd>",
        "  </button>",
        "</div>", "",
    ]
    if cards:
        L += ['<div class="grid cards" markdown>', ""]
        for emoji, cat_title, desc, url in cards:
            L += [f'-   <span class="sc-card-emoji">{emoji}</span>', f"    **{cat_title}**", "", "    ---", ""]
            if desc:
                L += [f"    {desc}", ""]
            L += [f"    [Ver artículos]({url}){{ .sc-card-cta }}", ""]
        L += ["</div>"]
    else:
        L += ['<p style="text-align:center;color:var(--sc-ink-3)">Pronto encontrarás aquí nuestras guías.</p>']
    # FAQ hub card (if the hub exists)
    if cards and (DOCS / FAQ_HUB).exists():
        L += ["", '<div class="grid cards" markdown>', "",
              '-   <span class="sc-card-emoji">❓</span>', "    **Preguntas frecuentes**", "", "    ---", "",
              "    Respuestas rápidas a las dudas más comunes.", "",
              "    [Ver preguntas](preguntas-frecuentes.md){ .sc-card-cta }", "", "</div>"]

    L += ["", '<p style="text-align:center; color:var(--sc-ink-3); font-size:.75rem; margin-top:2.5rem">',
          "  ¿No encuentras lo que buscas? Escribe con tus propias palabras en el buscador.", "</p>", ""]
    (DOCS / "index.md").write_text("\n".join(L), encoding="utf-8")


def generate_faq_hub(items: list[dict]) -> None:
    """Render all FAQ articles into one 'Preguntas frecuentes' page (collapsible accordion,
    grouped by category, with per-item anchors for deep-linking). Removes it if no FAQs."""
    hub = DOCS / FAQ_HUB
    if not items:
        if hub.exists():
            hub.unlink()
        return
    items = sorted(items, key=lambda a: (a["category_slug"], a["order"], a["slug"]))
    L = ["---", "title: Preguntas frecuentes", "icon: material/help-circle", "hide:",
         "  - toc", "---", "", "# Preguntas frecuentes", "",
         "Respuestas rápidas a las dudas más comunes. Tocá una pregunta para ver la respuesta.", ""]
    current = None
    for a in items:
        if a["category"] != current:
            current = a["category"]
            L += [f"## {current}", ""]
        L.append(f'<a id="{a["slug"]}"></a>')
        L.append(f'??? question "{a["title"]}"')
        for line in a["_body"].split("\n"):
            L.append(f"    {line}" if line.strip() else "")
        if a.get("aliases"):
            L.append(f'    <p class="doc-aliases" markdown>Términos relacionados: {a["aliases"]}</p>')
        L.append("")
    hub.write_text("\n".join(L), encoding="utf-8")


def write_root_nav() -> None:
    """Root nav: index first, categories (alphabetical via '...'), FAQ hub last."""
    nav = ["index.md", "..."]
    if (DOCS / FAQ_HUB).exists():
        nav.append(FAQ_HUB)
    (DOCS / ".pages").write_text(
        yaml.safe_dump({"nav": nav}, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------
def main() -> None:
    if "--homepage-only" in sys.argv:
        generate_homepage()
        print("Regenerated docs/index.md from the docs tree.")
        return
    if "--faq-demo" in sys.argv:
        # Local preview of the FAQ hub without Notion (real articles are still Draft).
        demo = [
            {"title": "¿Cómo elimino un producto que cargué mal?", "slug": "estados-producto",
             "category": "Catálogo", "category_slug": "catalogo", "order": 50,
             "aliases": "borrar producto, eliminar prenda, quedan dobles",
             "_body": "Los productos no se eliminan: se **pausan**.\n\n## Pasos\n1. Entrá a Productos.\n"
                      "2. En \"Acciones\" cambiá el estado a \"Pausado\".\n\n> Si duplicaste un producto, "
                      "pausalo y escribinos para darlo de baja."},
            {"title": "¿Qué formato deben tener las fotos?", "slug": "fotos-productos",
             "category": "Catálogo", "category_slug": "catalogo", "order": 20,
             "aliases": "no me deja subir la foto, HEIC, iphone",
             "_body": "Las imágenes deben ser JPG, PNG o WEBP y medir al menos 500x500 px.\n\n## Si usás "
                      "iPhone\n1. Ajustes → Cámara → Formatos.\n2. Elegí \"Más compatible\"."},
            {"title": "¿Por qué no aparecen mis comisiones para pagar?", "slug": "finalizar-ordenes",
             "category": "Ventas", "category_slug": "ventas", "order": 60,
             "aliases": "no figura la comisión, cerrar el mes",
             "_body": "Las comisiones se habilitan cuando la orden está **finalizada**.\n\n## Pasos\n"
                      "1. Entrá a Órdenes.\n2. Filtrá por fecha y local.\n3. Cambiá a \"Finalizada\" las "
                      "órdenes entregadas."},
        ]
        generate_faq_hub(demo)
        write_root_nav()
        generate_homepage()
        print("FAQ demo generated (docs/preguntas-frecuentes.md + homepage card).")
        return
    load_dotenv(ROOT / ".env")
    token = os.environ.get("NOTION_API_TOKEN") or os.environ.get("NOTION_TOKEN")
    if not token:
        die("NOTION_API_TOKEN not set (add it to .env or the CI secret store)", code=3)
    db_env = os.environ.get("NOTION_DATABASE_ID")
    if not db_env:
        die("NOTION_DATABASE_ID not set (add it to .env or the CI secret store)", code=3)
    db_id = normalize_db_id(db_env)

    notion = Notion(token)
    # Image downloads need a clean session: Notion's file URLs are presigned S3 links,
    # and S3 rejects any request that also carries an Authorization header (400).
    images = requests.Session()
    print(f"Querying Notion database {db_id} ...")
    pages = notion.query_database(db_id)
    print(f"  {len(pages)} rows returned")

    # Extract + filter to Published
    articles = []
    for pg in pages:
        art = extract_article(pg)
        if not art:
            continue
        if art["status"].lower() != "published":
            continue
        if not art["slug"]:
            warn(f"published page '{art['title']}' has no Slug — skipped")
            continue
        articles.append(art)

    # ---- Sanity gate: duplicate slug -----------------------------------------------
    seen: dict[str, str] = {}
    dupes = []
    for a in articles:
        if a["slug"] in seen:
            dupes.append(a["slug"])
        seen[a["slug"]] = a["title"]
    if dupes:
        die(f"duplicate slug(s): {sorted(set(dupes))}", code=2)

    # Deterministic order: category, then Order, then slug
    articles.sort(key=lambda a: (a["category_slug"], a["order"], a["slug"]))

    # Load old manifest for diff-based removal + slug-change detection
    old_manifest = {}
    if MANIFEST_PATH.exists():
        old_manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    old_pages = old_manifest.get("pages", {})
    old_count = old_manifest.get("count", 0)

    # ---- Sanity gate: slug changed on an existing page -----------------------------
    slug_changes = []
    for a in articles:
        prev = old_pages.get(a["page_id"])
        if prev and prev.get("slug") and prev["slug"] != a["slug"]:
            slug_changes.append((prev["slug"], a["slug"], a["title"]))
    if slug_changes:
        lines = "\n".join(f"  {o} -> {n}  ({t})" for o, n, t in slug_changes)
        die(
            "Slug changed on published page(s). Slugs are immutable — a human must "
            f"confirm and update redirects:\n{lines}",
            code=2,
        )

    # ---- Sanity gate: article count drop -------------------------------------------
    if old_count and articles:
        drop = (old_count - len(articles)) / old_count
        if drop > COUNT_DROP_GATE:
            die(
                f"published article count dropped {drop:.0%} ({old_count} -> {len(articles)}). "
                "Refusing to publish — check for a broken filter or revoked token.",
                code=2,
            )

    # ---- Build page bodies + emit files --------------------------------------------
    new_pages: dict[str, dict] = {}
    written_paths: set[Path] = set()
    by_category: dict[str, list[dict]] = {}
    faq_items: list[dict] = []

    for a in articles:
        conv = BlockConverter(notion)
        blocks = notion.block_children(a["page_id"])
        body_lines = conv.convert(blocks)
        body = collapse_blank_lines("\n".join(body_lines)).strip()

        # ---- Sanity gate: empty body on a Published page ---------------------------
        if not body:
            die(f"published page '{a['title']}' ({a['slug']}) has an empty body", code=2)

        body = rehost_images(body, a["slug"], conv.image_jobs, images)

        # FAQ articles have no page of their own; they collect into the FAQ hub.
        if a.get("type") == "FAQ":
            faq_items.append({**a, "_body": body})
            new_pages[a["page_id"]] = {"slug": a["slug"], "path": FAQ_HUB, "type": "FAQ"}
            print(f"  faq   {a['slug']}")
            continue

        markdown = render_markdown(a, body)
        rel = f"{a['category_slug']}/{a['slug']}.md"
        dest = DOCS / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(markdown, encoding="utf-8")
        written_paths.add(dest)

        a["_relpath"] = rel
        new_pages[a["page_id"]] = {"slug": a["slug"], "path": rel}
        by_category.setdefault(a["category_slug"], []).append(a)
        print(f"  wrote {rel}")

    # FAQ hub (generated from all FAQ articles at once)
    generate_faq_hub(faq_items)

    # ---- Per-category .pages (nav order via awesome-pages) --------------------------
    for cat_slug, arts in by_category.items():
        arts_sorted = sorted(arts, key=lambda a: (a["order"], a["slug"]))
        pages_yaml = {
            "title": arts_sorted[0]["category"],
            "nav": [f"{a['slug']}.md" for a in arts_sorted],
        }
        (DOCS / cat_slug / ".pages").write_text(
            yaml.safe_dump(pages_yaml, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    # Root nav: index first, categories, FAQ hub last
    write_root_nav()

    # Regenerate the landing page from the categories that now exist (data-driven).
    generate_homepage()

    # ---- Removals + redirects (brief §3.5) -----------------------------------------
    redirects = {}
    if REDIRECTS_PATH.exists():
        redirects = yaml.safe_load(REDIRECTS_PATH.read_text(encoding="utf-8")) or {}
    removed = [pid for pid in old_pages if pid not in new_pages]
    for pid in removed:
        old = old_pages[pid]
        old_path = old["path"]
        # FAQ items live in the regenerated hub — never a file to delete; redirect the
        # old anchor to the hub.
        if old.get("type") == "FAQ" or old_path == FAQ_HUB:
            redirects.setdefault(f"/preguntas-frecuentes/#{old['slug']}", "/preguntas-frecuentes/")
            print(f"  removed FAQ {old['slug']} (regenerated in hub)")
            continue
        f = DOCS / old_path
        if f.exists():
            f.unlink()
        # /category/slug.md -> /category/slug/  (MkDocs directory URL)
        url = "/" + re.sub(r"\.md$", "/", old_path).replace("index/", "")
        redirects.setdefault(url, "/")  # never shrinks; editor can retarget
        print(f"  removed {old_path} (redirect {url} -> /)")

    # Prune now-empty category directories (and their .pages)
    for cat_dir in DOCS.iterdir():
        if cat_dir.is_dir() and cat_dir.name != "assets":
            md_files = list(cat_dir.glob("*.md"))
            if not md_files:
                for leftover in cat_dir.iterdir():
                    leftover.unlink()
                cat_dir.rmdir()

    # ---- Write manifest + redirects -------------------------------------------------
    manifest = {
        "count": len(articles),
        "pages": dict(sorted(new_pages.items())),
    }
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if redirects:
        REDIRECTS_PATH.write_text(
            yaml.safe_dump(redirects, allow_unicode=True, sort_keys=True),
            encoding="utf-8",
        )

    # ---- Report ---------------------------------------------------------------------
    print(f"\nSynced {len(articles)} published article(s) across {len(by_category)} categor(y/ies).")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings[:50]:
            print(f"  - {w}")
        if len(warnings) > 50:
            print(f"  ... and {len(warnings) - 50} more")


if __name__ == "__main__":
    main()
