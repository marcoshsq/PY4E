<div align="center">
  
# Leveling up with upgrades 🍄🍄🍄

</div>

## Lesson 04 Content:

1. [Talking about cars](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_04_Leveling_up_with_upgrades.md#talking-about-cars)
2. [Packages, packages and more packages](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_04_Leveling_up_with_upgrades.md#packages-packages-and-more-packages)
3. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_04_Leveling_up_with_upgrades.md#lesson-wrap-up)
4. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_04_Leveling_up_with_upgrades.md#conclusion)
5. [More Content](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_04_Leveling_up_with_upgrades.md#more-content)

##

### Talking about cars:
Imagine the following, you are going to buy a car, and you decide to buy a basic car. After a while you decide to install things in your car, air conditioning, electric windows, a better sound system and so on.
The base car is the python you are using now, which you have installed or are in the jupyter notebook. It serves many things, in fact this basic python works to build everything. But for everything you want to do, you'll have to make it from scratch. For example: 

- A program to select a random number between say 1 and 1,000:

```python
def randint(a, b):
    "Return random integer in range [a, b], including both end points."
    return a + randbelow(b - a + 1)

def randbelow(n):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r

def random_bytes(n):
    "Return n random bytes"
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)

print(randint(1, 1000))
```


- or:

```python
import random   

a = random.randint(1, 1000)
print(a)
 ```

What happend here. Basically in the first code you wanted a random number between 0 and 1000, and for that you had to write all this code, in the second you imported the random package and it did all the work much more efficiently. u.u

That's the packages, or modules (there's a technical difference between them, but we'll deal with that later). Basically it's people who had the same problem as you, solved this problem and thought: Does anyone else have this problem?🤔🤔🤔, I think so, so I'll make my code available. And then you jubilee, you can download this ready code and use it in your program. Topster isn't?


##

### Packages, packages and more packages:
The first package, and one of the most important is [pip](https://pypi.org/project/pip/). Because pip is the package who install other packages. If you use the command pip list in your terminal, you can see all the packages one have installed on your python. 

There are thousands of packages in python, each one solves a different problem, why don't you [play around a bit](https://pypi.org/).

For this class, you will need the Math module and Random. The math module you probably have installed, but you need to import to your code, for that use the command import:

```python
    import math 

    sen = math.sin(1)
    cos = math.cos(1)
    tan = math.tan(1)

    print(sen, cos, tan)
    # Output: 0.8414709848078965 0.5403023058681398 1.5574077246549023
 ```   
    
You can also import only what you want from a module using the ''from'' command:

```python
from math import sin, cos, tan 

    sin = sin(1)
    cos = cos(1)
    tan = tan(1)

    print(sin, cos, tan)
    # Output: 0.8414709848078965 0.5403023058681398 1.5574077246549023
```
    
You can also give the module a nickname, to make it easier later, but be aware that there are naming conventions, to make things more organized:

 ```python  
from math import sin as bolaGato 
from math import cos as queijoBranco
from math import tan as sebastiao

sin = bolaGato(1)
cos = queijoBranco(1)
tan = sebastiao(1)
print(sin, cos, tan)
```
    
        
Math Module is a package of mathematical functions, that is, instead of doing the calculations in your head, you use the module. The ramdom helps make things random :), but I'll let you play around.

16. Exercise 016 - []()
17. Exercise 017 - []()
18. Exercise 018 - []()
19. Exercise 019 - []()
20. Exercise 020 - []()
21. Exercise 021 - []()


---

### Lesson Wrap Up:

Packages are pieces of code that you install in your python for you to solve specific problems without having to create the code from scratch.

---

### Conclusion:

In this lesson we talked about packages in python, and we solved some exercises using the math and random packages, in the next lesson we'll talk about strings.

---

## More Content:

- [Python Packages](https://pypi.org/)
- [Math Docs](https://docs.python.org/3/library/math.html)
- [random Docs](https://docs.python.org/3/library/random.html)
- [Modules](https://docs.python.org/3/tutorial/modules.html)
