```python
import random
from midi_pattern_generator import constants
from midi_pattern_generator import midi_utils

def generate_pattern():
    pattern = []
    for _ in range(constants.PATTERN_LENGTH):
        note = midi_utils.generate_random_note()
        pattern.append(note)
    return pattern

def save_pattern(pattern, filename):
    with open(filename, 'w') as f:
        for note in pattern:
            f.write(f"{note}\n")

def validate_pattern(pattern):
    if len(pattern) != constants.PATTERN_LENGTH:
        return False
    for note in pattern:
        if not midi_utils.validate_note(note):
            return False
    return True
```