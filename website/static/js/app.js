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
        index / 7 + 0.4
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

const cart = () => {
  var updateBtns = document.getElementsByClassName("update-cart");

  for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
      var productId = this.dataset.product;
      var action = this.dataset.action;
      console.log("productId:", productId, "action:", action);

      console.log("USER:", user);
      if (user === "AnonymousUser") {
        console.log("Not logged in");
      } else {
        updateUserOrder(productId, action);
      }
    });
  }

  function updateUserOrder(productId, action) {
    console.log("User is logged in, sending data...");

    var url = "/update_item/";

    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({'productId': productId, 'action': action }),
    })
      .then((response) => {
        return response.json();
      })

      .then((data) => {
        console.log('data:', data)
        location.reload()
      });
  }
};

const app = () => {
  navSlide();
  cart();
};

app();
