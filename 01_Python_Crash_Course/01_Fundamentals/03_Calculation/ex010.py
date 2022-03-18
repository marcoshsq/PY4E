# Exercício Python 010: Conversor de moedas
'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
e mostre quantos dólares ela pode comprar.'''

money_real = float(input('Qual quantia você possui: '))
dolar = money_real / 5.10
print(f'Com R${money_real} você pode comprar US${dolar:.2f} ') 
