import math

# Exercise 017: Right Triangle
"""Write a program that reads the length of the opposite side and the adjacent side of a right triangle.
Calculate and display the length of the hypotenuse."""

# To do this we will use the Pythagorean theorem: a^2 = b^2 + c^2

# Method 01, without the module Math:
# First we ask for the leg values
leg_a = float(input("Enter the value of leg a: "))
leg_b = float(input("Enter the value of leg b: "))
# Then we do the Pythagorean theorem: sqrt((leg_a^2)+(leg_b^2))
hyp = ((leg_a**2) + (leg_b**2)) ** 0.5
print(f"The triangle hypotenuse measures {hyp:.2f} m.u. ")

# Method 02, with the module using pow function:
hypo = math.sqrt(math.pow(leg_a, 2) + math.pow(leg_b, 2))
print(f"The triangle hypotenuse measures {hypo:.2f} m.u. ")

# Method 03 using the module with the hypotenuse function u.u
hypot = math.hypot(leg_a, leg_b)
print(f"The triangle hypotenuse measures {hypot:.2f} m.u. ")
