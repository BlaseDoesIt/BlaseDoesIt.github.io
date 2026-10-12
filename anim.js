// Plays the before/after flow animation when the map scrolls into view.
(function(){
  const flows = document.querySelectorAll(".flow");
  const play = f => {
    f.classList.add("in");
    const n = f.querySelectorAll(".node").length;
    // drop the stagger delays once the entrance is done so hovers react instantly
    setTimeout(() => f.classList.add("done"), n * 110 + 700);
  };
  if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) {
    flows.forEach(f => { f.classList.add("in", "done"); });
    return;
  }
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { play(e.target); io.unobserve(e.target); }
  }), {threshold: .25});
  flows.forEach(f => io.observe(f));
})();
