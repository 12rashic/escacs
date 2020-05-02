import unittest

import pytest
from escacs.board import Board, Position
from escacs.exceptions import InvalidPosition


class TestBoard(unittest.TestCase):
    def _makeOne(self):
        return Board()

    def test_empty(self):
        b = self._makeOne()
        for col in range(8):
            for row in range(8):
                self.assertIsNone(b[Position(row, col)])

        for row in "abcdefgh":
            for col in range(1, 9):
                pos = "".join([row, str(col)])
                self.assertIsNone(b[pos])

    def test_set_get_position(self):
        b = self._makeOne()
        foo = "foo"
        b["a1"] = foo
        self.assertIs(b["a1"], foo)


class TestPosition_from_string(unittest.TestCase):
    def _makeOne(self, pos: str):
        return Position.from_string(pos)

    def test_invalid_raises_exception(self):
        for invalid in ("c44", "x1", "", "a9"):
            with pytest.raises(InvalidPosition):
                self._makeOne(invalid)

    def test_valid_returns_instance(self):
        for col in "abcdefgh":
            for row in range(1, 9):
                valid = "".join([col, str(row)])
                self.assertIsInstance(self._makeOne(valid), Position)
