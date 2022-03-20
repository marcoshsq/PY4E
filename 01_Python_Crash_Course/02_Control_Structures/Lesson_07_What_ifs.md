<div align="center">
  
# Nested if 😕😕😕

</div>

## Lesson 07 Content:

1. [First of all](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#first-of-all)
2. [Quick reminder](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#quick-reminder-if-else)
3. [Indentation](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#indentation)
4. [Elif](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#elif)
5. [Else](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#else)
6. [If Inside If](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#if-inside-if)
7. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#lesson-wrap-up)
8. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#conclusion)
9. [More content](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#more-content)

##

### First of all:

Welcome to part two of our intensive python course, we've already done dozens of exercises and covered a lot of content, but we're not even halfway through yet, so sit in a comfortable place and let's study.

---

### Quick reminder If:

Python supports the usual logical conditions from mathematics:

Equals: a == b

Not Equals: a != b

Less than: a < b

Less than or equal to: a <= b

Greater than: a > b

Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops. An "if statement" is written by using the if keyword.

````python
a = 33
b = 200
if b > a:
    print("b is greater than a") 
````

##

### Indentation

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

##

### Elif

The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

````python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
````
##

### Else

The else keyword catches anything which isn't caught by the preceding conditions.

````python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
````

Now that we've reviewed the entire contents of the ifs statement, I need you to pay close attention, because nested if's are super hard to understand, so wacht carefully.

##

### If Inside If

You can have if statements inside if statements, this is called nested if statements. Here's an example:

````python
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

````

## 

Tha's it, u.u. It was harder than Prey's last boss during the agdq. But now... it's time for the challenges u.u

36. Exercise 036 - Write a program to approve the bank loan for the purchase of a house. Ask the value of the home, the buyer's salary and how many years he will pay.
The monthly installment cannot exceed 30% of the salary or else the loan will be denied. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex036.py)
37. Exercise 037 - Write a Python program that reads any integer and asks it to the user to choose what the conversion base will be: 1 for binary, 2 for octal and 3 for hexadecimal. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex037.py)
38. Exercise 038 - Write a program that reads two integers and compares them. displaying a message on the screen: The first value is higher. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex038.py)
39. Exercise 039 - Make a program that reads a young person's year of birth and reports, according to their age,whether he is still going to enlist in the military,  whether it's the exact time to enlist or whether it's past the time of enlistment. Your program should also show the time remaining or overdue. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex039.py)
40. Exercise 040 - Create a program that reads two grades from a student and calculates their average, showing a message at the end, according to the average achieved: - Average below 5.0: FAIL [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex040.py)
41. Exercise 041 - The National Swimming Confederation needs a program that reads the year of birth of an athlete and show their category, according to age: - Up to 9 years: MIRIM, - Up to 14 years: CHILDREN, - Up to 19 years old: JUNIOR, - Up to 25 years old: SENIOR,- Over 25 years: MASTER. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex041.py)
42. Exercise 042 - Redo Exercise 035, the one of triangles, adding the feature to show what type of triangle will be formed: - EQUILATERAL: all sides equal; - ISOSCELES: two equal sides, one different; - SCALENO: all different sides. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex042.py)
43. Exercise 043 - Develop a logic that reads a person's weight and height, calculates their Body Mass Index (BMI) and show your status according to the table below: - BMI below 18.5: Underweight; - Between 18.5 and 25: Ideal Weight; - 25 to 30: Overweight; - 30 to 40: Obesity; - Above 40: Morbid Obesity. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex043.py)
44. Exercise 044 - Develop a program that calculates the amount to be paid for a product, Considering your normal price and payment term: - cash/check: 10% discount; - cash on card: 5% discount; - up to 2x on the card: formal price; - 3x or more on the card: 20% interest. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex044.py)
45. Exercise 045 - Create a program that makes the computer play Jokenpo with you. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/07_Conditionals_II_(If%2C%20Elif%2C%20Else)/ex045.py)

---

### Lesson Wrap Up:

You can have an inception of if's.

---

### Conclusion:

Well, in this lesson we reviewed the content of conditional structure, and learned nested conditional structures, in the next lesson we will get into the loops part, now things start to get more... interesting u.u
See you space cowboy...

---

### More content:

[Free Code Camp - Blog](https://www.freecodecamp.org/news/)
