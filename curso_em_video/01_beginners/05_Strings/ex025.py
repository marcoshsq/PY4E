# Exercício Python 025 - Procurando uma string dentro de outra
'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

name = input('Insert name: ').casefold()
print(f'Seu nome é {name}')
print('Ele contem Silva? ','silva' in name)
