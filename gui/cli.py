from escacs.board import Board
from escacs.exceptions import CheckMate
from escacs.exceptions import Draw
from escacs.exceptions import InvalidMove
from escacs.exceptions import InvalidSquare
from escacs.exceptions import Stalemate
from escacs.pieces import Piece
from escacs.square import Square
from escacs.types import Color
from typing import Optional
from typing import Tuple

import os

UNICODE_PIECES = {
    "r": "♜",
    "n": "♞",
    "b": "♝",
    "q": "♛",
    "k": "♚",
    "p": "♟",
    "R": "♖",
    "N": "♘",
    "B": "♗",
    "Q": "♕",
    "K": "♔",
    "P": "♙",
    None: " ",
}


class BoardConsoleGUI:
    def __init__(self, board: Board):
        self.board = board

    def move(self):
        os.system("clear")
        self.print_board()
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

    def print_board(self) -> None:
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
                    abbr = piece.abbr
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
    except CheckMate as cm:
        print(f"{cm.color} won!")
    except Resign as r:
        print(f"{r.color} resigned")
    except Draw:
        print(f"Game ended in draw! 1/2")
    except Stalemate:
        print("Stalemate! 1/2")
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        print("Bye!")
        exit()


class InvalidGUIMove(Exception):
    ...


class Resign(Exception):
    def __init__(self, color: Color):
        self.color = color


if __name__ == "__main__":
    print("Welcome to escacs!")
    print("=" * 18)
    print()
    print("State a move in coordinates notation (e.g. a3b4). 'exit' to leave")
    input("Press any key to start playing...")
    board = Board()
    board.initialize()
    run(board)
