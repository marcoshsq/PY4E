<div align="center">
  
# The if statement 🤔🤔🤔

</div>

## Lesson 06 Content:

1. [If... else](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_06_What_if.md#if-else)
2. [If...elif...elif... else](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_06_What_if.md#ifelifelif-else)
3. [Atention](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_06_What_if.md#atention)
4. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_06_What_if.md#lesson-wrap-up)
5. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_06_What_if.md#conclusion)
6. [More content](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_06_What_if.md#more-content)

### If... else

The if statement is one of the most basic control structures, it basically follows this flowchart:

<div align="center">
  
![scala_decision_making](https://user-images.githubusercontent.com/64812097/159143967-7636d10c-6fcc-43ae-9afa-4b0174b9c478.jpg)
  
</div>


The logic is pretty simple, you want Python to do something only if a condition is met, otherwise it will do something else, e.g.: Let's say you are a seller of alcoholic beverages, and you need to create a system for your online store, in your system you cannot sell alcohol to minors. Therefore, your system needs to ask customers for their age. And decide whether they can buy it or not.

```python
age = int(input('Enter your age: '))        # Frist we ask for the client's age;
if age < 18:                                # Then we tell Python, if the client has less than 18 years;
    print('I\'m sorry, you\'re underage!')  # print this;
else:                                       # else means else u.u
    print('Welcome, have fun!')             # print this u.u
```

### If...elif...elif... else

We can also check more than one if condition before we get to the else statement. For this we use the else if statement, elif statement.

<div align="center">
  
![if-elseif-ladder](https://user-images.githubusercontent.com/64812097/159144615-eba073bc-75e3-49c9-bf68-458529a15317.jpg)
  
</div>

Let's say that in your online liquor store you received a notification that seniors can no longer buy alcoholic beverages, because of public health reasons u.u. Now you cannot sell to over 70s. Let's update our system.

```python
age = int(input('Enter your age: '))
if age < 18:
    print('I\'m sorry, you\'re underage!')
elif age > 70:                                
    print('Sorry, For legal reasons, we cannot sell to you')
else:
    print('Welcome, have fun!')
```

## Atention:

We are programming in a sequential way, that is, imagine that each line of your program is like a list:

1. start here
2. then do this
3. then this
4. then this
5. then this
6. then this
7. end here

Python will follow thi list when running your code, what I'm trying to say is, Build your code logically so that every line of code is accessed if needed. For example, Let's say you've started selling soft drinks to people under 15, it's a SpongeBob store, and you decide to use your store's system to recommend this to people under 15, let's update our code.

```python

age = int(input('Enter your age: '))
if age < 18:
    print('I\'m sorry, you\'re underage!')
elif age > 70:
    print('Sorry, For legal reasons, we cannot sell to you')
elif age <= 15:
    print('We have this spongebob store, look how cool. spongebobshop.com ')
else:
    print('Welcome, have fun!')

```
If you run this code, and enter a value lower than 15, you will notice a problem. The spongebob recommendation does not appear, why? Like I said, we are programming in a sequential way, which means that, Python will first ask the age, if we enter, anything between 18 and 70, it will say "Wellcome, have fun", if we print anything above 70, it will say "Sorry, For legal reasons, we cannot sell to you", now, if we put anything under 18, it will first go to our first line, that say, if age is less than 18, give to the user "I'm sorry, you\'re underage!", and finish the program, the problem is 15 is less than 18, but python will never get to that line. And the kids will never know about your Sponge Bob Shop, that's why is super important that you write your code in a sequential and logical way, so we don't let the kids down, ok? Let's fix our code.

```python

age = int(input('Enter your age: '))
if age <= 15:
    print('We have this spongebob store, look how cool. spongebobshop.com ')
elif age < 18:
    print('I\'m sorry, you\'re underage!')
elif age > 70:
    print('Sorry, For legal reasons, we cannot sell to you')
else:
    print('Welcome, have fun!')

```

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


##


That's it, simple isn't? Some important notes:

- Identation, blocks of code are defined by indentation. Code on the same indent level are in the same block. Python will not allow mixed indentation, it's very important that you respect that, ok! 
- For indentation we use 4 spaces, if you are going to use tab, you must configure your IDE, or interpreter to make the tab in space. The important thing is not to mix spaces and tabs. Python is very sensitive about this.
- And lastly the colon, colon is used to represent an indented block. Every time you do something in python that needs indented blocks (for loops, while loops, def functions, etc.), you need the colon ('':'').


##

Pretty simple isn't it? I'm talking, python is super easy u.u. Now let's do some exercises shall we?

28. Exercise 028 - Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try to find out which number was chosen by the computer. The program should write on the screen if the user won or lost. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/06_Conditionals/ex028.py)
29. Exercise 029 - Write a program that reads the speed of a car. If he has 80 km, show a message saying he has been fined. The fine will cost R$7.00 for each km over the limit. [Solution](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/01_Fundamentals/06_Conditionals/ex029.py)
30. Exercise 030 - Create a program that reads an integer and shows on the screen whether it is ODD or EVEN. [Solution](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/01_Fundamentals/06_Conditionals/ex030.py)
31. Exercise 031 - Develop a program that asks the distance of a trip in Km. Calculate the ticket price, charging R$0.50 per km for travel of up to 200Km and R$0.45 for longer trips. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/06_Conditionals/ex031.py)
32. Exercise 032 - Make a program that reads any year and shows if it is a leap year. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/06_Conditionals/ex032.py)
33. Exercise 033 - Create a program that reads three values and says which is the largest and which is the smallest. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/06_Conditionals/ex033.py)
34. Exercise 034 - Write a program that asks for an employee's salary and calculates the amount of his raise: For salaries greater than R$1250.00, calculate a 10% increase. For those below or equal, the increase is 15%. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/06_Conditionals/ex034.py)
35. Exercise 035 - Develop a program that reads the length of three lines and tell the user whether or not they can form a triangle. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/06_Conditionals/ex035.py)
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
---

### Lesson Wrap Up:

````python

name = input('Enter your name')
if name == 'Alice':
    print('Hi, Alice.')
elif name == 'Joe':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')
````

---

### Conclusion:

In this lesson we will talk about if, elif and else, in the next one we will talk about nested if, it's like that movie inception by Nolan where Leonardo di Carpio enters a dream within a dream, only different from the movie, it's important to understand what are nested if.

---

### More content

- [Creator of Python Programming Language, Guido van Rossum | Oxford Union](https://www.youtube.com/watch?v=7kn7NtlV6g0)
- [If... Else](https://www.w3schools.com/python/python_conditions.asp)
