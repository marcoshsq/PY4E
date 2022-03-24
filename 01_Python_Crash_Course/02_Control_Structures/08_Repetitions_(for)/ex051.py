# Exercise 051 - Arithmetic Progression

"""Develop a program that reads the first term and reason of an AP.
At the end, show the first 10 terms of this progression."""

# To facilitate your viewing:

first_term = int(input("What is the first term of this Arithmetic Progression?: "))
r = int(input("What is the common difference for progression? "))
num_terms = int(input("How many terms you want in this Arithmetic Progression?: "))
nth_term = first_term + (num_terms - 1) * r

for i in range(first_term, nth_term, r):
    print(i, end=" > ")

print("End")

# -------

# Code explained

"""An arithmetic progression is a numerical sequence in which each term, starting from the second, 
is equal to the sum of the previous term with a constant r. The number r is called the ratio 
or common difference of the arithmetic progression."""

# 1. We'll ask the user to input the first term of our AP
first_term = int(input("What is the first term of this Arithmetic Progression?: "))

# 2. We ask the common difference (r) of our AP
r = int(input("What is the common difference for progression? "))

""" Here's the trick, only with these two variables we have a problem
Our AP, will not work, because we want the first ten terms of this progression
to solve our problem we use what is calles the general term of an arithmetic progression (nth term)
The formula is: nth term = first term + (the_nº_of_terms_we_want - 1) * r
We could do this calculation and put 10 as our "the_nº_of_terms_we_want"
But that would only solve this question for the first 10 terms
Let's create a question that solves for any number of terms """

# 3. We create a variable with the_nº_of_terms_we_want
num_terms = int(input("How many terms you want in this Arithmetic Progression?: "))

# 4. Now let's do our nth_term equation
nth_term = first_term + (num_terms - 1) * r

# When creating our for loop, we will use the range function, remember range(star, stop, step)
# 5. So it'll be for i in range(start with the first_term, stop at the nth_term, step from r to r) this is:
for i in range(first_term, nth_term, r):
    # 6. Then we print our control variable inside the loop, because we want to see each iteration
    print(i, end=" > ")

print("End")
