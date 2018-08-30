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

# create midi outputs
midiProcessing = rtmidi.MidiOut()
midiVocoder = rtmidi.MidiOut()

# check available ports to pick vocoder
available_ports = midiProcessing.get_ports()
print(available_ports)
vocoderIndex = 0

outProcessing = midiProcessing.open_virtual_port("python-midi")

outVocoder = midiVocoder.open_port(vocoderIndex)

# create messages for showing different
# 0x90 means 144 in decimal
# 144 is note on channel 1
midiLil = [0x90, 60, 112];
midiKendrick = [0x90, 61, 112];

# midi cc control of tune in roland vp-03 vocoder
tuneCC = 79
tuneLil = 0
tuneKendrick = 127
ccLil = [0xb0, 79, 0]
ccKendrick = [0xb0, 79, 127]


# infinite loop
while True:
    # get next lyrics
    lineLil = textLil[counter]
    lineKendrick = textKendrick[counter]

    # change tune via midi cc
    midiVocoder.send_message(ccLil)
    time.sleep(0.1)
    # send lil wayne midi message
    midiProcessing.send_message(midiLil);
    # say lil wayne lyric
    os.system("say " + voiceLil + lineLil)
    # wait
    time.sleep(1.0)

    # change tune via midi cc
    midiVocoder.send_message(ccKendrick)
    time.sleep(0.1)
    # send kendrick lamar midi message
    midiProcessing.send_message(midiKendrick);
    # say kendrick lamar lyric
    os.system("say " + voiceKendrick + lineKendrick)
    # wait
    time.sleep(1.0)


    # update counter
    counter = counter + 1
    counter = counter % lengthShortest
