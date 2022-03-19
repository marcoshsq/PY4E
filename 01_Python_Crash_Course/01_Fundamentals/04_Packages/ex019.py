import random
# Exercise 019 - Sorting an item in the list
''' A teacher wants to draw one of his four students to erase the board. Make a program that helps him, raffling one of the students.'''

name_01 = str(input('Enter the first student\'s name: '))
name_02 = str(input('Enter the second student\'s name: '))
name_03 = str(input('Enter the third student\'s name: '))
name_04 = str(input('Enter the fourth student\'s name: '))

students = [name_01, name_02, name_03, name_04] # This is a list, we're gonna talk about them later
choice = random.choices(students)
print(f'The chosen student was {choice}')
