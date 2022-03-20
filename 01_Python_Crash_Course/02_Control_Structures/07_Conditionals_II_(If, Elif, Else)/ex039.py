from datetime import date

# Exercise 039 - Military Enlistment

'''Make a program that reads a young person's year of birth and reports, according to their age,whether he is still going to enlist in the military, 
whether it's the exact time to enlist or whether it's past the time of enlistment. Your program should also show the time remaining or overdue..'''



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
