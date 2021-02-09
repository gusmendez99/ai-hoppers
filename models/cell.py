from settings import *


class Cell:
    """
    Class to represent every cell in board
    - region
    - player_owner:
        0 if empty, 1 for player1 and 2 for player2
    """

    def __init__(self, player_owner, region):
        """ Constructor """
        self.player_owner = player_owner
        self.region = region

    def get_symbol(self):
        if self.player_owner == PLAYER_ONE_VALUE:
            return "♟"
        elif self.player_owner == PLAYER_TWO_VALUE:
            return "♙"
        else:
            return "x"

    def set_player_owner(self, player_owner):
        self.player_owner = player_owner

    def set_region(self, region):
        self.region = region

    def __str__(self):
        return f"{self.get_symbol()}"
