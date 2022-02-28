# Python Exercise 011: Painting the Wall
'''Make a program that reads the width and height of a wall in meters,
calculate its area and the amount of paint needed to paint it,
knowing that each liter of paint paints an area of 2 square meters.'''

height = float(input('Qual a altura da parede? '))
width = float(input('Qual a largura da parede? '))
area = height * width
paint = area / 2
print(f'Sua parede possui as seguintes dimensões {height}m x {width}m e possui uma área de {area}m²')
print(f'Para pintar essa parede, será necessário {paint}L de tinta')
