# 1. We import the packages we are going to use, as we are going to make the computer choose something random, 
# we need random, and we import the team, to give the game a thrill
from random import randint
from time import sleep

# Exercise 068 - Odd or Even Game

'''Make a program that plays odd or even with the computer.
The game will only be stopped when the player loses,
showing the total number of consecutive wins he had at the end of the game. '''
# As always, this is going to be a pretty big program, so, let's make a script


# 2. we want to show the number of times the player has won, so we will create an adder
victories = 0

# 3. We create our loop, and we will leave it with True, and we will use break to break
while True:

    # 4. We ask the user, we will only consider integers
    player = int(input('Enter a number betwenn 0 and 10 to play or 999 to stop: \n'))
    

    #  5. Exception control, let's limit our player to a number from 0 to 10
    # less than zero:
    if player < 0:
        print('Enter a positive integer less than ten: ')
        

    # greater than 10
    elif player > 10 and player != 999:
        print("Enter an integer less than 10")

    # If the player wants to stop
    elif player == 999:
        print('You decided to stop. I\'m sorry I\'m not so nice')
        print(f'Consecutive wins: {victories}')
        break

    # 6. If between 0 and 10, then run:
    else:  
        computer = randint(0, 10)  # pc play
        choice = str(input('Even or odd? [E / O] \n')).strip().upper()

        # 7. If user chose even:
        if choice == "E":  
            print('You chose even!')
            sum = player + computer

            # 7.1 If it was even 
            if sum % 2 == 0:  
                victories += 1
                sleep(1)
                print(f'The computer chose {computer}.')
                print(f'{sum} it\'s even, so you\'ve won!')


            # 7.2 If it was odd
            else:  
                sleep(1)
                print(f'The computer chose {computer}.')
                print(f'{sum} it\'s odd, so you\'ve loose!')
                print(f'Consecutive wins: {victories}')
                break

        # 8. If user chose odd:
        elif choice == "O":  
            sum = player + computer
            print('You chose odd!')

            # 8.1 If it was odd 
            if sum % 2 != 0:  
                victories += 1
                sleep(1)
                print(f'The computer chose {computer}.')
                print(f'{sum} it\'s odd, so you\'ve won!')

            # 8.2 If it was even 
            else:  
                sleep(1)
                print(f'The computer chose {computer}.')
                print(f'{sum} it\'s even, so you\'ve loose!')
                print(f'Consecutive wins: {victories}')
                break

        # 9. If the user does not choose even or odd
        else:
            print('Please choose Even or odd!')
            sleep(1.5)
            print('Please (づ｡◕‿‿◕｡)づ')
            sleep(1)
