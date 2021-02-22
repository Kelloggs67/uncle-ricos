const navSlide = () => {
  const burger = document.querySelector(".burger img");
  const nav = document.querySelector(".nav-links");
  const navLinks = document.querySelectorAll(".nav-links li");
  const cancel = document.querySelector(".cancel");

  burger.addEventListener("click", () => {
    //Toggle Nav
    nav.classList.toggle("nav-active");
    burger.classList.toggle("burger-clicked");
    cancel.classList.toggle("cancel-display");

    //Animate Links
    navLinks.forEach((link, index) => {
      link.style.animation = `navLinkFade 0.5s ease forwards ${
        index / 7 + 0.6
      }s`;
    });
  });
  //Toggle Burger
  cancel.addEventListener("click", () => {
    nav.classList.toggle("nav-active");
    burger.classList.toggle("burger-clicked");
    cancel.classList.toggle("cancel-display");

    navLinks.forEach((link) => {
      link.style.animation = "";
    });
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.toggle("nav-active");
      burger.classList.toggle("burger-clicked");
      cancel.classList.toggle("cancel-display");

      navLinks.forEach((link) => {
        link.style.animation = "";
      });
    });
  });
};

navSlide();
