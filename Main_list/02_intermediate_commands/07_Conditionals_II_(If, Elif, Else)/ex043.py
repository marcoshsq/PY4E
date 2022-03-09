# Exercício Python 043 - Índice de Massa Corporal

'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual o seu peso (kg): '))
altura = float(input('Qual a sua altura (m): '))
imc = peso / (altura * altura)
if imc < 18.5 :
    print(f'Seu imc é {imc:.2f}, você está abaixo do peso.')
elif 18.5 < imc < 25 :
    print(f'Seu imc é {imc:.2f}, você está no peso ideal.')
elif 25 < imc < 30 :
    print(f'Seu imc é {imc:.2f}, você está acima do peso ideal.')
elif 30 < imc < 40 :
    print(f'Seu imc é {imc:.2f}, você está obeso.')
else :
    print(f'Seu imc é {imc:.2f}, você está super obeso... wow')    