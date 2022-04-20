from datetime import date

# Exercise 012 - Military Enlistment

"""Make a program that reads a young person's year of birth and reports, according to their age,whether he is still going to enlist in the military, 
whether it's the exact time to enlist or whether it's past the time of enlistment. Your program should also show the time remaining or overdue.."""

# First let's assign the current year to a variable
# That's why we import datetime
current_year = date.today().year

# Now we ask the user for his birth year
birth_year = int(input("Year of birth: "))

# We get his age, using simple math
age = current_year - birth_year


if age == 18:
    print(f"You have {age} years old, you must report IMMEDIATELY!")

elif age > 18:
    print(
        f"The candidate has {age} years past the enlistment period, you should have reported {age - 18} years ago!"
    )
    print(f"Your enlistment was in {current_year - (age - 18)}")

else:
    print("The candidate has less than 18 years!")
    print(f"You have {age} years, {18 - age} years to go before enlisting!")
    print(f"Your enlistment will be in {current_year + (18 - age)}")
