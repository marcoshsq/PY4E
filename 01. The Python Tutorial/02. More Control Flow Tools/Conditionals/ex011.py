# Exercise 011 - Comparing numbers

"""Write a program that reads two integers and compares them. displaying a message on the screen: The first value is higher"""

# First we ask the user for the two numbers
num_1 = int(input("Enter the first value: "))
num_2 = int(input("Enter the second value: "))

# We make simple comparisons
if num_1 > num_2:
    print(f"The number {num_1} is bigger than {num_2}")

elif num_2 > num_1:
    print(f"The number {num_2} is bigger than {num_1}")

elif num_1 == num_2:
    print("The values are the same")
