class Game:
    guesses = []

    def __init__(self, answer):
        self.answer = answer

    def guess(self, guess):
        score = self.score_guess(guess)

    def score_guess(self, guess):
        blacks = 0  # correct color and position
        whites = 0  # correct color wrong position
        answer = self.answer.copy()
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                blacks += 1
                answer[i] = -1
                guess[i] = -2  # need to be different
        for i in range(len(guess)):
            if guess[i] in answer:
                whites += 1
                answer[answer.index(guess[i])] = -1
                guess[i] = -2
        return blacks, whites