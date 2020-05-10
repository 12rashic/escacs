from abc import ABCMeta
from abc import abstractmethod
from escacs.interfaces import IBoard
from escacs.interfaces import IPiece
from escacs.interfaces import ISquare
from escacs.square import Square
from escacs.types import Color
from escacs.types import Coordinate
from escacs.utils import get_square
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

    Also keeps a pointer of its current position/square in the board.
    """

    # Used to compute all possible moves per piece
    _deltas: Optional[List[Tuple[int, int]]] = None
    abbr: str = ""
    points: int = 0

    def __init__(self, color: Color, board: IBoard, pos: Coordinate):
        self.color = color
        self.board = board
        self.pos: ISquare = get_square(pos)
        self.init()

    def init(self):
        pass

    def __repr__(self):
        kls_name = self.__class__.__name__
        if self.color == "black":
            kls_name = kls_name.lower()
        return kls_name

    @abstractmethod
    def all_moves(self) -> Set[ISquare]:
        """Returns all possible squares of the piece given the current
        position (this includes ilegal moves too)

        """
        ...

    def _all_moves(self) -> Set[ISquare]:
        moves = set({})
        for vector in self._deltas or []:
            x, y = vector
            factor = 1
            while True:
                col = self.pos.col
                row = self.pos.row
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

    def move(self, pos: Coordinate) -> None:
        pos: ISquare = get_square(pos)
        self.pos = pos


class Pawn(Piece):
    abbr = "P"
    points = 1

    def init(self):
        self.direction = 1 if self.color == "white" else -1
        self.start_row = 1 if self.color == "white" else 6

    def all_moves(self) -> Set[ISquare]:
        moves = set({})

        # On starting position, pawn can jump 2 squares
        pos = self.pos
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
    points = 3

    def all_moves(self) -> Set[ISquare]:
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
            col = self.pos.col + x
            row = self.pos.row + y
            if not self._in_board(col, row):
                continue
            moves.update({Square(col=col, row=row)})
        return moves


class Bishop(Piece):
    abbr = "B"
    points = 3
    _deltas = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def all_moves(self) -> Set[ISquare]:
        return self._all_moves()


class Rook(Piece):
    abbr = "R"
    points = 5
    _deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def all_moves(self) -> Set[ISquare]:
        return self._all_moves()


class Queen(Piece):
    abbr = "Q"
    points = 9
    _deltas = Rook._deltas + Bishop._deltas

    def all_moves(self) -> Set[ISquare]:
        return self._all_moves()


class King(Piece):
    abbr = "K"

    def all_moves(self) -> Set[ISquare]:
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
            col = self.pos.col + x
            row = self.pos.row + y
            if not self._in_board(col, row):
                continue
            moves.update({Square(col=col, row=row)})
        return moves
