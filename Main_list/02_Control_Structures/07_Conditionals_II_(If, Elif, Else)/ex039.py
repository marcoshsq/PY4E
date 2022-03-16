# Exercício Python 039 - Alistamento Militar

'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade == 18 :
    print(f'O candidato possuí {idade} anos, deve se apresentar IMEDIATAMENTE!')
elif idade > 18 :
    print(f'O candidato possuí {idade} anos, já passou do período de alistamento, você deveria ter se apresentado há {idade - 18} anos!')
    print(f'Seu alistamento foi em {ano_atual - (idade - 18)}')
else :
    print('O candidato tem menos de 18 anos!')
    print(f'Ele possui {idade} anos, faltam {18 - idade} anos para ele se apresentar!')
    print(f'Seu alistamento será em {ano_atual + (18 - idade)}')
