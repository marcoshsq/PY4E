# Extra Exercise
'''Write a program that prompts the user for the hours and fee amount
per hours to calculate the amount to be paid for hours of service.'''

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
