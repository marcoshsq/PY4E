#Exercício Python 016: Quebrando um número
'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

import math

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num}, e sua porção inteira é', math.trunc(num)) # Jeito 01 usando trunc
print(f'O valor digitado foi {num}, e sua porção inteira é', math.floor(num)) # Jeito 02 usando floor
print(f'O valor digitado foi {num}, e sua porção inteira é', int(num)) # Jeito 02 usando a função int()
