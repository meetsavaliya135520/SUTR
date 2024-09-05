import unittest
from numAdd import Scrabble__Score


class MyTestCase(unittest.TestCase):
    scrabble = Scrabble__Score()

    def test_scorelower(self):
        self.assertEqual(5, self.scrabble.scrabble_score("dog"))

    def test_scoreupper(self):
        self.assertEqual(5, self.scrabble.scrabble_score("DOG"))
