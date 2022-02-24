# Exercício Extra:
'''Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

# Primeiro, vou definir uma função para cada equação.


def male(mh) :              # Função para homens
    m = (72.7*mh) - 58
    return m

def female(fh) :            # Função para mulheres
    f = (62.1*fh) - 44.7
    return f

# Depois fazer perguntar o sexo ao user.

sex = input('What is your gender? Male or Female: ').lower()

# Usando condições posso chamar cada função para o genêro específico.

if sex == 'male' :      # Se forem homens.
    male_height = float(input('What is your height? (In meters) '))
    male_imc = male(male_height)
    print(f'Your ideal weight is {male_imc:.2f} Kg')

elif sex == 'female' :      # Se forem mulheres.
    female_height = float(input('What is your height? (In meters) '))
    female_imc = female(female_height)
    print(f'Your ideal weight is {female_imc:.2f} Kg')

else :
    print('Wrong data u.u')
