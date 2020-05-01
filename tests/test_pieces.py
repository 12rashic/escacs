import unittest


class TestPawn(unittest.TestCase):
    def _makeOne(self, pos: Position, color: Color, board: Board):
        return Pawn(pos=pos, color=color, board=board)

    def test_can_move(self):
        board = Board()
        pawn = board.get_piece("a2")
        pawn = _makeOne(Position("a2", "white", board))
        self.assertIsNone(self._makeOne())
