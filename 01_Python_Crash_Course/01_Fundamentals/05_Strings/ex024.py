# Exercise 024 - Checking the first letters of a text
'''Create a program that reads the name of a city
say whether or not it starts with a specific name.'''

name = str(input('Enter a name: ')).strip().casefold()
city = name.startswith('specify_a_name_here')
print(city)
