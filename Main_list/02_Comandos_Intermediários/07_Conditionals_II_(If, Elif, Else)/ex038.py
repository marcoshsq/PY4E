# Exercício Python 038 - Comparando números

'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior'''

num_1 = int(input('Insira o primeiro valor: '))
num_2 = int(input('Insira o segundo valor: '))

if num_1 > num_2 :
    print(f'O número {num_1} é maior que {num_2}')
elif num_2 > num_1 :
    print(f'O número {num_2} é maior que {num_1}')
elif num_1 == num_2 :
    print('Os valores são iguais')