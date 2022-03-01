# Extra Exercise 012
'''Make a Program for a paint shop.
The program should ask for the size in square meters of the area to be painted.
Assume that the paint coverage is 1 liter for every 6 square meters and that the paint is sold in 18 liter cans,
that cost R$ 80.00 or in gallons of 3.6 liters, which cost R$ 25.00.
Inform the user of the quantities of ink to be purchased and the respective prices in 3 situations:

a) buy only 18 liter cans;

b) buy only 3.6 liter gallons;

c) mix cans and gallons, so that paint waste is less.

Add 10% clearance and always round the values up, ie, consider full cans.'''


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
