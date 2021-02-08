from settings import *
from pawn import Pawn, Position


class Player:
    """
    Class for player agent, consists in two props:
    - no_player
    - pawn_array
    """

    def __init__(self, no_player):
        """ Player Constructor """
        self.no_player = no_player
        self.pawn_array = []
        if no_player == PLAYER_ONE_VALUE:
            self.set_player_one(BOARD_SIZE)
        else:
            self.set_player_two(BOARD_SIZE)

    def set_player_one(self, board_size):
        """ Sets the pawn values for player 1 at the start of the game """
        middle = int(board_size / 2)
        for i in range(middle):
            for j in range(middle):
                if i + j < middle:
                    self.add_pawn(Pawn(self.no_player, Position(i, j)))

    def set_player_two(self, board_size):
        """ Sets the pawn values for player 2 at the start of the game """
        middle = int(board_size / 2)
        for i in range(middle, board_size):
            for j in range(middle, i + 1):
                offset = i - j
                x = i
                y = board_size - 1 - offset
                self.add_pawn(Pawn(self.no_player, Position(x, y)))

    def load_array(self, array):
        """ Assign each player's pawn position with a new set of positions based on loaded data """
        index = 0
        for pawn in self.pawn_array:
            pawn.current_position = array[index]
            index += 1

    def add_pawn(self, pawn):
        self.pawn_array.append(pawn)

    def print_pawns(self):
        """ Prints pawn info for each item on pawn array """
        index = 0
        for pawn in self.pawn_array:
            print(f"Pawn {index} --> {pawn}")
            index += 1

    def get_pawn_id(self, position):
        """ Gets a pawn by id """
        for index in range(len(self.pawn_array)):
            if self.pawn_array[index].current_position == position:
                return index

        return -1

    def move_pown(self, pawn_id, position, board):
        self.pawn_array[pawn_id].move(position, board)

    def get_possible_moves(self, pawn_id, board):
        """
        Returns all possible moves (as list) of a pawn with the pawn_id on the board
        """
        possible_moves_queue = []
        simulation_queue = []

        pawn = self.pawn_array[pawn_id]
        x_pos = pawn.current_position.x
        y_pos = pawn.current_position.y

        # move one step for up down left right and diagonal
        for x in range(-1, 2):
            for y in range(-1, 2):
                if pawn.is_valid_move(Position(x_pos + x, y_pos + y), board):
                    possible_moves_queue.append(Position(x_pos + x, y_pos + y))

        # move jump for up down left right
        simulation_queue.append(pawn.current_position)
        current_position = pawn.current_position

        # search for possible moves using BFS (Breadth First Search).
        while simulation_queue:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if pawn.is_inside(
                        Position(current_position.x + x, current_position.y + y), board
                    ):
                        if pawn.has_owner(
                            Position(current_position.x + x, current_position.y + y),
                            board,
                        ):
                            temp_position = Position(
                                current_position.x + 2 * x, current_position.y + 2 * y
                            )
                            if pawn.is_valid_move(temp_position, board) and (
                                temp_position not in possible_moves_queue
                            ):
                                simulation_queue.append(temp_position)
                                possible_moves_queue.append(temp_position)

            # validates that queue node is empty and then, terminates
            if simulation_queue:
                new_position = simulation_queue.pop()
                current_position = new_position

        return possible_moves_queue
