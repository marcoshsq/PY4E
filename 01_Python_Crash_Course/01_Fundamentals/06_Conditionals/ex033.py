# Python Exercise 033 - Maior e menor.
'''Crie um programa que leia três valores e diga qual o maior e qual o menor.'''

a, b, c = [int(x) for x in input("Please enter the numbers: ").split()]

# For the largest

if a > b and c :
    print(f'O maior é {a}')
elif b > c and a :
    print(f'O maior é {b}')
else :
    print(f'O maior é {c}')    

# For the smallest

if a < b and c :
    print(f'E o menor é {a}')
elif b < c and a :
    print(f'E o menor é {b}')
else :
    print(f'O menor é {c}')