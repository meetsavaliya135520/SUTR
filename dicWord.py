from nltk.corpus import wordnet

class Scrabble__Score(object):
    def scrabble_score(self, word):

        if not wordnet.synsets(word):
            return "No"
        else:
            return "Yes"
