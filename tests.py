from unittest import TestCase
from game import Game
from solver import Solver, is_possible
from math import log2


class TestGame(TestCase):
    def setUp(self):
        self.game = Game(['red', 'blue', 'green', 'yellow'])

    def test_guess(self):
        self.skipTest("Not implemented")

    def test_score_guess(self):
        b, w = self.game.score_guess(['red', 'blue', 'green', 'yellow'])
        assert b == 4
        assert w == 0
        b, w = self.game.score_guess(['red', 'red', 'yellow', 'green'])
        assert b == 1
        assert w == 2
        self.game = Game(['red', 'red', 'green', 'green'])
        b, w = self.game.score_guess(['red', 'green', 'red', 'red'])
        assert b == 1
        assert w == 2


class TestSolver(TestCase):
    def setUp(self):
        colors = ["red", "green", "blue"]
        self.game = Game(colors[:2])
        self.solver = Solver(self.game, colors, 2)

    def test_generate_all(self):
        assert len(self.solver.all_combinations) == 3 ** 2

    def test_is_possible(self):
        combo1 = ["red", "green", "blue"]
        combo2 = ["red", "green", "green"]
        assert is_possible(combo1, combo1, 3, 0)
        assert is_possible(combo1, combo2, 2, 0)
        assert not is_possible(combo1, combo1, 2, 0)
        assert not is_possible(combo1, combo2, 3, 0)

    def test_receive_feedback_one(self):
        combo = ['red', 'green', 'blue']
        self.solver.receive_feedback(combo[:2])
        result = list(self.solver.remaining_combinations)
        assert result == [combo[:2]], (result, combo[:2])
        self.solver.remaining_combinations = self.solver.all_combinations
        self.solver.receive_feedback(["red", "blue"])
        result = list(self.solver.remaining_combinations)
        assert len(result) == 4, result

    def test_receive_feedback_two(self):
        combo = ['green', 'red', 'blue']
        self.solver.receive_feedback(combo[:2])
        result = self.solver.remaining_combinations
        assert result == [["red", "green"]], (result, [["red", "green"]])
        self.solver.remaining_combinations = self.solver.all_combinations
        self.solver.receive_feedback(["red", "red"])
        result = self.solver.remaining_combinations
        assert len(result) == 4, result

    def test_get_expected_info(self):
        result = self.solver.get_expected_info(["red", "green"])
        size = 3 ** 2
        expected = 1 / size * log2(size)  # 2 black
        expected += 4 / size * log2(size / 4)  # 1 black
        expected += 1 / size * log2(size / 1)  # 2 white
        expected += 2 / size * log2(size / 2)  # 1 white
        expected += 1 / size * log2(size)  # no pips
        assert result == expected, (result, expected)
