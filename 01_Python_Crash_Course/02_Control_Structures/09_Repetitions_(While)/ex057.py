# Exercise #057 - Data Validation

'''Make a program that reads a person's sex, but only accepts 'M' or 'F' values.
If it is wrong, ask for the typing again until you have a correct value.'''

# Create our control variable
control = 0 

# Here we start our loop with our control variable equals 0
while control == 0:

    # We put our question inside the loop, so it will repeat itself until the condition is met
    sexo = input('Enter your sex [M/F]:').strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        control += 1

        if sexo == 'M':
            print('You chose male')
        else:
            print(f'You chose female')
    else:
        print('Wrong data, please type again!')


# another simpler way
sexo = input('Enter your sex [M/F]:').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Wrong data, please type again:').strip().upper()[0]
print(f'You chose {sexo}')
