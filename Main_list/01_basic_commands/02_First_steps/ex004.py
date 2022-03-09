from typing import Type

# Exercício Python 004: Dissecando uma variável.
'''Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ele.'''

variable = input('Insira um valor')
print('O tipo primitivo desse valor é:', type(variable))
print('Contêm apenas letras:', variable.isalpha())
print('Contêm números e letras:', variable.isalnum())
print('Contêm apenas números:', variable.isnumeric())
print('Está em maiuscula:', variable.isupper())
print('Está em minuscula: ', variable.islower())
print('Está capitalizado:', variable.istitle())


'''essa função .is____() permite descobrir algumas informações interessantes 
sobre o meu input, então é legal deixar salvo isso, para algum momento'''
