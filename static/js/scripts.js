const htmlTag = document.documentElement;
const modeCheckbox = document.getElementById("mode-toggle");
const message = document.querySelector(".message");

// util to get browser cookie by name
const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie != "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};

/* 
Toggle theme API call 
Note 'content-type' automatically set if using FormData
*/
const setTheme = (theme) => {
  const formData = new FormData();
  formData.append("theme", theme);
  fetch("/theme", {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: formData,
  }).catch((e) => console.log(e));
};

// Dark mode client toggle
modeCheckbox.addEventListener("change", function () {
  if (this.checked) {
    htmlTag.classList.add("dark");
    setTheme("dark");
  } else {
    htmlTag.classList.remove("dark");
    setTheme("");
  }
});

// Timeout to remove flash messages
setTimeout(() => {
  if (message) {
    message.remove();
  }
}, 7000);
