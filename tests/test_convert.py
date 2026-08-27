#!/usr/bin/env python3
"""Offline unit tests for the Notion->markdown converter.

No network: a FakeNotion feeds canned block children so we can prove the fragile
conversion logic deterministically. Run:  python tests/test_convert.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import sync_notion as sn  # noqa: E402


class FakeNotion:
    """Stands in for the HTTP client; returns pre-seeded children by block id."""

    def __init__(self, children_by_id=None):
        self.children_by_id = children_by_id or {}
        self.s = None  # not used in these tests

    def block_children(self, block_id):
        return self.children_by_id.get(block_id, [])


def rt(text, **ann):
    return {"plain_text": text, "annotations": ann, "href": ann.pop("href", None)}


def block(bt, **data):
    b = {"type": bt, "id": data.pop("id", f"blk-{bt}"), "has_children": data.pop("has_children", False)}
    b[bt] = data
    return b


def convert(blocks, fake=None):
    conv = sn.BlockConverter(fake or FakeNotion())
    lines = conv.convert(blocks)
    return sn.collapse_blank_lines("\n".join(lines)).strip(), conv


def check(name, cond):
    if not cond:
        raise AssertionError(f"FAILED: {name}")
    print(f"  ok  {name}")


def test_rich_text():
    md = sn.rich_to_md([rt("hola "), rt("mundo", bold=True), rt(" y ", ), rt("code", code=True)])
    check("bold+code inline", md == "hola **mundo** y `code`")
    link = sn.rich_to_md([{"plain_text": "aquí", "annotations": {}, "href": "https://x.io"}])
    check("link rendered", link == "[aquí](https://x.io)")


def test_headings_shift():
    md, _ = convert([block("heading_1", rich_text=[rt("Título")])])
    check("notion h1 -> markdown h2", md == "## Título")
    md, _ = convert([block("heading_2", rich_text=[rt("Sub")])])
    check("notion h2 -> markdown h3", md == "### Sub")


def test_lists_and_code():
    md, _ = convert([
        block("bulleted_list_item", rich_text=[rt("uno")]),
        block("numbered_list_item", rich_text=[rt("dos")]),
        block("code", language="python", rich_text=[rt("print(1)")]),
    ])
    check("bullet", "- uno" in md)
    check("numbered", "1. dos" in md)
    check("code fence", "```python" in md and "print(1)" in md)


def test_callout_and_quote_and_divider():
    md, _ = convert([
        block("callout", rich_text=[rt("cuidado")], icon={"emoji": "⚠️"}),
        block("quote", rich_text=[rt("cita")]),
        block("divider"),
    ])
    # El emoji del callout elige el tipo de admonition (y con él su icono y color);
    # ya no se copia al título, que traía dos iconos encimados.
    check("callout -> admonition", '!!! warning "Atención"' in md and "cuidado" in md)
    check("callout sin emoji en el título", "⚠️" not in md)
    check("quote", "> cita" in md)
    check("divider", "---" in md)


def test_callout_emoji_desconocido_cae_en_note():
    md, _ = convert([block("callout", rich_text=[rt("algo")], icon={"emoji": "🦊"})])
    check("callout desconocido -> note", '!!! note "Nota"' in md)


def test_callout_emoji_sin_selector_de_variacion():
    # Notion puede guardar ⚠ como U+26A0 pelado, sin el U+FE0F con el que se tipeó
    # la clave; sin normalizar caería en silencio a `note`.
    md, _ = convert([block("callout", rich_text=[rt("ojo")], icon={"emoji": "⚠"})])
    check("callout U+26A0 pelado -> warning", '!!! warning "Atención"' in md)


def test_callout_cuerpo_multilinea_queda_indentado():
    md, _ = convert([block("callout", rich_text=[rt("primera\nsegunda")], icon={"emoji": "💡"})])
    check("primera línea indentada", "    primera" in md)
    check("segunda línea indentada", "    segunda" in md)
    check("ninguna línea escapa de la admonition", "\nsegunda" not in md.replace("\n    segunda", ""))


def test_image_collected_and_rewritten():
    img = block("image", type="file", file={"url": "https://s3.example.com/x/pic.png?sig=abc"},
                caption=[rt("un gato")])
    md, conv = convert([img])
    check("image markdown", "![un gato](https://s3.example.com/x/pic.png?sig=abc)" in md)
    check("image job collected", len(conv.image_jobs) == 1)
    check("image kind recorded", conv.image_jobs[0][2] == "file")


class FakeResponse:
    def __init__(self, content):
        self.content = content

    def raise_for_status(self):
        pass


class FakeSession:
    """Stands in for requests.Session; serves canned bytes for any URL."""

    def __init__(self, content):
        self._content = content

    def get(self, url, timeout=None):
        return FakeResponse(self._content)


class FailingSession:
    """Every request raises, like a dead host or an expired link."""

    def get(self, url, timeout=None):
        raise RuntimeError("boom")


class FlakySession:
    """Fails the first request, then serves the payload."""

    def __init__(self, content):
        self._content = content
        self.calls = 0

    def get(self, url, timeout=None):
        self.calls += 1
        if self.calls == 1:
            raise RuntimeError("transient")
        return FakeResponse(self._content)


def test_rehost_presigned_failure_is_fatal():
    import tempfile

    url = "https://s3.example.com/x/rota.png?X-Amz-Signature=abc"
    old_docs, old_backoff = sn.DOCS, sn.RETRY_BACKOFF
    sn.RETRY_BACKOFF = (0, 0)
    sn.rehost_failures.clear()
    with tempfile.TemporaryDirectory() as td:
        sn.DOCS = Path(td)
        try:
            out = sn.rehost_images(f"![x]({url})", "articulo", [(url, "x", "file")], FailingSession())
        finally:
            sn.DOCS, sn.RETRY_BACKOFF = old_docs, old_backoff
        check("md unchanged on presigned failure", out == f"![x]({url})")
        check("failure recorded as fatal", len(sn.rehost_failures) == 1 and "articulo" in sn.rehost_failures[0])
        check("unsigned url in failure report", "https://s3.example.com/x/rota.png" in sn.rehost_failures[0])
        check("no file cached", not any(p.is_file() for p in Path(td).rglob("*")))
    sn.rehost_failures.clear()


def test_rehost_external_failure_only_warns():
    import tempfile

    url = "https://blog.example.com/diagrama.png"
    old_docs, old_backoff = sn.DOCS, sn.RETRY_BACKOFF
    sn.RETRY_BACKOFF = (0, 0)
    sn.rehost_failures.clear()
    n_warn = len(sn.warnings)
    with tempfile.TemporaryDirectory() as td:
        sn.DOCS = Path(td)
        try:
            out = sn.rehost_images(f"![x]({url})", "articulo", [(url, "x", "external")], FailingSession())
        finally:
            sn.DOCS, sn.RETRY_BACKOFF = old_docs, old_backoff
        check("external url kept", out == f"![x]({url})")
        check("no fatal failure for external", len(sn.rehost_failures) == 0)
        check("warning emitted for external", len(sn.warnings) == n_warn + 1)
    del sn.warnings[n_warn:]


def test_rehost_retries_transient_failure():
    import io
    import tempfile
    from PIL import Image

    buf = io.BytesIO()
    Image.new("RGB", (8, 8), (10, 20, 30)).save(buf, "PNG")
    url = "https://s3.example.com/x/ok.png?X-Amz-Signature=abc"
    sess = FlakySession(buf.getvalue())
    old_docs, old_backoff = sn.DOCS, sn.RETRY_BACKOFF
    sn.RETRY_BACKOFF = (0, 0)
    n_fail = len(sn.rehost_failures)
    with tempfile.TemporaryDirectory() as td:
        sn.DOCS = Path(td)
        try:
            out = sn.rehost_images(f"![x]({url})", "articulo", [(url, "x", "file")], sess)
        finally:
            sn.DOCS, sn.RETRY_BACKOFF = old_docs, old_backoff
        check("retried after transient failure", sess.calls == 2)
        check("md rewritten after retry", "/assets/articulo/" in out and out.endswith(".webp)"))
        check("no failure recorded after retry", len(sn.rehost_failures) == n_fail)


def test_rehost_images_recompresses_to_webp():
    import io
    import tempfile
    from PIL import Image

    buf = io.BytesIO()
    Image.new("RGBA", (40, 20), (200, 30, 30, 255)).save(buf, "PNG")
    url = "https://s3.example.com/x/shot.png?X-Amz-Signature=abc"
    md = f"![captura]({url})"
    digest = sn.hashlib.sha256(b"https://s3.example.com/x/shot.png").hexdigest()[:12]
    rel = f"assets/articulo/{digest}.webp"

    old_docs = sn.DOCS
    with tempfile.TemporaryDirectory() as td:
        sn.DOCS = Path(td)
        try:
            out = sn.rehost_images(md, "articulo", [(url, "captura", "file")], FakeSession(buf.getvalue()))
        finally:
            sn.DOCS = old_docs
        check("markdown rewritten to .webp asset", out == f"![captura](/{rel})")
        data = (Path(td) / rel).read_bytes()
        check("webp container written", data[:4] == b"RIFF" and data[8:12] == b"WEBP")
        img = Image.open(Path(td) / rel)
        check("dimensions preserved", img.size == (40, 20))


def test_rehost_images_non_raster_kept_verbatim():
    import tempfile

    gif = b"GIF89a\x01\x00\x01\x00\x00\x00\x00;"
    url = "https://s3.example.com/x/anim.gif?X-Amz-Signature=abc"
    digest = sn.hashlib.sha256(b"https://s3.example.com/x/anim.gif").hexdigest()[:12]
    rel = f"assets/articulo/{digest}.gif"

    old_docs = sn.DOCS
    with tempfile.TemporaryDirectory() as td:
        sn.DOCS = Path(td)
        try:
            out = sn.rehost_images(f"![g]({url})", "articulo", [(url, "g", "file")], FakeSession(gif))
        finally:
            sn.DOCS = old_docs
        check("gif markdown rewritten", out == f"![g](/{rel})")
        check("gif bytes untouched", (Path(td) / rel).read_bytes() == gif)


def test_table():
    rows = [
        {"type": "table_row", "id": "r1", "table_row": {"cells": [[rt("A")], [rt("B")]]}},
        {"type": "table_row", "id": "r2", "table_row": {"cells": [[rt("1")], [rt("2")]]}},
    ]
    fake = FakeNotion({"tbl": rows})
    tbl = block("table", id="tbl", has_children=True, has_column_header=True)
    md, _ = convert([tbl], fake)
    check("table header row", "| A | B |" in md)
    check("table separator", "| --- | --- |" in md)
    check("table data row", "| 1 | 2 |" in md)


def test_helpers():
    check("slugify accents", sn.slugify("Configuración Básica") == "configuracion-basica")
    check("url_without_query", sn.url_without_query("https://a.io/p.png?x=1") == "https://a.io/p.png")
    check("guess_ext", sn.guess_ext("https://a.io/p.PNG?x=1") == ".png")


def test_extract_article():
    page = {
        "id": "pg1",
        "last_edited_time": "2026-01-01T00:00:00Z",
        "properties": {
            "Name": {"type": "title", "title": [rt("Cómo empezar")]},
            "Slug": {"type": "rich_text", "rich_text": [rt("como-empezar")]},
            "Category": {"type": "select", "select": {"name": "Primeros pasos"}},
            "Order": {"type": "number", "number": 10},
            "Status": {"type": "select", "select": {"name": "Published"}},
            "Aliases": {"type": "rich_text", "rich_text": [rt("no sé por dónde empezar")]},
        },
    }
    a = sn.extract_article(page)
    check("title", a["title"] == "Cómo empezar")
    check("slug", a["slug"] == "como-empezar")
    check("category_slug", a["category_slug"] == "primeros-pasos")
    check("order", a["order"] == 10)
    check("status", a["status"] == "Published")
    check("aliases", "empezar" in a["aliases"])


def test_render_markdown_frontmatter():
    art = {"title": "T", "slug": "s", "order": 20, "aliases": "x, y"}
    out = sn.render_markdown(art, "cuerpo")
    check("frontmatter title", "title: T" in out)
    check("frontmatter slug", "slug: s" in out)
    check("h1 injected", "# T" in out)
    check("hidden aliases block", 'class="doc-aliases"' in out and "x, y" in out)


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    print(f"Running {len(tests)} conversion test group(s):")
    for t in tests:
        t()
    print("\nALL CONVERSION TESTS PASSED")


if __name__ == "__main__":
    main()
