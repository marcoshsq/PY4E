# Exercício Python 013: Reajuste salarial
'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

wage = float(input('Qual o valor do sálario: '))
aumento = wage * 1.15
print(f'Após o aumento de 15%, o salário de R${wage} passou a ser R${aumento:.2f} ')