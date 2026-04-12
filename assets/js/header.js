// LOAD HEADER INTO ALL PAGES
// Detect if page is in pages/ folder
const isInPages = window.location.pathname.includes('/pages/');

fetch("header.html")
  .then(response => response.text())
  .then(data => {
    document.getElementById("header-container").innerHTML = data;

    // AFTER LOAD → ADD MOBILE MENU FUNCTION
    const toggle = document.getElementById("menu-toggle");
    const nav = document.querySelector(".header-nav");

    if (toggle && nav) {
      toggle.addEventListener("click", () => {
        nav.classList.toggle("active");
      });
    }
  })
  .catch(error => console.log("Header load error:", error));