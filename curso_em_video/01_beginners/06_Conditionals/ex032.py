# Python Exercise 032 - Leap Year
'''Make a program that reads any year and shows if it is a leap year.'''

from datetime import date

year = int(input('Insert the year to be analysed, or zero for current year: '))
if year == 0 :
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print(f'O ano {year} é bissexto')
else :
    print(f'O ano {year} não é bissexto')
