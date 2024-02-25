const checkbox = document.getElementById("mode-toggle");
const htmlTag = document.documentElement;
const theme = sessionStorage.getItem("theme");
const message = document.querySelector(".message");

if (theme) {
  if (theme === "dark") {
    htmlTag.classList.add("dark");
    checkbox.checked = true;
  } else {
    htmlTag.classList.remove("dark");
    checkbox.checked = false;
  }
}

checkbox.addEventListener("change", function () {
  if (this.checked) {
    htmlTag.classList.add("dark");
    sessionStorage.setItem("theme", "dark");
  } else {
    htmlTag.classList.remove("dark");
    sessionStorage.removeItem("theme");
  }
});

setTimeout(() => {
  if (message) {
    message.remove();
  }
}, 5000);
