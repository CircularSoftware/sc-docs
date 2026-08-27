/* "¿Te resultó útil este artículo?" — un voto por artículo y por navegador.

   El voto se manda al endpoint configurado en mkdocs.yml (extra.feedback_endpoint).
   Va como texto plano y con mode:"no-cors" porque el destino previsto es un Web App
   de Apps Script, que no devuelve cabeceras CORS. El payload no identifica a la
   persona: solo qué página votó, si fue sí o no, y cuándo (como en cualquier
   request HTTP, el endpoint igual ve IP y user-agent a nivel transporte).

   Trade-off asumido: el voto se marca como emitido en localStorage antes del POST,
   y con no-cors la respuesta es opaca, así que un POST fallido no se reintenta.
   Preferimos perder algún voto a bloquear o re-preguntar a la persona.

   Usa document$ (el stream de Material) para volver a enlazar después de cada
   navegación instantánea. */
document$.subscribe(function () {
  var box = document.querySelector(".sc-feedback");
  if (!box || box.dataset.bound) return;
  box.dataset.bound = "1";

  var page = box.dataset.page || location.pathname;
  var endpoint = box.dataset.endpoint || "";
  var key = "sc-feedback:" + page;
  var thanks = box.querySelector(".sc-feedback__thanks");
  var buttons = box.querySelectorAll(".sc-feedback__btn");

  function settle(value) {
    buttons.forEach(function (b) {
      b.disabled = true;
      b.classList.toggle("is-chosen", b.dataset.value === value);
    });
    if (thanks) thanks.hidden = false;
  }

  var previous = null;
  try { previous = localStorage.getItem(key); } catch (e) { /* modo privado */ }
  if (previous) { settle(previous); return; }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var value = btn.dataset.value;
      settle(value);
      try { localStorage.setItem(key, value); } catch (e) { /* modo privado */ }

      if (!endpoint) return;
      var payload = JSON.stringify({
        page: page,
        value: value,
        at: new Date().toISOString()
      });
      fetch(endpoint, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "text/plain;charset=utf-8" },
        body: payload,
        keepalive: true
      }).catch(function () { /* un voto perdido no rompe la página */ });
    });
  });
});
