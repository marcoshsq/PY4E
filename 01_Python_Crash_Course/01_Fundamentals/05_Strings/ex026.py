# Exercise 026 - First and last occurrence of a string
'''Make a program that reads a sentence on the keyboard and shows how many times the letter "A" appears,
what position it first appears in and what position it appears last time.'''

name = input('Insert name: ').casefold().strip()
num_a = name.count('a') 
first_a = name.find('a')
last_a = name.rfind('a')

print(f'The letter a appears {num_a} times')
print(f'The first appearence is at {first_a + 1}')
print(f'The last is at {last_a + 1}')
