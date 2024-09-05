import unittest
from validAlpha import Scrabble__Score


class MyTestCase(unittest.TestCase):
    scrabble = Scrabble__Score()

    def test_non_alpha_input(self):
        self.assertEqual("Invalid input. Please enter alphabets only.", self.scrabble.scrabble_score("d0g"))

