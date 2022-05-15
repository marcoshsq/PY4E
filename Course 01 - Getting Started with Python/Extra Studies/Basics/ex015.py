# Exercise 015: Car rent
"""Write a program that asks the number of kilometers traveled by a rental car
and the number of days for which it was rented. Calculate the price to pay, 
knowing that the car costs R$60 per day and R$0.15 per km driven."""

number_days = float(input("Number of rental days: "))
km_used = float(input("Number of kilometers traveled: "))
payment = (number_days * 60) + (km_used * 0.15)
print(f"The fee is R${payment}")
