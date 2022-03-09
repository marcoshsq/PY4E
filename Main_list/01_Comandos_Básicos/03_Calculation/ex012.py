# Python Exercise 012: Calculating Discounts
''' Make an algorithm that reads the price of a product and displays its new price, with a 5% discount.'''

preço = float(input('Qual o valor do produto: '))
desc = preço * 0.95
print(f'O produto que custava R${preço}, na promoção, com 5% off, ficou R${desc:.2f}')

'''This (:.2f) limits the number of places after the comma, but I'm not sure how it works yet u.u'''
