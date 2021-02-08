from board import Board
from copy import deepcopy


class GameState:
    """
    Class to represent the state of the game.
    - board = stores board information in a certain state
    - current_player = stores current_player information in a specified state
    - opponent = stores opponent information in specified state
    """
    def __init__(self, Board, Player1, Player2):
        """ Constructor """
        self.board = deepcopy(Board)
        self.current_player = deepcopy(Player1)
        self.opponent = deepcopy(Player2)

    def next_turn(self):
        """ Switchs player simulating a turn """
        temp = self.current_player
        self.current_player = self.opponent
        self.opponent = temp

