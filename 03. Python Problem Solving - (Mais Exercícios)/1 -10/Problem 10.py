# Como encontrar a área de um círculo em Python.
from math import pi


def area_circulo():
    """Função que calcula a
    área de um circulo"""
    raio = int(input("Entre o valor do raio do cícrulo: "))
    area = pi * pow(raio, 2)
    return print(f"A área do circulo é: {area:.2f} u.a.")


area_circulo()
