# Exercise 002: Answering the User.
"""Ask the user for his name and give him a welcome message."""


# Solution
name = input("What's is your name? ")
print(f"Hi {name}, nice to meet you!")
print("Hi {}, nice to meet you!".format(name))
print("Hi", name + ", nice to meet you!")  # If we use the comma it will add a space
# But with the plus it concatenates!


""" This 'f' inside the print function is a f-string
Also called “formatted string literals”, f-strings 
are strings with the letter f at the beginning and
braces {} to perform expression interpolation.
"""
