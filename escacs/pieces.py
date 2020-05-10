from .interfaces import IBoard
from .interfaces import IPiece
from .square import Square
from .types import Color
from abc import ABCMeta
from abc import abstractmethod
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from zope.interface import implementer


@implementer(IPiece)
class Piece(metaclass=ABCMeta):
    """Meta-class that encapsulates all comon piece logic.

    Keeps a pointer to the current board, to know the position of all
    other pieces of the game.
    """

    # Used to compute all possible moves per piece
    _deltas: Optional[List[Tuple[int, int]]] = None
    abbr: str = ""

    def __init__(self, color: Color, board: IBoard):
        self.color = color
        self.board = board
        self.init()

    def init(self):
        pass

    def __repr__(self):
        kls_name = self.__class__.__name__
        if self.color == "black":
            kls_name = kls_name.lower()
        return kls_name

    @abstractmethod
    def all_moves(self, pos: Square) -> Set[Square]:
        """Returns all possible squares of the piece given the current
        position (this includes ilegal moves too)

        """
        ...

    def _all_moves(self, pos: Square) -> Set[Square]:
        moves = set({})
        for vector in self._deltas or []:
            x, y = vector
            factor = 1
            while True:
                col = pos.col
                row = pos.row
                if x != 0:
                    col += x * factor
                if y != 0:
                    row += y * factor
                factor = factor + 1
                if not self._in_board(col, row):
                    break
                else:
                    moves.update({Square(col=col, row=row)})
        return moves

    def _in_board(self, col, row) -> bool:
        return col in range(8) and row in range(8)


class Pawn(Piece):
    abbr = "P"

    def init(self):
        self.direction = 1 if self.color == "white" else -1
        self.start_row = 1 if self.color == "white" else 6

    def all_moves(self, pos: Square) -> Set[Square]:
        moves = set({})

        # On starting position, pawn can jump 2 squares
        if pos.row == self.start_row:
            col = pos.col
            row = pos.row + (self.direction * 2)
            moves.update({Square(col=col, row=row)})

        # Moving one square ahead + capturing moves
        for side in (-1, 0, 1):
            row = pos.row + self.direction
            col = pos.col + side
            if self._in_board(col, row):
                moves.update({Square(col=col, row=row)})

        return moves


class Knight(Piece):
    abbr = "N"

    def all_moves(self, pos: Square) -> Set[Square]:
        moves = set({})
        for (x, y) in [
            [1, 2],
            [1, -2],
            [2, 1],
            [2, -1],
            [-1, 2],
            [-1, -2],
            [-2, 1],
            [-2, -1],
        ]:
            col = pos.col + x
            row = pos.row + y
            if not self._in_board(col, row):
                continue
            moves.update({Square(col=col, row=row)})
        return moves


class Bishop(Piece):
    abbr = "B"

    _deltas = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def all_moves(self, pos: Square) -> Set[Square]:
        return self._all_moves(pos)


class Rook(Piece):
    abbr = "R"

    _deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def all_moves(self, pos: Square) -> Set[Square]:
        return self._all_moves(pos)


class Queen(Piece):
    abbr = "Q"
    _deltas = Rook._deltas + Bishop._deltas

    def all_moves(self, pos: Square) -> Set[Square]:
        return self._all_moves(pos)


class King(Piece):
    abbr = "K"

    def all_moves(self, pos: Square) -> Set[Square]:
        moves = set({})
        for (x, y) in [
            [1, 0],
            [1, 1],
            [1, -1],
            [0, -1],
            [0, 1],
            [-1, 0],
            [-1, 1],
            [-1, -1],
        ]:
            col = pos.col + x
            row = pos.row + y
            if not self._in_board(col, row):
                continue
            moves.update({Square(col=col, row=row)})
        return moves
