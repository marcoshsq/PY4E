# Exercício Python 023 - Separando dígitos de um número
'''Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.'''

number = int(input('Insira um número: '))
unity = (number // 1) % 10
ten = (number // 10) % 10
hundred = (number // 100) % 10
thousand = (number // 1000) % 100

print(f'Analisando o número {number} ele é composto por: ')
print(f'Unidade: {unity}')
print(f'Dezena: {ten}')
print(f'Centena: {hundred}')
print(f'Milhar: {thousand}')