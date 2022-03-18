# Exercício Python 015: Aluguel de carros
'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

number_days =  float(input('Quantidade de dias de aluguel: '))
km_used = float(input('Quantidade de Km percorridos: '))
payment = (number_days * 60) + (km_used * 0.15)
print(f'O valor a pagar é de R${payment}')
