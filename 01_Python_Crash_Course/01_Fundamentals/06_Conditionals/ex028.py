import random
import time
# Exercise 028 - Guessing Game v.1.0
'''Write a program that makes the computer "think" of an integer between 0 and 5
and ask the user to try to find out which number was chosen by the computer.
The program should write on the screen if the user won or lost.'''



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('I\'ll think of a number between 0 and 5, try to guess!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

computer_guess = random.randint(0, 5) # Make the computer choose a number
user_guess = int(input('What number did I think of? ')) 
print('processing...')   
time.sleep(1)  # This function comes with the time package and allows me put a little delay in the code
if user_guess == computer_guess :
    print('Good job, you\'ve nailed !')
else :
    print ('Sorry, maybe next time!!!')
