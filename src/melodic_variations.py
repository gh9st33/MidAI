```python
from src.utils import generate_variation
from src.constants import MelodicVariation

def generateMelodicVariations(analyzed_pattern, song_structure):
    melodic_variations = {}

    for section in song_structure:
        if section == 'chorus' or section == 'bridge':
            variation = generate_variation(analyzed_pattern, MelodicVariation.CHORUS_BRIDGE)
            melodic_variations[section] = variation
        else:
            variation = generate_variation(analyzed_pattern, MelodicVariation.OTHER_SECTIONS)
            melodic_variations[section] = variation

    return melodic_variations
```