# Exercício Python 012: Calculando descontos
''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preço = float(input('Qual o valor do produto: '))
desc = preço * 0.95
print(f'O produto que custava R${preço}, na promoção, com 5% off, ficou R${desc:.2f}')

'''This (:.2f) limits the number of places after the comma, but I'm not sure how it works yet u.u'''
