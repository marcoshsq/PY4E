# Exercise 075 - Data Analysis in a Tuple

"""Develop a program that reads four values from the 
keyboard and stores them in a tuple. At the end, show:

A) How many times did the value 9 appear.
B) In which position was the first value entered 3.
C) What were the even numbers.
"""

n = (
    int(input("Enter a number: ")),
    int(input("Enter another number: ")),
    int(input("One more, almost there, I promise: ")),
    int(input("The last one: ")),
)

print(f"You entered these numbers: {n}")

# A)
print(f"The number 9 appeared {n.count(9)} times")

# B)
if 3 in n:
    print(f"The number 3 appeared at the {n.index(3) + 1}ª position")

else:
    print("You have not entered any number 3")

# C)
print("The even values were ", end="")
for i in n:
    if i % 2 == 0:
        print(i, end="")
