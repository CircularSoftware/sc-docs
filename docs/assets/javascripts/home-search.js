/* Buscador del hero (portada).

   Antes era un botón que abría el buscador del header, así que el buscador grande
   de la página no buscaba nada. Ahora es un input de verdad: escribe en el input
   real de Material — que es el que tiene el índice — y copia los resultados debajo
   del hero. Copiamos en vez de mover el panel de Material para no romper su
   overlay, y como los resultados son <a href> simples, la copia sigue navegando.

   Usa document$ (el stream de Material) para re-enlazar tras cada navegación. */
document$.subscribe(function () {
  var wrap = document.querySelector(".sc-hero__search-wrap");
  if (!wrap || wrap.dataset.bound) return;
  wrap.dataset.bound = "1";

  var input = wrap.querySelector(".sc-hero__input");
  var panel = wrap.querySelector(".sc-hero__results");
  var list = wrap.querySelector(".sc-hero__results-list");
  var empty = wrap.querySelector(".sc-hero__results-empty");
  var real = document.querySelector(".md-search__input");
  var source = document.querySelector(".md-search-result__list");
  if (!input || !real || !source) return;

  function render() {
    var hasQuery = input.value.trim().length > 0;
    list.innerHTML = hasQuery ? source.innerHTML : "";
    // La portada indexa las tarjetas de categoría, así que aparece en casi toda
    // búsqueda sin aportar nada. La sacamos de la lista.
    list.querySelectorAll(".md-search-result__link").forEach(function (a) {
      var url = new URL(a.getAttribute("href"), location.href);
      if (url.pathname === "/" || url.pathname.endsWith("/index.html")) {
        var item = a.closest(".md-search-result__item") || a;
        item.remove();
      }
    });
    var hits = list.querySelectorAll(".md-search-result__link").length;
    empty.hidden = !hasQuery || hits > 0;
    panel.hidden = !hasQuery;
  }

  // Material rellena su lista de forma asíncrona (worker), así que observamos.
  new MutationObserver(render).observe(source, { childList: true, subtree: true });

  function forward() {
    real.value = input.value;
    // Material escucha keyup en su input, no input: sin esto no dispara la búsqueda.
    real.dispatchEvent(new KeyboardEvent("keyup", { bubbles: true, key: "a" }));
    render();
  }

  input.addEventListener("input", forward);

  input.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { input.value = ""; forward(); input.blur(); }
    if (e.key === "Enter") {
      var first = list.querySelector("a[href]");
      if (first) { e.preventDefault(); first.click(); }
    }
  });

  // La tecla "/" enfoca este buscador, no el del header.
  document.addEventListener("keydown", function (e) {
    if (e.key !== "/" || e.target === input) return;
    var tag = (e.target.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea") return;
    e.preventDefault();
    input.focus();
  });

  document.addEventListener("click", function (e) {
    if (!wrap.contains(e.target)) panel.hidden = true;
    else if (input.value.trim()) panel.hidden = false;
  });
});
