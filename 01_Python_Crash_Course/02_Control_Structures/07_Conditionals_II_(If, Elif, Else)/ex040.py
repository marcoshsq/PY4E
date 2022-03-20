# Exercise 040 - That Classic Average

'''Create a program that reads two grades from a student and calculates their average, showing a message at the end, according to the average achieved:
- Average below 5.0: FAIL'''

grade_01 = float(input('Enter the first grade: ')) 
grade_02 = float(input('Enter the second grade: '))
average = (grade_01 + grade_02) / 2

if 5 <= average <= 10 :
    print(f'The student took {average} of note, was approved! ')

elif 0 <= average < 5 :
    print(f'The student took {average} of note, was disapproved! ')
    
else :
    print('Wrong value')
