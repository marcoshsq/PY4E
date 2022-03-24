# Extra Exercise 005

"""Make a program that calculates the area of a square, then show double this area to the user."""

square_base = float(input("Insert the base value: "))
square_height = float(input("Insert the height value: "))
square_area = square_base * square_height
print(
    f"The square area is {square_area} area units, and its double is {square_area * 2} area units"
)
