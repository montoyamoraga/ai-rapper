# import libraries
import mido
import time
import rtmidi

midiOut = rtmidi.MidiOut()

outPort = midiOut.open_virtual_port("python-midi")

outPorts = mido.get_output_names()

noteOn = [0x90, 60, 112];

while True:
    midiOut.send_message(noteOn);
    time.sleep(1.0)
