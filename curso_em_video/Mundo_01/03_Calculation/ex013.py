# Python Exercise 013: Salary Readjustment
'''Make an algorithm that reads an employee's salary and displays their new salary, with a 15% increase.'''

wage = float(input('Qual o valor do sálario: '))
aumento = wage * 1.15
print(f'Após o aumento de 15%, o salário de R${wage} passou a ser R${aumento:.2f} ')
