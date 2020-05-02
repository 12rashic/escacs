import unittest

from escacs.pieces import Pawn
from escacs.square import Square


class TestPawn(unittest.TestCase):
    def _makeOne(self, pos: Square):
        p = Pawn(pos=pos, color="white")
        return p.all_moves()

    def test_all_moves(self):
        moves = self._makeOne(Square.from_string("a2"))
        self.assertEqual(moves, {Square.from_string("a3"), Square.from_string("a4")})

        # No more moves
        moves = self._makeOne(Square.from_string("a8"))
        self.assertEqual(moves, set({}))
