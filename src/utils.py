```python
import mido
from mido import MidiFile, MidiTrack, Message

def load_midi_file(file_path):
    try:
        midi_file = MidiFile(file_path)
        return midi_file
    except Exception as e:
        print(f"Failed to load MIDI file. Error: {str(e)}")
        return None

def save_midi_file(midi_file, file_path):
    try:
        midi_file.save(file_path)
        print("MIDI file saved successfully.")
    except Exception as e:
        print(f"Failed to save MIDI file. Error: {str(e)}")

def get_tempo(midi_file):
    for msg in midi_file:
        if msg.type == 'set_tempo':
            return msg.tempo
    return None

def get_key_signature(midi_file):
    for msg in midi_file:
        if msg.type == 'key_signature':
            return msg.key
    return None

def get_time_signature(midi_file):
    for msg in midi_file:
        if msg.type == 'time_signature':
            return (msg.numerator, msg.denominator)
    return None

def get_melodic_structure(midi_file):
    notes = []
    for msg in midi_file:
        if msg.type == 'note_on':
            notes.append(msg.note)
    return notes

def create_midi_track(notes, tempo, time_signature):
    track = MidiTrack()
    track.append(Message('set_tempo', tempo=tempo))
    track.append(Message('time_signature', numerator=time_signature[0], denominator=time_signature[1]))
    for note in notes:
        track.append(Message('note_on', note=note, velocity=64, time=32))
        track.append(Message('note_off', note=note, velocity=64, time=32))
    return track

def add_track_to_midi_file(midi_file, track):
    midi_file.tracks.append(track)
```
