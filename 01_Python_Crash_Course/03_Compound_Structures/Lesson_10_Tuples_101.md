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
1. []()
2. []()

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

##

---

### Lesson Wrap Up:

A summary of everything, or some important concept.

---
      
### Conclusion:

Conclusio.

---

## More content:

Useful links

- []()
- []()

