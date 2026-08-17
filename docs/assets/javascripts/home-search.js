/* Make the hero search box open Material's real search overlay.
   Uses document$ (Material's RxJS stream) so it re-binds after instant navigation. */
document$.subscribe(function () {
  var hero = document.querySelector(".sc-hero__search");
  if (!hero || hero.dataset.bound) return;
  hero.dataset.bound = "1";

  function openSearch() {
    var toggle = document.getElementById("__search");
    if (toggle) toggle.checked = true;              // opens overlay (mobile) / reveals (desktop)
    var input = document.querySelector(".md-search__input");
    if (input) { input.focus(); input.select && input.select(); }
  }

  hero.addEventListener("click", openSearch);
  hero.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " " || e.key === "/") { e.preventDefault(); openSearch(); }
  });
});
