# Exercício Python 020 - Sorteando uma ordem na lista
'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random

aluno_01 = str(input('Insira o nome do primeiro aluno: '))
aluno_02 = str(input('Insira o nome do primeiro aluno: '))
aluno_03 = str(input('Insira o nome do primeiro aluno: '))
aluno_04 = str(input('Insira o nome do primeiro aluno: '))

alunos = [aluno_01, aluno_02, aluno_03, aluno_04]
random.shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')