# Exercício Python #059 - Criando um Menu de Opções
'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''



controle = 0
while controle != 1:
    print('=' * 5, 'Calculadora Simples!', '=' * 5)
    valor_01 = int(input('Escolha um valor: '))
    valor_02 = int(input('Escolha outro valor: '))
    print('='*25)
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    print('='*25)
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1:
        soma = valor_01 + valor_02
        print(f'A soma entre {valor_01} e {valor_02} é {soma}')      
    elif escolha == 2:
        produto = valor_01 * valor_02
        print(f'O produto entre {valor_01} e {valor_02} é {produto}') 
    elif escolha == 3:
        if valor_01 > valor_02:
            print(f'Entre {valor_01} e {valor_02}, o maior é {valor_01}')
        elif valor_01 < valor_02:
            print(f'Entre {valor_01} e {valor_02}, o maior é {valor_02}')
        else:
            print('Os valores são iguais')
    elif escolha == 4:
        continue
    elif escolha == 5:
        controle += 1
    else:
        print('Escolha invalida: ')
        continue