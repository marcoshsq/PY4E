# Exercício Python 042 - Analisando Triângulos v2.0

'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

'''Dados três segmentos de reta distintos, 
se a soma das medidas de dois deles é sempre maior que a medida do terceiro, 
então, eles podem formar um triângulo'''

lado_a = float(input('Insira o valor do lado a do triângulo '))
lado_b = float(input('Insira o valor do lado b do triângulo '))
lado_c = float(input('Insira o valor do lado c do triângulo '))

if lado_a < lado_b + lado_c and lado_b < lado_c + lado_a and lado_c < lado_a + lado_c :
    if lado_a == lado_b == lado_c :
        print('Esse segmento forma um triângulo Equilátero!')
    elif lado_a != lado_b != lado_c != lado_a :
        print('Esse segmento forma um triângulo Escaleno!')
    else :
        print('Esse segmento forma um triângulo Isóceles!')
else :
    print('Esse segmento não forma triângulo')
