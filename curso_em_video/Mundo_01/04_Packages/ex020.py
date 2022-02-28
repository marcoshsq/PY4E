# Python Exercise 020 - Sorting an order from the list
'''The same teacher from challenge 019 wants to draw the order of presentation of students' work.
Make a program that reads the names of the four students and displays the order drawn.'''

import random

aluno_01 = str(input('Insira o nome do primeiro aluno: '))
aluno_02 = str(input('Insira o nome do primeiro aluno: '))
aluno_03 = str(input('Insira o nome do primeiro aluno: '))
aluno_04 = str(input('Insira o nome do primeiro aluno: '))

alunos = [aluno_01, aluno_02, aluno_03, aluno_04]
random.shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')
