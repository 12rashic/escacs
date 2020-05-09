import os
from typing import Tuple

from escacs.board import Board
from escacs.exceptions import InvalidSquare
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
        if len(move) != 4:
            print("Invalid move! Try again...")
            return self.get_move()
        try:
            return Square(move[:2]), Square(move[2:])
        except InvalidSquare:
            print("Invalid move! Try again...")
            return self.get_move()

    def unicode_print(self) -> None:
        tmp = [" ", "a", "b", "c", "d", "e", "f", "g", "h"]
        print(" ".join(tmp))
        for row in reversed(range(8)):
            print(row + 1),
            for col in range(8):
                sq = Square(col=col, row=row)
                piece: Optional[Piece] = self.board[sq]
                abbr = piece.abbriviation
                if piece.color == "black":
                    abbr = abbr.lower()
                print(UNICODE_PIECES[abbr]),
            print(row + 1),
            print()
        tmp = ["a", "b", "c", "d", "e", "f", "g", "h"]
        print(" ".join(tmp))


"""
print "\n", ("%s's turn\n" % self.board.player_turn.capitalize()).center(28)
        for number in self.board.axis_x[::-1]:
            print " " + str(number) + " ",
            for letter in self.board.axis_y:
                piece = self.board[letter+str(number)]
                if piece is not None:
                    print UNICODE_PIECES[piece.abbriviation] + ' ',
                else: print '  ',
            print "\n"
        print "    " + "  ".join(self.board.axis_y)
"""


def run(board: Board):
    try:
        gui = BoardConsoleGUI(board)
        while True:
            gui.move()
    except (KeyboardInterrupt, EOFError):
        print("Bye!")
        os.system("clear")
        exit(0)


class InvalidGUIMove(Exception):
    ...


if __name__ == "__main__":
    print("Welcome to escacs!")
    print("=" * 20)
    print("State a move (e.g. a3b4). 'exit' to leave")
    input("Press any key to start playing")
    board = Board()
    board.initialize()
    run(board)
