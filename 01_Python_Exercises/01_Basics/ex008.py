# Exercise 008: Measurement converter
"""Create a program that reads a value in meters and display it converted to centimeters and millimeters. """

# First we ask for the value
# Since we working with sizes, we're gonna do a Type casting to get a float variable
meters = float(input("Enter a value: "))

# A cool thing we can do with f-strings
# is make the calculation inside the print u.u
print(
    f"The multiples of {meters}m are: {meters / 10}dam, {meters / 100}hm, e {meters / 1000}km"
)
print(
    f"The submultiples of {meters}m are: {meters * 10}dm, {meters * 100}cm e {meters * 1000}mm"
)
