# Exercício Python 034 - Aumentos múltiplos
''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.'''

wage = float(input('Insert a value: '))
if wage >= 1250 :
    print(f'O seu sálario que é R${wage:.2f} passou a ser R${wage * 1.1:.2f}, o valor do aumento foi de R${(wage * 1.1) - wage:.2f}')
else :
    print(f'O seu sálario que é R${wage:.2f} passou a ser R${wage * 1.15:.2f}, o valor do aumento foi de R${(wage * 1.15) - wage:.2f}')