# Exercise 035 - Analyzing Triangle v1.0
'''Develop a program that reads the length of three lines and
tell the user whether or not they can form a triangle.'''

'''Given three distinct line segments, if the sum of the measures of two of them is always greater than the measure of the third, then they can form a triangle'''

a, b, c = [float(x) for x in input("Please enter the size of three distincts segments: ").split()]

if a + b > c and a + c > b and b + c > a :
    print('The segments can form a triangle')
else :
    print('The segments can not form a triangle')
