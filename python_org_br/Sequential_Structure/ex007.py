# Extra Exercise 007
'''Make a program that asks for 2 integers and a real number.
Calculate and show:
a) the product of the double of the first and half of the second.
b) the sum of the triple of the first and the third.
c) the third cubed.'''

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
