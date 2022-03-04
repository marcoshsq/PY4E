# Python Exercise 019 - Sorting an item in the list
''' A teacher wants to draw one of his four students to erase the board.
Make a program that helps him, reading the name of the students and writing on the screen the name of the chosen one.'''

import random


aluno_01 = str(input('Insira o nome do primeiro aluno: '))
aluno_02 = str(input('Insira o nome do primeiro aluno: '))
aluno_03 = str(input('Insira o nome do primeiro aluno: '))
aluno_04 = str(input('Insira o nome do primeiro aluno: '))

alunos = [aluno_01, aluno_02, aluno_03, aluno_04]
escolha = random.choices(alunos)
print(f'O aluno escolhido/a foi {escolha}')
