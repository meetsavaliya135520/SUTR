import unittest
from wordLen import Scrabble__Score


class MyTestCase(unittest.TestCase):
    scrabble = Scrabble__Score()

    #check word length
    def test_dicWordLen1(self):
        self.assertEqual("Correct word limit", self.scrabble.scrabble_score("dog"))

    def test_dicWordLen2(self):
        self.assertEqual("Enter word in valid word limit", self.scrabble.scrabble_score("green"))




