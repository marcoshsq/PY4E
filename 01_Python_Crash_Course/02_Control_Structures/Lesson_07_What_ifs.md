<div align="center">
  
# Nested if 😕😕😕

</div>

## Lesson 07 Content:

1. []()
2. []()
3. []()
4. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#lesson-wrap-up)
5. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#conclusion)
6. [More content](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/02_Control_Structures/Lesson_07_What_ifs.md#more-content)

##

### Quick reminder If... else:


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
### Indentation

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

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

Tha's it, u.u. It was harder than Prey's last boss during the agdq. But now... it's time for the challenges u.u



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
