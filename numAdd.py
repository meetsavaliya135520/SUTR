
class Scrabble__Score(object):

    def scrabble_score(self, word):
        # Define the score dictionary
        score_dict = {
            1: "AEIOULNRST",
            2: "DG",
            3: "BCMP",
            4: "FHVWY",
            5: "K",
            8: "JX",
            10: "QZ"
        }

        if not word.isalpha():
            print("Invalid input. Please enter alphabets only.")

        score = 0
        for letter in word.upper():
            for points, letters in score_dict.items():
                if letter in letters:
                    score += points
                    break
        return score
