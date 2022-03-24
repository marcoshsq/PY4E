# Exercise 014: Temperature converter
"""Write a program that converts a temperature by typing in degrees Celsius
and convert to degrees Fahrenheit."""

celsius = float(input("Enter the temperature in Celsius: \n"))
farenheit = (1.8 * celsius) + 32
print(f"{celsius}ºC correspond to {farenheit:.1f}ºF.")
