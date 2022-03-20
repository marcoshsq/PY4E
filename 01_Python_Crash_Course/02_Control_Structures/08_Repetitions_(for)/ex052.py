# Exercise 052 - Prime Numbers

'''Write a program that reads an integer and tells whether or not it is a prime number.'''

number = int(input('Enter a number: '))
total = 0

for i in range(1, number + 1):
    if number % i == 0:
        total += 1
print(f'The number {number} was divided {total} times ')
if total == 2:
    print(f'The number {number} is prime')
else:
    print(f'{number} isn\'t prime')
    
