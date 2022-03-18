# Exercício Python 052 - Números primos

'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

número = int(input('Insira um valor: '))
# Números primos são maiores que 1
if número > 1:
    for i in range(2,número):
        if (número % i) == 0:
            print(f'{número} Não é um número primo!')
            print(f'{i} x {número // i} é {número}')
            break
    else:
        print(f'{número} é um número primo!')

# Se o número for <= 1, não primo
else:
    print(f'{número} Não é um número primo!')