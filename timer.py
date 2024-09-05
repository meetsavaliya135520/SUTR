
class Scrabble__Score(object):

    def scrabble_score(self, time):
        # 15 seconds timer

        if time > 15:
            return "Time's up! You took too long."
        else:
            return "In time limit"