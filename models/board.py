from models.cell import Cell
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
        self.cells = [
            [Cell(EMPTY_CELL_VALUE, EMPTY_CELL_VALUE) for j in range(self.size)]
            for i in range(self.size)
        ]
        self.initialize_board()

    def print_board(self):
        """ Prints the current board state """
        print("\n")
        print("x ", *range(self.size))

        for i in range(self.size):
            print("{} |".format(i), end="")
            for j in range(self.size):
                print(self.cells[i][j], end="")
                print("", end="|")
            print()
        print("\n")

    def initialize_board(self):
        """ sets the initial state """
        self.set_player_regions()

    def set_player_regions(self):
        middle = int(self.size / 2)
        for i in range(middle):
            for j in range(middle):
                if i + j < middle:
                    self.cells[i][j].set_region(PLAYER_ONE_VALUE)

        for i in range(middle, self.size):
            for j in range(middle, i + 1):
                offset = i - j
                self.cells[i][self.size - 1 - offset].set_region(PLAYER_TWO_VALUE)

    def set_pawns_position(self, player1, player2):
        """ assign each of the positions of player1 and player2's pawns to the board cells """
        for pawn in player1.pawn_array:
            self.cells[pawn.current_position.x][pawn.current_position.y].set_player_owner(
                PLAYER_ONE_VALUE
            )
        for pawn in player2.pawn_array:
            self.cells[pawn.current_position.x][pawn.current_position.y].set_player_owner(
                PLAYER_TWO_VALUE
            )

    def check_winner(self, no_player):
        """ Checks if game has ended - someone won """
        middle = int(self.size / 2)
        at_least_one_reached_opponent_region = False

        if no_player == PLAYER_ONE_VALUE:
            for i in range(middle, self.size):
                for j in range(middle, i + 1):
                    offset = i - j
                    # or (
                    #    self.cells[i][self.size - 1 - offset].player_owner == EMPTY_CELL_VALUE
                    #):
                    if self.cells[i][self.size - 1 - offset].player_owner == EMPTY_CELL_VALUE:
                        return False
                    if self.cells[i][self.size - 1 - offset].player_owner == PLAYER_ONE_VALUE:
                        at_least_one_reached_opponent_region = True

            if not at_least_one_reached_opponent_region: return False
            return True

        elif no_player == PLAYER_TWO_VALUE:
            for i in range(middle):
                for j in range(middle):
                    if i + j < middle:
                        #if () or (
                        #    self.cells[i][j].player_owner == EMPTY_CELL_VALUE
                        #):
                        if self.cells[i][j].player_owner == EMPTY_CELL_VALUE:
                            return False
                        if self.cells[i][j].player_owner == PLAYER_TWO_VALUE:
                            at_least_one_reached_opponent_region = True

            if not at_least_one_reached_opponent_region: return False
            return True
