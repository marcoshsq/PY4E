# Exercício Python 007: Média Aritmética 
'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

score_a = float(input('Insira a primeira nota do aluno: '))
score_b = float(input('Insira a segunda nota do aluno: '))
average = (score_a + score_b) / 2
print(f'A média do aluno foi {average}')
