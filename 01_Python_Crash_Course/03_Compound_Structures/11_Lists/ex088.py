# Exercise 088 - Guesses for the Mega Sena

'''Write a program that helps a MEGA SENA player to create guesses. 
The program will ask how many games will be generated and will 
draw 6 numbers between 1 and 60 for each game, 
registering everything in a composite list.'''

"""he Mega-Sena is the largest lottery in Brazil, 
organised by the Caixa Econômica Federal bank since March 1996."""

from random import randint
from time import sleep
list_a = list()
games = list()
quantity = int(input("How many games do you want me to draw? \n"))
total = 1

while total <= quantity:
    counter = 0
    while True:
        number = randint(1, 60)
        if number not in list_a:
            list_a.append(number)
            counter += 1
        if counter >= 6:
            break
    list_a.sort()
    games.append(list_a[:])
    list_a.clear()
    total += 1

for i, l in enumerate(games):
    print(f"Game {i + 1}: {l}")
    sleep(1)