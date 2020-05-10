from escacs.exceptions import InvalidMove
from escacs.game import Game
from escacs.square import Square

import pytest
import unittest


class TestGame(unittest.TestCase):
    def makeOne(self):
        return Game()

    def test_turn(self):
        g = self.makeOne()
        self.assertEqual(g.turn, "white")
        g.pass_turn()
        self.assertEqual(g.turn, "black")
        g.pass_turn()
        self.assertEqual(g.turn, "white")

    def test_player_move_where_no_piece_is_found(self):
        g = self.makeOne()
        with pytest.raises(InvalidMove):
            g.player_move(Square("a4"), Square("a5"))

    def test_player_move_on_wrong_turn(self):
        g = self.makeOne()

        # Try to move black piece on white's turn
        self.assertEqual(g.turn, "white")
        with pytest.raises(InvalidMove):
            g.player_move(Square("a7"), Square("a6"))

        # Try to move white piece on black's turn
        g.pass_turn()
        self.assertEqual(g.turn, "black")
        with pytest.raises(InvalidMove):
            g.player_move(Square("a2"), Square("a3"))

    def test_move_valid_piece_move(self):
        g = self.makeOne()
        # Try to move white pawn 4 squares ahead
        with pytest.raises(InvalidMove):
            g.player_move(Square("a2"), Square("a6"))

        # Try to move white pawn diagonally like a bishop
        with pytest.raises(InvalidMove):
            g.player_move(Square("a2"), Square("d4"))
