# Exercise 060 - Factorial Calculation
'''Make a program that reads any number and displays its factorial.
Example: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

number = int(input('Enter a number: '))

flag = 1
tracker = number

while tracker > 0:
    print(f'{tracker}',end=' ')
    if tracker > 1:
        print(' x ')
    else:
        print(' = ')
    flag *= tracker
    tracker -= 1

print(flag)
