# Exercício Python 044 - Gerenciador de Pagamentos

'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''



valor_produto = float(input('Qual o valor do Produto: '))
print('-=' * 25, '''
        Escolha uma forma de pagamento:
[1] - À vista no dinheiro/cheque: 10% de desconto   
[2] - À vista no cartão de crédito: 5% de desconto
[3] - 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% juros
''')
pagamento = int(input('Escolha a forma de pagamento: '))

if pagamento == 1 :
    print(f'O valor a ser pago é de R${valor_produto * 0.9}')
elif pagamento == 2 :
    print(f'O valor a ser pago é de R${valor_produto * 0.95}')
elif pagamento == 3 :
    print(f'O valor a ser pago é de R${valor_produto}')
elif pagamento == 4 :
    print(f'O valor a ser pago é de R${valor_produto * 1.2}')
else :
    print('Escolha invalida!')