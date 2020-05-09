import os
from typing import Optional, Tuple

from escacs.board import Board
from escacs.exceptions import InvalidMove, InvalidSquare
from escacs.pieces import Piece
from escacs.square import Square

UNICODE_PIECES = {
    "r": u"♜",
    "n": u"♞",
    "b": u"♝",
    "q": u"♛",
    "k": u"♚",
    "p": u"♟",
    "R": u"♖",
    "N": u"♘",
    "B": u"♗",
    "Q": u"♕",
    "K": u"♔",
    "P": u"♙",
    None: " ",
}


class BoardConsoleGUI:
    def __init__(self, board: Board):
        self.board = board

    def move(self):
        os.system("clear")
        self.unicode_print()
        _from, _to = self.get_move()
        self.board.move(_from, _to)

    def get_move(self) -> Tuple[Square, Square]:
        move = input(">>> ")
        if move == "exit":
            raise KeyboardInterrupt
        try:
            assert len(move) == 4
            return Square(move[:2]), Square(move[2:])
        except (AssertionError, InvalidSquare, InvalidMove):
            print("Invalid move! Try again...")
            return self.get_move()

    def unicode_print(self) -> None:
        tmp = [" ", "a", "b", "c", "d", "e", "f", "g", "h"]
        print(" ".join(tmp))
        for row in reversed(range(8)):
            rowprint = []
            rowprint.append(str(row + 1))
            for col in range(8):
                sq = Square(col=col, row=row)
                piece: Optional[Piece] = self.board[sq]
                if piece is None:
                    rowprint.append(" ")
                else:
                    abbr = piece.abbriviation
                    if piece.color == "black":
                        abbr = abbr.lower()
                    rowprint.append(UNICODE_PIECES[abbr])
            rowprint.append(str(row + 1))
            print(" ".join(rowprint))
        print(" ".join(tmp))


def run(board: Board):
    try:
        gui = BoardConsoleGUI(board)
        while True:
            gui.move()
    except (KeyboardInterrupt, EOFError):
        print("Bye!")
        os.system("clear")
        exit()


class InvalidGUIMove(Exception):
    ...


if __name__ == "__main__":
    print("Welcome to escacs!")
    print("=" * 18)
    print()
    print("State a move in coordinates notation (e.g. a3b4). 'exit' to leave")
    input("Press any key to start playing...")
    board = Board()
    board.initialize()
    run(board)
