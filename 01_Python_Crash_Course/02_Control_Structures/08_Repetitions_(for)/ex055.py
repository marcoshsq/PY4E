# Exercise 055 - Highest and lowest of the Sequence

'''Make a program that reads the weight of five people. At the end, show which was the highest and lowest weight read.'''


# 1. Trackers
greater_weight = 0
less_weight = 0
question_counter = 0

# 2. Let's ask the user 5x
for i in range(0, 5):
    weight = float(input('Please, enter your weight: '))
    question_counter += 1
    print(f'You entered {weight} for the {question_counter}° person')

# 3. Logic of our program

    if i == 1:
        greater_weight = weight
        less_weight = weight

    else:
        if weight > greater_weight:
            greater_weight = weight

        elif weight < less_weight:
            less_weight = weight


# 4. We print everything
print(f'The biggest weight is {greater_weight}kg')
print(f'The smallest weight is {less_weight}kg')


'''Imagine the following situation, I want you to tell me which is the highest and lowest number.
I'll start: 7. Which is the biggest? 7 right, and the smallest, also 7, agree?.

We've applied the same logic here, we're going to assume that our first loop is already the right one, 
otherwise we'll replace it.'''
    
