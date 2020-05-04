from typing import Optional

from .board import Board
from .pieces import *
from .square import Square
from .types import Color


class Game:
    def __init__(self):
        self._turn: Color = "white"
        self.moves = List[Tuple[Square, Square]] = []
        self.init_board()

    def turn(self) -> Color:
        return self._turn

    def move(self, _from: Square, _to: Square) -> Optional[Piece]:
        piece = self._board[_from]
        if not piece:
            raise InvalidMove(_from, _to)

        target = self._board[_to]
        if target:
            target.pos = None

        piece.move(_to)
        self._board[_to] = piece

        return target
