# Exercise Python 008: Measurement converter
'''Write a program that reads a value in meters and displays it converted to centimeters and millimeters. '''

meters = float(input('Insira o valor em metros: '))
print(f'Os múltiplos de {meters} m são {meters * 10} dam, {meters * 100} hm, e {meters * 1000} km')
print(f'Os submúltiplos de {meters} m são {meters / 10} dm, {meters / 100} cm e {meters / 1000} mm')
