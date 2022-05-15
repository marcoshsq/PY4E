# Extra Exercise 008

"""Having as input the height (h) of a person, build an algorithm that calculates its ideal weight, using the following formulas:
For men: (72.7*h) - 58
For women: (62.1*h) - 44.7"""

# First, I'll define a function for each equation.


def male(mh):  # Function for men
    m = (72.7 * mh) - 58
    return m


def female(fh):  # Function for women
    f = (62.1 * fh) - 44.7
    return f


# Then ask the user for the gender.

sex = input("What is your gender? Male or Female: ").lower()

# Using conditions I can call each function for the specific genre.

if sex == "male":  # If they are men.
    male_height = float(input("What is your height? (In meters) "))
    male_imc = male(male_height)
    print(f"Your ideal weight is {male_imc:.2f} Kg")

elif sex == "female":  # If they are women.
    female_height = float(input("What is your height? (In meters) "))
    female_imc = female(female_height)
    print(f"Your ideal weight is {female_imc:.2f} Kg")

else:
    print("Wrong data u.u")
