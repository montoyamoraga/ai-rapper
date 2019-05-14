// function for storing background color
let backgroundColor;

// variables for storing rapper images
let rapperKendrickLamar;
let rapperLilWayne;

// variable for speech
let speech = null;

// variables for tempo
let tempo = 100;

// variables for startup
let hasStarted = false;

// variable for alternating between rappers
// true is left, false is right
let whichRapper = false;

// function for loading assets
function preload() {
  rapperKendrickLamar = loadImage("./assets/kendrick-lamar.png");
  rapperLilWayne = loadImage("./assets/lil-wayne.png");
}

function setup() {
  // create fullscreen canvas
  createCanvas(windowWidth, windowHeight);

  // define background color
  backgroundColor = color("#D10B6C");

  // setup text alignment
  textAlign(CENTER);

  //setup image alignment
  imageMode(CENTER);

  // initialize p5 speech
  speech = new p5.Speech();

}

function draw() {

  // paint background
  background(backgroundColor);

  // credits
  textSize(32);
  text("ai rapper", width/2, 10*height/100);
  textSize(10);
  text("moises404 x montoyamoraga", width/2, 15*height/100);

  if (whichRapper) {
    effectSemiTransparent();
    image(rapperLilWayne, 1*width/4, height/2);
    effectFullSolid();
    image(rapperKendrickLamar, 3*width/4, height/2);
  } else {
    effectFullSolid();
    image(rapperLilWayne, 1*width/4, height/2);
    effectSemiTransparent();
    image(rapperKendrickLamar, 3*width/4, height/2);
  }
}

function effectSemiTransparent() {
  tint(255, 255/2);
}

function effectFullSolid() {
  tint(255, 255);
}

// callback when window is resized
function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}

function rap(speech, rapper, text, rapper) {
  speech.speak(text);
}

function keyPressed() {
  // TODO: make this dependent on beat tempo
  setInterval(rap(speech,"kendrick", "yo moises"), 1000);
}

// function for alternating rapper
function alternateRapper() {
  whichRapper = !whichRapper;
}

// tempo alternate
// TODO: make this dependent on beat tempo
window.setInterval(alternateRapper, 1000);
