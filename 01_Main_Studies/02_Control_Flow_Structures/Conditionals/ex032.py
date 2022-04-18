from datetime import date

# Exercise 032 - Leap Year
"""Make a program that reads any year and shows if it is a leap year."""

year = int(input("Insert the year to be analysed, or zero for current year: "))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"The year {year} is a Leap Year")

else:
    print(f"The year {year} isn't a Leap Year")
