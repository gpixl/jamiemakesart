
icons = document.getElementsByClassName("icon");
for(i = 0; i < icons.length; i++) {
  icons[i].alt = " "
}

function hide() {
  event.target.style.display = "none";
}

function showele(ele) {
  if (ele) {
    window.location.hash = ele;
    ele = document.getElementById(ele);
    if (ele != null) {
      ele.style.display = "flex";
    }
  }
}

function copy(copyText,ele,returnText) {


   // Copy the text inside the text field
  navigator.clipboard.writeText(copyText);
  if (returnText.length > 1) {
    ele.textContent = returnText;
    ele.className = "copied"
  }

} 

showele(window.location.hash)