from copy import deepcopy


class GameState:
    """
    Class to represent the state of the game.
    - board = stores board information in a certain state
    - current_player = stores current_player information in a specified state
    - opponent = stores opponent information in specified state
    """

    def __init__(self, board, player_1, player_2):
        """ Constructor """
        self.board = deepcopy(board)
        self.current_player = deepcopy(player_1)
        self.opponent = deepcopy(player_2)

    def next_turn(self):
        """ Switches player simulating a turn """
        temp = self.current_player
        self.current_player = self.opponent
        self.opponent = temp