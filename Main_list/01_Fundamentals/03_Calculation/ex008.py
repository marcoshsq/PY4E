# Exercício Python 008: Conversor de Medidas
'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. '''

meters = float(input('Insira o valor em metros: '))
print(f'Os múltiplos de {meters} m são {meters * 10} dam, {meters * 100} hm, e {meters * 1000} km')
print(f'Os submúltiplos de {meters} m são {meters / 10} dm, {meters / 100} cm e {meters / 1000} mm')
