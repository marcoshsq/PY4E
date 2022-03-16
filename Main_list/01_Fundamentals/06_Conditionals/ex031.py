# Exercício Python 031 - Custo da Viagem
'''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
de até 200Km e R$0,45 para viagens mais longas.'''

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