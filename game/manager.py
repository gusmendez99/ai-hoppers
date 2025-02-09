import time
import math
from models.board import Board
from models.player import Player
from ai.minimax import minimax, minimax_local_search

from game.state import GameState
from settings import *


class GameManager:
    """
    Class to represent Game Manager, manages the game flow and store all important game info
     - current_player
     - opponent
     - board
     - mode (1 vs 1, or 1 vs AI Minimax)
     - player_pawn_color = player 1 (white) or player 2 (black) choice
    """

    def __init__(self, mode, player_pawn_color):
        """ Constructor """
        self.current_player = Player(PLAYER_ONE_VALUE)
        self.opponent = Player(PLAYER_TWO_VALUE)
        self.board = Board()
        self.board.set_pawns_position(self.current_player, self.opponent)
        self.mode = mode
        self.time_limit = TIME_LIMIT
        self.player_pawn_color = player_pawn_color
        self.total_time = 0
        self.depth_mode = MINIMAX_DEPTH

    def show_game(self):
        self.board.print_board()

    def next_turn(self):
        """ Switches the player's turn after current_player has taken the last move """
        temp = self.current_player
        self.current_player = self.opponent
        self.opponent = temp

    def start_game(self):
        """ Displays the game menu based on game mode """
        if self.mode == P_VS_P_MODE:
            self.player_vs_player()
        elif self.mode == P_VS_MINIMAX:
            self.player_vs_minimax()
        elif self.mode == P_VS_MINIMAX_LS:
            self.player_vs_minimax_ls()
        elif self.mode == MINIMAX_VS_MINIMAX_LS:
            self.minimax_vs_minimax_ls()

    # --------------------------------------
    #       GAME INTERFACE - Terminal
    # --------------------------------------

    def minimax_move(self):
        """ Run Minimax bot on bot's turn """
        print("PLAYER {} - MINIMAX TURN!".format(self.current_player.no_player))
        # Minimax Process
        initial_time = time.time()
        current_state = GameState(self.board, self.current_player, self.opponent)
        minimax_state, _ = minimax(
            current_state,
            self.depth_mode,
            time.time() + self.time_limit,
            -math.inf,
            math.inf,
            self.current_player.no_player,
        )
        delta_time = time.time() - initial_time
        self.total_time += delta_time
        print("Exec time = {} seconds".format(delta_time))

        self.assign_state(minimax_state)
        return self.board.check_winner(self.current_player.no_player)

    def assign_state(self, new_state):
        """ Assign new game state after bot takes a step """
        self.current_player = new_state.current_player
        self.opponent = new_state.opponent
        self.board = new_state.board

    def player_vs_player(self):
        """ Mode P1 vs P2"""
        has_game_ended = False
        while not (has_game_ended):

            self.show_game()
            print("PLAYER {} TURN!".format(self.current_player.no_player))
            self.current_player.print_pawns()

            chosen_pawn_id = int(input("Choose which Pawn ID to play with: "))
            possible_moves = self.current_player.listAllPossibleMove(
                chosen_pawn_id, self.board
            )

            for i in range(len(possible_moves)):
                print("{}. {}".format(i + 1, possible_moves[i]))

            chosen_move = int(input("Select the desired move by entering the number: "))
            self.current_player.move_pawn(
                chosen_pawn_id, possible_moves[chosen_move - 1], self.board
            )
            if self.board.check_winner(self.current_player.no_player):
                has_game_ended = True
            else:
                self.next_turn()

        self.show_game()
        print("Player {} win the game!".format(self.current_player.no_player))

    """
    Minimax & Minimax with LS
    """
    def player_vs_minimax(self):
        """ Mode: Player vs Minimax Bot"""
        has_game_ended = False
        bot_total_time = 0

        while not (has_game_ended):
            self.show_game()

            # Minimax bot's turn
            if self.current_player.no_player != self.player_pawn_color:
                print("PLAYER {} - MINIMAX TURN!".format(self.current_player.no_player))

                # Minimax process
                current_state = GameState(
                    self.board, self.current_player, self.opponent
                )
                initial_time = time.time()
                minimax_state, _ = minimax(
                    current_state,
                    self.depth_mode - 1,
                    time.time() + self.time_limit,
                    -math.inf,
                    math.inf,
                    self.current_player.no_player,
                )
                self.assign_state(minimax_state)
                delta_time = time.time() - initial_time
                bot_total_time += delta_time
                print("Exec time = {} seconds".format(delta_time))

                print(
                    "PLAYER {} MINIMAX has played".format(self.current_player.no_player)
                )

            # Human player turn
            else:
                print("PLAYER {} TURN!".format(self.current_player.no_player))
                self.current_player.print_pawns()
                chosen_pawn_id = int(input("Choose which Pawn ID to play with: "))

                possible_moves = self.current_player.get_possible_moves(
                    chosen_pawn_id, self.board
                )

                for i in range(len(possible_moves)):
                    print("{}. {}".format(i + 1, possible_moves[i]))

                chosen_move = int(
                    input("Select the desired move by entering the number: ")
                )
                self.current_player.move_pawn(
                    chosen_pawn_id, possible_moves[chosen_move - 1], self.board
                )

            # Check for game final status
            if self.board.check_winner(self.current_player.no_player):
                has_game_ended = True
            else:
                self.next_turn()

        self.show_game()
        print("Player {} won the game!".format(self.current_player.no_player))
        print("BOT Time: {} ".format(bot_total_time))

    def player_vs_minimax_ls(self):
        """ Mode: Player VS Minimax LS Bot"""
        has_game_ended = False
        bot_total_time = 0
        while not (has_game_ended):
            self.show_game()

            # Minimax Local Search turn
            if self.current_player.no_player != self.player_pawn_color:
                print("PLAYER {} - MINIMAX TURN!".format(self.current_player.no_player))
                
                # Minimax Local Search process for the BOT
                current_state = GameState(
                    self.board, self.current_player, self.opponent
                )
                initial_time = time.time()
                minimax_state, _ = minimax_local_search(
                    current_state, 
                    self.depth_mode, 
                    time.time() + self.time_limit, 
                    -math.inf, 
                    math.inf, 
                    self.current_player.no_player
                )
                self.assign_state(minimax_state)
                delta_time = time.time() - initial_time
                bot_total_time += delta_time
                print("Exec time = {} seconds".format(delta_time))

                print(
                    "PLAYER {} MINIMAX LS has played".format(self.current_player.no_player)
                )

            # Human player turn
            else:
                print("PLAYER {} TURN!".format(self.current_player.no_player))
                self.current_player.print_pawns()
                chosen_pawn_id = int(input("Choose which Pawn ID to play with: "))

                possible_moves = self.current_player.get_possible_moves(
                    chosen_pawn_id, self.board
                )

                for i in range(len(possible_moves)):
                    print("{}. {}".format(i + 1, possible_moves[i]))

                chosen_move = int(
                    input("Select the desired move by entering the number: ")
                )
                self.current_player.move_pawn(
                    chosen_pawn_id, possible_moves[chosen_move - 1], self.board
                )

            # Check for game final status
            if self.board.check_winner(self.current_player.no_player):
                has_game_ended = True
            else:
                self.next_turn()

        self.show_game()
        print("Player {} won the game!".format(self.current_player.no_player))
        print("BOT Time: {} ".format(bot_total_time))



    def minimax_vs_minimax_ls(self):
        """ Mode: Minimax Bot vs Minimax LS Bot"""
        has_game_ended = False
        bot_one_total_time = 0
        bot_two_total_time = 0
        while not (has_game_ended):
            self.show_game()
            if (self.current_player.no_player == 1):
                print("PLAYER {} - MINIMAX TURN!".format(self.current_player.no_player))
                # self.current_player.print_pawns()
                # Minimax
                current_state = GameState(
                    self.board, self.current_player, self.opponent)
                initial_time = time.time()
                minimax_state, _ = minimax(
                    current_state, 
                    self.depth_mode, 
                    time.time() + self.time_limit, 
                    -math.inf, 
                    math.inf, 
                    self.current_player.no_player
                )
                self.assign_state(minimax_state)
                delta_time = time.time() - initial_time
                bot_one_total_time += delta_time
                print("Exec time = {} seconds".format(delta_time))

                print(
                    "PLAYER {} MINIMAX has played".format(self.current_player.no_player)
                )

            else:
                print("PLAYER {} - MINIMAX LOCAL SEARCH TURN!".format(self.current_player.no_player))
                # self.current_player.print_pawns()
                # Minimax
                current_state = GameState(
                    self.board, self.current_player, self.opponent)
                initial_time = time.time()
                minimax_state, _ = minimax_local_search(
                    current_state, 
                    self.depth_mode, 
                    time.time() + self.time_limit, 
                    -math.inf, 
                    math.inf, 
                    self.current_player.no_player
                )
                self.assign_state(minimax_state)
                delta_time = time.time() - initial_time
                bot_two_total_time += delta_time
                print("Exec time = {} seconds".format(delta_time))

                print(
                    "PLAYER {} MINIMAX LOCAL SEARCH has played".format(self.current_player.no_player)
                )

            # Check for game final status
            if self.board.check_winner(self.current_player.no_player):
                has_game_ended = True
            else:
                self.next_turn()
        
        self.show_game()
        print("Player {} won the game!".format(self.current_player.no_player))
        print("BOT Minimax Time: {} ".format(bot_one_total_time))
        print("BOT Minimax LocalSearch Time: {} ".format(bot_two_total_time))
