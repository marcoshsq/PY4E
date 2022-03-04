# Python Exercise 024 - Checking the first letters of a text
'''Create a program that reads the name of a city
say whether or not it starts with the name "Santo".'''

name = str(input('Insira o nome da cidade: ')).strip().casefold()
city = name.startswith('santo')
print(city)
