# Exercicio extra 002: let's Code

'''Faça um programa que leia a validade das informações:
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro;
O programa deve imprimir uma mensagem de erro para cada informação
inválida.'''

while True :
    age = int(input('Insert your age: ').strip())
    if 0 <= age <= 150 :
        print('Valid age!')
        print(f'You are {age} year(s) old!')
        break
    else :
        print('Wrong data!')
        print('Please insert a valid number! Between 0 and 150')
        continue
while True :
    wage = float(input('Insert your wage: ').strip())
    if wage > 0 :
        print('Valid wage!')
        print(f'You earn about US${wage}')
        break
    else :
        print('Invalid wage value!')
        print('Please insert a valid number! Bigger then 0')
        continue
while True :
    sex = int(input('Choose your sex: 1 for Male, 2 for Female and 3 for other: '))
    if sex == 1 :
        print('You choose male')
        break
    elif sex == 2 :
        print('You choose Female')
        break
    elif sex == 3 :
        print('You choose other')
        break
    else :
        print('Invalid sex value!')
        print('Please insert a valid number! 1 for Male, 2 for Female and 3 for other')
        continue