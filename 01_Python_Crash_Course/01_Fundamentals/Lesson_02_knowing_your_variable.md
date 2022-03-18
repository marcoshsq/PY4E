<div align="center">
  
# Getting to know your variables ✘ 	( ´(ｴ)ˋ )

</div>

## Lesson 02 Content:
1. 0
2. 0
3. 3
4. 4

---

### What is a variable?

Like I've said in the previous lesson, a variable is like a container to a value, once you've assigned some value to a variable it will behaves as the value that it contains. Like high school algebra classes where you needed to find the value of X in an equation, once you found it, you could use X elsewhere and X had the value you had found. But unlike x in algebra classes, in python we can assign different ''types'' values within a variable.

### String (str):

We can assign text to a variable, known as string(str) in python, which is basicaly a series of characters:

    first_name = 'Marcos'    # When we want to write a str in Python we use quotes
    print(first_name)        # But when you want to use a variable you don't need to use quotes
    #output: Marcos
    
    last_name = 'Quirino'
    full_name = first_name +" "+ last_name    # This is string concatenation, we use it to create 
    print("Hello "+full_name)                 # a new variable using the plus sign to join everything.
    #output: Hello Marcos Quirino
    
    print(type(first_name))     # The type function is another built-in function, 
    #output: <class 'str'>      # it gives us the data type of a variable.
    


### Integer (int):

We can assign whole numbers to a variable, since we can't do math with string, we use the next data types for that.

    age = 20      # note, we don't use quotes with integers, because if we do, they become a str.
    age = age + 1      # This is a simple sum, we're adding 1 to our age. 
    print(age)         # We can do that with variables, and the original value will be replaced.
    print(type(age))
    #output: 21
    #output: <class 'int'>
    
    # Let's try to display a message along with age
    
    print("Your age is: "+str(age))   # To do that, we need to do a type cast, 
    # output: Your age is: 21         # transforming our int into a str.
   


### Floating point (float):

A float is a numeric value that can store a decimal portion.

    height(cm) = 175.5
    temperature(C) = 35.8 
    salary(US$) = 959.32
    
    print(type(height))
    print(type(temperature))
    print(type(salary))
    
    #output: <class 'float'>
    #output: <class 'float'>
    #output: <class 'float'>
  
### Boolean:

It is a variable that can only store true or false (0 or 1).

    human = True
    f = 5 > 9
    t = 9 > 5
    
    print(f)
    #output: False
    
    print(t)
    #output: True
    
    print(type(f))
    #output: <class 'bool'>
    
    print(type(t))
    #output: <class 'bool'>



### Python multiple assignment:

Multiple assignment allows us to assign multiple variables at the same time in one line of code.

    name = 'Marcos'
    age = 25
    happy = True

    name, age, happy = "Marcos", 25, True  # We can assign multiple values to different variables
                                           # We just need to use a comma, and assign the values 
    print(name)                            # in the same order we want.
    print(age)
    print(happy)
    
    #output: Marcos
    #output: 25
    #output: True
    
    # If you have different variables with the same value
    # Instead of writing them like this:
    
    a = 30
    b = 30
    c = 30
    d = 30
    
    # You can use multiple assignment:

    a = b = c = d = 30

    print(a)
    print(b)
    print(c)
    print(d)
    
    #output: 30
    #output: 30
    #output: 30
    #output: 30


Wow, we cover a lot till now, what about a challenge?

3. Exercise 003 - Create a program that reads two numbers and displays the sum between them. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/02_First_steps/ex003.py)

---

### String Methods:


### Type Casting:

### Conclusion:

### More content:

