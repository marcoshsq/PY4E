# Exercício Python 049 - Tabuada v.2.0

'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input('Digite um número: '))
#tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'A tabuada do {num} é:')
print('=' * 13)
for i in range(1, 11) :
    print(num , 'x', i, '=', num * i )

print('=' * 13)
