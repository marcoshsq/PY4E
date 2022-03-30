# Exercise 081 - Extracting data from a List

"""Create a program that will read several numbers and put them in a list. 

After that, show:

A) How many numbers were entered.
B) The list of values, sorted in descending order.
C) Whether the value 5 was entered and is or is not in the list.
"""

list_numbers = []
while True:
    list_numbers.append(int(input("Enter a number: ")))
    question = str(input("Want to continue? [Yes] or [No]")).upper().split()

    if question[0] in "Y":
        print("continuing...")
        continue
    elif question[0] in "N":
        print("Ending program...")
        break
    else:
        print("Please, enter a valid answer.")
        continue

print(f"You entered {len(list_numbers)} elements in the list")

list_numbers.sort(reverse=True)
print(f"The values are {list_numbers}")

if 5 in list_numbers:
    print("The number 5 is within the list.")
else:
    print("The number 5 isn't in the list ")
