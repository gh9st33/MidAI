```python
import os
from midiutil import MIDIFile

# Shared variables
user_midi_pattern = None

def uploadMidiPattern():
    global user_midi_pattern
    print("Please enter the path of your MIDI file:")
    file_path = input()
    if not os.path.isfile(file_path):
        print("File does not exist. Please try again.")
        return
    try:
        with open(file_path, 'rb') as file:
            user_midi_pattern = MIDIFile(file)
        print("MidiUploadSuccess: MIDI file uploaded successfully.")
    except Exception as e:
        print(f"MidiUploadFailure: Error in uploading MIDI file. {str(e)}")

if __name__ == "__main__":
    uploadMidiPattern()
```