
var images = document.getElementsByTagName('img'); 
for (var i = 0; i < images.length; i++) {
  if (images[i].getAttribute("link") != null) {
    images[i].src = images[i].getAttribute("display").replace(".gif", ".png").replace("assets/", "assets/thumbnails/").replace(".jpg",".png");
  }
}

  var imageNodes = document.getElementsByTagName('img');
  for (var i=0; i<imageNodes.length; i++)
  {
    if (imageNodes[i].id != "main" && imageNodes[i].getAttribute("class") != "icon") {
      imageNodes[i].setAttribute("onclick","setimage(this);");
      imageNodes[i].setAttribute("class", "img");
    }

  }
  
  document.getElementById("show").style.display = "none";

function upscale() {
  
  resX = parseInt(document.getElementById("resolution").innerText.split("x")[1].split("(")[0]);

  if (document.getElementById('main').style.height == 'auto') {
    document.getElementById('main').style.cssText = 'height: 80vh; cursor:zoom-in;';
  } else {
    if (window.innerWidth >= resX) {
      document.getElementById('main').style.cssText = 'height: auto; cursor:zoom-out;';
    } else {
      window.open(document.getElementById('main').getAttribute("src"), "_blank", "noopener, noreferrer");
    }
  }


}

function setimage(thisElement) {

document.getElementById("show").style.display = "";

  var largeImage = thisElement;

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

  if (window.innerWidth < 800) {
    imageToSet.style.cssText = 'width: 100%; cursor:default;';
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

  window.scrollTo(0, 0);
  history.pushState({}, "", "#" +  largeImage.getAttribute("id"));
}


if (window.location.hash) {
  setimage(document.getElementById(window.location.hash.replace("#", "")))
}

function newWindow() {
  top.location.href = location.href;
}