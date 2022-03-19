import random

# Exercise 020 - Sorting an order in the list
'''The same teacher from challenge 019 wants to draw the order of presentation of student work.
Make a program that reads the names of the four students and shows a random order.'''

name_01 = str(input('Enter the first student\'s name: '))
name_02 = str(input('Enter the second student\'s name: '))
name_03 = str(input('Enter the third student\'s name: '))
name_04 = str(input('Enter the fourth student\'s name: '))

students = [name_01, name_02, name_03, name_04]
random.shuffle(students)
print(f'The order of presentation will be: {students}')
