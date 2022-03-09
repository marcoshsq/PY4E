# Python Exercício 041 - Classificando Atletas

''' A Confederação Nacional de Natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

idade = int(input('Qual a idade do atleta: '))
if idade <= 9 :
    print('Você é um atleta mirim.')
elif 9 < idade <= 14 :
    print('Você é um atleta infantil.')
elif 14 < idade <= 19 :
    print('Você é um atleta júnior.')
elif 19 < idade <= 25  :
    print('Você é um atleta sênior.')
else :
    print('Você é um atleta master.')
