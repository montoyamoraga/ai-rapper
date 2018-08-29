import gifAnimation.*;

//playback gifs

//PImages to store gifs
PImage[] lil;
PImage[] kendrick;

Gif lilGif;
Gif kendrickGif;

boolean lilShow = false;
boolean kendrickShow = false;

void setup() {

  size(600, 600);
  
  lilGif = new Gif(this, "./data/lil_wayne.gif");
  kendrickGif = new Gif(this, "./data/kendrick_lamar.gif");
  
  lilGif.loop();
  kendrickGif.loop();
  
  lil = Gif.getPImages(this, "./data/lil_wayne.gif");
  kendrick = Gif.getPImages(this, "./data/kendrick_lamar.gif");
  
}

void draw() {
  background(255);
  
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
