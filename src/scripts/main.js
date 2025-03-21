import { initMobileMenu } from "./navigation.js";
import { initThemeToggle } from "./themeToggle.js";

// Initialisation au chargement de la page
document.addEventListener("DOMContentLoaded", () => {
  initMobileMenu();
  initThemeToggle();
});

// Gestion des transitions CSS
document.documentElement.classList.add("transitions-enabled");

// Prévention du FOUC (Flash of Unstyled Content)
document.documentElement.classList.remove("no-js");
