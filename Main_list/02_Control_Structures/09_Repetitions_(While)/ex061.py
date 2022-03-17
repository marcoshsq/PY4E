# Exercício Python #061 - Progressão Aritmética v2.0
'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''


primeiro_termo = int(input('Qual o primeiro termo da Progressão Aritmética: '))
razao = int(input('Qual a razão de progressão: '))
termo = primeiro_termo
c = 1
while c <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    c += 1

print('FIM')
