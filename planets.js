

let theButton = document.getElementById("startstars");
theButton.addEventListener("click", startStars);

function startStars() {
        
  
  theButton.style.display = "none";
  
  if (starInterval) {
clearInterval(starInterval);
  }
        
      var canvas = document.getElementById("canvas");
      var ctx = canvas.getContext("2d");
      canvas.width = canvas.clientWidth;
      canvas.height = canvas.clientHeight;
        
      var planets = {},
          planetIndex = 0,
          settings = {
            planetSize: 2,
            density: 15
          };

      function Planet() {
        
        console.log("created");
        
        this.dist = (Math.random() * 1000) / (planetIndex / 3);
        this.speed = (1 / this.dist) * 1000 * (planetIndex / 10);
        if (Math.random > 0.9) {
          this.speed *= -1;
        }
        this.size = ((Math.random() * 1) + 2) / ((planetIndex / 2) + 1);
        
      
        
        this.rotspeed = (Math.random() - 0.5) * 1;
        
        this.color = Math.floor(Math.random()*16777215).toString(16);
        
        this.points = 4 + getRandomInt(6);
        
        this.x = canvas.width / 2;
        this.y = canvas.height / 2;
        
        planetIndex ++;
        planets[planetIndex] = this;
        this.id = planetIndex;
        if (planetIndex > 0) {
          this.parent = planets[getRandomInt(planetIndex)]; 
        }
      }
        
        
        for (var i = 0; i < settings.density; i++) {
            new Planet();
        }
        
      Planet.prototype.draw = function() {
        
      
        if (this.parent) {
          this.x = this.parent.x;
          this.y = this.parent.y;
          
          
          var rottime = (Date.now() * 0.005 * this.rotspeed);
          var time = (Date.now() * 0.005 * this.speed);
          
          this.x += this.dist * Math.cos(time * Math.PI / 180);
          this.y += (this.dist * Math.sin(time * Math.PI / 180) / 1);
          
          
        ctx.strokeStyle="#" + this.color;
        ctx.beginPath();
        ctx.ellipse(this.parent.x, this.parent.y, this.dist, this.dist / 1, 0, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.closePath();
          
        var offset = [this.x, this.y];
ctx.fillStyle="#" + this.color;
var penta = generateStarTriangles(this.points, this.size * 25, rottime);
drawObj(ctx, penta, offset, true);
ctx.closePath();
        } else {
        this.x = canvas.width / 2;
        this.y = canvas.height / 2;
        }
        
      } 
        
        
        
        
        
        
        
        //https://stackoverflow.com/questions/14580033/algorithm-for-drawing-a-5-point-star
      function rotate2D(vecArr, byRads) {
    var mat = [ [Math.cos(byRads), -Math.sin(byRads)], 
                [Math.sin(byRads), Math.cos(byRads)] ];
    var result = [];
    for(var i=0; i < vecArr.length; ++i) {
        result[i] = [ mat[0][0]*vecArr[i][0] + mat[0][1]*vecArr[i][1],
                      mat[1][0]*vecArr[i][0] + mat[1][1]*vecArr[i][1] ];
    }
    return result;
}
     
        function generateStarTriangles(numPoints, r, rot) {
    var triangleBase = r * Math.tan(Math.PI/numPoints);
    var triangle = [ [0,r], [triangleBase/2,0], [-triangleBase/2,0], [0,r] ];
    var result = [];
    for(var i = 0; i < numPoints; ++i) {
       result[i] = rotate2D(triangle, i*(2*Math.PI/numPoints) + rot);
    }
    return result;
}
        
        
        function drawObj(ctx, obj, offset, flipVert) {
   var sign=flipVert ? -1 : 1;
   for(var objIdx=0; objIdx < obj.length; ++objIdx) {
      var elem = obj[objIdx];
      ctx.moveTo(elem[0][0] + offset[0], sign*elem[0][1] + offset[1]);
      ctx.beginPath();
      for(var vert=1; vert < elem.length; ++vert) {
        ctx.lineTo(elem[vert][0] + offset[0], sign*elem[vert][1] + offset[1]);
      }
      ctx.fill();
   }
}
        
        
        
        
        
        
        
        
      function getRandomInt(max) {
      return Math.floor(Math.random() * max);
      }
        
     var starInterval = setInterval(renderStars, 30);
  
  
  function renderStars() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
            canvas.width = canvas.clientWidth;
      canvas.height = canvas.clientHeight;

        for (var i in planets) {
          planets[i].draw();
        }}
      
      }