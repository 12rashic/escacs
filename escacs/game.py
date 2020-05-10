from escacs import pieces
from escacs.board import Board
from escacs.exceptions import InvalidMove
from escacs.interfaces import IBoard
from escacs.interfaces import IGame
from escacs.interfaces import IPiece
from escacs.square import Square
from escacs.types import Color
from typing import cast
from typing import List
from typing import Optional
from typing import Tuple
from zope.interface import implementer


@implementer(IGame)
class Game:
    def __init__(self):
        self.start()

    def start(self):
        self._turn: Color = "white"
        self.moves: List[Tuple[Square, Square]] = []
        self.initialize_board()

    def initialize_board(self):
        self.board: IBoard = Board()
        for col in range(8):
            self.board[Square(col=col, row=1)] = pieces.Pawn("white", self.board)
            self.board[Square(col=col, row=6)] = pieces.Pawn("black", self.board)
        self.board["a1"] = pieces.Rook("white", self.board)
        self.board["h1"] = pieces.Rook("white", self.board)
        self.board["a8"] = pieces.Rook("black", self.board)
        self.board["h8"] = pieces.Rook("black", self.board)
        self.board["b1"] = pieces.Knight("white", self.board)
        self.board["g1"] = pieces.Knight("white", self.board)
        self.board["b8"] = pieces.Knight("black", self.board)
        self.board["g8"] = pieces.Knight("black", self.board)
        self.board["c1"] = pieces.Bishop("white", self.board)
        self.board["f1"] = pieces.Bishop("white", self.board)
        self.board["c8"] = pieces.Bishop("black", self.board)
        self.board["f8"] = pieces.Bishop("black", self.board)
        self.board["d1"] = pieces.Queen("white", self.board)
        self.board["d8"] = pieces.Queen("black", self.board)
        self.board["e1"] = pieces.King("white", self.board)
        self.board["e8"] = pieces.King("black", self.board)

    @property
    def turn(self) -> Color:
        return self._turn

    def pass_turn(self) -> None:
        if self._turn == "white":
            self._turn = cast(Color, "black")
        else:
            self._turn = cast(Color, "white")

    def player_move(self, _from: Square, _to: Square) -> Optional[IPiece]:
        """Move a piece from a square to another one. Checks agains valid
        moves. Returns the eaten piece, if any.

        """
        # Check that there is a piece in source square
        piece = self.board.get_piece(_from)
        if not piece:
            # No piece found
            raise InvalidMove(_from, _to)

        # Check that the piece is from the same color as the player
        if piece.color != self.turn:
            raise InvalidMove(_from, _to)

        # Check that it's a valid piece move
        all_moves = piece.all_moves(_from)
        if _to not in all_moves:
            raise InvalidMove(_from, _to)

        # TODO: Take into account moves where can take!
        # TODO: check that the move doesn't crash against any other
        # piece.
        # TODO: prevent moves that leave the king on check.
        # TODO: check for stalemate.
        taken: Optional[IPiece] = self.board.move_piece(_from, _to)
        self.moves.append((_from, _to))
        self.pass_turn()
        return taken
