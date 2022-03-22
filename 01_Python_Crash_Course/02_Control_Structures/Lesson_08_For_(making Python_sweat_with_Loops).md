<div align="center">
  
# For loops | (* ^ ω ^) ＼(^ω^＼)

</div>

## Lesson 08 Content:

1. [Python for loops](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#python-for-loops)
2. [Looping Through a String](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#looping-through-a-string)
3. [The break Statement](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#the-break-statement)
4. [The continue Statement](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#the-continue-statement)
5. [The range() Function](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#the-range-function)
6. [Else in For Loop](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#else-in-for-loop)
7. [Nested Loops](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#nested-loops)
8. [The pass Statement](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#the-pass-statement)
9. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#lesson-wrap-up)
10. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#conclusion)
11. [More Content](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_08_For_(making%20Python_sweat_with_Loops).md#more-content)


##

### Python for loops:

Have you noticed that the programs we've written so far don't run continuously? And to repeat a command 20 times we need to do it manually 20 times? This can be a problem when we want to write a program that runs continuously or that repeats x commands N times. To solve this problem we can use loops of repetition.

A loop is a structure that repeats a block of code multiple times while a condition is true. Just like with the if statement, a loop has a block of code, this block will repeat N times given a condition that is recognized for this loop. In python we have two types of loops of repetition: the while and the for loop, let's start with the for.

A for loop is called a looping structure with control variable. It is used when there is a defined amount of repetitions to execute.

![flowchart-for-loop 003-1024x576](https://user-images.githubusercontent.com/64812097/159174654-a27e3a2e-72d8-4e73-a1ae-1a95e9ce030f.jpeg)

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

````python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  # Output: apple
  # Output: banana
  # Output: cherry
````

The for loop does not require an indexing variable to set beforehand.

##

### Looping Through a String:

Strings are iterable objects, they contain a sequence of characters:

````python
for x in "banana":
  print(x)
  # Output: b
  # Output: a
  # Output: n
  # Output: a
  # Output: n
  # Output: a
````

##

### The break Statement:

With the break statement we can stop the loop before it has looped through all the items:

````python
# Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  # Output: apple
  # Output: banana
````

##

### The continue Statement:

With the continue statement we can stop the current iteration of the loop, and continue with the next:

````python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  # Output: apple
  # Output: cherry
````

##

### The range() Function:

To loop through a set of code a specified number of times, we can use the range() function, The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration. You can even use a negative number for the step argument to make the for loop count down instead of up.

````python
for x in range(2, 30, 3):
  print(x)
````

##

### Else in For Loop:

The else keyword in a for loop specifies a block of code to be executed when the loop is finished. The else block will NOT be executed if the loop is stopped by a break statement.

````python
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
````

##

### Nested Loops:

A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop":

````python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
````

##

### The pass Statement:

for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

````python
Example
for x in [0, 1, 2]:
  pass
````
## 

Exercises

46. Exercise 046 - Write a program that displays a countdown on the screen, going from 10 to 0, with a 1 second pause between. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex046.py)
47. Exercise 047 - Create a program that displays on the screen all even numbers that are in the range between 1 and 50. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex047.py)
48. Exercise 048 - Write a program that calculates the sum of all numbers that are multiples of three and that lie in the range 1 to 500. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex048.py)
49. Exercise 049 - Redo Exercise 009, showing the multiplication table of a number that the user chooses. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex049.py)
50. Exercise 050 - Develop a program that reads six integers and displays the sum of only those that are even. If the value entered is odd, disregard it. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex050.py)
51. Exercise 051 - Develop a program that reads the first term and reason of an AP. At the end, show the first 10 terms of this progression. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex051.py)
52. Exercise 052 - Write a program that reads an integer and tells whether or not it is a prime number. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex052.py)
53. Exercise 053 - Create a program that reads any sentence and tells if it is a palindrome, disregarding the spaces. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex053.py)
54. Exercise 054 - Create a program that reads the birth year of seven people. And show how many people are underage and who is an adult. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex054.py)
55. Exercise 055 - Make a program that reads the weight of five people. At the end, show which was the highest and lowest weight read. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex055.py)
56. Exercise 056 - Develop a program that reads the name, age and gender of 4 people. At the end of the program, show: [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/08_Repetitions_(for)/ex056.py)

        - the average age of the group;
        - what is the name of the oldest man;
        - how many women are under 20 years old. 

---

### Lesson Wrap Up:

A for loops, is a loop a statement that will execute it's block of code a limited amount of times.

---

### Conclusion:

In this lesson we talked about for loops, coming up, let's discuss while loops.

---

### More content

- [For loops](https://wiki.python.org/moin/ForLoop)
- [loops in python](https://www.geeksforgeeks.org/loops-in-python/)
- [Python "for" Loops (Definite Iteration)](https://realpython.com/python-for-loop/)
- [Introduction to For Loops in Python](https://www.youtube.com/watch?v=OnDr4J2UXSA&t=111s)
