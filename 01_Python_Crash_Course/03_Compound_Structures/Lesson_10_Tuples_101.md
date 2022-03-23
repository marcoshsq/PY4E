<div align="center">
  
# Tuples 101

</div>

### Compound structures in python:

A compound structure is something quite simple to understand. Until now, we've been working only with simple variables, which is, you have a value (one value), and you assign this value to a variable, e,g,:


````python
    # Each of this variable were assign to only one value
    # This is a simple structure
    lunch = 'Steak'
    drink = 'Orange juice'
    dessert = 'Ice Cream'
    
    # With compound structures we can do this:
    today_lunch = ('Steak', 'Orange juice', 'Ice Cream') # This is a Tuple btw
````
Basically compound structures, are structures... wait for it... compound by more than one variable. TOday we're gonna star learnig about then and we're gonna start with the Tuple, but know that Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

##

## Lesson 10 Content:
1. [Tuples](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/Lesson_10_Tuples_101.md#tuples)
2. [What can I do with Tuples?](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/Lesson_10_Tuples_101.md#what-can-i-do-with-tuples)
3. [Tuples Inception](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/Lesson_10_Tuples_101.md#tuple-inception)
4. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/Lesson_10_Tuples_101.md#lesson-wrap-up)
5. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/Lesson_10_Tuples_101.md#conclusion)
6. [More Content](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/Lesson_10_Tuples_101.md#more-content)

---

### Tuples:

Tuples are an ordered collection of data, which are immutable, this is important, tuples are immutable. When we say that tuples are ordered, it means that the items have a defined order, and that order will not change. Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created. Since tuples are indexed, they can have items with the same value:

```python   
   thistuple = ("apple", "banana", "cherry", "apple", "cherry")
   print(thistuple)    
```
    
To determine how many items a tuple has, use the len() function, this is one of the mothods of a tuple.

```python
    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))
```

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

```python
    thistuple = ("apple",)
    print(type(thistuple))

    #NOT a tuple
    thistuple = ("apple")
    print(type(thistuple))
```

Tuple items can be of any data type and  a tuple can contain different data types, strings, integers and boolean values, because from Python's perspective, tuples are defined as objects with the data type <class 'tuple'>::

```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```
     
##

### What can I do with Tuples?

Constructors: There's two way to create a tuple, you can either just assign a series of comma separeted values to a variable (in todays version of Python the parentheses aren't required anymore), or you can use the tuple() constructor.

````python
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
````
Methods: index which returns the index of the first occurrence of the specified tuple item and count that returns the number of times the specified item appears in the tuple.

````python
# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p' 
print(my_tuple[5])   # 't'

# IndexError: list index out of range
# print(my_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# my_tuple[2.0]

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4
````

````python
# Accessing tuple elements using slicing
my_tuple = ('p','r','o','g','r','a','m','i','z')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[:])
````

Functions: 

len
Returns an int type specifying number of elements in the collection.

min
Returns the smallest item from a collection.

max
Returns the largest item in an iterable or the largest of two or more arguments.

cmp
Compares two objects and returns an integer according to the outcome.

sum
Returns a total of the items contained in the iterable object.

sorted
Returns a sorted list from the iterable.

reversed
Returns a reverse iterator over a sequence.

all
Returns a Boolean value that indicates whether the collection contains only values that evaluate to True.

any
Returns a Boolean value that indicates whether the collection contains any values that evaluate to True.

enumerate
Returns an enumerate object.

zip
Returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

Operators:

- index operator: Gives access to a sequence’s element;
- slicing: Gives access to a specified range of sequence’s elements,
- concatenation - Returns a concatenation of two sequences,
- multiple concatenation: Returns a sequence self-concatenated specified amount of times.

All these functions, methods and operators were introduced before, in case you forgot, you know, search, search, search.

The mantra you must follow is: "I don't know how to do it, but i know how to google it."


### Tuple Inception



##

Exercises u.u

- 72. Exercise 072 -  - [Solution]()
- 73. Exercise 073 -  - [Solution]()
- 74. Exercise 074 -  - [Solution]()
- 75. Exercise 075 -  - [Solution]()
- 76. Exercise 076 -  - [Solution]()
- 77. Exercise 077 -  - [Solution]()



---

### Lesson Wrap Up:

Tuples are ordered sequences of values, where we can put different types of data inside. We can use various indexing and slicing methods with a tuple. And most importantly, tuples are immutable.

---
      
### Conclusion:

In this lesson we start our studies of composite structures with tuples, in the next lesson we will talk about lists.

---

## More content:

- [Tuple](https://python-reference.readthedocs.io/en/latest/docs/tuple/)
- [Python Tuple](https://www.programiz.com/python-programming/tuple)

