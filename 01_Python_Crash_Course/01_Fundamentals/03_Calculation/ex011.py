# Exercise 011: Painting a wall
'''Write a program that reads the width and height of a wall in meters,
calculate its area and the amount of paint needed to paint it,
knowing that each liter of paint paints an area of 2 square meters.'''

height = float(input('What is the height of the wall? '))
width = float(input('What is the width of the wall? '))
area = height * width
paint = area / 2
print(f'Your wall has the following dimensions: {height}m x {width}m and has an area of: {area}m²')
print(f'To paint this wall, you will need {paint}L of paint')
