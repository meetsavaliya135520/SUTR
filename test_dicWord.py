import unittest
from dicWord import Scrabble__Score


class MyTestCase(unittest.TestCase):
    scrabble = Scrabble__Score()

    def test_dicWordY(self):
        self.assertEqual("Yes", self.scrabble.scrabble_score("Car"))

    def test_dicWordN(self):
        self.assertEqual("No", self.scrabble.scrabble_score("qsad"))




