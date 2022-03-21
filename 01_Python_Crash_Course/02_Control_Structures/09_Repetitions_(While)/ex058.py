import random
import time

# Exercise 058 - Guessing Game v2.0

'''Improve the game of exercise 028 where the computer will "think" of a number between 0 and 10.
But now the player will try to guess until he gets it right, showing at the end how many
guesses were needed to win.'''

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('I\'ll think of a number between 0 and 10, try to guess!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

computer_guess = random.randint(0, 10) 
user_guess = int(input('What number did I think of? '))
print('loading...')   
time.sleep(1) 

# Now, instead of using if, we'll use a while
counter = 0
while user_guess != computer_guess:
    user_guess = int(input('Hmm, not this time. Why don\'t you try again? '))
    print('loading...')   
    time.sleep(1)
    counter += 1       


# Here we will show how many attempts the player had to make
if counter <= 1:
    print(f'Congratulations, you are very good, just needed {counter} try')
elif 1 < counter < 3:
    print(f'You\'re pretty good, needed only {counter} attempts')
else:
    print(f'You got it, needed only {counter} attempts.')
    
