import mido
from mido import Message
import sys


print(mido.get_input_names())
port_io = ("Network Session 1") #input("Choisissez le port d'entrée MIDI :")
print(port_io)

# Définir le port de sortie MIDI
port = mido.open_output(port_io)
def send_midi_note(note, velocity):
    port.send(Message('note_on', note=note, velocity=velocity))
    port.send(Message('note_off', note=note, velocity=0))

# Envoi d'une note MIDI
play = send_midi_note(60, 127)  # Envoi d'une note MIDI Stop Qlab
stop = send_midi_note(61, 127)  # Envoi d'une note MIDI play

sys.argv[1] = play
sys.argv[1] = stop