document.querySelector("#image_input").addEventListener("change", () => {
  let image_file = document.getElementById("image_input").files[0];
  let preview_url = window.URL.createObjectURL(image_file);
  document.getElementById("image_card_top").src = preview_url;
  console.log(image_file);
  console.log(window.URL.createObjectURL(image_file));
});
