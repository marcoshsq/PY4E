<div align="center">
  
# Getting to know your variables ✘ 	( ´(ｴ)ˋ )

</div>

## Lesson 02 Content:
1. [What is a variable?
](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#what-is-a-variable)
2. [String](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#string-str)
3. [Integer](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#integer-int)
4. [Floating point](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#floating-point-float)
5. [Boolean](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#boolean)
6. [Python multiple assignment](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#python-multiple-assignment)
7. [Type Conversion](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#type-conversion)
8. [String Methods](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#string-methods)
9. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/edit/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#lesson-wrap-up)
10. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#conclusion)
11. [More content](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_02_knowing_your_variable.md#more-content)

---

### What is a variable?

Like I've said in the previous lesson, a variable is like a container to a value, once you've assigned some value to a variable it will behaves as the value that it contains. Like high school algebra classes where you needed to find the value of X in an equation, once you found it, you could use X elsewhere and X had the value you had found. But unlike x in algebra classes, in python we can assign different ''types'' values within a variable.

And about their names. It's important that you give them a nice name as well ok. A variable can have a short name (like x or y) or a more descriptive name (age, name, sum_numbers). But there are some rules:

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- And don't use python [reserved words](https://www.programiz.com/python-programming/keyword-list), he's very sensitive about them, ok.

Here's a list of all keywords in Python Programming:

| False | await | else | import | pass |
| :--: | :--: | :--: | :--: | :--: |
None |	break |	except |	in	| raise
True |	class |	finally |	is |	return
and |	continue |	for |	lambda |	try
as |	def |	from |	nonlocal |	while
assert |	del	| global |	not |	with
async |	elif |	if |	or |	yield

The above keywords may get altered in different versions of Python. Some extra might get added or some might be removed. You can always get the list of keywords in your current version by typing the following in the prompt:

```python
    >>> import keyword
    >>> print(keyword.kwlist) 
```

##

### String (str):

We can assign text to a variable, known as string(str) in python, which is basicaly a series of characters:

```python
    first_name = 'Marcos'    # When we want to write a str in Python we use quotes
    print(first_name)        # But when you want to use a variable you don't need to use quotes
    #output: Marcos
    
    last_name = 'Quirino'
    full_name = first_name +" "+ last_name    # This is string concatenation, we use it to create 
    print("Hello "+full_name)                 # a new variable using the plus sign to join everything.
    #output: Hello Marcos Quirino
    
    print(type(first_name))     # The type function is another built-in function, 
    #output: <class 'str'>      # it gives us the data type of a variable.
```   

##

### Integer (int):

We can assign whole numbers to a variable, since we can't do math with string, we use the next data types for that.


```python
    age = 20      # note, we don't use quotes with integers, because if we do, they become a str.
    age = age + 1      # This is a simple sum, we're adding 1 to our age. 
    print(age)         # We can do that with variables, and the original value will be replaced.
    print(type(age))
    #output: 21
    #output: <class 'int'>
    
    # Let's try to display a message along with age
    
    print("Your age is: "+str(age))   # To do that, we need to do a type cast, 
    # output: Your age is: 21         # transforming our int into a str.
```


##

### Floating point (float):

A float is a numeric value that can store a decimal portion.


```python

    height(cm) = 175.5
    temperature(C) = 35.8 
    salary(US$) = 959.32
    
    print(type(height))
    print(type(temperature))
    print(type(salary))
    
    #output: <class 'float'>
    #output: <class 'float'>
    #output: <class 'float'>
```


##  
  
### Boolean:

It is a variable that can only store true or false (0 or 1).

```python

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
```


##

### Python multiple assignment:

Multiple assignment allows us to assign multiple variables at the same time in one line of code.

```python
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
```

##

### Type Conversion:

The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion. Implicit and Explicit.

In Implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement:

```python
    num_01 = 15   # This is an Int
    num_02 = 10.5 # This is a float

    sum = num_01 + num_02   # We add two variables num_01 and num_02, storing the value in sum

    print(type(sum))
    print(sum)
    
    #output: <class 'float'>  # We get a float from sum
    #output: 25.5   
```

In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion. This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

```python
    x = 1   #int
    y = 2.0 #float
    z = "3" #str
    
    # To convert to int
    x = int(x)
    y = int(y)
    z = int(z)
    
    
    # To convert to float
    x = float(x)
    y = float(y)
    z = float(z)
    
    # To convert to str
    x = str(x)
    y = str(y)
    z = str(z)
```    

Wow, we cover a lot till now, what about a challenge?

3. Exercise 003 - Create a program that reads two numbers and displays the sum between them. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/02_First_steps/ex003.py)

##

### String Methods:

Python has a set of built-in methods that you can use on strings.

```python
    name = "Marcos"
    
    # Actually this is a function, give you the lentgh of you string.
    print(len(name)) 
    #output: 6
    
    # Searches the string for a specified value and returns the position of where it was found
    print(name.find("o")) 
    #output: 4
    
    # Converts the first character to upper case
    print(name.capitalize())
    #output: Marcos
    
    # Converts a string into upper case
    print(name.upper())
    #output: MARCOS
    
    # Converts a string into lower case
    print(name.lower())
    #output: marcos
    
    # Returns True if all characters in the string are digits
    print(name.isdigit())
    #output: False
    
    # Returns True if all characters in the string are in the alphabet
    print(name.isalpha())
    #output: True
    
    # Returns the number of times a specified value occurs in a string
    print(name.count("o"))
    #output: 1
    
    # Returns a string where a specified value is replaced with a specified value
    print(name.replace("o","a"))
    #output: Marcas
    
    # This is not a method, but you can multiply a string
    print(name*3)
    #output: MarcosMarcosMarcos
```

Wow, how many string methods, but there are many others, here is a [list](https://www.w3schools.com/python/python_ref_string.asp) with all of them, for you to play a little bit. Remember, all string methods returns new values. They do not change the original string.

But speaking of playing, how about another exercise?
 
 4. Exercise 004 - Make a program that reads an input from the user and display it on the screen its type and all informations about it. [Solution, if you need](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/02_First_steps/ex004.py)

---

### Lesson Wrap Up:

Data Types:

```python
    Integers:	-2, -1, 0, 1, 2, 3, 4, 5
    Floating-point numbers:	-1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25
    Strings:	'a', 'aa', 'aaa', 'Hello!', '11 cats'
    Bool: True, False, 0, 1
```

String Concatenation and Replication:

```python
    # String concatenation
    'Alice' 'Bob'
    'AliceBob'

    # String Replication:
    'Alice' * 5
    'AliceAliceAliceAliceAlice'
``` 

Variables: 

```python
    '''You can name a variable anything as long as it obeys the following rules:

    - It can be only one word.
    - It can use only letters, numbers, and the underscore (_) character.
    - It can’t begin with a number.
    - Variable name starting with an underscore (_) are considered as "unuseful`. '''
```


The str(), int(), and float() Functions:

```python
      Integer to String or Float:

      str(29)
      #output: '29'
      print(f'I am {29} years old.')
      #output: I am 29 years old.
      str(-3.14)
      #output: '-3.14'

      Float to Integer:

      int(7.7)
      #output: 7
      int(7.7) + 1
      #output: 8  
```

---

### Conclusion:

In this class we talked about variables and data types, type conversion and string methods. So far we are just warming up, from the next lesson things will really start, we will have dozens of exercises to do and you will learn how to turn python into your favorite calculator. See you space cowboy.

---

## More content:

- [Python Type Conversion and Type Casting](https://www.programiz.com/python-programming/type-conversion-and-casting)
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)
- [List of Keywords in Python](https://www.programiz.com/python-programming/keyword-list)
