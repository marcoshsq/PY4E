# Exercício Python 005: Antecessor e sucessor
'''Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor'''

num = float(input('Insira um número: '))
prev_num = num - 1
next_num = num + 1
print(f'Analizando o valor {num}, o seu antecessor é {prev_num} e seu sucessor é {next_num}')
