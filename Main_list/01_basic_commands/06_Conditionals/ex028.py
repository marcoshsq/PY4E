# Python Exercise 028 - Guessing Game v.1.0
'''Write a program that makes the computer "think" of an integer between 0 and 5
and ask the user to try to find out which number was chosen by the computer.
The program should write to the screen if the user won or lost.'''

import random
import time

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

computer_guess = random.randint(0, 5) # Faz o computador escolher um número
user_guess = int(input('Em que número eu pense? ')) # Número do jogador
print('Processando...')   
time.sleep(1)  # Essa funçãp vem com o pacote time e ele deixa eu colocar um time no meu código
if user_guess == computer_guess :
    print('Parabéns, você acertou!')
else :
    print ('Booh, Booh... ERROU!!!')