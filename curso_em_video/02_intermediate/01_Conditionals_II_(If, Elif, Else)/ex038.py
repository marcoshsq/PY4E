# Python Exercise 038 - Comparing numbers

'''Write a program that reads two integers and compares them. displaying a message on the screen:
- The first value is larger'''

num_1 = int(input('Insira o primeiro valor: '))
num_2 = int(input('Insira o segundo valor: '))

if num_1 > num_2 :
    print(f'O número {num_1} é maior que {num_2}')
elif num_2 > num_1 :
    print(f'O número {num_2} é maior que {num_1}')
elif num_1 == num_2 :
    print('Os valores são iguais')