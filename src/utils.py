```python
import mido
from mido import MidiFile, MidiTrack, Message

def load_midi_file(file_path):
    try:
        return MidiFile(file_path)
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
    return next((msg.tempo for msg in midi_file if msg.type == 'set_tempo'), None)

def get_key_signature(midi_file):
    return next(
        (msg.key for msg in midi_file if msg.type == 'key_signature'), None
    )

def get_time_signature(midi_file):
    return next(
        (
            (msg.numerator, msg.denominator)
            for msg in midi_file
            if msg.type == 'time_signature'
        ),
        None,
    )

def get_melodic_structure(midi_file):
    return [msg.note for msg in midi_file if msg.type == 'note_on']

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
