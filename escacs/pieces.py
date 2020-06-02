from abc import ABCMeta
from abc import abstractmethod
from escacs.square import Square
from escacs.types import Color
from escacs.types import Coordinate
from escacs.utils import get_square
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple


class Piece(metaclass=ABCMeta):
    """Meta-class that encapsulates all comon piece logic.

    Keeps a pointer to the current board, to know the position of all
    other pieces of the game.

    Also keeps a pointer of its current position/square in the board.

    Attributes
    ----------
    color: Color
        states the color of the piece.
    board: Board
        object of the class Board.
    pos: Square
        object of the class Square.
    _deltas: list
        list of tuples which represent the sense of the directions in
        which the piece can move. Not always used. See Pawn, Knight
        and King pieces.
    abbr: str
        Abbreviation of the piece.
    points: int
        Points of the piece.
    """

    # Used to compute all possible moves per piece
    _deltas: Optional[List[Tuple[int, int]]] = None
    abbr: str = ""
    points: int = 0

    def __init__(self, color: Color, board, pos: Coordinate):
        self.color = color
        self.board = board
        self.pos: Square = get_square(pos)
        self.init()

    def init(self):
        pass

    def __repr__(self):
        kls_name = self.__class__.__name__
        if self.color == "black":
            kls_name = kls_name.lower()
        return kls_name

    @abstractmethod
    def all_moves(self) -> Set[Square]:
        """Returns all possible squares of the piece given the current
        position (this includes ilegal moves too)

        """
        ...

    def _all_moves(self) -> Set[Square]:
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
        _pos: Square = get_square(pos)
        self.pos = _pos

    def is_legal_move(self, pos: Coordinate) -> bool:
        return True


class Pawn(Piece):
    """Represents the pawn piece.

    Attributes
    ----------
    direction: int
        sense of the direction (always x = 0) of the pawn (1 or -1)
    start_row: int
        starting row of the pawn (1 or 6)

    """

    abbr = "P"
    points = 1

    def init(self):
        self.direction = 1 if self.color == "white" else -1
        self.start_row = 1 if self.color == "white" else 6

    def all_moves(self) -> Set[Square]:
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
    """Represents the Knight piece.

    """

    abbr = "N"
    points = 3

    def all_moves(self) -> Set[Square]:
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
    """Represents the Bishop piece.

    """

    abbr = "B"
    points = 3
    _deltas = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def all_moves(self) -> Set[Square]:
        return self._all_moves()


class Rook(Piece):
    """Represents the Rook piece.

    """

    abbr = "R"
    points = 5
    _deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def all_moves(self) -> Set[Square]:
        return self._all_moves()


class Queen(Piece):
    """Represents the Queen piece.

    """

    abbr = "Q"
    points = 9
    _deltas = Rook._deltas + Bishop._deltas

    def all_moves(self) -> Set[Square]:
        return self._all_moves()


class King(Piece):
    """Represents the King piece.

    """

    abbr = "K"

    def all_moves(self) -> Set[Square]:
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
