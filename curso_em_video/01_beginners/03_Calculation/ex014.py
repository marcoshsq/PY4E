# Python Exercise 014: Temperature Converter
'''Write a program that converts a temperature by typing in degrees Celsius and converts it to degrees Fahrenheit.'''

# Conversor de Celcius

while True:
    try :
        unity_choice = input('Choose: 1) ° Celcius to ° Farhenheit 2) ° Celcius to °Kelvin : ')
        celcius = float(unity_choice)

# Celcius to Farhenheit

        if celcius == 1 :
            c_to_f = input('Put a value: ')
            c_to_f_value = float(c_to_f)
            result_c_to_f = (c_to_f_value * 9 / 5) + 32
            print(f'{c_to_f}° celcius is {result_c_to_f}° farhenheit')
            break

# Celcius to Kelvin

        elif celcius == 2 :
            c_to_k = input('Put a value: ')
            c_to_k_value = float(c_to_k)
            result_c_to_k = c_to_k_value + 273.15
            print(f'{c_to_k}° celcius is {result_c_to_k}° kelvin')
            break

        elif celcius > 2 :
            print('Choose 1 or 2')

# Update one day 

    except :
        print('Updating Soon')
        break

    else :
        continue
