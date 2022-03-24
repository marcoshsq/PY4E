# Exercise 023 - Separating digits of a number
"""Write a program that reads a number from 0 to 9999 and
display each of the separate digits on the screen."""

number = int(input("Enter a number: "))
unity = (number // 1) % 10
ten = (number // 10) % 10
hundred = (number // 100) % 10
thousand = (number // 1000) % 100

print(f"Analyzing the number {number} it is composed of: ")
print(f"Unit: {unity}")
print(f"ten: {ten}")
print(f"Hundred: {hundred}")
print(f"thousand: {thousand}")
