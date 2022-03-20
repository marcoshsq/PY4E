# Exercise 050 - Sum of pairs

'''Develop a program that reads six integers and displays the sum of only those that are even.
If the value entered is odd, disregard it.'''

# Our accumulator
sum = 0

for i in range(0, 6):
    
    # This time we want to repeat the question to the user
    # So our iput function goes inside the loop, and it'll repeat per the number of iterations
    num = int(input('Enter a whole number: '))

    # If the number inputted into our variable sum divided by two has zero remainder
    if num % 2 == 0 :

        # will be added
        sum += num       

if sum > 0:     
    print(f'The sum is {sum}')
else:
    print('No number inputted was a pair')
