# Exercise 063 - Fibonacci Sequence v1.0

"""Write a program that reads any integer N and show on the screen the first N 
elements of a Fibonacci Sequence.

e.g.: 0 - 1 - 1 - 2 - 3 - 5 - 8"""

print("=" * 30)
print("Fibonacci Sequence")
print("=" * 30)
number = int(input("How many terms do you want to show: "))
print("~" * 30)

# As we already know that the first two terms are always the same (0, 1), we have already created them here.
term_1 = 0
term_2 = 1
print("~" * 30)
print(f"{term_1} -> {term_2}", end="")

# As we already have the first and second term, we will start our counter at 3
counter = 3
while counter <= number:
    # At last, As the Fibonacci sequence is the sum of the two previous terms, we create this inside the loop
    term_3 = term_1 + term_2
    print(f" -> {term_3}", end="")
    term_1 = term_2
    term_2 = term_3
    counter += 1
print(" End")
print("~" * 30)
