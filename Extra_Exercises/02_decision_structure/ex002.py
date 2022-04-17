"""
Exercise 002 - 

Write a program that checks whether a typed letter is a vowel or a consonant.

"""

letter = str(input("Please enter a letter: "))
print("It's a voewl!" if letter in "AaEeIiOoUu" else "It's a consonant!")
