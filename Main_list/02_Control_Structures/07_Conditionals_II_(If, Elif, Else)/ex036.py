# Exercício Python 036 - Aprovando Empréstimo
'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

preço_casa = float(input('Qual o preço da casa: '))
salario = float(input('Qual o seu salário: '))
anos_emprestimo = int(input('Em quantos anos será feito o empréstimo: '))

valor_prestaçao = preço_casa / (anos_emprestimo * 12) # Converter os anos para mesês

if valor_prestaçao < (salario * 0.30) :
    print('O empréstimo foi aprovado! ')
    print(f'O valor da prestação é de R${valor_prestaçao:.2f}')
    print(f'Você deverá pagar por {anos_emprestimo * 12} meses')
elif valor_prestaçao >= (salario * 0.30) :
    print('O empréstimo foi negado! ')
    print(f'O valor do empréstimo foi de {valor_prestaçao:.2f} e o seu sálario é R${salario}')
    print('Renda insuficiente!')
else :
    print('Valores incoretos')