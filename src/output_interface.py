```python
import os
from midiutil import MIDIFile

def generate_midi_output(final_midi_file):
    # Create a new MIDI file with a single track
    midi_file = MIDIFile(1)

    # Add track name and tempo
    midi_file.addTrackName(0, 0, "Generated Track")
    midi_file.addTempo(0, 0, final_midi_file['tempo'])

    # Add notes
    for i, note in enumerate(final_midi_file['notes']):
        midi_file.addNote(0, 0, note['pitch'], note['start_time'], note['duration'], note['volume'])

    # Write it to disk
    output_file_path = os.path.join(os.getcwd(), 'output.mid')
    with open(output_file_path, 'wb') as output_file:
        midi_file.writeFile(output_file)

    return output_file_path

def display_midi_output(output_file_path):
    print(f"MIDI output file has been generated and saved at {output_file_path}")

def output_interface(final_midi_file):
    output_file_path = generate_midi_output(final_midi_file)
    display_midi_output(output_file_path)
```