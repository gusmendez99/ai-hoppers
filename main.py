"""
Main - initializes terminal menu
"""

from game.manager import GameManager
from settings import *


def main_menu():
    print("Welcome to Hoppers AI!")
    print("1. P1 vs P2")
    print("2. Player vs AI Minimax")
    print("3. Player vs AI Minimax LS")
    print("4. AI Minimax vs AI Minimax LS")

    # TODO: show Minimax start and final coords selected, and the taken path
    # TODO: add minimax vs minimax game mode
    # TODO: validate when pawn has no possible moves (empty move list)
    # TODO: let the user enter coordinates, and no longer the ID

    mode = int(input("Enter the desired game mode options: "))
    pawns_color = 0

    if mode != 1 or mode != 4:
        pawns_color = int(
            input(
                "Choose {} ({}) or {} ({}): ".format(
                    PLAYER_ONE_VALUE,
                    PLAYER_ONE_PAWN_COLOR,
                    PLAYER_TWO_VALUE,
                    PLAYER_TWO_PAWN_COLOR,
                )
            )
        )

    manager = GameManager(mode, pawns_color)
    manager.start_game()


main_menu()
