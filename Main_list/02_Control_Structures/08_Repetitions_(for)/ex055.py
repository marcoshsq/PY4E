# Exercício Python 055 - Maior e menor da sequência

'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''


maior = 0
menor = 0

# Primeiro ler o peso das pessoas 5x
for i in range(1, 6):
    peso = float(input(f'Qual o peso da {i}º pessoa: ')) 
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    
print(f"O maior peso é {maior}kg")
print(f"O menor peso é {menor}kg.")  
    