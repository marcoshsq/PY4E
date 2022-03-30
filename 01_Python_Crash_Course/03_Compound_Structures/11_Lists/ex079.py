# Exercise 079 - Single Values in a List

"""Create a program where the user can enter several numeric values and register them in a list. 
If the number already exists in there, it will not be added. 
At the end, all unique values entered will be displayed, in ascending order."""

list_numbers = []

while True:
    number = int(input("Enter a number: \n"))
    if number in list_numbers:
        print("The number you enter is already on the list!")
    else:
        list_numbers.append(number)
        print("The number you entered was added")

    question = str(input("Want to continue? [Yes] or [No]\n")).strip().upper()

    if question[0] == "N":
        break
    elif question == "Y":
        print("Continuing on!...")
    else:
        print("Please, enter Yes or No!")

list_numbers.sort()
print(f"You entered the values: {list_numbers}!")
