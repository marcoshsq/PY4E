# Exercise 042 - Analyzing Triangles v2.0

'''Redo Exercise 035, the one of triangles, 
adding the feature to show what type of triangle will be formed:
    - EQUILATERAL: all sides equal
    - ISOSCELES: two equal sides, one different
    - SCALENO: all different sides'''

'''Given three distinct line segments, if the sum of the measures of two of them
is always greater than the measure of the third, then they can form a triangle'''

# First we ask for the sides of the triangles
side_a = float(input('Insira o valor do lado a do triângulo '))
side_b = float(input('Insira o valor do lado b do triângulo '))
side_c = float(input('Insira o valor do lado c do triângulo '))

# Our first if, is to know if these values form one of the triangles we are looking for, for this we will use the and operator
if side_a < side_b + side_c and side_b < side_c + side_a and side_c < side_a + side_b :

    # If our first if is true we enter this second layer, this is a nested if
    if side_a == side_b == side_c :
        print('Esse segmento forma um triângulo Equilátero!')

    elif side_a != side_b != side_c != side_a :
        print('Esse segmento forma um triângulo Escaleno!')
        
    else :
        print('Esse segmento forma um triângulo Isóceles!')
        
else :
    print('Esse segmento não forma triângulo')
