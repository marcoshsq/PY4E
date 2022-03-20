# Exercise 047 - Counting evens

'''Create a program that displays on the screen all even numbers that are in the range between 1 and 50.'''

# We star at 2 because if we put zero it'll star at zero
# If we put one, it will start at one, then jump two, to three, then 5... and so on up to 50, and we don't want odds, just evens
# Since the range function has an index, it'll always ignore the last number that's why we put 51 at the finish
for i in range(2, 51, 2):
    print(i, end=' ') 

'''end='' is an argument of the print() function that contains a string to be inserted at the end of the line. 
By default it contains the character \n which represents a newline, i.e. end='\n
Since we're putting (end=' ') this command tell python to dysplay the values in just one line.
'''
