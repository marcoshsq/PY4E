# Exercise 048 - Sum of odd multiples of three

"""Write a program that calculates the sum of all numbers that are multiples of three and that lie in the range 1 to 500"""

# This is an accumulator, it'll help us build up a value across iterations of a loop
sum = 0
# This is a tracker, it'll help us keep track of some value inside the loop
cont = 0

# Here we're saying [start at 1, stop at 500, jump two by two]
for i in range(1, 501, 2):

    if i % 3 == 0:

        # We add one to our tracker, because we want to count the number of iterarions it has made
        cont += 1
        # We add our control variable to sum, because in each loop, it'll receive a new value
        sum += i

# Our print go outside the loop, because we don't want to repeat it in each iteration
print(f"The sum between all the {cont} numbers is {sum}")
