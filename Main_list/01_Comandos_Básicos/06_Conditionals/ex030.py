# Exercício Python 030 - Par ou Ímpar?
'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

number = int(input('Insert a value: '))
even_or_odd = number % 2
if even_or_odd == 0 :
    print(f'O número {number} é par')
else :
    print(f'O número {number} é impar')