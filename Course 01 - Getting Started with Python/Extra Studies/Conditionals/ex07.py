# Exercise 007 - Multiple increases
""" Write a program that asks for an employee's salary and calculates the amount of his raise:
For salaries greater than R$1250.00, calculate a 10% increase.
For those below or equal, the increase is 15%."""

wage = float(input("Insert a value: "))
if wage >= 1250:
    print(
        f"Your salary is R${wage:.2f} became R${wage * 1.1:.2f}, the value of the increase was R${(wage * 1.1) - wage:.2f}"
    )
else:
    print(
        f"Your salary is R${wage:.2f} became R${wage * 1.15:.2f}, the value of the increase was R${(wage * 1.15) - wage:.2f}"
    )
