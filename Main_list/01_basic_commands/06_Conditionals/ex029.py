# Python Exercise 029 - Electronic Radar
'''Write a program that reads the speed of a car. If it exceeds 80 km/h,
show a message saying he has been fined.
The fine will cost R$7.00 for each km over the limit.'''

velocity = float(input('Qual a velocidade do carro: '))
if velocity > 80 :
    print('MULTADO! Você excedeu o limite de 80km/h ')
    traffic_ticket = (velocity - 80) * 7
    print(f'Você deve paga uma multa de R${traffic_ticket}, seu abestado')
else :
    print('Você não excedeu o limite de velocidade.')
print('Tenha um bom dia, dirija com segurança')