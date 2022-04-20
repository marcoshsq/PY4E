# Exercise 066 - Multiple numbers with flag

"""Create a program that reads integers from the keyboard.

The program will only stop when the user enters the value 999, which is the stop condition. In the end,
show how many numbers were entered and what was the sum between them (disregarding the flag)."""

sum = counter = 0
while True:
    n = int(input("Enter a number [999 to stop] \n"))
    if n == 999:
        break
    else:
        counter += 1
        sum += n
print(f"were typed in total {counter} numbers")
print(f"The sum between them is: {sum}")
