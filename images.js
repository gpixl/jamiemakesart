function swipe() {
  var largeImage = event.srcElement;
  var url = largeImage.getAttribute("src");
  var alttext = largeImage.getAttribute("alt");
  if (alttext == null) {
    alttext = "";
  }
  console.log(alttext);
  url = "/image.html?img=" + url + "&alt=" + alttext;
  window.open(url, "_blank", "noopener, noreferrer");
}

function newWindow() {
  top.location.href = location.href;
}
