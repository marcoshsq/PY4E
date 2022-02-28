# Exercício Python 024 - Verificando as primeiras letras de um texto
'''Crie um programa que leia o nome de uma cidade 
diga se ela começa ou não com o nome "SANTO".'''

name = str(input('Insira o nome da cidade: ')).strip().casefold()
city = name.startswith('santo')
print(city)
