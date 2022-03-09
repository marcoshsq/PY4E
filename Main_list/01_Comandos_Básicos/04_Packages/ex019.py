# Exercício Python 019 - Sorteando um item na lista
''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random


aluno_01 = str(input('Insira o nome do primeiro aluno: '))
aluno_02 = str(input('Insira o nome do primeiro aluno: '))
aluno_03 = str(input('Insira o nome do primeiro aluno: '))
aluno_04 = str(input('Insira o nome do primeiro aluno: '))

alunos = [aluno_01, aluno_02, aluno_03, aluno_04]
escolha = random.choices(alunos)
print(f'O aluno escolhido/a foi {escolha}')
