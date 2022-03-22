# Exercise #069 - Group Data Analysis

'''Create a program that reads the age and gender of multiple people.

For each registered person, the program should ask if the user 
wants to continue or not. At the end, show:

A) how many people are over 18 years old.
B) how many men were registered.
C) how many women are under 20 years old. 
'''

# Let's star with our counters
add_major = men = woman = 0

while True:

    # We ask for age, and we add up those who are over 18
    age = int(input('Enter age: \n'))
    if age >= 18:
        add_major += 1

    # We ask for the sex, and we add up those who are men
    sex = str(input("Sexo: [M / F] \n")).strip().upper()
    if sex == "M":
        men += 1

    # If they are not men, we see if they are women under 20 and we add
    elif sex == "F":
        if age < 20:
            woman += 1

    # Let's see if the user wants to continue
    choice = str(input("Continue? [Y / N] \n")).strip().upper()
    if choice == "N":
        print(f'People over 18 years: {add_major}.')
        print(f'Total men registered: {men}')
        print(f'Number of women under 20: {woman}')
        break
