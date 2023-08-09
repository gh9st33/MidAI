```python
from src.constants import InstrumentSelection, MelodicVariation, SongStructure
from src.utils import update_instrument_selection, update_melodic_variation, update_song_structure

def customize_instruments(user_instruments):
    """
    Function to allow users to customize the instrument selection.
    """
    if not isinstance(user_instruments, InstrumentSelection):
        raise TypeError("Invalid input type. Expected InstrumentSelection.")
    
    global selected_instruments
    selected_instruments = update_instrument_selection(user_instruments)
    return selected_instruments

def customize_melodic_variations(user_variations):
    """
    Function to allow users to customize the melodic variations.
    """
    if not isinstance(user_variations, MelodicVariation):
        raise TypeError("Invalid input type. Expected MelodicVariation.")
    
    global melodic_variations
    melodic_variations = update_melodic_variation(user_variations)
    return melodic_variations

def customize_song_structure(user_structure):
    """
    Function to allow users to customize the song structure.
    """
    if not isinstance(user_structure, SongStructure):
        raise TypeError("Invalid input type. Expected SongStructure.")
    
    global song_structure
    song_structure = update_song_structure(user_structure)
    return song_structure
```