function stickIt() {
  const header = document.querySelector(".custom-header");

  if (!header) return; // ✅ FIX (prevents crash)

  const top = header.offsetTop;

  if (window.scrollY > top) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

window.addEventListener("scroll", stickIt);