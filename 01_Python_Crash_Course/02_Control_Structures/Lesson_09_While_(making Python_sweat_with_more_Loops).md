<div align="center">
  
# While loops (ﾉ◕ヮ◕)ﾉ ＼(^ω^＼) ヽ(^◇^*)/

</div>

## Lesson 09 Content:

1. []()
2. []()
3. []()
4. []()
5. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_09_While_(making%20Python_sweat_with_more_Loops).md#lesson-wrap-up)
6. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_09_While_(making%20Python_sweat_with_more_Loops).md#conclusion)
7. [More Content](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_09_While_(making%20Python_sweat_with_more_Loops).md#more-content)


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





---

### Lesson Wrap Up:

The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true. We generally use this loop when we don't know the number of times to iterate beforehand.

---

### Conclusion:

In this lesson we talked about the while loop, learned its syntax with some examples and did a lot of exercises, remember there is a lot more to learn about this topic so do a lot of research, a lot of your work as a programmer will be researching and studying, here is just a quick summary to not fill you with theory, so, access the links available at more content, and play with python, remember, you won't break it.

Wow, and so we come to the end of our part 02, how much studied, right? If you made it this far, congratulations and thank you very much, if this material is helping you in any way I will be very happy.
---

### More content
