# Exercise Python 031 - Cost of Travel
'''Develop a program that asks the distance of a trip in Km.
Calculate the ticket price, charging R$0.50 per km for travel
of up to 200Km and R$0.45 for longer trips.'''

distance = float(input('Qual a distância a ser percorrida: '))
print(f'Você vai realizar uma viagem de {distance:.2f}Km')


# Condicional Comum
if distance <= 200 :
    value_01 = distance * 0.50
    print(f'O valor da passagem será de R${value_01:.2f}')
else :
    value_02 = distance * 0.45
    print(f'O valor da passagem será de R${value_02:.2f}')

# Condicional simplificada
price = distance * 0.50 if distance <= 200 else distance * 0.45   
print(f'O valor da viagem é R${price}')