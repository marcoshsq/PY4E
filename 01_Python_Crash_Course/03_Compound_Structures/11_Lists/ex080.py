# Exercise 080 - Ordered list without repetitions

"""Create a program where the user can type five numeric values and register 
them in a list, already in the correct insertion position 
(without using sort()). At the end, show the sorted list on the screen."""

list_numbers = []

for i in range(0, 5):
    number = int(input("Enter a number: "))
    if i == 0 or number > list_numbers[-1]:
        list_numbers.append(number)
        print("Added to the end of the list!")
    else:
        position = 0
        while position < len(list_numbers):
            if number <= list_numbers[position]:
                list_numbers.insert(position, number)
                print(f"Added in position {position} of the list")
                break
            position += 1

print(f"The list you created is {list_numbers}")

# Another solution is:

list_numbers = []

for i in range(0, 5):
    number = int(input(f"Enter a number {i/5}: \n"))

    if len(list_numbers) == 0:  # Dealing with the zero.
        list_numbers.append(number)
        print(
            f"Number {number} added to the position {list_numbers.index(number)} of the list."
        )

    else:
        if number < list_numbers[0]:  # The firs number of the list.
            list_numbers.insert(0, number)
            print(f"Number {number} added to the beginning of the list.")

        elif number > list_numbers[-1]:  # The last number of the list.
            list_numbers.append(number)
            print(f"Number added at the end of the list")

        else:
            for j in list_numbers:
                if number > j:
                    list_numbers.insert(j, number)
        print(f"The sorted list is {list_numbers}")
