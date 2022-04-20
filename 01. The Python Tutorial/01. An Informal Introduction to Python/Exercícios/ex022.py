# Exercise 022 - Text Analyzer
"""Create a program that reads a person's full name and displays:
- The name in all uppercase and lowercase letters.
- How many letters in total (without considering spaces).
- How many letters are in the first name."""

name = str(input("Enter your full name: ")).strip()
name_up = name.upper()  # The name in all capital letters
name_low = name.lower()  # The name in all lowercase letters
number_name = len(name) - name.count(
    " "
)  # How many letters in total (not including spaces)
find_the_space = name.find(
    " "
)  # Find the first space to use as a reference when slicing the first name
first_name = name[:find_the_space]
number_first_name = len(first_name)

print(
    f"Analyzing your name... \n"
    f"Your capitalized name is: {name_up} \n"
    f"Your name in lowercase is: {name_low} \n"
    f"Your name has {number_name} letters \n"
    f"Your name is {first_name} \nand it has {number_first_name} letters"
)
