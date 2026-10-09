/* El nombre del sitio en la cabecera lleva a la portada.

   Material solo muestra el logo (que ya enlaza a la portada) en pantallas
   anchas: en el celular quedan la hamburguesa y el texto "Centro de Ayuda",
   y desde un artículo no hay forma de volver al inicio sin el botón atrás.

   Envolvemos el texto en un <a> de verdad —no un handler de click— para que
   funcione el clic del medio, "abrir en pestaña nueva" y el teclado. El
   destino sale del href del logo, que MkDocs ya escribe relativo a la página.

   Usa document$ (el stream de Material) porque la navegación instantánea
   reemplaza la cabecera en cada visita; por eso también es idempotente. */
document$.subscribe(function () {
  var topic = document.querySelector(".md-header__title .md-header__topic .md-ellipsis");
  if (!topic || topic.querySelector("a")) return;

  var logo = document.querySelector(".md-header__button.md-logo");
  var link = document.createElement("a");
  link.href = logo ? logo.getAttribute("href") : "/";
  link.className = "sc-header-home";
  link.textContent = topic.textContent.trim();

  topic.textContent = "";
  topic.appendChild(link);
});
