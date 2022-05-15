import math

# Extra Exercise 004

"""Write a program that asks for the radius of a circle, calculates and displays its area."""

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius
print(
    f"The area of the circle is {area:.2f} and its circumference is {circumference:.2f}"
)
