<div align="center">
  
# Dictionaries

</div>

## Lesson 12 Content:
1. []()
2. []()

---

### Dictionaries


A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.

![image](https://user-images.githubusercontent.com/64812097/160974726-aeb91fcd-3d8e-4cef-92f2-2c3a03699642.png)

An example of a Dictionary Dict:

```python
   
# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
a = Dict
    
```

The keys can be strings:

```python
   
# Access to the value by the key

Dict["key1"]
    
```

Keys can also be any immutable object such as a tuple:

```python
   
# Access to the value by the key

Dict[(0, 1)]
    
```
   
Each key is separated from its value by a colon ":". Commas separate the items, and the whole dictionary is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this "{}".
    
```python
   
# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict
    
```

In summary, like a list, a dictionary holds a sequence of elements. Each element is represented by a key and its corresponding value. Dictionaries are created with two curly braces containing keys and values separated by a colon. For every key, there can only be one single value, however, multiple keys can hold the same value. Keys can only be strings, numbers, or tuples, but values can be any data type.

It is helpful to visualize the dictionary as a table, as in the following image. The first column represents the keys, the second column represents the values.

![image](https://user-images.githubusercontent.com/64812097/160975373-5059bf2f-f09f-4cc1-804e-fa8d2649277a.png)

### Keys:

You can retrieve the values based on the names:

```python
   
# Get value by keys

release_year_dict['Thriller'] 
    
```

This corresponds to:

![image](https://user-images.githubusercontent.com/64812097/160975456-c53b61c9-b908-4bfb-9a26-a41c14821cc8.png)

Similarly for The Bodyguard:

```python
   
# Get value by key

release_year_dict['The Bodyguard'] 
    
```

![image](https://user-images.githubusercontent.com/64812097/160975505-ee08e3c1-0573-4d45-aab1-9545916a30d8.png)

Now let us retrieve the keys of the dictionary using the method keys():

```python
   
# Get all the keys in dictionary

release_year_dict.keys() 
    
```

You can retrieve the values using the method values():

```python
# Get all the values in dictionary

release_year_dict.values()

```


We can add an entry:

```python

# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict

```

We can delete an entry:

```python

# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict

```

We can verify if an element is in the dictionary:

```python

# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict

```

##

90. Exercises 090 -  - [Solution]()
91. Exercises 090 -  - [Solution]()
92. Exercises 090 -  - [Solution]()
93. Exercises 090 -  - [Solution]()
94. Exercises 090 -  - [Solution]()
95. Exercises 090 -  - [Solution]()

---

### Lesson Wrap Up:

A summary of everything, or some important concept.

---
      
### Conclusion:

Conclusio.

---

## More content:

Useful links

- [Python Dictionary](https://www.programiz.com/python-programming/dictionary)
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lists, Tuples, and Sets](https://www.youtube.com/watch?v=W8KRzm-HUcc)
- [Python: Data Structures - Lists, Tuples, Sets & Dictionaries tutorial](https://www.youtube.com/watch?v=R-HLU9Fl5ug)
