# Exercise 004: knowing your variable.
''' Make a program that reads an input from the user and display it on the screen its type and all informations about it. '''

variable = input('Insert a value: ')
print('The type of this variable is:', type(variable))
print('Contain only letters:', variable.isalpha())
print('Contain numbers and letters:', variable.isalnum())
print('Contain only numbers:', variable.isnumeric())
print('It\'s in capital:', variable.isupper())
print('It\'s in lowercase: ', variable.islower())
print('Is capitalized:', variable.istitle())
