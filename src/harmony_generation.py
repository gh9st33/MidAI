```python
import mido
from src.utils import get_scale_notes, get_chord_notes
from src.constants import MIDI_NOTE_NUMBERS

def generateHarmonies(analyzed_pattern, selected_genre):
    """
    Function to generate harmonies based on the analyzed MIDI pattern and selected genre.
    """
    harmonies = []
    scale_notes = get_scale_notes(analyzed_pattern['key'], selected_genre['scale'])
    
    for note in analyzed_pattern['notes']:
        if note in scale_notes:
            chord_notes = get_chord_notes(note, selected_genre['chord_progression'])
            harmonies.append(chord_notes)
        else:
            harmonies.append([note])
    
    return harmonies

def create_harmony_track(harmonies, tempo):
    """
    Function to create a MIDI track from the generated harmonies.
    """
    harmony_track = mido.MidiTrack()
    for harmony in harmonies:
        for note in harmony:
            note_number = MIDI_NOTE_NUMBERS[note]
            harmony_track.append(mido.Message('note_on', note=note_number, velocity=64, time=0))
            harmony_track.append(mido.Message('note_off', note=note_number, velocity=64, time=int(480*60/tempo)))
    return harmony_track

def save_harmony_track(harmony_track, filename):
    """
    Function to save the generated harmony track as a MIDI file.
    """
    midi_file = mido.MidiFile()
    midi_file.tracks.append(harmony_track)
    midi_file.save(filename)
```
