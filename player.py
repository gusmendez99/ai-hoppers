from settings import *


class Position:
    """
    Class to define position
    - x = line
    - y = column
    """

    def __init__(self, x, y):
        """ Constructor """
        self.x = x
        self.y = y

    def euclidean(self, G):
        """ Calculates the euclidean distance from own position to position G (goal) """
        return ((self.x - G.x) ** 2 + (self.y - G.y) ** 2) ** 0.5

    def __eq__(self, P):
        return (self.x == P.x) and (self.y == P.y)

    # TODO: fix the representation as (y,x) instead of (x,y) on print
    def __str__(self):
        return f"({self.x},{self.y})"


class Player:
    """
    Class for player agent, consists in two props:
    - no_player
    - pawn_array
    """

    def __init__(self, no_player, size):
        """ Player Constructor """
        self.no_player = no_player
        self.pawn_array = []
        if no_player == PLAYER_ONE_VALUE:
            # self.set_player_one(size)
            pass
        else:
            # self.set_player_two(size)
            pass
