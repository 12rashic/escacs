from typing import Dict, Optional, Union

from .pieces import Piece
from .square import Square


class Board:
    """
    Stores the position of the pieces along the game.
    """

    def __init__(self):
        self._board: Dict[int, Dict[int, Optional[Piece]]] = {}
        for col in range(8):
            self._board[col] = {}
            for row in range(8):
                self._board[col][row] = None

    def __getitem__(self, pos: Union[str, Square]) -> Optional[Piece]:
        if isinstance(pos, str):
            pos = Square(pos)
        return self._board[pos.col][pos.col]

    def __setitem__(self, pos: Union[str, Square], piece: Piece) -> None:
        if isinstance(pos, str):
            pos = Square(pos)
        self._board[pos.col][pos.col] = piece
