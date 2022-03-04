# Extra Exercise 001: let's Code
'''Make a program that asks for a monetary value and decrease it by 15%. Your
program should print the message “New value is [value]”.'''

value = float(input('Insira o valor total: '))
descount = value * 0.85
print(f'O novo valor é R${descount:.2f}')
