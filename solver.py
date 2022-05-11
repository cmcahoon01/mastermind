from game import Game
from math import log2


def score_guess(guess, answer):
    game = Game(answer)
    return game.score_guess(guess)


def is_possible(answer, guess, black, white):
    return score_guess(guess, answer) == (black, white)


class Solver:
    def __init__(self, game, colors, size=4):
        self.colors = colors
        self.game = game
        self.size = size
        self.all_combinations = self.generate_all_combinations(size)
        self.remaining_combinations = self.all_combinations.copy()

    def generate_all_combinations(self, size):
        colors = [[color] for color in self.colors]
        if size == 1:
            return colors
        all_combinations = []
        subset = self.generate_all_combinations(size - 1)
        for color in colors:
            for combination in subset:
                all_combinations.append(combination + color)
        return all_combinations

    def guess(self):
        expected_info = {}
        for combination in self.all_combinations:
            expected_info[combination] = self.get_expected_info(combination)
        max_expected_info = max(expected_info.values())
        for combination in self.all_combinations:
            if expected_info[combination] == max_expected_info:
                return self.receive_feedback(combination)

    def get_expected_info(self, combination):
        results = {}
        for i in range(self.size + 1):
            for j in range(self.size + 1 - i):
                results[(i, j)] = 0
        for potential in self.remaining_combinations:
            results[score_guess(combination, potential)] += 1
        expected_value = 0
        num_remaining = len(self.remaining_combinations)
        for occurrences in results.values():
            probability = occurrences / num_remaining
            expected_value += probability * log2(1 / probability)
        return expected_value

    def receive_feedback(self, combination):
        black, white = self.game.guess(combination)
        self.remaining_combinations = filter(lambda x: is_possible(x, combination, black, white),
                                             self.remaining_combinations)
