import unittest


class TestExample(unittest.TestCase):
    def _makeOne(self):
        return None

    def test_dummy(self):
        self.assertIsNone(self._makeOne())
