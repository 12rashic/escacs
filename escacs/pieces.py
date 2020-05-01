from abc import ABCMeta, abstractmethod
from types import Board, Color, Position
from typing import List


class Piece(metaclass=ABCMeta):
    def __init__(self, board: Board, color: Color, pos: Position):
        self.board = board
        self.color = color
        self.pos = pos

    @abstractmethod
    def legal_moves(self) -> List[Position]:
        """Returns the complete list of legal moves given the current
        position.

        """
        ...

    @abstractmethod
    def legal_move(self, pos: Position) -> bool:
        """
        Returns whether the input position is a legal move.
        """
        ...

    @abstractmethod
    def can_move(self) -> bool:
        """Returns whether the piece can move at all at current position.

        """
        ...

    def move(self, pos: Position):
        self.pos = pos

    def row(self):
        return self.pos.row

    def column(self):
        return self.pos.column


class Pawn(Piece):
    def legal_moves(self) -> List[Position]:
        return [Position(0, 1)]

    def legal_move(self, pos: Position) -> bool:
        return True

    def can_move(self) -> bool:
        return True
