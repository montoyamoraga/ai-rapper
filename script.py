# import libraries
import mido
import time
import rtmidi
import os

# fileLil = open("lil-wayne.txt", "r")
# linesLil = fileLil.read().split("\n")

# content = open("lil-wayne.txt").readlines()

textLil = [line.rstrip("\n") for line in open('lil-wayne.txt')]

textKendrick = [line.rstrip("\n") for line in open('kendrick-lamar.txt')]

voiceLil = " -v Alex "
voiceKendrick = " -v Fred "

minLength = min(len(textKendrick), len(textLil))

counter = 0

while True:
    lineLil = textLil[counter]
    os.system("say " + voiceLil + lineLil)
    time.sleep(1.0)

    lineKendrick = textKendrick[counter]
    os.system("say " + voiceKendrick + lineKendrick)
    time.sleep(1.0)

    counter = counter + 1
    counter = counter % minLength



# for line in ltextLil:
#     os.system("say " + line)
#     time.sleep(1.0)

# print(textLil)
#
# with open("lil-wayne.txt") as f:
#     lines = f.readlines()


# print(content)

# os.system("say 'hi moises 404'")

midiOut = rtmidi.MidiOut()

outPort = midiOut.open_virtual_port("python-midi")

outPorts = mido.get_output_names()

noteOn = [0x90, 60, 112];

while True:
    midiOut.send_message(noteOn);
    time.sleep(1.0)
