# import libraries
# time for delays
import time
# os for sending commands to bash terminal
import os
# midi library
# pip3 install mido
import mido
# midi library
# pip3 install python-rtmidi
import rtmidi

# read .txt files and strip new line characters
textLil = [line.rstrip("\n") for line in open('lil-wayne.txt')]
textKendrick = [line.rstrip("\n") for line in open('kendrick-lamar.txt')]

# pick voices and rate for terminal
voiceLil = " -v Alex -r 200 "
voiceKendrick = " -v Fred -r 200 "

# calculate the length of shortest
lengthShortest = min(len(textKendrick), len(textLil))

# init counter
counter = 0

# create midi output
midiOut = rtmidi.MidiOut()
# create midi virtual port and make it output port
outPort = midiOut.open_virtual_port("python-midi")

# create messages for showing different
midiLil = [0x90, 60, 112];
midiKendrick = [0x90, 61, 112];

# infinite loop
while True:
    # get next lyrics
    lineLil = textLil[counter]
    lineKendrick = textKendrick[counter]

    # say lil wayne lyric
    os.system("say " + voiceLil + lineLil)
    time.sleep(1.0)
    # send lil wayne midi message
    midiOut.send_message(midiLil);

    # say kendrick laamr lyric
    os.system("say " + voiceKendrick + lineKendrick)
    time.sleep(1.0)
    # send kendrick lamar midi message
    midiOut.send_message(midiKendrick);

    # update counter
    counter = counter + 1
    counter = counter % lengthShortest
