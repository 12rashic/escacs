from typing import Dict, Optional, Union

from .pieces import Piece
from .position import Position


class Board:
    """
    Stores the position of the pieces along the game.
    """

    def __init__(self):
        self._board: Dict[int : Dict[int, Optional[Piece]]] = {}
        for col in range(8):
            self._board[col] = {}
            for row in range(8):
                self._board[col][row] = None

    def __getitem__(self, pos: Union[str, Position]) -> Optional[Piece]:
        if isinstance(pos, str):
            pos = Position.from_string(pos)
        return self._board[pos.col][pos.col]

    def __setitem__(self, pos: Union[str, Position], piece: Piece) -> None:
        if isinstance(pos, str):
            pos = Position.from_string(pos)
        self._board[pos.col][pos.col] = piece
