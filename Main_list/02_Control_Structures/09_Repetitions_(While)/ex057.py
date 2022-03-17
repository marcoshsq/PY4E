# Exercício Python #057 - Validação de Dados
'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

controle = 0 
while controle == 0:
    sexo = input('Insira o seu gênero [M/F]:').strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        controle += 1
        if sexo == 'M':
            print('Você escolheu Masculino')
        else:
            print(f'Você escolheu Feminino')
    else:
        print('Dados incorretos, por favor tente de novo!')


# outra forma mais simples
sexo = input('Insira o seu gênero [M/F]:').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados incorretos, por favor insira o seu sexo [M/F]:').strip().upper()[0]
print(sexo)