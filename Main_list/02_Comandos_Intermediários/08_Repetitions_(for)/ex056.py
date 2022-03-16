# Exercício Python 056 - Analisador completo

'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
- a média de idade do grupo;
- qual é o nome do homem mais velho;
- quantas mulheres têm menos de 20 anos.'''


soma_idade = 0
nome_mais_velho = ' '
idade_mais_velho = 0
mulheres = 0


# Primeiro fazer as perguntas: 

for i in range(1,5):
    print(f'-----{i}° pessoa -----')
    nome = str(input('Qual o seu nome: ')).strip()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()

    # Para a média de idade:
    soma_idade += idade
    
    # Para o homem mais velho:
    if i == 1 and sexo in 'Mm':
        idade_mais_velho = idade
        nome_mais_velho = nome
    elif sexo in 'Mm' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome


    # Para mulheres com menos de 20 anos:

    if sexo in 'Ff' and idade < 20:
        mulheres += 1

media = soma_idade / 4


print(f'A média de idade do grupo é de {media} anos!')
print(f'O homem mais velho tem {idade_mais_velho}, e se chama {nome_mais_velho}')
print(f'Ao todo temos {mulheres} mulheres com mais de 20 anos')
