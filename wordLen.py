import random
class Scrabble__Score(object):
    def scrabble_score(self, word):

        word_length = 3
        user_input = word
        if len(user_input) != word_length:
            return "Enter word in valid word limit"
        else:
            return "Correct word limit"

