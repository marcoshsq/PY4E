# Exercício Python #060 - Cálculo do Fatorial
'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''


'''n = int(input('Insira um valor: '))
factorial = 1
while n > 1:
    factorial = factorial * n
    n = n - 1
print(factorial)'''


n = int(input('Insira um valor: '))
f = 1
c = n
while c > 0:
    print(f'{c}',end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f)