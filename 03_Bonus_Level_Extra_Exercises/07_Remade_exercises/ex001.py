# Extra Exercise 001 - 

'''
Make a program that asks for a monetary value and decrease it by 15%. 
Your program should print the message "New value is [value]".
'''

value = float(input('Enter the total amount: '))
descount = value * 0.85
print(f'The new value is US${descount:.2f}')
