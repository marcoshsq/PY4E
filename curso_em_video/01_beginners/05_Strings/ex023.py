# Python Exercise 023 - Separating digits from a number
'''Make a program that reads a number from 0 to 9999 and
display each of the separate digits on the screen.'''

number = int(input('Insira um número: '))
unity = (number // 1) % 10
ten = (number // 10) % 10
hundred = (number // 100) % 10
thousand = (number // 1000) % 100

print(f'Analisando o número {number} ele é composto por: ')
print(f'Unidade: {unity}')
print(f'Dezena: {ten}')
print(f'Centena: {hundred}')
print(f'Milhar: {thousand}')
