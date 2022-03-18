# Exercício Python 037 - Conversor de Bases Numéricas

'''Escreva um programa em Python que leia um número inteiro qualquer e peça para 
o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.'''

print('-=' * 25)
print('Escolha um número inteiro para conversão, as bases são:')
print('-=' * 25)
print('[1] Para binário')
print('[2] Para octal')
print('[1] Para hexadecimal')

num = int(input('Escolha um número inteiro: '))

while True :
    escolha = int(input('Qual será a base de conversão: '))
    if escolha == 1 :
        print(f'O número {num} em binário fica {bin(num) [2:]}')
        break
    elif escolha == 2 :
        print(f'O número {num} em octal fica {oct(num) [2:]}')

    elif escolha == 3 :
        print(f'O número {num} em hexadecimal fica {hex(num) [2:]}')

    else :
        print('Valor incorreto, escolha entre as três opções: ')