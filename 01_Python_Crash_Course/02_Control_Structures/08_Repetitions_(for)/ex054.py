from datetime import datetime

# Exercise 054 - Majority Group

'''Create a program that reads the birth year of seven people.
And show how many people are underage and who is an adult.'''

# 1. Get the current year
current_year = datetime.now().year

# 2. trackers
count_majors = 0
count_minors = 0

# 3. Ask 7x a person's birthday and get their age
for i in range(1, 8):
    birthdate_year = int(input('Enter your birthdate year: '))
    age = current_year - birthdate_year

# 4. The logic of our program
    if age >= 21:
        count_majors += 1

    elif age < 21:
        count_minors += 1   

    else: 
        print('Wrong number.')

# 5. We print everything
print(f'There are {count_majors} people of legal age de idade.') 
print(f'There are {count_minors} underage.')
