# Exercise 082 - Splitting values into multiple lists

"""Create a program that will read several numbers and put them in a list. 
After that, create two extra lists that will contain only the even values 
and the odd values entered, respectively. At the end, show the content 
of the three generated lists."""

general_list = []
even_numbers = []
odd_numbers = []

while True:
    general_list.append(int(input("Enter a number:\n")))
    question = str(input("Want to continue? [Yes] or [No]\n")).upper().split()

    if question[0] in "Yy":
        print("continuing...")
        continue
    elif question[0] in "Nn":
        print("Ending program...")
        break
    else:
        print("Please, enter a valid answer.")
        continue

for i in general_list:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(f"The general list is: {general_list}.")
print(f"List of even numbers: {even_numbers}.")
print(f"List of odd numbers: {odd_numbers}.")
