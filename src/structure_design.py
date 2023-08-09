```python
from src.utils import SongStructure

song_structure = SongStructure()

def design_structure(user_input):
    """
    Function to design the structure of the song based on user input.
    """
    global song_structure
    song_structure.intro = user_input.get('intro', [])
    song_structure.verse = user_input.get('verse', [])
    song_structure.chorus = user_input.get('chorus', [])
    song_structure.bridge = user_input.get('bridge', [])
    song_structure.outro = user_input.get('outro', [])

    return song_structure

def arrange_tracks():
    """
    Function to arrange the generated tracks according to the designed structure.
    """
    global song_structure
    arranged_tracks = []
    for section in [song_structure.intro, song_structure.verse, song_structure.chorus, song_structure.bridge, song_structure.outro]:
        for track in section:
            arranged_tracks.append(track)

    return arranged_tracks
```