import unittest

import pytest
from escacs.board import Board, Square
from escacs.exceptions import InvalidSquare


class TestBoard(unittest.TestCase):
    def _makeOne(self):
        return Board()

    def test_empty(self):
        b = self._makeOne()
        b.clear()
        for col in range(8):
            for row in range(8):
                self.assertIsNone(b[Square((row, col))])

        for row in "abcdefgh":
            for col in range(1, 9):
                pos = "".join([row, str(col)])
                self.assertIsNone(b[pos])

    def test_set_get_position(self):
        b = self._makeOne()
        foo = "foo"
        b["a1"] = foo
        self.assertIs(b["a1"], foo)

    def test_init_board(self):
        b = self._makeOne()
        self.assertEqual(b["a2"].__class__.__name__, "Pawn")
        self.assertEqual(b["a2"].color, "white")
        self.assertEqual(b["a7"].__class__.__name__, "Pawn")
        self.assertEqual(b["a7"].color, "black")


class TestSquare_from_string(unittest.TestCase):
    def _makeOne(self, pos: str):
        return Square(pos)

    def test_invalid_raises_exception(self):
        for invalid in ("c44", "x1", "", "a9"):
            with pytest.raises(InvalidSquare):
                self._makeOne(invalid)

    def test_valid_returns_instance(self):
        for col in "abcdefgh":
            for row in range(1, 9):
                valid = "".join([col, str(row)])
                self.assertIsInstance(self._makeOne(valid), Square)


class TestSquare_color(unittest.TestCase):
    def _makeOne(self, pos: str):
        p = Square(pos)
        return p.color

    def test_black_squares(self):
        for col in "aceg":
            for row in [1, 3, 5, 7]:
                self.assertEqual(self._makeOne(f"{col}{row}"), "black")
        for col in "bdfh":
            for row in [2, 4, 6, 8]:
                self.assertEqual(self._makeOne(f"{col}{row}"), "black")

    def test_white_squares(self):
        for col in "aceg":
            for row in [2, 4, 6, 8]:
                self.assertEqual(self._makeOne(f"{col}{row}"), "white")
        for col in "bdfh":
            for row in [1, 3, 5, 7]:
                self.assertEqual(self._makeOne(f"{col}{row}"), "white")
