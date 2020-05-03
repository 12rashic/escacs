import unittest

from escacs.pieces import Pawn
from escacs.square import Square


class TestPawn(unittest.TestCase):
    def _makeOne(self, pos: Square, color="white"):
        p = Pawn(pos=pos, color=color)
        return p.all_moves()

    def test_all_moves_white(self):
        self.assertEqual(self._makeOne(Square("a1")), {Square("a2"), Square("b2")})
        self.assertEqual(
            self._makeOne(Square("a2")), {Square("a3"), Square("a4"), Square("b3")}
        )
        self.assertEqual(self._makeOne(Square("a3")), {Square("a4"), Square("b4")})
        self.assertEqual(self._makeOne(Square("a4")), {Square("a5"), Square("b5")})
        self.assertEqual(self._makeOne(Square("a8")), set({}))

        self.assertEqual(
            self._makeOne(Square("b2")),
            {Square("b3"), Square("b4"), Square("a3"), Square("c3")},
        )
        self.assertEqual(
            self._makeOne(Square("b3")), {Square("b4"), Square("c4"), Square("a4")}
        )
        self.assertEqual(
            self._makeOne(Square("b4")), {Square("b5"), Square("c5"), Square("a5")}
        )
        self.assertEqual(self._makeOne(Square("b8")), set({}))

        self.assertEqual(self._makeOne(Square("h1")), {Square("h2"), Square("g2")})
        self.assertEqual(
            self._makeOne(Square("h2")), {Square("h3"), Square("h4"), Square("g3")}
        )
        self.assertEqual(self._makeOne(Square("h3")), {Square("h4"), Square("g4")})
        self.assertEqual(self._makeOne(Square("h4")), {Square("h5"), Square("g5")})
        self.assertEqual(self._makeOne(Square("h8")), set({}))

    def test_all_moves_black(self):
        self.assertEqual(
            self._makeOne(Square("a8"), color="black"), {Square("a7"), Square("b7")}
        )
        self.assertEqual(
            self._makeOne(Square("a7"), color="black"),
            {Square("a6"), Square("a5"), Square("b6")},
        )
        self.assertEqual(
            self._makeOne(Square("a6"), color="black"), {Square("a5"), Square("b5")}
        )
        self.assertEqual(
            self._makeOne(Square("a4"), color="black"), {Square("a3"), Square("b3")}
        )
        self.assertEqual(self._makeOne(Square("a1"), color="black"), set({}))

        self.assertEqual(
            self._makeOne(Square("b7"), color="black"),
            {Square("b5"), Square("b6"), Square("a6"), Square("c6")},
        )
        self.assertEqual(
            self._makeOne(Square("b5"), color="black"),
            {Square("b4"), Square("c4"), Square("a4")},
        )
        self.assertEqual(
            self._makeOne(Square("b4"), color="black"),
            {Square("b3"), Square("c3"), Square("a3")},
        )
        self.assertEqual(self._makeOne(Square("b1"), color="black"), set({}))

        self.assertEqual(
            self._makeOne(Square("h8"), color="black"), {Square("h7"), Square("g7")}
        )
        self.assertEqual(
            self._makeOne(Square("h7"), color="black"),
            {Square("h6"), Square("h5"), Square("g6")},
        )
        self.assertEqual(
            self._makeOne(Square("h6"), color="black"), {Square("h5"), Square("g5")}
        )
        self.assertEqual(
            self._makeOne(Square("h5"), color="black"), {Square("h4"), Square("g4")}
        )
        self.assertEqual(self._makeOne(Square("h1"), color="black"), set({}))
