```python
class InstrumentLibrary:
    def __init__(self):
        self.library = {
            'Jazz': ['Piano', 'Double Bass', 'Drums', 'Saxophone', 'Trumpet'],
            'Rock': ['Electric Guitar', 'Bass Guitar', 'Drums', 'Keyboard', 'Vocals'],
            'Classical': ['Violin', 'Viola', 'Cello', 'Double Bass', 'Piano'],
            'Electronic': ['Synthesizer', 'Drum Machine', 'Sampler', 'Sequencer', 'Vocals']
        }

    def get_instruments(self, genre):
        return self.library.get(genre, [])

    def add_instrument(self, genre, instrument):
        if genre in self.library:
            self.library[genre].append(instrument)
        else:
            self.library[genre] = [instrument]

    def remove_instrument(self, genre, instrument):
        if genre in self.library and instrument in self.library[genre]:
            self.library[genre].remove(instrument)
```