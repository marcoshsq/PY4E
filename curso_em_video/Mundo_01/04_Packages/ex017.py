# Exercício Python 017: Catetos e hipotenusa 
'''Faça um programa que leia o comprimento do cateto oposto 
e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''

import math

# Método 01, sem o módulo:

cat_op = float(input('Insira o valor do Cateto Oposto: ')) 
cat_ad = float(input('Insira o valor do Cateto Adjacente: '))
hip = ((cat_op ** 2) + (cat_ad ** 2)) ** 0.5
print(f'A hipotenusa do triangulo mede {hip:.2f} u.m. ')

# Método 02, com módulo:

hipo = math.sqrt(math.pow(cat_op, 2) + math.pow(cat_ad, 2))
print(f'A hipotenusa do triangulo mede {hipo:.2f} u.m ')

# Outro método usando o módulo u.u

hipot = math.hypot(cat_op, cat_ad)
print(f'A hipotenusa do triangulo mede {hipot:.2f} u.m. ')