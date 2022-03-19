strings
<div align="center">
  
# Strings ✂️✂️✂️

</div>

## Lesson 05 Content:

##

## Manipulating Strings

### Escape Characters:

| Escape character	| Prints as |
| :--: | :--: |
| \' |	Single quote |
| \" |	Double quote |
| \t |	Tab |
| \n |	Newline (line break) |
| \\ |	Backslash |

Example: 
```python
print("Hello there!\nHow are you?\nI\'m doing fine.")
>>> Hello there!
How are you?
I'm doing fine.
```

##

### Raw Strings:

A raw string completely ignores all escape characters and prints any backslash that appears in the string.

```python
>>> print(r'That is Carol\'s cat.')
That is Carol\'s cat.
```

### Multiline Strings with Triple Quotes:

```python
>>> print('''Dear Alice,
>>>
>>> Eve's cat has been arrested for catnapping, cat burglary, and extortion.
>>>
>>> Sincerely,
>>> Bob''')
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
```

To keep a nicer flow in your code, you can use the dedent function from the textwrap standard package.

```python

>>> from textwrap import dedent
>>>
>>> def my_function():
>>>     print('''
>>>         Dear Alice,
>>>
>>>         Eve's cat has been arrested for catnapping, cat burglary, and extortion.
>>>
>>>         Sincerely,
>>>         Bob
>>>         ''').strip()
```

This generates the same string than before.


### Indexing and Slicing Strings:

| H | e | l | l | o |  | w | o | r | l | d | ! |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

```python
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> spam[4]
'o'
>>> spam[-1]
'!'
```

### Slicing [start:stop:step]:

```python
>>> spam[0:5]
'Hello'
>>> spam[:5]
'Hello'
>>> spam[6:]
'world!'
>>> spam[6:-1]
'world'
>>> spam[:-1]
'Hello world'
>>> spam[::-1]
'!dlrow olleH'
>>> spam = 'Hello world!'
>>> fizz = spam[0:5]
>>> fizz
'Hello'
```

### The in and not in Operators with Strings:

```python
>>> 'Hello' in 'Hello World'
True
>>> 'Hello' in 'Hello'
True
>>> 'HELLO' in 'Hello World'
False
>>> '' in 'spam'
True
>>> 'cats' not in 'cats and dogs'
False
```

### The in and not in Operators with list:

```python
>>> a = [1, 2, 3, 4]
>>> 5 in a
False
>>> 2 in a
True
```

### The upper(), lower(), isupper(), and islower() String Methods:

upper() and lower():

```python
>>> spam = 'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> spam = spam.lower()
>>> spam
'hello world!'
```

isupper() and islower():

```python
>>> spam = 'Hello world!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>> 'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
```

The isX String Methods

- isalpha() returns True if the string consists only of letters and is not blank.
- isalnum() returns True if the string consists only of letters and numbers and is not blank.
- isdecimal() returns True if the string consists only of numeric characters and is not blank.
- isspace() returns True if the string consists only of spaces,tabs, and new-lines and is not blank.
- istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

### The startswith() and endswith() String Methods:

```python
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!')
True
>>> 'Hello world!'.endswith('Hello world!')
True
```

### The join() and split() String Methods:

join():

```python
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```

split():

```python
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

### Justifying Text with rjust(), ljust(), and center():

rjust() and ljust():

```python
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20)
'               Hello'
>>> 'Hello World'.rjust(20)
'         Hello World'
>>> 'Hello'.ljust(10)
'Hello     '
```

An optional second argument to rjust() and ljust() will specify a fill character other than a space character. Enter the following into the interactive shell:

```python
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
```

center():

```python
>>> 'Hello'.center(20)
'       Hello       '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

### Removing Whitespace with strip(), rstrip(), and lstrip():

```python
>>> spam = '    Hello World     '
>>> spam.strip()
'Hello World'
>>> spam.lstrip()
'Hello World '
>>> spam.rstrip()
'    Hello World'
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'
```

### Copying and Pasting Strings with the pyperclip Module (need pip install):

```python
>>> import pyperclip

>>> pyperclip.copy('Hello world!')

>>> pyperclip.paste()
'Hello world!'
```

### String Formatting:

% operator

```python
>>> name = 'Pete'
>>> 'Hello %s' % name
"Hello Pete"
```

We can use the %x format specifier to convert an int value to a string:

```python
>>> num = 5
>>> 'I have %x apples' % num
"I have 5 apples"
```

Note: For new code, using str.format or f-strings (Python 3.6+) is strongly recommended over the % operator.

### String Formatting (str.format):

Python 3 introduced a new way to do string formatting that was later back-ported to Python 2.7. This makes the syntax for string formatting more regular.

```python
>>> name = 'John'
>>> age = 20'

>>> "Hello I'm {}, my age is {}".format(name, age)
"Hello I'm John, my age is 20"
>>> "Hello I'm {0}, my age is {1}".format(name, age)
"Hello I'm John, my age is 20"
```

The official Python 3.x documentation recommend str.format over the % operator:

The formatting operations described here exhibit a variety of quirks that lead to a number of common errors (such as failing to display tuples and dictionaries correctly). Using the newer formatted string literals or the str.format() interface helps avoid these errors. These alternatives also provide more powerful, flexible and extensible approaches to formatting text.

### Lazy string formatting:

You would only use %s string formatting on functions that can do lazy parameters evaluation, the most common being logging:

Prefer:

```python
>>> name = "alice"
>>> logging.debug("User name: %s", name)
```

Over:

```python
>>> logging.debug("User name: {}".format(name))
```

Or:

```python
>>> logging.debug("User name: " + name)
```

### Formatted String Literals or f-strings (Python 3.6+):

```python

>>> name = 'Elizabeth'
>>> f'Hello {name}!'
'Hello Elizabeth!
```

It is even possible to do inline arithmetic with it:

```python
>>> a = 5
>>> b = 10
>>> f'Five plus ten is {a + b} and not {2 * (a + b)}.'
'Five plus ten is 15 and not 30.'
```

### Template Strings:

A simpler and less powerful mechanism, but it is recommended when handling format strings generated by users. Due to their reduced complexity template strings are a safer choice.

```python
>>> from string import Template
>>> name = 'Elizabeth'
>>> t = Template('Hey $name!')
>>> t.substitute(name=name)
'Hey Elizabeth!'
```
##




---

### Lesson Wrap Up:

---

### Conclusion:

---

## More content

- [Strings](https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-strings/cheatsheet)
- [Python Strings Cheat Sheet](https://www.shortcutfoo.com/app/dojos/python-strings/cheatsheet)
