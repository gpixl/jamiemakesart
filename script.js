icons = document.getElementsByClassName("icon");
for(i = 0; i < icons.length; i++) {
  icons[i].alt = " "
}

function hide() {
  event.target.style.display = "none";
}

function copy(copyText,ele) {


   // Copy the text inside the text field
  navigator.clipboard.writeText(copyText);
  ele.textContent = "copied " + copyText;
  ele.className = "copied"

} 