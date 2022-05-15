# Exercise 072 - Number by Extension

""" Create a program that has a fully populated 
Tuple with a count in words,from zero to twenty. 

Your program should read a number from the keyboard 
(between 0 and 20) and display it in full.
"""

number_extension = (
    "zaro",
    "one",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "thirteen",
    "Fourteen",
    "Fifhteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "nineteen",
    "Twenty",
)


while True:
    count = int(input("Enter a number between 0 and 20: "))
    if 0 <= count <= 20:
        break
    print("Try again.", end="")
print(f"You entered the number {number_extension[count]}")
