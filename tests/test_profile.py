import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProfileTests(unittest.TestCase):
    def test_profile_resources_and_startup_are_consistent(self):
        board = json.loads((ROOT / 'board.json').read_text(encoding='utf-8'))
        for name in board['profiles'].values():
            profile = json.loads((ROOT / name).read_text(encoding='utf-8'))
            self.assertEqual(board['id'], profile['board'])
            self.assertEqual('systemd', profile['startup']['init'])
            self.assertEqual('gar-target', profile['startup']['manager'])
            for gpio in profile['gpio']:
                self.assertEqual(set(gpio['lines']), set(map(int, gpio['line_pins'])))
                self.assertEqual(len(gpio['lines']), len(set(gpio['line_pins'].values())))
                self.assertTrue(all(1 <= pin <= 40 for pin in gpio['line_pins'].values()))
            for spi in profile['spi']:
                self.assertEqual(set(spi['pins']), set(spi['routing']))


if __name__ == '__main__':
    unittest.main()
