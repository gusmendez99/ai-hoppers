"""
Main - initializes terminal menu
"""

from game.manager import GameManager
from settings import *


def main_menu():
    print("Welcome to Hoppers AI!")
    print("1. P1 vs P2")
    print("2. Player vs AI Minimax")

    # TODO: let the user enter coordinates, and no longer the ID
    # TODO: validate when pawn has no possible moves (empty move list)
    # TODO: show Minimax start and final coords selected, and the taken path
    # TODO: add minimax vs minimax game mode
    # TODO: validate winner regardless of the color of the pawns, but by the full target (goal) region

    mode = int(input("Enter the desired game mode options: "))
    pawns_color = 0

    if mode != 1:
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
