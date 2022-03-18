# Exercício Python 051 - Progressão Aritmética

'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''


primeiro_termo = int(input('Qual o primeiro termo da Progressão Aritmética: '))
num_termos = int(input('Qual o número de termos da Progressão Aritmética: '))
razao = int(input('Qual a razão de progressão: '))

ultimo = primeiro_termo + (num_termos-1) * razao
ultimo = ultimo + 1

for i in range(primeiro_termo, ultimo, razao):
    print(i, end=' ')