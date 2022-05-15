# Exercise 027 - A person's first and last name
"""Make a program that reads a person's full name,
then showing the first and last name separately."""

name = input("Insert name: ")
first_name = name.split()[0]
last_name = name.split()[-1]
print(f"Hi. nice to meet you mr. {last_name}, or I should call you {first_name}")
