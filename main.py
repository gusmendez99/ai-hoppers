"""
Main - initializes terminal menu
"""

from game.manager import GameManager
from settings import *


def main_menu():
    print("Welcome to Hoppers AI!")
    print("1. P1 vs P2")
    print("2. Player vs AI Minimax")

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
