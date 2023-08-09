```python
import unittest
from midi_pattern_generator.pattern_generator import generate_pattern, save_pattern, PATTERN_LENGTH, NOTE_RANGE

class TestPatternGenerator(unittest.TestCase):
    def setUp(self):
        self.pattern_length = PATTERN_LENGTH
        self.note_range = NOTE_RANGE

    def test_generate_pattern(self):
        pattern = generate_pattern(self.pattern_length, self.note_range)
        self.assertEqual(len(pattern), self.pattern_length)
        for note in pattern:
            self.assertTrue(self.note_range[0] <= note <= self.note_range[1])

    def test_save_pattern(self):
        pattern = generate_pattern(self.pattern_length, self.note_range)
        save_pattern(pattern, "test_pattern.mid")
        with open("test_pattern.mid", "r") as f:
            content = f.read()
        self.assertNotEqual(content, "")

if __name__ == "__main__":
    unittest.main()
```