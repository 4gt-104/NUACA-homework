"""Minimax Game Module.

"https://en.wikipedia.org/wiki/Minimax"

This module implements a game where a human player competes against a program
using the Minimax algorithm. The game involves picking numbers from a list, with
the goal of accumulating the highest score.

The module includes functions to generate a random list of numbers, play the game,
and calculate the optimal move for the program using the Minimax algorithm.

Functions:
    play_game: Plays the game, allowing the human player to make moves and the
        program to respond.
    optimal_move: Calculates the optimal move for the program using the Minimax
        algorithm.
"""  # noqa: INP001

from __future__ import annotations

import random

POSSIBLE_VALUES_RANGE = [1, 1001]
LIST_LEN_RANGE = [1, 101]


def _generate_random_list() -> list[int]:
    return [
        random.randint(*POSSIBLE_VALUES_RANGE)  # noqa: S311
        for _ in range(random.randint(*LIST_LEN_RANGE))  # noqa: S311
    ]


def optimal_move(
    nums: list[int],
    left: int,
    right: int,
    is_program_turn: bool,
    memo: dict,
):
    """Recursively calculate the optimal move for the program.

    This function implements the Minimax algorithm to determine the optimal move for the
    program in a game.

    Parameters
    ----------
        nums (list[int]): The list of numbers from which the program can pick.
        left (int): The leftmost index of the range of numbers from which the program can pick.
        right (int): The rightmost index of the range of numbers from which the program can pick.
        is_program_turn (bool): A flag indicating whether it is the program's turn to make a move.
        memo (dict): A dictionary used to store precomputed values for memoization.

    Returns
    -------
        int: The optimal score the program can achieve.

    """  # noqa: E501
    if left > right:
        return 0

    # Use precomputed state if possible
    if (left, right, is_program_turn) in memo:
        return memo[(left, right, is_program_turn)]

    if is_program_turn:
        # Max program's score
        choose_left = nums[left] + optimal_move(nums, left + 1, right, False, memo)
        choose_right = nums[right] + optimal_move(nums, left, right - 1, False, memo)
        result = max(choose_left, choose_right)
    else:
        # Player minimizes program's score
        choose_left = optimal_move(nums, left + 1, right, True, memo)
        choose_right = optimal_move(nums, left, right - 1, True, memo)
        result = min(choose_left, choose_right)

    # Memoize the result
    memo[(left, right, is_program_turn)] = result
    return result


def play_game() -> None:
    """Play a game of Minimax.

    A human player competes against a program using the Minimax algorithm.
    The game involves picking numbers from a list, with the goal of accumulating
    the highest score.

    """
    nums = _generate_random_list()
    print(f"Starting list: {nums}")

    human_score = 0
    program_score = 0
    # left and right are indices
    left, right = 0, len(nums) - 1

    while left <= right:
        # Human turn
        print(f"Current list: {nums[left:right+1]}")
        human_choice = (
            input(f"Pick left ({nums[left]}) or right ({nums[right]}): ")
            .strip()
            .lower()
        )
        if human_choice == "left":
            human_score += nums[left]
            left += 1
        elif human_choice == "right":
            human_score += nums[right]
            right -= 1
        else:
            print("Invalid choice. Please choose 'left' or 'right'.")
            continue

        # Program turn
        if left <= right:
            memo = {}
            choose_left = nums[left] + optimal_move(nums, left + 1, right, False, memo)
            choose_right = nums[right] + optimal_move(
                nums,
                left,
                right - 1,
                False,
                memo,
            )

            if choose_left >= choose_right:
                print(f"Program picks left ({nums[left]})")
                program_score += nums[left]
                left += 1
            else:
                print(f"Program picks right ({nums[right]})")
                program_score += nums[right]
                right -= 1

        print(f"Scores - Human: {human_score}, Program: {program_score}")

    print(f"Final Scores - Human: {human_score}, Program: {program_score}")
    if human_score > program_score:
        print("Player wins! 👨‍🎓👨‍🎓👨‍🎓")
    elif program_score > human_score:
        print("Program wins! 🤖🤖🤖")
    else:
        print("It's a tie! 🤝🤝🤝")


play_game()
