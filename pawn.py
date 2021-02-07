from cell import Cell
from settings import *


class Pawn:
    """
    Class for each existing pawn in board
     - pawn id
     - current_position
    """

    def __init__(self, owner, current_position):
        """ Constructor """
        self.pawn_owner = owner
        self.current_position = current_position

    def move(self, position, board):
        """ Move the position from current_position to a new position on the board """
        if self.is_valid_move(position, board):
            # set cell to be empty, i.e. no pawns occupy (empty)
            board.cells[self.current_position.x][self.current_position.y].set_owner(
                EMPTY_CELL_VALUE
            )

            # assign new position
            self.current_position = position
            board.cells[position.x][position.y].set_owner(self.pawn_owner)

    def is_valid_move(self, position, board):
        # position out of range
        if self.is_inside(position, board):
            return False

        if self.has_owner(position, board):
            return False

        # Make sure that when you have entered, you cannot leave and vice versa
        if self.is_own_or_reached_region(position, board):
            return False
        return True

    def is_inside(self, position, board):
        """ Checks if new position is outside the range of the board """
        if (
            position.x < 0
            or position.x >= board.size
            or position.y < 0
            or position.y >= board.size
        ):
            return True
        else:
            return False

    def has_owner(self, position, board):
        """ Checks if position on the board has been filled by another pawn """
        if board.cell[position.x][position.y].owner != 0:
            return True
        else:
            return False

    def is_own_or_reached_region(self, position, board):
        """ Checks when you have entered, you cannot leave region and vice versa """
        if (
            board.cell[position.x][position.y].region == self.pawn_owner
            and board.cell[self.current_position.x][self.current_position.y].region == 0
        ):
            return True

        opponent = PLAYER_TWO_VALUE
        if self.pawn_owner == PLAYER_TWO_VALUE:
            opponent = PLAYER_TWO_VALUE

        if (
            board.cell[position.x][position.y].region == 0
            or board.cell[position.x][position.y].region == self.pawn_owner
        ) and board.cell[self.current_position.x][
            self.current_position.y
        ].region == opponent:
            return True
        return False

    def print_pawn(self):
        """ Prints on terminal """
        print("P.Owner: {} {}", self.pawn_owner, self.current_position)
