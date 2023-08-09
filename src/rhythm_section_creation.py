```python
from src.utils import get_rhythm_patterns
from src.constants import RhythmSection

def createRhythmSection(analyzed_pattern, selected_genre, selected_instruments):
    """
    Function to create a rhythmic section that complements the primary pattern and fits the chosen genre.
    """
    rhythm_patterns = get_rhythm_patterns(selected_genre)

    rhythm_section = []
    for instrument in selected_instruments:
        if instrument in RhythmSection:
            rhythm_pattern = rhythm_patterns[instrument]
            rhythm_track = generate_rhythm_track(analyzed_pattern, rhythm_pattern)
            rhythm_section.append(rhythm_track)

    return rhythm_section

def generate_rhythm_track(analyzed_pattern, rhythm_pattern):
    """
    Function to generate a rhythm track based on the analyzed pattern and the rhythm pattern.
    """
    rhythm_track = []
    for note in analyzed_pattern:
        rhythm_note = apply_rhythm_pattern(note, rhythm_pattern)
        rhythm_track.append(rhythm_note)

    return rhythm_track

def apply_rhythm_pattern(note, rhythm_pattern):
    """
    Function to apply the rhythm pattern to a note.
    """
    rhythm_note = note.copy()
    rhythm_note.duration = rhythm_pattern[note.pitch % len(rhythm_pattern)]

    return rhythm_note
```