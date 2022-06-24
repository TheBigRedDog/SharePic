document.querySelector("#image_input").addEventListener("change", () => {
  let image_file = document.getElementById("image_input").files[0];
  let preview_url = window.URL.createObjectURL(image_file);
  document.getElementById("image_card_top").src = preview_url;
  console.log(image_file);
  console.log(window.URL.createObjectURL(image_file));
});
document.querySelector("#id_title").addEventListener("input", () => {
  let title = document.getElementById("id_title").value;
  document.getElementById("preview_card_title").textContent = title;
});
document.querySelector("#id_public").addEventListener("change", (checkbox) => {
  if (checkbox.target.checked) {
    document.getElementById("preview_card_public").textContent = "";
  } else {
    document.getElementById("preview_card_public").textContent = "Private";
  }
});
document.querySelector("#id_description").addEventListener("input", () => {
  let title = document.getElementById("id_description").value;
  document.getElementById("preview_card_description").textContent = title;
});
