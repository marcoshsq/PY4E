import math
# Exercício Extra: 
'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

radius = float(input('Insira o valor de um círculo'))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f'The area of the circle is {area:.2f} and its circumference is {circumference:.2f}')
