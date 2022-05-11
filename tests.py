from unittest import TestCase
from game import Game
from solver import Solver


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

    def test_receive_feedback(self):
        pass

    def test_get_expected_info(self):
        pass

