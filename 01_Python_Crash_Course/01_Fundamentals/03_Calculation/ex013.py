# Exercise 013: Salary readjustment
'''Make an algorithm that reads an employee's salary and displays their new salary, with a 15% increase.'''

salary = float(input('Salary: '))
increase = salary * 1.15
print(f'After the 15% increase, the salary of R${salary} became R${increase:.2f} ')
