# Exercise 067 - Multiplication table v3.0

''' Write a program that displays the multiplication table of several numbers, one at a time, for each value entered by the user.
The program will stop when the requested number is negative. '''

while True:
    n = int(input('What table do you want?: \n'))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')        
print('End.')
