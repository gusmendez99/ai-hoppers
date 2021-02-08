import time
import math
from models.pawn import Position, Pawn
from game.state import GameState
from models.board import Board
from models.player import Player

from settings import *

"""
Minimax utils
"""


def eval_function(current_player, opponent, max_entity):
    """ Calculation of eval function based on player pawn info and certain state in the game """
    goal_player_one = Position(BOARD_SIZE - 1, BOARD_SIZE - 1)
    goal_player_two = Position(0, 0)

    sum_player_one_pawns = 0
    sum_player_two_pawns = 0

    if current_player.no_player == PLAYER_ONE_VALUE:
        for pawn in current_player.pawn_array:
            sum_player_one_pawns += pawn.current_position.euclidean(goal_player_one)
        for pawn in opponent.pawn_array:
            sum_player_two_pawns += pawn.current_position.euclidean(goal_player_two)

    if current_player.no_player == PLAYER_TWO_VALUE:
        for pawn in current_player.pawn_array:
            sum_player_two_pawns += pawn.current_position.euclidean(goal_player_two)
        for pawn in opponent.pawn_array:
            sum_player_one_pawns += pawn.current_position.euclidean(goal_player_one)

    if max_entity == PLAYER_ONE_VALUE:
        return -sum_player_one_pawns + sum_player_two_pawns

    return -sum_player_two_pawns + sum_player_one_pawns


def minimax(game_state, depth, total_time, alpha, beta, max_entity):
    """
    Minimax algorithm that Minimax Bot player will run
    """
    extra_points = 0
    has_game_ended = game_state.board.check_winner(game_state.current_player.no_player)

    # base: return game_state and eval_function if time exceeded, depth == 0 or game has ended
    if depth == 0 or time.time() > total_time or has_game_ended:
        if has_game_ended and game_state.current_player.no_player == max_entity:
            extra_points = 10
        elif has_game_ended and game_state.current_player.no_player != max_entity:
            extra_points = -10

        return (
            game_state,
            eval_function(
                game_state.current_player,
                game_state.opponent,
                max_entity,
            )
            + extra_points,
        )

    # recurrence: branching and recursive minmax based on player turn
    if game_state.current_player.no_player == max_entity:
        # choose the max val of eval_func of the state
        max_game_state = GameState(
            game_state.board, game_state.current_player, game_state.opponent
        )
        max_value = -math.inf

        # iterates all pawns and possible moves
        # TODO: verify time

        for index in range(len(game_state.current_player.pawn_array)):
            possible_moves = game_state.current_player.get_possible_moves(
                index, game_state.board
            )

            for move in possible_moves:
                new_game_state = GameState(
                    game_state.board, game_state.current_player, game_state.opponent
                )
                new_game_state.current_player.movePion(
                    index, move, new_game_state.board
                )

                recursive_state = GameState(
                    new_game_state.board,
                    new_game_state.current_player,
                    new_game_state.opponent,
                )
                recursive_state.next_turn()
                _, eval_value = minimax(
                    recursive_state, depth - 1, total_time, alpha, beta, max_entity
                )

                # compare values
                if eval_value > max_value:
                    max_value = eval_value
                    max_game_state = new_game_state

                # alpha-beta pruning
                alpha = max(alpha, max_value)
                if beta <= alpha:
                    return max_game_state, max_value

        return max_game_state, max_value

    else:
        # Choose the min val of eval_value of the state
        min_game_state = GameState(
            game_state.board, game_state.current_player, game_state.opponent
        )
        min_value = math.inf

        for index in range(len(game_state.current_player.pawn_array)):
            possible_moves = game_state.current_player.get_possible_moves(
                index, game_state.board
            )

            # iterates all pawns and possible moves
            # TODO: verify time
            for move in possible_moves:
                new_game_state = GameState(
                    game_state.board, game_state.current_player, game_state.opponent
                )
                new_game_state.current_player.movePion(
                    index, move, new_game_state.board
                )

                recursive_state = GameState(
                    new_game_state.board,
                    new_game_state.current_player,
                    new_game_state.opponent,
                )
                recursive_state.next_turn()
                _, eval_value = minimax(
                    recursive_state, depth - 1, total_time, alpha, beta, max_entity
                )

                # Compare values
                if eval_value < min_value:
                    min_value = eval_value
                    min_game_state = new_game_state

                # alpha-beta pruning
                beta = min(beta, min_value)
                if beta <= alpha:
                    return min_game_state, min_value

        return min_game_state, min_value
