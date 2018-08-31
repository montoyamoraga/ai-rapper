
//import libraries
import gifAnimation.*;
import themidibus.*;

//PImages Arrays to store gifs
PImage[] lil;
PImage[] kendrick;

// instance of Gif library 
Gif lilGif;
Gif kendrickGif;

// boolean to determine if you are showing or not gifs
boolean lilShow = false;
boolean kendrickShow = false;

//MidiBus instances
MidiBus midiBus;

void setup() {

  size(480, 263);

  // load gifs from data folder
  lilGif = new Gif(this, "./data/lil_wayne.gif");
  kendrickGif = new Gif(this, "./data/kendrick_lamar.gif");

  // make them loop
  lilGif.loop();
  kendrickGif.loop();

  //list Midibus devices
  MidiBus.list();

  //create midiBus link
  //first number is input, second number is output
  //midiBus = new MidiBus(this, 1, 1);
  midiBus = new MidiBus(this, "python-midi", -1);
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
  } else if (key == '2') {
    lilShow = false;
    kendrickShow = true;
  } else {
    lilShow = false;
    kendrickShow = false;
  }
}


//receive a note on
void noteOn(Note note) {
  println("channel: " + note.channel());
  println("pitch: " + note.pitch());
  println("velocity: " + note.velocity());

  int currentNote = note.pitch();

  if (currentNote == 60) {
    lilShow = true;
    kendrickShow = false;
  } else if (currentNote == 61) {
    lilShow = false;
    kendrickShow = true;
  }
}
