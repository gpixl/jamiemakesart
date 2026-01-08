var pixelRatio = 1;

var canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
ctx.fillStyle = "rgb(255,255,255)";
ctx.fillRect(0,0,255,255);
ctx.imageSmoothingEnabled = false;
let isDrawing = false;
var oldclientX = 0;
var oldclientY = 0;


//https://stackoverflow.com/questions/17130395/real-mouse-position-in-canvas
function getMousePos(canvas, evt) {
  var rect = canvas.getBoundingClientRect();
  return {
    x: evt.clientX - rect.left,
    y: evt.clientY - rect.top
  };
}

//start drawing
function startPosition(e) {
  oldclientX = e.clientX;
  oldclientY = e.clientY;
	isDrawing = true;
	draw(e);
}

//end drawing
function endPosition() {
	isDrawing = false;
	ctx.beginPath();
}

var imgData=ctx.getImageData(0,0,canvas.width,canvas.height);
var data=imgData.data;

function draw(e) {
	if (!isDrawing) return;
	ctx.strokeStyle =
		"rgb(0,0,0)"; 
		//pick the color
	ctx.lineWidth =
		"1"; 
		//Select the brush size

  var imgData=ctx.getImageData(0,0,canvas.width,canvas.height);
  data=imgData.data;
  bline(e.clientX - canvas.offsetLeft,e.clientY - canvas.offsetTop,oldclientX - canvas.offsetLeft,oldclientY - canvas.offsetTop)
	ctx.lineTo(
		e.clientX - canvas.offsetLeft,
		e.clientY - canvas.offsetTop
	);
  oldclientX = e.clientX;
  oldclientY = e.clientY;

    ctx.putImageData(imgData,0,0);
}


//https://stackoverflow.com/questions/25277023/complete-solution-for-drawing-1-pixel-line-on-html5-canvas
function pixelPerfectLine(x1, y1, x2, y2) {

  ctx.save();
  ctx.beginPath();
  thickness = 1;
  // Multiple your stroke thickness  by a pixel ratio!
  ctx.lineWidth = thickness * pixelRatio;

  ctx.strokeStyle = "Black";
  ctx.moveTo(getSharpPixel(thickness, x1/2), getSharpPixel(thickness, y1/2));
  ctx.lineTo(getSharpPixel(thickness, x2/2), getSharpPixel(thickness, y2/2));
  ctx.stroke();
  ctx.restore();
}

function getSharpPixel(thickness, pos) {

  if (thickness % 2 == 0) {
    return pos;
  }
  return pos + pixelRatio / 2;

}

function setPixel(x,y){
    var n=(y*canvas.width+x)*4;
    data[n]=255;
    data[n+1]=0;
    data[n+2]=0;
    data[n+3]=255;
}

// Refer to: http://rosettacode.org/wiki/Bitmap/Bresenham's_line_algorithm#JavaScript
function bline(x0, y0, x1, y1) {
  var dx = Math.abs(x1 - x0), sx = x0 < x1 ? 1 : -1;
  var dy = Math.abs(y1 - y0), sy = y0 < y1 ? 1 : -1; 
  var err = (dx>dy ? dx : -dy)/2;        
  while (true) {
    setPixel(x0,y0);
    if (x0 === x1 && y0 === y1) break;
    var e2 = err;
    if (e2 > -dx) { err -= dy; x0 += sx; }
    if (e2 < dy) { err += dx; y0 += sy; }
  }
}


//https://www.geeksforgeeks.org/javascript/create-a-paint-clone-using-html-css-javascript/

canvas
canvas
	.addEventListener('mousedown', startPosition);
canvas
	.addEventListener('mouseup', endPosition);
canvas
	.addEventListener('mousemove', draw);

function printData() {
  console.log(canvas.toDataURL())
}