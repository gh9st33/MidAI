import unittest
from midi_pattern_generator.midi_utils import midi_to_note, note_to_midi, generate_random_note, validate_note
from midi_pattern_generator.constants import MIDI_NOTE_RANGE

class TestMidiUtils(unittest.TestCase):

    def test_midi_to_note(self):
        midi_note = 60
        note = midi_to_note(midi_note)
        self.assertEqual(note, 'C4')

    def test_note_to_midi(self):
        note = 'C4'
        midi_note = note_to_midi(note)
        self.assertEqual(midi_note, 60)

    def test_generate_random_note(self):
        note = generate_random_note()
        midi_note = note_to_midi(note)
        self.assertTrue(MIDI_NOTE_RANGE[0] <= midi_note <= MIDI_NOTE_RANGE[1])

    def test_validate_note(self):
        note = 'C4'
        self.assertTrue(validate_note(note))

        invalid_note = 'H8'
        self.assertFalse(validate_note(invalid_note))


if __name__ == '__main__':
    unittest.main()