//import libraries
import gifAnimation.*;

//PImages Arrays to store gifs
PImage[] lil;
PImage[] kendrick;

// instance of Gif library 
Gif lilGif;
Gif kendrickGif;

// boolean to determine if you are showing or not gifs
boolean lilShow = false;
boolean kendrickShow = false;

void setup() {

  size(600, 600);

  // load gifs from data folder
  lilGif = new Gif(this, "./data/lil_wayne.gif");
  kendrickGif = new Gif(this, "./data/kendrick_lamar.gif");

  // make them loop
  lilGif.loop();
  kendrickGif.loop();
}

void draw() {
  background(255);

  //showing gif if needed
  if (lilShow) {
    image(lilGif, 0, 0);
  }

  if (kendrickShow) {
    image(kendrickGif, 0, 0);
  }

}

void keyPressed() {
  if (key == '1') {
    lilShow = true;
    kendrickShow = false;
  }
  else if(key == '2') {
    lilShow = false;
    kendrickShow = true;
  } else {
    lilShow = false;
    kendrickShow = false;
  }
}
