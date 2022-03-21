# Exercise 056 - Complete analyzer

'''Develop a program that reads the name, age and gender of 4 people.
At the end of the program, show:
- the average age of the group;
- what is the name of the oldest man;
- how many women are under 20 years old.'''

# 1. Our trackers and accumulators
sum_age = 0
oldest_name = ' '
age_oldest = 0
women = 0


# 1. First we ask the questions 

for i in range(1,5):
    print(f'-----For the {i}° person -----')
    name = str(input('What\'s your name: ')).strip()
    age = int(input('What\'s your age: '))
    sex = str(input('What\'s your sex:[M/m for male | F/f for female] ')).strip().upper()

    # 3. For the average age, let's add it all up here
    sum_age += age
    
    # 4. For the eldest man's name
    if i == 1 and sex in 'Mm':
        age_oldest = age
        oldest_name = name

    # We're following the same logic from the last program
    else:
        if sex in 'Mm' and age > age_oldest:
            age_oldest = age
            oldest_name = name


    # 5. For women under 20:
    if sex in 'Ff' and age < 20:
        women += 1

average_age = sum_age / 4

# 6. print u.u
print(f'The average age of the group is {average_age} years!')
print(f'The older man has {age_oldest}, and it\'s called {oldest_name}')
print(f'In all we have {women} women under 20 years old')
