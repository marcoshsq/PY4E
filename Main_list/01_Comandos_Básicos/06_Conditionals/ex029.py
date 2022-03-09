# Exercício Python 029 - Radar eletrônico
'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocity = float(input('Qual a velocidade do carro: '))
if velocity > 80 :
    print('MULTADO! Você excedeu o limite de 80km/h ')
    traffic_ticket = (velocity - 80) * 7
    print(f'Você deve paga uma multa de R${traffic_ticket}, seu abestado')
else :
    print('Você não excedeu o limite de velocidade.')
print('Tenha um bom dia, dirija com segurança')