# Exercise 061 - Arithmetic Progression v2.0
'''Redo CHALLENGE 051, reading the first term and the ratio of an AP, 
showing the first 10 terms of the progression using the while structure.'''


first_term = int(input('Enter the first term: '))
r = int(input('Enter the common difference: '))
term = first_term
counter = 1
while counter <= 10:
    print(f'{term} ->', end=' ')
    term += r
    counter += 1

print('End')
