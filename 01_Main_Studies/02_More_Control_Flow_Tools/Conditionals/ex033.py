# Exercise 033 - Largest and smallest.
"""Create a program that reads three values and says which is the largest and which is the smallest."""

a, b, c = [int(x) for x in input("Please enter the numbers: ").split()]

# For the largest

if a > b and c:
    print(f"The largest is {a}")
elif b > c and a:
    print(f"The largest is {b}")
else:
    print(f"The largest is {c}")

# For the smallest

if a < b and c:
    print(f"The smallest is {a}")
elif b < c and a:
    print(f"The smallest is {b}")
else:
    print(f"The smallest is {c}")
