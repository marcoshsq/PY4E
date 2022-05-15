"""Write a program to prompt for a score between 0.0 and 1.0. 

If the score is out of range, print an error. If the score is between 
0.0 and 1.0, print a grade using the following table:

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85."""


score = input("Enter Score: ")
scr = float(score)

if scr > 1:
    print("Invalid Number")
if 0.9 <= scr <= 1:
    print("A")
elif 0.8 <= scr <= 0.89:
    print("B")
elif 0.7 <= scr <= 0.79:
    print("C")
elif 0.6 <= scr <= 0.69:
    print("D")
elif scr <= 0.59:
    print("F")
elif scr < 0:
    print("Invalid Number")

else:
    print("GG")
