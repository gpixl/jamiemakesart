
var images = document.getElementsByTagName('img'); 
for (var i = 0; i < images.length; i++) {
  if (images[i].getAttribute("display") != null) {
    images[i].src = images[i].getAttribute("display").replace(".gif", ".png").replace("assets/", "assets/thumbnails/").replace(".jpg",".png")
  }
}

  var imageNodes = document.getElementsByTagName('img');
  for (var i=0; i<imageNodes.length; i++)
  {
    if (imageNodes[i].id != "main") {
      imageNodes[i].setAttribute("onclick","setimage();");
      imageNodes[i].setAttribute("class", "img");
    }

  }
  
  document.getElementById("show").style.display = "none";

function upscale() {
  
  if (window.innerWidth >= 500) {
    if (document.getElementById('main').style.height == 'auto') {
      document.getElementById('main').style.cssText = 'height: 80vh; cursor:zoom-in;';
    } else {
      document.getElementById('main').style.cssText = 'height: auto; cursor:zoom-out;';
    }
  } else {
    window.open(document.getElementById('main').getAttribute("src"), "_blank", "noopener, noreferrer");
  }


}

function setimage() {

document.getElementById("show").style.display = "";

  var largeImage = event.srcElement;

  window.scrollTo(0, 0);
  var imageToSet = document.getElementById("main");

  var height = largeImage.naturalHeight;

  var slink = document.getElementById("link");
  var linkText = largeImage.getAttribute("link").replace("https://","");
  link.href = largeImage.getAttribute("link");
  if (linkText.length > 35) {
    link.innerText = linkText.substring(0, 34) + "...";
  } else {
      link.innerText = linkText;
  }


  imageToSet.style.cssText = 'height: 80vh; width: auto; cursor:zoom-in;';

  if (window.innerWidth < 500) {
    imageToSet.style.cssText = 'height: auto; cursor:default;';
  }

  var src = largeImage.getAttribute("display");
  imageToSet.setAttribute("src", src);
  var alt = largeImage.getAttribute("alt");
  imageToSet.setAttribute("alt", alt);
  document.getElementById("maintext").innerText = largeImage.getAttribute("alt");
  var width = imageToSet.naturalWidth;
  var height = imageToSet.naturalHeight;
  document.getElementById("resolution").innerText = largeImage.getAttribute("dimensions") + "\n(Click image to view original size)";
  document.getElementById("date").innerText = largeImage.getAttribute("date");
}


function newWindow() {
  top.location.href = location.href;
}