from escacs.board import Board
from escacs.board import Square
from escacs.exceptions import InvalidSquare
from unittest.mock import Mock

import pytest
import unittest


class TestBoard(unittest.TestCase):
    def _makeOne(self):
        return Board()

    def test_empty(self):
        b = self._makeOne()
        for col in range(8):
            for row in range(8):
                self.assertIsNone(b[Square((row, col))])

        for row in "abcdefgh":
            for col in range(1, 9):
                pos = "".join([row, str(col)])
                self.assertIsNone(b[pos])

    def test_set_get_position(self):
        b = self._makeOne()
        foo = Mock()
        b["a1"] = foo
        self.assertIs(b["a1"], foo)


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


class TestSquare_path(unittest.TestCase):
    def _makeOne(self, _from: str, _to: str):
        b = Board()
        return b.path(_from, _to)

    def test_path_orthogonal(self):
        expected = [
            Square("a2"),
            Square("a3"),
            Square("a4"),
            Square("a5"),
            Square("a6"),
            Square("a7"),
            Square("a8"),
        ]
        self.assertEqual(self._makeOne("a1", "a2"), expected[:1])
        self.assertEqual(self._makeOne("a1", "a3"), expected[:2])
        self.assertEqual(self._makeOne("a1", "a4"), expected[:3])
        self.assertEqual(self._makeOne("a1", "a5"), expected[:4])
        self.assertEqual(self._makeOne("a1", "a6"), expected[:5])
        self.assertEqual(self._makeOne("a1", "a7"), expected[:6])
        self.assertEqual(self._makeOne("a1", "a8"), expected)
        self.assertEqual(self._makeOne("a2", "a8"), expected[1:])

    def test_path_diagonal(self):
        expected = [
            Square("b3"),
            Square("c4"),
            Square("d5"),
            Square("e6"),
            Square("f7"),
            Square("g8"),
        ]
        self.assertEqual(self._makeOne("a2", "b3"), expected[:1])
        self.assertEqual(self._makeOne("a2", "c4"), expected[:2])
        self.assertEqual(self._makeOne("a2", "d5"), expected[:3])
        self.assertEqual(self._makeOne("a2", "e6"), expected[:4])
        self.assertEqual(self._makeOne("a2", "f7"), expected[:5])
        self.assertEqual(self._makeOne("a2", "g8"), expected)
        self.assertEqual(self._makeOne("c4", "e6"), expected[2:4])
