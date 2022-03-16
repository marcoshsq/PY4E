# Exercício Python 054 - Grupo da Maioridade

'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

# Primeiro: Obter o ano atual:
from datetime import datetime
ano_atual = datetime.now().year

# Segundo: Contadores:
cont_maiores = 0
cont_menores = 0

# Terceiro: Ler o ano de nascimento 7x:
for i in range(1, 8):
    ano = int(input('Insira o seu ano de nascimento: '))

# Quarto: Lógica do programa:
    if ano_atual - ano >= 18:
        cont_maiores += 1

    elif ano_atual - ano < 18:
        cont_menores += 1   

    else: 
        print('Dados invalidos.')

print(f'Existem {cont_maiores} maiores de idade.') 
print(f'Existem {cont_menores} menores de idade.')