'''Whenever you are going to do a program that requires many lines, or that requires some more advanced logic, 
write a script of what you want to do, and if you are already a little more advanced in programming, 
create a general skeleton of the program, with the steps than you need to add.'''

# 1. We import the packages we are going to use, as we are going to make the computer choose something random, 
# we need random, and we import the team, to give the game a thrill

# 2. First, we want to show the number of times the player has won, so we will create an adder
# 3. We create our loop, and we will leave it with True, and we will use break to break
# 4. We ask the user, we will only consider integers

# 5. Exception control, let's limit our player to a number from 0 to 10
# So we have two situations to deal with. Player chooses a number less than 0, or player chooses a number greater than 10

# 6. If between 0 and 10, then we ask, odd or even?

# 7. If user chose even, then we do the calculations and if he won
# 7.1 User chose even and won
# 7.2 User chose even and loose

# 8. If user chose odd, then we do the calculations and if he won
# 8.1 User chose odd and won
# 8.2 User chose odd and loose

# 9. If the user does not choose even or odd
# 10. If the player wants to stop


from random import randint
from time import sleep

victories = 0
while True:
    player = int(input('Enter a number betwenn 0 and 10 to play or 999 to stop: \n'))
    if player < 0:
        print('Enter a positive integer less than ten: ')
    elif player > 10 and player != 999:
        print("Enter an integer less than 10")
    elif player == 999:
        print('You decided to stop. I\'m sorry I\'m not so nice...(｡•́︿•̀｡)')
        print(f'Consecutive wins: {victories}')
        break
    else:  
        computer = randint(0, 10)
        choice = str(input('Even or odd? [E / O] \n')).strip().upper()
        if choice == "E":  
            print('You chose even!')
            sum = player + computer
            if sum % 2 == 0:  
                victories += 1
                sleep(1)
                print(f'The computer chose {computer}.')
                print(f'{sum} it\'s even, so you\'ve won!')
            else:  
                sleep(1)
                print(f'The computer chose {computer}.')
                print(f'{sum} it\'s odd, so you\'ve loose!')
                print(f'Consecutive wins: {victories}')
                break
        elif choice == "O":  
            sum = player + computer
            print('You chose odd!')
            if sum % 2 != 0:  
                victories += 1
                sleep(1)
                print(f'The computer chose {computer}.')
                print(f'{sum} it\'s odd, so you\'ve won!')
            else:  
                sleep(1)
                print(f'The computer chose {computer}.')
                print(f'{sum} it\'s even, so you\'ve loose!')
                print(f'Consecutive wins: {victories}')
                break
        else:
            print('Please choose Even or odd!')
            sleep(1.5)
            print('Please (づ｡◕‿‿◕｡)づ')
            sleep(1)
