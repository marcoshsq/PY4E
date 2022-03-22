# Exercise 070 - Statistics on Products

''' Create a program that reads the name and price of multiple products.
The program should ask if the user will continue or not. At the end, show:

A) what is the total spent on the purchase.
B) how many products cost more than R$1000.
C) what is the name of the cheapest product. 
'''


cheaper = ''
total = highest_price = smallest = counter =  0

while True:
    product = str(input('Enter the product brand: '))
    price = float(input('Enter the product price: R$'))
    total += 1
    counter += 1

    if price > 1000:
        highest_price += price    
    
    if counter == 1 or price < smallest:
        smallest = price
        cheaper = product

    answer = ' '
    while answer not in 'YN':
        answer = str(input('Wish to continue? [Y/N]')).upper().strip()[0]
    if answer == 'N':
        break

print('-=' * 7, 'Program Ended', '-=' * 7 )
print(f'The total purchase amount was R${total:.2f}')
print(f'{highest_price} products cost more than R$1000')
print(f'The cheapest product {cheaper} was R${smallest:.2f}')

