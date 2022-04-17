# Exercise 091 - Dice Game in Python

"""Create a program where 4 players roll a dice and get random results. 
Store these results in a Python dictionary. In the end, put that dictionary 
in order, knowing that the winner rolled the highest number on the dice.
"""

from random import randint
from time import sleep
from operator import itemgetter

game = {
    "player 01": randint(0, 6),
    "player 02": randint(0, 6),
    "player 03": randint(0, 6),
    "player 04": randint(0, 6),
}

ranking = dict()

for k, v in game.items():
    print(f"{k} rolled a {v} on the dice")
    sleep(0.5)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print()
for i, v in enumerate(ranking):
    print(f"{i + 1}º place: {v[0]} with {v[1]}")
    sleep(0.5)
