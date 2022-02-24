# Exercício Extra: 
'''Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''

hour_pay = float(input('Earning per hour: '))
worked_hour = float(input('Hours of work: '))
payment = hour_pay * worked_hour
print(f'This month you will receive US${payment:.2f}, be happy u.u')