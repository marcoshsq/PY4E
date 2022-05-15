# Exercise 004 - Travel Cost
"""Develop a program that asks the distance of a trip in Km.
Calculate the ticket price, charging R$0.50 per km for travel
of up to 200Km and R$0.45 for longer trips."""

distance = float(input("What is the distance to be covered: "))
print(f"You will take a trip of {distance:.2f}Km")


# Normal way
if distance <= 200:
    value_01 = distance * 0.50
    print(f"The ticket price will be R${value_01:.2f}")
else:
    value_02 = distance * 0.45
    print(f"The ticket price will be R${value_02:.2f}")

# or
price = distance * 0.50 if distance <= 200 else distance * 0.45
print(f"The ticket price will be R${price}")
