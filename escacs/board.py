from copy import copy
from escacs.exceptions import PieceNotFound
from escacs.interfaces import IBoard
from escacs.interfaces import IPiece
from escacs.interfaces import ISquare
from escacs.square import Square
from escacs.types import Coordinate
from typing import Dict
from typing import List
from typing import Optional
from zope.interface import implementer

_none = object()


@implementer(IBoard)
class Board:
    """
    Stores the position of the pieces along the game.
    """

    def __init__(self):
        self.clear()

    def clear(self):
        self._board: Dict[ISquare, Optional[IPiece]] = {
            Square(col=col, row=row): None for col in range(8) for row in range(8)
        }

    def __getitem__(self, pos: Coordinate) -> Optional[IPiece]:
        if isinstance(pos, str):
            pos = Square(pos)
        return self._board[pos]

    def __setitem__(self, pos: Coordinate, piece: Optional[IPiece]) -> None:
        if isinstance(pos, str):
            pos = Square(pos)
        piece.board = self
        piece.move(pos)
        self._board[pos] = piece

    get_piece = __getitem__
    place_piece = __setitem__

    def path(self, _from: Coordinate, _to: Coordinate) -> List[Square]:
        """Returns the ordered list of squares that conform the shortest path
        between 2 board coordinates.
        """
        if isinstance(_from, str):
            _from = Square(_from)
        if isinstance(_to, str):
            _to = Square(_to)
        path = []
        while _from != _to:
            if _to.row > _from.row:
                _from.row += 1
            elif _to.row < _from.row:
                _from.row -= 1
            if _to.col > _from.col:
                _from.col += 1
            elif _to.col < _from.col:
                _from.col -= 1
            path.append(copy(_from))
        return path

    def move_piece(self, _from: Coordinate, _to: Coordinate):
        """Moves whichever piece is found in _from to _to positions. If no
        piece found, nothing is done.

        It does not check against valid chess moves.

        """
        if isinstance(_from, str):
            _from = Square(_from)
        if isinstance(_to, str):
            _to = Square(_to)
        piece: Optional[IPiece] = self[_from]
        if not piece:
            # No piece found
            return

        self[_from] = None
        self[_to] = piece
        piece.move(_to)

    def get_square(self, piece: IPiece) -> Square:
        for square, p in self._board.items():
            if not p:
                continue
            if p == piece:
                return square
        raise PieceNotFound(piece)
