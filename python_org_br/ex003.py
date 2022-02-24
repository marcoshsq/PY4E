# Exercício Extra
'''Escreva um programa que solicite ao usuário as horas e o valor da taxa 
por horas para calcular o valor a ser pago por horas de serviço.'''

horas = float(input('Digite a quantidade de horas: '))
taxa = float(input('Digite o valor da taxa: '))
print('O valor a ser pago é: US$', horas * taxa)

# Exercício Extra 
'''Escreva um programa que solicite ao usuário uma temperatura Celsius, 
converta para Fahrenheit, e mostre a temperatura convertida.'''

print('Conversor de temperatura')
celcius = float(input('Insira a temperatura em celcius: '))
a = (celcius*9/5)+32
print('A temperatura em fahrenheit é:', a, 'º fahrenheit')
