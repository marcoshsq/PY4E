# Exercise 041 - Classifying Athletes

""" The National Swimming Confederation needs a program that reads the year of
    birth of an athlete and show their category, according to age:
        - Up to 9 years: MIRIM
        - Up to 14 years: CHILDREN
        - Up to 19 years old: JUNIOR
        - Up to 25 years old: SENIOR
        - Over 25 years: MASTER"""

age = int(input("Enter the athlete's age: "))
if age <= 9:
    print("He's a Mirim.")

elif 9 < age <= 14:
    print("He's a Children.")

elif 14 < age <= 19:
    print("He's a Junior.")

elif 19 < age <= 25:
    print("He's a Senior.")

else:
    print("He's a Master.")
