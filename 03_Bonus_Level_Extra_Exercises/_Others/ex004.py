# Exercício Extra 004: let's Code

'''Escreva um programa que imprima a tabuada dos 9 (de 9*1 a 9*10) usando loops.'''

# Usando o for:

num = int(input('Digite um número: '))
print(f'A tabuada do {num} é:')
print('=' * 13)
for i in range(1, 11) :
    print(num , 'x', i, '=', num * i )

print('=' * 13)

