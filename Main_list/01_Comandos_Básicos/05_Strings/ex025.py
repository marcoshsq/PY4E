# Python Exercise 025 - Finding a string inside another
'''Create a program that reads a person's name and tells if they have "SILVA" in their name.'''

name = input('Insert name: ').casefold()
print(f'Seu nome é {name}')
print('Ele contem Silva? ','silva' in name)
