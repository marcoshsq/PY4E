# Exercício Python 035 - Analisando Triângulo v1.0
'''Desenvolva um programa que leia o comprimento de três retas e 
diga ao usuário se elas podem ou não formar um triângulo.'''

'''Dados três segmentos de reta distintos, 
se a soma das medidas de dois deles é sempre maior que a medida do terceiro, 
então, eles podem formar um triângulo'''

a, b, c = [float(x) for x in input("Please enter the size of three distincts segments: ").split()]

if a + b > c and a + c > b and b + c > a :
    print('The segments can form a triangle')
else :
    print('The segments can not form a triangle')