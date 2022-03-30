# Exercise 078 - Largest and Smallest Values in the List

"""Write a program that reads 5 numeric values and stores them in a list. 
At the end, show which was the highest and lowest value entered, 
and their respective positions in the list.
"""

list_numbers = []
list_highest = []
list_lowest = []
highest = lowest = pos_highest = pos_lowest = 0

# 1 - Read five values and store then in a list:
for number in range(0, 5):
    list_numbers.append(int(input(f"Enter the {number + 1}º number: \n")))

print(f"You entered the values: {list_numbers}.")

# 2 - Highest and lowest value entered:

for i, num in enumerate(list_numbers):
    if lowest == 0:  # We equal everything to zero.
        lowest = num

    if num < lowest:  # Finding the lowest.
        lowest = num
    if num > highest:  # Finding the highest.
        highest = num

# Or

lowest_list = min(list_numbers)
highest_list = max(list_numbers)

print(f"The highest value was {highest}")
for position, index in enumerate(list_numbers):
    if index == highest:
        print(f"And it appeared in the {index}º position in the list.")

print(f"The lowest values was {lowest}")
for position, index in enumerate(list_numbers):
    if index == lowest:
        print(f"And it appeared in the {index}º position in the list.")
