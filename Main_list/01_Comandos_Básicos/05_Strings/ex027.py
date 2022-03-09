# Python Exercise 027 - A person's first and last name
'''Make a program that reads a person's full name,
then showing the first and last name separately.'''

name = input('Insert name: ')
first_name = name.split()[0]
last_name = name.split()[-1]
print(f'Olá, prazer em conhece-lo sr. {last_name}, ou posso chama-lo de {first_name}')
