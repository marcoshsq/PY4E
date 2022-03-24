from time import sleep

# Exercise 046 - Countdown

"""Write a program that displays a countdown on the screen,
going from 10 to 0, with a 1 second pause between."""

print("It's the final Countdown!!!")

sleep(1)  # Function imported from time package

# The range funtion has an index [star, finish, step]
for i in range(10, -1, -1):
    # This will print every iteration of the loop
    # With an second of delay
    print(i)
    sleep(1)

print("The final countdown")
print("OHHHH, OHHHH")
