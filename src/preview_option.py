```python
import mido
from mido import MidiFile

def play_midi(midi_file):
    """
    Function to play a MIDI file.
    """
    for msg in MidiFile(midi_file).play():
        mido.get_output_names()
        outport = mido.open_output()
        outport.send(msg)

def preview_generated_track():
    """
    Function to preview the generated MIDI track.
    """
    print("Previewing the generated MIDI track...")
    play_midi(final_midi_file)

def preview_section(section):
    """
    Function to preview a specific section of the generated MIDI track.
    """
    print(f"Previewing the {section} section...")
    play_midi(song_structure[section])
```