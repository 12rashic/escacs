import unittest

from escacs.pieces import Bishop, King, Knight, Pawn, Queen, Rook
from escacs.square import Square


class TestPawn(unittest.TestCase):
    def _makeOne(self, pos: Square, color="white"):
        p = Pawn(color=color)
        return p.all_moves(pos)

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


def all_squares():
    for i in range(8):
        for j in range(8):
            yield Square([i, j])


class TestRook(unittest.TestCase):
    def _makeOne(self, pos: Square, color="white"):
        p = Rook(color=color)
        return p.all_moves(pos)

    def test_horizontal_and_vertical(self):
        for square in all_squares():
            self.assertEqual(len(self._makeOne(square)), 14)

        # Check that it always stays inthe same row or in the same
        # column
        for m in self._makeOne(Square("a1")):
            self.assertTrue(
                (m.col == 0 and m.row in range(8)) or (m.col in range(8) and m.row == 0)
            )

        for m in self._makeOne(Square("a5")):
            self.assertTrue(
                (m.col == 0 and m.row in range(8)) or (m.col in range(8) and m.row == 4)
            )


class TestBishop(unittest.TestCase):
    def _makeOne(self, pos: Square, color="white"):
        b = Bishop(color=color)
        return b.all_moves(pos)

    def test_diagonals(self):
        for square in all_squares():
            square_color = square.color
            moves = self._makeOne(square)
            for m in moves:
                assert m.color == square_color

        # From all the board perimeter squares, bishop has only 7
        # possible moves
        for i in range(0, 8):
            self.assertEqual(len(self._makeOne(Square((0, i)))), 7)
            self.assertEqual(len(self._makeOne(Square((i, 0)))), 7)
            self.assertEqual(len(self._makeOne(Square((7, i)))), 7)
            self.assertEqual(len(self._makeOne(Square((i, 7)))), 7)

        # Thes the inner perimeter squares
        for i in range(1, 7):
            self.assertEqual(len(self._makeOne(Square((1, i)))), 9)
            self.assertEqual(len(self._makeOne(Square((i, 1)))), 9)
            self.assertEqual(len(self._makeOne(Square((6, i)))), 9)
            self.assertEqual(len(self._makeOne(Square((i, 6)))), 9)

        for i in range(2, 6):
            self.assertEqual(len(self._makeOne(Square((2, i)))), 11)
            self.assertEqual(len(self._makeOne(Square((i, 2)))), 11)
            self.assertEqual(len(self._makeOne(Square((5, i)))), 11)
            self.assertEqual(len(self._makeOne(Square((i, 5)))), 11)

        for i in range(3, 5):
            self.assertEqual(len(self._makeOne(Square((3, i)))), 13)
            self.assertEqual(len(self._makeOne(Square((i, 3)))), 13)
            self.assertEqual(len(self._makeOne(Square((4, i)))), 13)
            self.assertEqual(len(self._makeOne(Square((i, 4)))), 13)


class TestQueen(unittest.TestCase):
    def _makeOne(self, pos: Square, color="white"):
        q = Queen(color=color)
        return q.all_moves(pos)

    def test_all_moves(self):
        for i in range(0, 8):
            self.assertEqual(len(self._makeOne(Square((0, i)))), 21)
            self.assertEqual(len(self._makeOne(Square((i, 0)))), 21)
            self.assertEqual(len(self._makeOne(Square((7, i)))), 21)
            self.assertEqual(len(self._makeOne(Square((i, 7)))), 21)

        for i in range(1, 7):
            self.assertEqual(len(self._makeOne(Square((1, i)))), 23)
            self.assertEqual(len(self._makeOne(Square((i, 1)))), 23)
            self.assertEqual(len(self._makeOne(Square((6, i)))), 23)
            self.assertEqual(len(self._makeOne(Square((i, 6)))), 23)

        for i in range(2, 6):
            self.assertEqual(len(self._makeOne(Square((2, i)))), 25)
            self.assertEqual(len(self._makeOne(Square((i, 2)))), 25)
            self.assertEqual(len(self._makeOne(Square((5, i)))), 25)
            self.assertEqual(len(self._makeOne(Square((i, 5)))), 25)

        for i in range(3, 5):
            self.assertEqual(len(self._makeOne(Square((3, i)))), 27)
            self.assertEqual(len(self._makeOne(Square((i, 3)))), 27)
            self.assertEqual(len(self._makeOne(Square((4, i)))), 27)
            self.assertEqual(len(self._makeOne(Square((i, 4)))), 27)


class TestKnight(unittest.TestCase):
    def _makeOne(self, pos: Square, color="white"):
        n = Knight(color=color)
        return n.all_moves(pos)

    def test_all_moves(self):
        for sq in ("a1", "a8", "h1", "h8"):
            self.assertEqual(len(self._makeOne(Square(sq))), 2)
        for sq in ("a2", "a7", "h2", "h7"):
            self.assertEqual(len(self._makeOne(Square(sq))), 3)
        for sq in ("a3", "a6", "h3", "h6"):
            self.assertEqual(len(self._makeOne(Square(sq))), 4)
        for sq in ("a3", "a6", "h3", "h6"):
            self.assertEqual(len(self._makeOne(Square(sq))), 4)

        self.assertEqual(
            self._makeOne(Square("d5")),
            {
                Square("c7"),
                Square("e7"),
                Square("c3"),
                Square("e3"),
                Square("f6"),
                Square("f4"),
                Square("b6"),
                Square("b4"),
            },
        )


class TestKing(unittest.TestCase):
    def _makeOne(self, pos: Square, color="white"):
        k = King(color=color)
        return k.all_moves(pos)

    def test_all_moves(self):
        for s in all_squares():
            self.assertIn(len(self._makeOne(s)), [3, 5, 8])

        self.assertEqual(
            self._makeOne(Square("a1")), {Square("a2"), Square("b2"), Square("b1")}
        )

        self.assertEqual(
            self._makeOne(Square("c4")),
            {
                Square("c3"),
                Square("b3"),
                Square("d3"),
                Square("c5"),
                Square("b5"),
                Square("d5"),
                Square("d4"),
                Square("b4"),
            },
        )
