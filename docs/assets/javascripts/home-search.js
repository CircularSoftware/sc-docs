/* Buscador del hero (portada).

   Antes era un botón que abría el buscador del header, así que el buscador grande
   de la página no buscaba nada. Ahora es un input de verdad: escribe en el input
   real de Material — que es el que tiene el índice — y copia los resultados debajo
   del hero. Copiamos en vez de mover el panel de Material para no romper su
   overlay, y como los resultados son <a href> simples, la copia sigue navegando.

   Usa document$ (el stream de Material) para re-enlazar tras cada navegación.
   Ojo con la navegación instantánea: el hero se reconstruye en cada visita a la
   portada, pero el observer y los listeners sobre document sobreviven. Por eso se
   registran una sola vez y trabajan sobre `hero`, que apunta a los elementos
   vigentes (o es null fuera de la portada); si se re-registraran por visita se
   acumularían copias durante toda la sesión. */
var hero = null;

function renderHero() {
  if (!hero) return;
  var hasQuery = hero.input.value.trim().length > 0;
  hero.list.innerHTML = hasQuery ? hero.source.innerHTML : "";
  // La portada indexa las tarjetas de categoría, así que aparece en casi toda
  // búsqueda sin aportar nada. La sacamos de la lista.
  hero.list.querySelectorAll(".md-search-result__link").forEach(function (a) {
    var url = new URL(a.getAttribute("href"), location.href);
    if (url.pathname === "/" || url.pathname.endsWith("/index.html")) {
      var item = a.closest(".md-search-result__item") || a;
      item.remove();
    }
  });
  var hits = hero.list.querySelectorAll(".md-search-result__link").length;
  hero.empty.hidden = !hasQuery || hits > 0;
  hero.panel.hidden = !hasQuery;
}

document$.subscribe(function () {
  var wrap = document.querySelector(".sc-hero__search-wrap");
  if (!wrap) { hero = null; return; }

  var input = wrap.querySelector(".sc-hero__input");
  var panel = wrap.querySelector(".sc-hero__results");
  var list = wrap.querySelector(".sc-hero__results-list");
  var empty = wrap.querySelector(".sc-hero__results-empty");
  var real = document.querySelector(".md-search__input");
  var source = document.querySelector(".md-search-result__list");
  if (!input || !panel || !list || !empty || !real || !source) { hero = null; return; }

  hero = { wrap: wrap, input: input, panel: panel, list: list, empty: empty, source: source };

  if (!wrap.dataset.bound) {
    wrap.dataset.bound = "1";

    var forward = function () {
      real.value = input.value;
      // Material escucha keyup en su input, no input: sin esto no dispara la búsqueda.
      real.dispatchEvent(new KeyboardEvent("keyup", { bubbles: true, key: "a" }));
      renderHero();
    };

    input.addEventListener("input", forward);

    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { input.value = ""; forward(); input.blur(); }
      if (e.key === "Enter") {
        var first = list.querySelector("a[href]");
        if (first) { e.preventDefault(); first.click(); }
      }
    });
  }

  // Todo lo de acá para abajo vive fuera del hero y persiste entre navegaciones:
  // registrarlo una única vez por sesión.
  if (document.body.dataset.scHeroBound) return;
  document.body.dataset.scHeroBound = "1";

  // Material rellena su lista de forma asíncrona (worker), así que observamos.
  new MutationObserver(renderHero).observe(source, { childList: true, subtree: true });

  // La tecla "/" enfoca este buscador, no el del header.
  document.addEventListener("keydown", function (e) {
    if (!hero || e.key !== "/" || e.target === hero.input) return;
    var tag = (e.target.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea") return;
    e.preventDefault();
    hero.input.focus();
  });

  document.addEventListener("click", function (e) {
    if (!hero) return;
    if (!hero.wrap.contains(e.target)) hero.panel.hidden = true;
    else if (hero.input.value.trim()) hero.panel.hidden = false;
  });
});
