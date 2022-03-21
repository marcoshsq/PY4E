# Exercise 061 - Arithmetic Progression v2.0
'''Redo CHALLENGE 051, reading the first term and the ratio of an AP, 
showing the first 10 terms of the progression using the while structure.'''


# 1. We'll ask the user to input the first term of our AP
first_term = int(input('Enter the first term: '))

# 2. We ask the common difference (r) of our AP
r = int(input('Enter the common difference: '))

# 3. Now we need to count the first 10 terms, so we will have our term that takes the first term
term = first_term

# 4. And our tracker that'll help us count 
counter = 1

# 5. As we want the first ten terms, we will put ten as our logical test
while counter <= 10:
    print(f'{term} ->', end=' ')
    # 6. Here we update our term, so it doesn't print the repeated values
    term += r
    # 7. And here the counter, so it'll end at 10
    counter += 1

print('End')
