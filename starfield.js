
canvas = document.getElementById("starfield");
const ctx = canvas.getContext("2d");


ctx.canvas.width = window.innerWidth;
ctx.canvas.height = window.innerHeight;

const star = {
  x:0.0,
  y:0.0,
  opacity: 255,
  distance: 1
}

stars = [];
stars.length = 500;

for (i = 0; i < stars.length; i++) {
  stars[i] = Object.create(star);
  stars[i].x = Math.random();
  stars[i].y = Math.random() * 1.5;
  stars[i].distance = Math.random();
}

let lasttime;
function repeatOften(timestamp) {

  delta = Math.round(timestamp - lasttime);

  lasttime = timestamp;
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (a = 0; a < stars.length; a++) {
    distance = stars[a].distance;
    // if (delta) {
    //   stars[a].y += ((1 * delta * distance) / 100000);
    // }

    distance *= 2;
    ctx.fillStyle = "white";

    scrollY = (window.pageYOffset / -5000) * distance;
    ctx.fillRect(stars[a].x * canvas.width, (stars[a].y + scrollY) * canvas.height , distance, distance);
    // if (stars[a].y > 1) stars[a].y = 0;
  }





  requestAnimationFrame(repeatOften);
}

requestAnimationFrame(repeatOften);