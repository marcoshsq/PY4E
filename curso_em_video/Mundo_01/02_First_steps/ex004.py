from typing import Type
# Exercise Python 004: Dissecting a variable.
'''Make a program that reads something from the keyboard and displays it on the screen
its primitive type and all possible information about it.'''

variable = input('Insira um valor')
print('O tipo primitivo desse valor é:', type(variable))
print('Contêm apenas letras:', variable.isalpha())
print('Contêm números e letras:', variable.isalnum())
print('Contêm apenas números:', variable.isnumeric())
print('Está em maiuscula:', variable.isupper())
print('Está em minuscula: ', variable.islower())
print('Está capitalizado:', variable.istitle())


'''this .is____() function lets you discover some interesting information
about my input, so it's nice to save that, for some time'''
