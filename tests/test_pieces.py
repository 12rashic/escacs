import unittest

from escacs.pieces import Pawn
from escacs.position import Position


class TestPawn(unittest.TestCase):
    def _makeOne(self, pos: Position):
        p = Pawn(pos=pos, color="white")
        return p.legal_moves()

    def test_legal_moves(self):
        # TODO: make sure you can't have a white pawn on the 1st raw
        # TODO: make sure you can't have a black pawn on the 8th raw
        moves = self._makeOne(Position.from_string("a1"))
        self.assertEqual(moves, {Position.from_string("a2"), Position.from_string("a")})

        # No more moves
        moves = self._makeOne(Position.from_string("a8"))
        self.assertEqual(moves, set({}))
