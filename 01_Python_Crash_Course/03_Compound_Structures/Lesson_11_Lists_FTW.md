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



```python
   
   if any code is displayed
    
```

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

### 


```python
   
   if any code is displayed
    
```

##

### Accessing List Elements



```python
   
   if any code is displayed
    
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



##

78. Exercise 78 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex078.py)
79. Exercise 79 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex079.py)
80. Exercise 80 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex080.py)
81. Exercise 81 -  - [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/03_Compound_Structures/11_Lists/ex081.py)
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

A summary of everything, or some important concept.

---
      
### Conclusion:

Conclusio.

---

## More content:

Useful links

- [Python List](https://www.programiz.com/python-programming/list)
- [Lists](https://www.w3schools.com/python/python_lists.asp)
- [Python List Methods](https://www.programiz.com/python-programming/methods/list)
