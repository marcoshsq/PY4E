# Exercício Extra 012

'''Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

a) comprar apenas latas de 18 litros;

b) comprar apenas galões de 3,6 litros;

c) misturar latas e galões, de forma que o desperdício de tinta seja menor. 

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''


import math

M2_POR_LITRO = 6
PRECO_GALAO = 80
LITROS_GALAO = 18
PRECO_LATA = 25
LITROS_LATA = 3.6
MARGEM_SEGURANCA = 1.1


m2 = float(input('informe a quantidade de METRO QUADRADO (m²) a ser pintado: '))

consumo_litro = m2 / M2_POR_LITRO * MARGEM_SEGURANCA

qtd_galao_apenas = math.ceil(consumo_litro / LITROS_GALAO)
valor_galao_apenas = qtd_galao_apenas * PRECO_GALAO

qtd_lata_apenas = math.ceil(consumo_litro / LITROS_LATA)
valor_lata_apenas = qtd_lata_apenas * PRECO_LATA

qtd_galao_misto = consumo_litro // LITROS_GALAO
qtd_lata_misto = math.ceil((consumo_litro - qtd_galao_misto * LITROS_GALAO) / LITROS_LATA)
valor_galao_misto = qtd_galao_misto * PRECO_GALAO
valor_lata_misto = qtd_lata_misto * PRECO_LATA

print()
print(f'o consumo de tinta é: {consumo_litro:.2f} LITROS')
print()
print(f'a quantidade de GALOES de 18 LITROS a ser usado é: {qtd_galao_apenas:.0f}')
print(f'o valor total em GALOES de 18 LITROS é: R$ {valor_galao_apenas:.2f}')
print()
print(f'a quantidade de LATAS de 3,6 LITROS a ser usado é: {qtd_lata_apenas:.0f}')
print(f'o valor total em LATAS de 3,6 LITROS é: R$ {valor_lata_apenas:.2f}')
print()
print('considerando o menor desperdíciode tinta, temos:')
print(f'quantidade galões: {qtd_galao_misto:.0f}')
print(f'quantidade latas: {qtd_lata_misto:.0f}')
print(f'quantidade total mistas: {qtd_galao_misto + qtd_lata_misto:.0f}')
print(f'valor total considerando GALOES e LATAS é: R$ {valor_galao_misto + valor_lata_misto:.2f}')
