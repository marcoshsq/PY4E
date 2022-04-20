# Exercise 062 - Super Arithmetic Progression v3.0

"""Improve CHALLENGE 061 by asking the user if he wants to show some more terms.
The program will terminate when it says it wants to display 0 terms."""

"""The difference between this program and the previous one is that 
we create two new flags and add one more loop level"""

first_term = int(input("Enter the first term: "))
r = int(input("Enter the common difference: "))
term = first_term
counter = 1

"""We create the total, to replace our logical test, 
and the variable plus, to add new terms to our pa"""
total = 0
plus = 10
while plus != 0:
    total += plus
    while counter <= total:
        print(f"{term} ->", end=" ")
        term += r
        counter += 1
    print("Stop!")
    plus = int(input("How many terms do you want to add: "))
print(f"The total number of terms was {total}")
print("End")
