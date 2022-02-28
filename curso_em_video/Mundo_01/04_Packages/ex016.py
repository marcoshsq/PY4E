# Python Exercise 016: Cracking a number
'''Create a program that reads any Real number from the keyboard and displays its entire portion on the screen.'''

import math

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num}, e sua porção inteira é', math.trunc(num)) # Jeito 01 usando trunc
print(f'O valor digitado foi {num}, e sua porção inteira é', math.floor(num)) # Jeito 02 usando floor
print(f'O valor digitado foi {num}, e sua porção inteira é', int(num)) # Jeito 02 usando a função int()
