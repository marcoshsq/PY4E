# Exercício Python 053 - Detector de Palíndromo

'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = str(input('Escreva algo: ')).strip().upper()
frase = ''.join(frase.split(' '))
if frase == frase[::-1]:
    print(f'{frase} é um palíndromo!')
else:
    print(f'{frase} Não é um palíndromo!')

# Apos a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona