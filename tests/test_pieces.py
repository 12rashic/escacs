import unittest

from escacs.pieces import Pawn
from escacs.square import Square


class TestPawn(unittest.TestCase):
    def _makeOne(self, pos: Square):
        p = Pawn(pos=pos, color="white")
        return p.all_moves()

    def test_all_moves(self):
        moves = self._makeOne(Square("a2"))
        self.assertEqual(moves, {Square("a3"), Square("a4")})

        # No more moves
        moves = self._makeOne(Square("a8"))
        self.assertEqual(moves, set({}))
