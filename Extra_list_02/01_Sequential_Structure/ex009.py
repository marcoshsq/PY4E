# Extra Exercise 009
'''João Papo-de-Pescador, a good man, bought a microcomputer to monitor the daily income of his work.
Every time he brings in a weight of fish greater than that established by the fishing regulations of the state of São Paulo
(50 kilos) must pay a fine of BRL 4.00 for each excess kilo.
João needs you to write a program that reads the variable weight (weight of fish) and calculates the excess.
Record in the excess variable the amount of kilos beyond the limit and in the fine variable the amount of the fine that João must pay.
Print the program data with the appropriate messages.'''

# Para cada kg acima dos 50kg estabelecidos, multa de R$4,00 por kg excedente;
# Criar um programa que leia a quantidade de peixe em kg e diga o excedente;
# Criar uma variável que receba o valor a mais;
# Calcular o valor da multa.

peso = float(input('Insira o número de kilos de peixe: '))
if peso > 50 :
    excedente = peso - 50
    multa = excedente * 4
    print(f'Você possui {excedente}kg a mais do que o permitido')
    print(f'O valor da multa é de R${multa}')
elif peso <= 50 :
    print('Quantidade dentro do permitido')
else :
    print('Nothing')
    
