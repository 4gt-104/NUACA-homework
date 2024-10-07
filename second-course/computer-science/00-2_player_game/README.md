# MINIMAX

Although I was initially assigned task `38` from `acru.ru` during the CS class on ``01.10.2024``, I was given the flexibility to modify the assignment if I found it uninteresting.

As an alternative, I decided to write a program that uses the ``Minimax`` algorithm to create a computer player to compete against a human player. The game involves two players, one being the program and the other the user. At the start, a list of random integers (ranging from 1 to 1000) is generated, containing 1 to 100 items. Both players start with 0 points. The human player goes first, and on each turn, a player can select either the leftmost or rightmost integer from the list, adding it to their score and removing it from the list. The player with the highest score at the end wins.

As a solution to this problem, I utilized the Minimax algorithm, which enables the program to find an optimal move by considering both maximizing its own score and anticipating that the user might try to minimize the computer's score.

## Requirements

The program doesn't rely on any external packages or modules beyond those available in the Python3 standard library, so it should run smoothly with ``Python`` versions ``~= 3.8``.

## Starting the game

Run the following code from the assignment's directory:

```bash
python3 main.py
```