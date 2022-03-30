# Exercise 085 - Odd and Even Lists

"""Create a program where the user can enter seven numeric values and register 
them in a single list that keeps even and odd values separate. At the end, show 
the even and odd values in ascending order."""

general_list = []
even_numbers = []
odd_numbers = []

for i in range(0, 7):
    general_list.append(int(input(f"Enter the {i + 1}º number:\n")))

for i in general_list:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

even_numbers.reverse()
odd_numbers.reverse()

print(even_numbers)
print(odd_numbers)
