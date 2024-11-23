function setup() {
   createCanvas(256, 256);
   noStroke();
 }
 
 function draw() {
   background(220);
   for(let x = 256; x >= 0; x -= 1){
     rect(0, 0, x, x);
     fill(x, 0, 0);
   }
 }