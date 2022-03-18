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

### String (str)

We can assign text to a variable, known as string(str) in python, which is basicaly a series of characters:

    first_name = 'Marcos'    # When we want to write a str in Python we use quotes
    print(first_name)        # But when you want to use a variable you don't need to use quotes
    #output: Marcos
    
    last_name = 'Quirino'
    full_name = first_name +" "+ last_name    # This is string concatenation, we use it to create a new variable using the plus sign to join everything.
    print("Hello "+full_name)
    #output: Hello Marcos Quirino
    
    print(type(first_name))     # The type function is another built-in function, it gives us the data type of a variable.
    #output: <class 'str'>
    


### Integer (int)

We can assign whole numbers to a variable, since we can't do math with string, we use the next data types for that.

    age = 20      # note, we don't use quotes with integers, because if we do, they become a str.
    age = age + 1      # This is a simple sum, we're adding 1 to our age. We can do that with variables, and the original value will be replaced.
    print(age)
    print(type(age))
    #output: 21
    #output: <class 'int'>
    
    # Let's try to display a message along with age
    
    print("Your age is: "+str(age))   # To do that, we need to do a type cast, transforming our int into a str.
    # output: Your age is: 21
   


### Floating point (float)

A float is a numeric value that can store a decimal portion.

    height(cm) = 175.5
    temperature(C) = 35.8 
    salary(US$) = 959.32
    #print(type(height))
    #print(type(temperature))
    #print(type(salary))
    #output: <class 'float'>
    #output: <class 'float'>
    #output: <class 'float'>
  
### Boolean

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








