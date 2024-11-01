var imageNodes = document.getElementsByTagName('img');
for (var i=0; i<imageNodes.length; i++)
{          
    imageNodes[i].setAttribute("onclick","swipe();");
}
  
function swipe() {
  var largeImage = event.srcElement;
  var url = largeImage.getAttribute("src");
  var alttext = largeImage.getAttribute("alt");
  var link = largeImage.getAttribute("link");
  if (alttext == null) {
    alttext = "";
  }
  console.log(alttext);
  url = url.replace("feed_thumbnail", "feed_fullsize")
  url = "/art/viewer.html?img=" + url + "&alt=" + alttext + "&link=" + link;
  window.open(url, "_blank", "noopener, noreferrer");
}

function newWindow() {
  top.location.href = location.href;
}