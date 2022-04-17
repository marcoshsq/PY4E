# Exercise 086 - Matrix in Python

"""Create a program that declares a 3x3 dimensional matrix and fills it with 
values read from the keyboard. At the end, show the matrix on the screen, 
with the correct formatting."""

list_a = list()
list_b = list()

for i in range(0, 3):  # For each line.
    for j in range(0, 3):  # For each column
        list_b.append(int(input(f"Enter a number for [{i}, {j}]: \n")))

    list_a.append(list_b[:])
    list_b.clear()

for l in list_a:
    print(l)

# Another solution

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matrix[i][j] = int(input(f"Enter a number for [{i}, {j}]: \n"))

for i in range(0, 3):
    for j in range(0, 3):
        print(f"{matrix[i][j]}", end=" ")
    print()
