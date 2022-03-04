# Python Exercise 034 - Multiple Increases
''' Write a program that asks for an employee's salary and calculates the amount of his raise.
For salaries greater than R$1250.00, calculate a 10% increase.
For those below or equal, the increase is 15%.'''

wage = float(input('Insert a value: '))
if wage >= 1250 :
    print(f'O seu sálario que é R${wage:.2f} passou a ser R${wage * 1.1:.2f}, o valor do aumento foi de R${(wage * 1.1) - wage:.2f}')
else :
    print(f'O seu sálario que é R${wage:.2f} passou a ser R${wage * 1.15:.2f}, o valor do aumento foi de R${(wage * 1.15) - wage:.2f}')