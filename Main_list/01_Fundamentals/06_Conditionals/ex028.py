# Exercício Python 028 - Jogo da Adivinhação v.1.0
'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

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