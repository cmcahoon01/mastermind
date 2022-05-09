from unittest import TestCase
from game import Game


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