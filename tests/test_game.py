from escacs.board import Board
from escacs.exceptions import InvalidMove
from escacs.game import clear_path
from escacs.game import Game
from escacs.game import legal_moves
from escacs.pieces import Pawn
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

    def test_move_where_no_piece_is_found(self):
        g = self.makeOne()
        with pytest.raises(InvalidMove):
            g.move(Square("a4"), Square("a5"))

    def test_move_on_wrong_turn(self):
        g = self.makeOne()

        # Try to move black piece on white's turn
        self.assertEqual(g.turn, "white")
        with pytest.raises(InvalidMove):
            g.move(Square("a7"), Square("a6"))

        # Try to move white piece on black's turn
        g.pass_turn()
        self.assertEqual(g.turn, "black")
        with pytest.raises(InvalidMove):
            g.move(Square("a2"), Square("a3"))

    def test_move_valid_piece_move(self):
        g = self.makeOne()
        # Try to move white pawn 4 squares ahead
        with pytest.raises(InvalidMove):
            g.move(Square("a2"), Square("a6"))

        # Try to move white pawn diagonally like a bishop
        with pytest.raises(InvalidMove):
            g.move(Square("a2"), Square("d4"))


class Test_clear_path(unittest.TestCase):
    def makeOne(self, pos1, pos2, clear_at):
        b = Board()
        b.clear()
        b[pos1] = Pawn("white")
        b[pos2] = Pawn("white")
        return clear_path(b, Pawn("white"))


class Test_legal_moves_pawn(unittest.TestCase):
    def makeOne(self, pos):
        b = Board()
        b.clear()
        b[pos] = Pawn("white")
        return b

    def test_legal_moves(self):
        sq = Square("a2")
        board = self.makeOne(sq)
        self.assertEquals(legal_moves(sq, board), {Square("a3"), Square("a4")})

        sq = Square("a3")
        board = self.makeOne(sq)
        self.assertEquals(legal_moves(sq, board), {Square("a4")})

        sq = Square("a8")
        board = self.makeOne(sq)
        self.assertEquals(legal_moves(sq, board), set())
