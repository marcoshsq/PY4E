# Exercise 064 - Handling Multiple Values v1.0

"""Create a program that reads several integers from the keyboard. The program will only stop when
the user enters the value 999, which is the stop condition. At the end, show how many numbers were entered
and what was the sum between them (disregarding the flag)."""

flag = False
sum = 0
counter = 0

while flag == False:
    num = int(input("Enter a value [999 to stop]: "))
    if num == 999:
        flag = True
    else:
        sum += 1
        counter += 1

print(f"You have entered {counter} numbers and the total sum between them is {sum}")
