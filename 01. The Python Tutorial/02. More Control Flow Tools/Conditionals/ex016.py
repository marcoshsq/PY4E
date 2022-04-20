# Exercise 016 - Body Mass Index

"""
Develop a logic that reads a person's weight and height, calculates their
Body Mass Index (BMI) and show your status according to the table below:
    - BMI below 18.5: Underweight
    - Between 18.5 and 25: Ideal Weight
    - 25 to 30: Overweight
    - 30 to 40: Obesity
    - Above 40: Morbid Obesity
    
"""

weight = float(input("Qual o seu peso (kg): "))
height = float(input("Qual a sua altura (m): "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, you're Underweight.")

elif 18.5 < bmi < 25:
    print(f"Your BMI is {bmi:.2f}, you have an Ideal Weight .")

elif 25 < bmi < 30:
    print(f"Your BMI is {bmi:.2f}, you're Overweight.")

elif 30 < bmi < 40:
    print(f"Your BMI is {bmi:.2f}, you're obese.")

else:
    print(f"Your BMI is {bmi:.2f}, you're Morbid obese ... wow")
