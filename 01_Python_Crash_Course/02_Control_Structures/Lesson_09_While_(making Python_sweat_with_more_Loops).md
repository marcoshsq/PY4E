<div align="center">
  
# While loops (ﾉ◕ヮ◕)ﾉ ＼(^ω^＼) ヽ(^◇^*)/

</div>

## Lesson 09 Content:

1. [While loop 101](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_09_While_(making%20Python_sweat_with_more_Loops).md#while-loop-101)
2. [While loop with else](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_09_While_(making%20Python_sweat_with_more_Loops).md#while-loop-with-else)
3. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_09_While_(making%20Python_sweat_with_more_Loops).md#lesson-wrap-up)
4. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_09_While_(making%20Python_sweat_with_more_Loops).md#conclusion)
5. [More Content](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/Lesson_09_While_(making%20Python_sweat_with_more_Loops).md#more-content)


##

### While loop 101:

A while loop is what we call a repetition structure with logical test. Unlike for, which was a repeating structure with a control variable, where we wanted to loop a certain number of times, and for that we had a control variable. With the while loop, our code will keep running infinitely until the condition we passed (logical test) becomes false. 

![flowchart-for-loop 003-1024x576](https://user-images.githubusercontent.com/64812097/159175471-ccbf68ef-f333-488b-845b-e4d6a121013b.jpeg)

In a super simple and summarized way, for is a finite loop, you use for when you want to perform a number of iterations for a known number of times. With while you don't know how many iterations it will take, so you create a logical condition that will only become false when the loop gets the iteration you're looking for.

````python
#Syntax of while Loop in Python:

while test_expression:
    Body of while
````

Example: Python while Loop

````python
# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
````

In the above program, the test expression will be True as long as our counter variable i is less than or equal to n (10 in our program).

We need to increase the value of the counter variable in the body of the loop. This is very important (and mostly forgotten). Failing to do so will result in an infinite loop (never-ending loop).

## While loop with else:

Same as with for loops, while loops can also have an optional else block.

The else part is executed if the condition in the while loop evaluates to False.

The while loop can be terminated with a break statement. In such cases, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.

Here is an example to illustrate this.

````python

'''Example to illustrate
the use of else statement
with the while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

````

Here, we use a counter variable to print the string Inside loop three times.

On the fourth iteration, the condition in while becomes False. Hence, the else part is executed.

##

Exercises ＼(^ω^＼): (o^▽^o)

57. Exercise 057 - Make a program that reads a person's sex, but only accepts 'M' or 'F' values. If it is wrong, ask for the typing again until you have a correct value. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex057.py)
58. Exercise 058 - Improve the game of exercise 028 where the computer will "think" of a number between 0 and 10. But now the player will try to guess until he gets it right, showing at the end how many guesses were needed to win. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex058.py)
59. Exercise 059 - Create a program that reads two values and displays a menu on the screen: [ 1 ] sum; [ 2 ] multiply; [ 3 ] bigger; [ 4 ] add new numbers; [5] exit the program. Your program should perform the requested operation in each case. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex059.py)
60. Exercise 060 - Make a program that reads any number and displays its factorial. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex060.py)
61. Exercise 061 - Redo CHALLENGE 051, reading the first term and the ratio of an AP, showing the first 10 terms of the progression using the while structure. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex061.py)
62. Exercise 062 - Improve CHALLENGE 061 by asking the user if he wants to show some more terms. The program will terminate when it says it wants to display 0 terms. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex062.py)
63. Exercise 063 - Write a program that reads any integer N and show on the screen the first N elements of a Fibonacci Sequence. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex063.py)
64. Exercise 064 - Create a program that reads several integers from the keyboard. The program will only stop when the user enters the value 999, which is the stop condition. At the end, show how many numbers were entered and what was the sum between them (disregarding the flag). [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex064.py)
65. Exercise 065 - Create a program that reads several integers from the keyboard. At the end of execution, show the average of all values and what was the highest and lowest values read. The program should ask the user whether or not he wants to continue typing values. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex065.py)
66. Exercise 066 - Create a program that reads integers from the keyboard. The program will only stop when the user enters the value 999, which is the stop condition. In the end, show how many numbers were entered and what was the sum between them (disregarding the flag). [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex066.py)
67. Exercise 067 - Write a program that displays the multiplication table of several numbers, one at a time, for each value entered by the user. The program will stop when the requested number is negative. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex067.py)
68. Exercise 068 - Make a program that plays odd or even with the computer. The game will only be stopped when the player loses, showing the total number of consecutive wins he had at the end of the game. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex068.py)
69. Exercise 069 - Create a program that reads the age and gender of multiple people. For each registered person, the program should ask if the user wants to continue or not. At the end, show: [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex069.py)
 
        A) how many people are over 18 years old. 
        B) how many men were registered. 
        C) how many women are under 20 years old. 

70. Exercise 070 - Create a program that reads the name and price of multiple products. The program should ask if the user will continue or not. At the end, show: [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex070.py)

        A) what is the total spent on the purchase.
        B) how many products cost more than R$1000.
        C) what is the name of the cheapest product. 
        
71. Exercise 071 - Create a program that simulates the operation of an ATM. At the beginning, ask the user what will be the amount to be withdrawn (integer) and the program will inform how many bills of each value will be delivered. OBS: consider that the ATM has notes of R$50, R$20, R$10 and R$1. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/02_Control_Structures/09_Repetitions_(While)/ex071.py)

---

### Lesson Wrap Up:

The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true. We generally use this loop when we don't know the number of times to iterate beforehand.

---

### Conclusion:

In this lesson we talked about the while loop, learned its syntax with some examples and did a lot of exercises, remember there is a lot more to learn about this topic so do a lot of research, a lot of your work as a programmer will be researching and studying, here is just a quick summary to not fill you with theory, so, access the links available at more content, and play with python, remember, you won't break it.

Wow, and so we come to the end of our part 02, how much studied, right? If you made it this far, congratulations and thank you very much, if this material is helping you in any way I will be very happy.

In the next part we will talk about composite structures in python, lists, tuples, dictionaries and so on. And we'll also learn some more advanced concepts like functions and classes, in addition to modularization. Ours is going to be really cool. Anyway, thank you very much for your attention and see you, space cowboy.

---

### More content:

- [Python Looping Techniques](https://www.programiz.com/python-programming/looping-technique)
- [loops in python](https://www.geeksforgeeks.org/loops-in-python/)
- [While loops](https://wiki.python.org/moin/WhileLoop)
