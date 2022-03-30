# Exercise 087 - More on Array in Python

"""Enhance the previous challenge by showing at the end:

A) The sum of all even values entered.
B) The sum of the values in the third column.
C) The largest value of the second row."""

list_a = list()
list_b = list()

for i in range(0, 3):  # For each line.
    for j in range(0, 3):  # For each column
        list_b.append(int(input(f"Enter a number for [{i}, {j}]: \n")))

    list_a.append(list_b[:])
    list_b.clear()

for l in list_a:
    print(l)

# A) The sum of all even values entered.
sum = 0

for i in range(3):
    for j in range(3):
        if list_a[i][j] % 2 == 0:
            sum += list_a[i][j]

print(f"Sum of even values: {sum}.")

# B) The sum of the values in the third column.
sum_column = 0

for i in range(3):
    for j in range(3):
        if j == 2:  # column 3
            sum_column += list_a[i][j]
print(f"Third column sum: {sum_column}.")

# C) The largest value of the second row.
largest = 0

for i in range(3):
    for j in range(3):
        if i == 1:  # linha 2
            if list_a[i][j] > largest:
                largest = list_a[i][j]
print(f"Highest value of the second row: {largest}.")
