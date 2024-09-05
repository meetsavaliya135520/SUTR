import unittest
from timer import Scrabble__Score


class MyTestCase(unittest.TestCase):
    scrabble = Scrabble__Score()

    def test_time1(self):
        self.assertEqual("Time's up! You took too long.", self.scrabble.scrabble_score(100))

    def test_time2(self):
        self.assertEqual("In time limit", self.scrabble.scrabble_score(10))

