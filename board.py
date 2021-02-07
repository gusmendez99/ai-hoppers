from cell import Cell
from settings import *

class Board:
    """
    Class to represent a new Hoppers board, contains:
    - size
    - cells (nxn board)
    """
    def __init__(self):
        """ Constructor """
        self.size = BOARD_SIZE
        self.cells = [[ Cell(EMPTY_CELL_VALUE) for j in range(self.size)] for i in range(self.size)]
        self.initialize_board()

    def print_board(self):
        """ Prints the current board state """
        for i in range(self.size):
            print("|", end="")
            for j in range(self.size):
                print(self.cells[i][j], end="")
                print("", end="|")
            print()

    def initialize_board(self):
        """ sets the initial state """
        self.set_player_one_region()
        self.set_player_two_region()

    def set_player_one_region(self):
        middle = int(self.size / 2)
        for i in range(middle):
            for j in range(middle):
                if (i + j < middle):
                    self.cells[i][j].set_owner(PLAYER_ONE_VALUE)

    def set_player_two_region(self):
        middle = int(self.size / 2)
        for i in range(middle, self.size):
            for j in range(middle, i + 1):
                offset = i - j
                self.cells[i][self.size - 1 - offset].set_owner(PLAYER_TWO_VALUE)

    def set_pawns_position(self, player1, player2):
        """ assign each of the positions of player1 and player2's pawns to the board cells """
        for pawn in player1.pawn_array:
            self.cells[pawn.current_position.x][pawn.current_position.y].set_owner(
                PLAYER_ONE_VALUE
            )
        for pawn in player2.pawn_array:
            self.cells[pawn.current_position.x][pawn.current_position.y].set_owner(
                PLAYER_TWO_VALUE
            )

    def check_winner(self, no_player):
        """ Checks if game has ended - someone won """
        if (no_player == PLAYER_ONE_VALUE):
            middle = int(self.size / 2)
            for i in range(middle, self.size):
                for j in range(middle, i + 1):
                    offset = i - j
                    if (self.cells[i][self.size - 1 - offset].owner
                            == PLAYER_TWO_VALUE) or (self.cells[i][self.size - 1 - temp].owner
                                      == EMPTY_CELL_VALUE):
                        return False
            return True

        elif (no_player == PLAYER_TWO_VALUE):
            middle = int(self.size / 2)
            for i in range(middle):
                for j in range(middle):
                    if (i + j < middle):
                        if (self.cells[i][j].owner
                                == PLAYER_ONE_VALUE) or (self.cells[i][j].owner == EMPTY_CELL_VALUE):
                            return False
            return True
