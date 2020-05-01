import unittest

from escacs import Board


class TestBoard(unittest.TestCase):
    def _makeOne(self):
        return Board()

    def test_empty(self):
        b = self._makeOne()
        for i in range(8):
            for j in range(8):
                self.assertIsNone(b[(i, j)])
