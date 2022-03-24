# Extra Exercise 006

"""Make a program that asks how much you earn per hour and the number of hours worked in the month. Calculate and display your total salary for that month."""

hour_pay = float(input("Earning per hour: "))
worked_hour = float(input("Hours of work: "))
payment = hour_pay * worked_hour
print(f"This month you will receive US${payment:.2f}, be happy u.u")
