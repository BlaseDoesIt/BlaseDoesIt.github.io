// Language toggle. Each page defines window.AR (Arabic strings keyed by data-i18n)
// and window.TITLES = {en, ar}. English is read from the page itself.
(function(){
  const ar = window.AR || {};
  const en = {};
  const nodes = document.querySelectorAll("[data-i18n]");
  nodes.forEach(el => { if (!(el.dataset.i18n in en)) en[el.dataset.i18n] = el.innerHTML; });
  const btn = document.getElementById("langBtn");

  function setLang(l){
    const d = l === "ar" ? ar : en;
    document.documentElement.lang = l;
    document.documentElement.dir = l === "ar" ? "rtl" : "ltr";
    nodes.forEach(el => { const v = d[el.dataset.i18n]; if (v != null) el.innerHTML = v; });
    btn.textContent = l === "ar" ? "English" : "العربية";
    if (window.TITLES) document.title = window.TITLES[l];
    try { localStorage.setItem("lang", l); } catch (e) {}
  }
  btn.addEventListener("click", () => setLang(document.documentElement.lang === "ar" ? "en" : "ar"));

  let start = "en";
  try {
    const q = new URLSearchParams(location.search).get("lang");
    start = q || localStorage.getItem("lang") || ((navigator.language || "").startsWith("ar") ? "ar" : "en");
  } catch (e) {}
  if (start === "ar") setLang("ar");
})();
