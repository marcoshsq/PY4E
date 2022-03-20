# Exercise 037 - Numerical Base Converter

'''Write a Python program that reads any integer and asks it to the user to choose what the conversion base will be: 1 for binary, 2 for octal and 3 for hexadecimal.'''

print('-=' * 25)
num = int(input('Enter a number for convertion: '))
print('-=' * 25)


while True :
    print('[1] For binary')
    print('[2] For octal')
    print('[3] For hexadecimal')
    escolha = int(input('What will be the conversion basis?: '))
# We're using the index here to get rid of the code that came before the numbers  
    if escolha == 1 :
        print(f'The number {num} in binary is {bin(num) [2:]}')
        break

    elif escolha == 2 :
        print(f'The number {num} in octal is {oct(num) [2:]}')
        break

    elif escolha == 3 :
        print(f'The number {num} in hexadecimal is {hex(num) [2:]}')
        break

    else :
        print('Wrong data, please enter a correct value: ')
