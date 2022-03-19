# Exercise 012: Calculating discounts
'''Make an algorithm that reads the price of a product and displays its new price, with a 5% discount.'''

price = float(input('Product\'s price: '))
discount = price * 0.95
print(f'The product that cost R${price}, in the promotion, with 5% off, is R${discount:.2f}')

#This (:.2f) limits the number of places after the comma u.u
