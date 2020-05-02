from abc import ABCMeta, abstractmethod
from typing import Set

from .position import Position
from .types import Color


class Piece(metaclass=ABCMeta):
    def __init__(self, color: Color, pos: Position):
        self.color = color
        self.pos = pos

    @abstractmethod
    def legal_moves(self) -> Set[Position]:
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


class Pawn(Piece):
    def legal_moves(self) -> Set[Position]:
        if self.pos.row == 8:
            return set({})
        return {Position(col=self.pos.col, row=self.pos.row + 1)}

    def legal_move(self, pos: Position) -> bool:
        return True

    def can_move(self) -> bool:
        return True
