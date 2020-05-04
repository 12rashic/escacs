from typing import Dict, Optional, Union

from .pieces import *
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

    def init_board(self):
        # Pawns first
        for col in "abcdefgh":
            self[f"{col}2"] = Pawn("white")
            self[f"{col}7"] = Pawn("black")

        # Rooks
        self["a1"] = Rook("white")
        self["h1"] = Rook("white")
        self["a8"] = Rook("black")
        self["h8"] = Rook("black")

        # Knights
        self["b1"] = Knight("white")
        self["g1"] = Knight("white")
        self["b8"] = Knight("black")
        self["g8"] = Knight("black")

        # Bishop
        self["c1"] = Bishop("white")
        self["f1"] = Bishop("white")
        self["c8"] = Bishop("black")
        self["f8"] = Bishop("black")

        # Queen and King
        self["d1"] = Queen("white")
        self["d8"] = Queen("black")
        self["e1"] = King("white")
        self["e8"] = King("black")
