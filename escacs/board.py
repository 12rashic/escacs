from typing import Game, Optional

from pieces import Piece


class Board:
    def __init__(self):
        self._board: Dict[int : Dict[int, Optional[Piece]]] = {}
        for col in range(8):
            self._board[col] = {}
            for row in range(8):
                self._board[col][row] = None

    def __getitem__(self, val: Union[str, Position]) -> Optional[Piece]:
        if isinstance(val, str):
            pos = _from_string(val)
        return self._board[pos.column][pos.col]


def _from_string(pos: str) -> Position:
    # TODO
    return Position(row=0, col=0)
