# Python Exercise 015: Car Hire
'''Write a program that asks the number of kilometers traveled by a rental car
and the number of days for which it was rented.
Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven.'''

number_days =  float(input('Quantidade de dias de aluguel: '))
km_used = float(input('Quantidade de Km percorridos: '))
payment = (number_days * 60) + (km_used * 0.15)
print(f'O valor a pagar é de R${payment}')
