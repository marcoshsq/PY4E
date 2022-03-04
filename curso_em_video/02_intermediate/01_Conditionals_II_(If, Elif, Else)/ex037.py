# Python Exercise 037 - Numerical Base Converter

'''Write a Python program that reads any integer and asks it to
the user to choose what the conversion base will be:
1 for binary, 2 for octal and 3 for hexadecimal.'''

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