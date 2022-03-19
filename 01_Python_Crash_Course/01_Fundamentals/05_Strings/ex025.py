# Exercise 025 - Finding a string inside another
'''Create a program that reads a person's name and tells if they have something specific in their name.'''

name = input('Insert name: ').casefold()
print(f'Your name is {name}')
print('And it has? ','specify_here' in name)
