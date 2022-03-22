# Exercise 065 - Largest and Smallest Values

'''Create a program that reads several integers from the keyboard. At the end of execution,
show the average of all values and what was the highest and lowest values read.
The program should ask the user whether or not he wants to continue typing values.'''

flag = False
counter = sum = average = highest = lowest = 0

while flag == False:
    n = float(input("Enter a number: \n"))
    cont = str(input("Do you want to continue? [YES NO] \n")).strip().upper()

    #  Average:
    sum += n
    counter += 1
    average = (sum / counter)

    # highest/lowest:
    if n > highest:
        highest = n
    if lowest == 0:
        lowest = n
    if n < lowest:
        lowest = n

    #  Continuação:
    if cont == "NO":
        flag = True

print(f'Average: {average:.1f}')
print(f'Highest {highest} / Lowest {lowest}')
