# Exercise 005: Before and After
'''Write a program that reads an integer and displays its successor and predecessor on the screen'''

# First we're gonna ask the user to input a number
num = float(input('Enter a number: ')) 

# We get the predecessor by subtracting 1 from our variable num
prev_num = num - 1 

# We get the successor by ading 1 to our variable num
next_num = num + 1                     

# Then we just print everything
print(f'Analyzing the value {num}, your predecessor is {prev_num} and his successor is {next_num}')
