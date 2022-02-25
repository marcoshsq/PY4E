# Exercício Python 027 - Primeiro e último nome de uma pessoa
'''Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.'''

name = input('Insert name: ')
first_name = name.split()[0]
last_name = name.split()[-1]
print(f'Olá, prazer em conhece-lo sr. {last_name}, ou posso chama-lo de {first_name}')
