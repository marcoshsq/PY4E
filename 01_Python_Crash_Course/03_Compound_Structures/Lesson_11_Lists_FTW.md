<div align="center">
  
# Lists For the WIN!!!

</div>

### Why do I need a List if I have a Tuple?

Because lists are mutable u.u

Actually, there are a few more differences between lists and tuples, but basically, almost all of them occur because of this mutability rule. I'll give you a few examples:

| LIST |	TUPLE |
| :-- | :-- |
| Lists are mutable |	Tuples are immutable |
| Implication of iterations is Time-consuming |	The implication of iterations is comparatively Faster |
| The list is better for performing operations, such as insertion and deletion. |	Tuple data type is appropriate for accessing the elements |
| Lists consume more memory |	Tuple consume less memory as compared to the list |
| Lists have several built-in methods |	Tuple does not have many built-in methods. |
| The unexpected changes and errors are more likely to occur |	In tuple, it is hard to take place. |

Later, when you, and me as well, get more proficient with python, we'll learn a few more applications with these Data Structures, for example, we use tuples to create tables using pandas... but this is a spoiler. Lists!
##

## Lesson xx Content:
1. []()
2. []()

---

### Creating lists:

Just like a Tuple, a Lit is a container for multiple data, to create a list we use square brackets [], separated by commas. A list can have any number of items and they may be of different types (integer, float, string, etc.). A list can also have another list as an item. This is called a nested list, just like the tuple... told ya.

````python

# Simple list
eg_list = [1, 2, 3]

# empty list
eg_list = []

# list with mixed data types
eg_list = [1, "Hello", 3.14]

# nested list
eg_list = ["mouse", [8, 4, 6], ['a']]

````

##

### Accessing List Elements

We can use the index operator [] to access an item in a list. In Python, indices start at 0. So, a list having 5 elements will have an index from 0 to 4.

Trying to access indexes other than these will raise an IndexError. The index must be an integer. We can't use float or other types, this will result in TypeError.

Nested lists are accessed using nested indexing.


```python
   
my_list = ['p', 'r', 'o', 'b', 'e']

# first item
print(my_list[0])  # p

# third item
print(my_list[2])  # o

# fifth item
print(my_list[4])  # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])
    
```

We can also use Negative indexing Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

```python
   
# Negative indexing in lists
my_list = ['p','r','o','b','e']

# last item
print(my_list[-1])

# fifth last item
print(my_list[-5])

```

##

### List Slicing

We can access a range of items in a list by using the slicing operator :.


```python
   
# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# elements from index 2 to index 4
print(my_list[2:5])

# elements from index 5 to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])
    
```

##

### Add/Change List Elements

Lists are mutable, meaning their elements can be changed unlike string or tuple.

We can use the assignment operator = to change an item or a range of items.

```python
   
# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd)                   
    
```

We can add one item to a list using the append() method or add several items using the extend() method.

```python
   
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)
    
```

We can also use + operator to combine two lists. This is also called concatenation.

The * operator repeats a list for the given number of times.

```python
   
# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)
    
```

Furthermore, we can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.

```python
   
# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd)

odd[2:2] = [5, 7]

print(odd)

```

##

### Delete List Elements

We can delete one or more items from a list using the Python del statement. It can even delete the list entirely.

```python
   
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete the entire list
del my_list

# Error: List not defined
print(my_list)
    
```

We can use remove() to remove the given item or pop() to remove an item at the given index.

The pop() method removes and returns the last item if the index is not provided. This helps us implement lists as stacks (first in, last out data structure).

And, if we have to empty the whole list, we can use the clear() method.

```python
   
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)
    
```
  
##

### Iterating Through a List

Using a for loop we can iterate through each item in a list.


```python
   
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
    
```
  
##

### Python List Methods:

Python has many methods to work with lists. Here are the more commonly used, with a few examples, but i'll leave in the end a reference sheet, so you can explore even further if you're interested.

| Methods |	Descriptions |
| :-- | :-- |
append() |	adds an element to the end of the list
extend() |	adds all elements of a list to another list
insert() |	inserts an item at the defined index
remove() |	removes an item from the list
pop() |	returns and removes an element at the given index
clear() |	removes all items from the list
index() |	returns the index of the first matched item
count() |	returns the count of the number of items passed as an argument
sort() |	sort items in a list in ascending order
reverse() |	reverse the order of items in the list
copy() | 	returns a shallow copy of the list


```python
   
# Example on Python list methods

my_list = [3, 8, 1, 6, 8, 8, 4]

# Add 'a' to the end
my_list.append('a')

# Output: [3, 8, 1, 6, 8, 8, 4, 'a']
print(my_list)

# Index of first occurrence of 8
print(my_list.index(8))   # Output: 1

# Count of 8 in the list
print(my_list.count(8))  # Output: 3 
    
```

##

78. Exercise 78 - Write a program that reads 5 numeric values and stores them in a list. At the end, show which was the highest and lowest value entered, and their respective positions in the list. - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex078.py)
79. Exercise 79 - Create a program where the user can enter several numeric values and register them in a list. If the number already exists in there, it will not be added. At the end, all unique values entered will be displayed, in ascending order. - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex079.py)
80. Exercise 80 - Create a program where the user can type five numeric values and register them in a list, already in the correct insertion position (without using sort()). At the end, show the sorted list on the screen. - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex080.py)
81. Exercise 81 - Create a program that will read several numbers and put them in a list. After that, show: A) How many numbers were entered; B) The list of values, sorted in descending order; C) Whether the value 5 was entered and is or is not in the list. - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex081.py)
82. Exercise 82 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex082.py)
83. Exercise 83 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex083.py)
84. Exercise 84 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex084.py)
85. Exercise 85 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex085.py)
86. Exercise 86 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex086.py)
87. Exercise 87 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex087.py)
88. Exercise 88 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex088.py)
89. Exercise 89 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex089.py)


---

### Lesson Wrap Up:

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

---
      
### Conclusion:

In this lesson we talked about Lists a built-in data type python has to store data, in the next lesson we'll talk about the other two, sets and dictionaries

---

## More content:

Useful links

- [Python List](https://www.programiz.com/python-programming/list)
- [Lists](https://www.w3schools.com/python/python_lists.asp)
- [Python List Methods](https://www.programiz.com/python-programming/methods/list)
