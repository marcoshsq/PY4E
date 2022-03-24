import math  # As a matter of good practice, everything we import comes before the program

# Exercise 016: Cracking a number
"""Create a program that reads any Real number from the keyboard and displays its Integer portion."""


num = float(input("Enter a value: "))
print(
    f"The value entered was {num}, and its integer portion is", math.trunc(num)
)  # Way 01 using trunc function
print(
    f"The value entered was {num}, and its integer portion is", math.floor(num)
)  # Way 02 using floor function
print(
    f"The value entered was {num}, and its integer portion is", int(num)
)  # Way 03 using type casting, int() function

# floor function - round numbers down to the nearest integer
# trunc function - find the integer part of different numbers
