# Exercise 049 - Multiplication Table v.2.0

'''Redo Exercise 009, showing the multiplication table of a number that the user chooses.'''

num = int(input('Enter a number: '))
print(f'The multiplication table of {num} is:')
print('=' * 13)

for i in range(1, 11) :
    print(num , 'x', i, '=', num * i )

print('=' * 13)
