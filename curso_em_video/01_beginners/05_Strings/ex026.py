# Exercício Python 026 - Primeira e última ocorrência de uma string
'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

name = input('Insert name: ').casefold().strip()
num_a = name.count('a') 
first_a = name.find('a')
last_a = name.rfind('a')

print(f'A letra A aparece {num_a} vezes na frase')
print(f'A primeira letra A aparece na posição {first_a + 1}')
print(f'A ultima letra A apareceu na posição {last_a + 1}')