# Python Exercise 030 - Odd or Even?
'''Create a program that reads an integer and shows on the screen whether it is ODD or EVEN.'''

number = int(input('Insert a value: '))
even_or_odd = number % 2
if even_or_odd == 0 :
    print(f'O número {number} é par')
else :
    print(f'O número {number} é impar')