# Exercício Extra: let's Code
'''Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
programa deve imprimir a mensagem “O novo valor é [valor]”.'''

value = float(input('Insira o valor total: '))
descount = value * 0.85
print(f'O novo valor é R${descount:.2f}')