# Exercício Extra:
'''Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

x , y , z = input('Insert three numbers: ').split()
first_int = int(x)
second_int = int(y)
real_num = float(z)

a = (first_int * 2) * (second_int / 2)
b = (first_int * 3) + real_num
c = real_num ** 3

print(f'O produto do dobro do primeiro com metade do segundo é: {a}')
print(f'A soma do triplo do primeiro com o terceiroé: {b}')
print(f'O terceiro elevado ao cubo é: {c}')
