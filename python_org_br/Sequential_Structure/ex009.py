# Exercício Extra:
'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.'''

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
    