function copy(copyText,ele) {


   // Copy the text inside the text field
  navigator.clipboard.writeText(copyText);
  ele.textContent = "copied " + copyText;
  ele.className = "copied"

} 