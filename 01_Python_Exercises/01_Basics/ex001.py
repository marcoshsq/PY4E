# Exercise 001: Let's get started.
"""Create your first program and help your computer greet the World."""


# Solution
from os import sep


print("Hello, World!")

# Other things we can do
print(
    "Hello", "World!", sep=","
)  # esse (sep="") separa as partes da string com o simbolo
print("Hello", "World", sep="**")
print("Hello", "World", sep="//")
print("Hello", end="*-*-*")  # o end coloca o seu conteúdo no final

"""Fun trivia
Brian Kernighan, authored one of the most widely read programming books, C Programming Language. 
He first referenced Hello World in his book titled A Tutorial Introduction to the Programming Language B. 
And while no one can scientifically explain why it became so wildly popular, 
the program marks a major change in the historical rhetoric of programming itself."""

"""It's the most famous program. Known as the first example in nearly every programming language for every programmer, 
where did this message come from? As a function, the computer program simply tells the computer to display the words “Hello, 
World!” Traditionally, it's the first program developers use to test systems."""
