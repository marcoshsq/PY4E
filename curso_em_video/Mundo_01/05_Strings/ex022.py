# Exercício Python 022 - Analisador de Textos
'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

name = str(input('Digite seu nome: ')).strip()
name_up = name.upper()          # O nome com todas as letras maiúsculas
name_low = name.lower()         # O nome com todas as letras minúsculas
number_name = len(name) - name.count(' ')  # Quantas letras ao todo (sem considerar espaços)
find_the_space = name.find(' ')         # encontrar o primeiro espaço para usar como referência ao fatiar o primeiro nome
first_name = name[:find_the_space]
number_first_name = len(first_name)

print(f'Analisando seu nome... \n'
f'Seu nome em maíuscula é: {name_up} \n'
f'Seu nome em mínuscula é: {name_low} \n'
f'Seu nome tem ao todo {number_name} letras \n'
f'Seu primeiro nome é {first_name} \nE ele tem {number_first_name} letras')