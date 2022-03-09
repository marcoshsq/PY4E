# Exercício Python 011: Pintando parede
'''Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

height = float(input('Qual a altura da parede? '))
width = float(input('Qual a largura da parede? '))
area = height * width
paint = area / 2
print(f'Sua parede possui as seguintes dimensões {height}m x {width}m e possui uma área de {area}m²')
print(f'Para pintar essa parede, será necessário {paint}L de tinta')
