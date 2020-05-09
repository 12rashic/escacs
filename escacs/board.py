from typing import Dict, Optional, Union

from .pieces import Bishop, King, Knight, Pawn, Piece, Queen, Rook
from .square import Square

_none = object()


class BaseBoard:
    """
    Stores the position of the pieces along the game.
    """

    def __init__(self):
        self.clear()

    def clear(self):
        self._board: Dict[Square, Optional[Piece]] = {
            Square(col=col, row=row): None for col in range(8) for row in range(8)
        }

    def __getitem__(self, pos: Union[str, Square]) -> Optional[Piece]:
        if isinstance(pos, str):
            pos = Square(pos)
        return self._board[pos]

    def __setitem__(self, pos: Union[str, Square], piece: Piece) -> None:
        if isinstance(pos, str):
            pos = Square(pos)
        self._board[pos] = piece

    def move(self, _from: Union[str, Square], _to: Union[str, Square]):
        """Moves whatever piece is found in _from to _to positions. If no
        piece found, nothing is done.

        This does not check against valid chess moves.
        """
        if isinstance(_from, str):
            _from = Square(_from)
        if isinstance(_to, str):
            _to = Square(_to)
        piece: Optional[Piece] = self[_from]
        if not piece:
            # No piece found
            return
        self[_from] = None
        self[_to] = piece


class Board(BaseBoard):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        for col in range(8):
            self[Square(col=col, row=1)] = Pawn("white")
            self[Square(col=col, row=6)] = Pawn("black")
        self["a1"] = Rook("white")
        self["h1"] = Rook("white")
        self["a8"] = Rook("black")
        self["h8"] = Rook("black")
        self["b1"] = Knight("white")
        self["g1"] = Knight("white")
        self["b8"] = Knight("black")
        self["g8"] = Knight("black")
        self["c1"] = Bishop("white")
        self["f1"] = Bishop("white")
        self["c8"] = Bishop("black")
        self["f8"] = Bishop("black")
        self["d1"] = Queen("white")
        self["d8"] = Queen("black")
        self["e1"] = King("white")
        self["e8"] = King("black")
