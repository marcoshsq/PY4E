<div align="center">
  
# Welcome to Python 🐍🐍🐍! (ﾉ◕ヮ◕)ﾉ ヽ(o＾▽＾o)ノ (◕‿◕✿)

</div>

### Before we start you need to have a place to write your code. right?

If you are interested in installing Python on your computer, along with an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) (if you don't know what an IDE is, is an acronym  for integrated development environment, think of it like a software that will help you write Python), you must first go to the official [Python website](https://www.python.org/downloads/) and install it. Now for IDE's, I like to use [Pycharm](https://www.jetbrains.com/pycharm/) but you can use [VScode](https://code.visualstudio.com/download), or [Atom](https://atom.io/).

But I don't wanna make you install anything, at least for now, so I'll recommend you use [Jupyter notebook](https://jupyter.org/) which is a web-based interactive computing platform, or if you have a Google account, you can use the [Google Colab](https://colab.research.google.com/), tha is basically, Google's jupyter notebook, but you can save it on Google Drive. If you need a tutorial to get started with Google Colab use this [video](https://www.youtube.com/watch?v=RLYoEyIHL6A).

## Lesson 01 Content:

---

### The Golden Rule:

Once you have your Jupyter notebook open, you must be wanting to do something right? Why don't you write something. The problem is, computers are dumb, they don't understand what you want them to do unless you "give the orders" in a very specific way. And that's the golden rule of programming, and it's the rule you're going to have the most trouble with. The rule is simple, once you've found a problem that you want/need to solve using code, you need to do two things:
1. Solving the problem in a structured way that the computer can follow, we call it an algorithm. (hardest part);
2. Write your algorithm in a way that the computer understands. That's the syntax. (Not that hard after some practice).

But don't worry, this is the kind of thing that take a while to get it, so don't rush it. But with that said, let's try to write our first program, shall we?

### The Print Function

When you started playing around with Python, one thing you might notice is that you can enter numbers but not text, this is because text has special delimiters, so not to cause confusion in Python, we put this type of data, in quotes, it can be double or single quotes (' ', " "), usually single quotes are used. So when you want to write a text message (and don't worry we'll talk about data types in a moment) you have to use quotes. But not just writing, you want to see what happens right? To see what you are doing in python you need to use a function, in python all commands are functions, we have [built-in functions](https://docs.python.org/3/library/functions.html), we have the functions that come with packages and eventually you will learn to create your own. But for now let's use one of the most important built-in function, the print function.

To use a function you must call the function by its name, and end it with parentheses, where in the case of print, what you want to print goes inside the parentheses, and if it's text, inside quotes too:

        #Let's print some stuff:
        #Basic operations: 
        
        print(1 + 1) # Notice that the numbers are outside the quotes, with numbers, we don't need quotes, just for text.
        #output: 2
        
        print(5 * 5) 
        #output: 25
        
        #printing text
        
        print('Hi Marcos')
        #output: Hi Marcos
        
        print('Splinter Cell is better than Metal Gear')
        #output: ERROR Traceback (This is a joke u.u)

    
Cool, now that we've talked about the print function, why don't you try it? Start printing. Not only that, here's your first exercise:
1. Exercise 001 - Create your first program and help your computer greet the World. [If you want the solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/01_Intro/ex001.py)

---

### Getting Data from the user:

In the same way as the print function, we have the input function, which allows us to obtain data from the user. But it's important to note that just using the input function is not going to be very useful if we can't use the user input. So we need to assign this input to a variable. The assignment symbol in Python is the equal sign '='. And work from the right to the left.

        # if i write, for example:
        a = 1 # That means 'a' receives '1'
        b = 2 # This means 'b' receives '2'
         
        # The variable is like a container, it stores one and allows you to use that data later.
        # if I do this now
        
        c = a + b
        print(c)
        # Output: 3

So, you can use variables to store your different types of data, including user data. To use the input function the syntax is:

      # And we are already assigning the user data to a variable
      number = input('Insert a number: ')
      # user insert  5
      print(number)
      # Output: 5 
      
Great now that you learned how to use the print and input function, you're ready for the second challenge:
2. Exercise 002 - Ask the user for his name and give him a welcome message. [If you want the solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/01_Intro/ex002.py)

---
      
### Conclusion:

In this class we talked a little bit about the print function and the input function and I talked about my golden rule. Some tips is, go play with python, it doesn't break. And do research, because is very important, when you go to solve an exercise and feel that you don't understand something, or that you don't know how to do it, research, it can seem frustrating but that's what will teach you and give you repertoire. For example, I asked you to use the input function to ask for someone's name, and then use print to say hi to the person, but i didn't teach string concatenation in this class, i did it for you to research u.u, trust me, that's a good part of this job.

---

Wow, and we get to the end of our first lesson, if anyone is reading this, thank you very much, this is the first teaching material I write, so any criticism or suggestion would love to hear, and we'll see you in the next class, where we will talk about types of variables and type casting. See you space cowboy.
