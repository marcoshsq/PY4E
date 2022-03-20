# 1. Packages we'll use, random for the game, time just to add some flavour
from random import randint
import time

# Exercise 045 - GAME: Rock Paper and Scissors
'''Create a program that makes the computer play Jokenpo with you.'''

''' This program is going to be long
So a tip before starting is:
Write the entire script of what you should do before
Programming logic in a nutshell for you '''


# 1. Let's import the libraries we'll need;
# 2. We create the logic Python will follow;
# 3. We create a menu for the player;
# 4. We ask the user to play´
# 5. We print the user and the Python choice
# 6. we create the scenarios for each situation using if's


# 2. These three lines are python's logic
itens = ('Rock', 'Paper', 'Scissors')
pc_choice = randint(0, 2)

# 3. The menu we'll display
print('-=' * 10 , 'Rock, Paper ou Scissors', '-=' * 10)
print('''
                         [0] Rock
                         [1] Paper
                         [2] Scissors
''')

print('-=' * 33)


# 4. Player choice
player_choice = int(input('What\'s your move (Choose between 0, 1 and 2): '))

# This is just to add some drama
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)

# 5. The player and the Python choice
print(f'Python chose {itens[pc_choice]}')
print(f'You chose {itens[player_choice]}')


# 6. Now we create the scenarios, for this we three
# Python chose rock, Python chose paper and scissors

# Python chose rock
if pc_choice == 0:          
    if player_choice == 0 :
        print('it\'s a tie')
    
    elif player_choice == 1 :
        print('You win!')

    elif player_choice == 2 :
        print('You loose!')
    
    else :
        print('Invalid Move')

# Python chose paper
if pc_choice == 1:          
    if player_choice == 0 :
        print('You loose!')
    elif player_choice == 1 :
        print('it\'s a tie')

    elif player_choice == 2 :
        print('You win!')
    
    else :
        print('Invalid Move')

# Python chose scissors
if pc_choice == 2:          
    if player_choice == 0 :
        print('You win!')
    elif player_choice == 1 :
        print('You loose!')

    elif player_choice == 2 :
        print('it\'s a tie')
    
    else :
        print('Invalid Move')
