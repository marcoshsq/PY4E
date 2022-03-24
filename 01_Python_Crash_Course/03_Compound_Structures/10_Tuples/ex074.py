from random import randint

# Exercise 074 - Largest and Smallest Tuple Values

'''Create a program that will generate five random numbers 
and put them in a tuple.After that, show the list of 
generated numbers and also indicate the smallest and 
largest value that are in the tuple.
'''


numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'The numbers drawn were: ', end='')
for i in numbers:
    print(f'{i} ', end='')
print(f'\nThe highest value was {max(numbers)}')
print(f'The smallest value was {min(numbers)}')
