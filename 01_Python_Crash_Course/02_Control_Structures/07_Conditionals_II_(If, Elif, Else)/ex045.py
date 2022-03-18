# Exercício Python 045 - GAME: Pedra Papel e Tesoura

'''Crie um programa que faça o computador jogar Jokenpô com você.'''


# Essas três linhas são o jogo do computador
from random import randint
import time
itens = ('Pedra', 'Papel', 'Tesoura')
pc_choice = randint(0, 2)

print('-=' * 10 , 'Pedra, Papel ou Tesoura', '-=' * 10)
print('''
                         [0] Pedra
                         [1] Papel
                         [2] Tesoura
''')

print('-=' * 33)


# Essas são as escolhas
player_choice = int(input('Qual sua jogada (Escolha entre 0, 1 e 2): '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)

print(f'Computador jogou {itens[pc_choice]}')
print(f'Você escolheu {itens[player_choice]}')


if pc_choice == 0:          # Computador escolhe pedra
    if player_choice == 0 :
        print('Deu empate')
    
    elif player_choice == 1 :
        print('Você ganhou uhuuu')

    elif player_choice == 2 :
        print('Você perdeu booooo')
    
    else :
        print('Jogada Invalida')

if pc_choice == 1:          # Computador escolhe papel
    if player_choice == 0 :
        print('Você perdeu booooo')
    elif player_choice == 1 :
        print('Deu empate')

    elif player_choice == 2 :
        print('Você ganhou uhuuu')
    
    else :
        print('Jogada Invalida')

if pc_choice == 2:          # Computador escolhe tesoura
    if player_choice == 0 :
        print('Você ganhou uhuuu')
    elif player_choice == 1 :
        print('Você perdeu boooooo')

    elif player_choice == 2 :
        print('Deu empate')
    
    else :
        print('Jogada Invalida')