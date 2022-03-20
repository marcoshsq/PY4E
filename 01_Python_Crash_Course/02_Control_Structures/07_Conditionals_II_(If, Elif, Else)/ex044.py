# Exercise 044 - Payment Manager

''' 
    Develop a program that calculates the amount to be paid for a product,
    Considering your normal price and payment term:
    - cash/check: 10% discount
    - cash on card: 5% discount
    - up to 2x on the card: formal price
    - 3x or more on the card: 20% interest
'''

product_price = float(input('What is the price of the Product: '))
print('-=' * 25, '''
        Choose a way to pay:
[1] - Cash/check: 10% discount
[2] - Cash on credit card: 5% discount
[3] - 2x on the card: regular price
[4] - 3x or more on the card: 20% interest
''')
payment = int(input('Choose the form of payment: '))

if payment == 1 :
    print(f'The amount to be paid is R${product_price * 0.9}')

elif payment == 2 :
    print(f'The amount to be paid is R${product_price * 0.95}')

elif payment == 3 :
    print(f'The amount to be paid is R${product_price}')

elif payment == 4 :
    print(f'The amount to be paid is R${product_price * 1.2}')

else :
    print('Wrong choice!')
