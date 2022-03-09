# Exercício Python 040 - Aquele clássico da Média

'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO'''

nota_01 = float(input('Insira a primeira nota do aluno: ')) 
nota_02 = float(input('Insira a segunda nota do aluno: '))
media = (nota_01 + nota_02) / 2
if media >= 5 :
    print(f'O aluno tirou {media} de nota, foi aprovado! ')
elif media < 5 :
    print(f'O aluno tirou {media} de nota, foi reprovado! ')
else :
    print('Valor invalido')