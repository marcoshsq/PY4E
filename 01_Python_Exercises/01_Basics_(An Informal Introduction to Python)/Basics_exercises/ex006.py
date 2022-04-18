# Exercise 006: Double, Triple, Square Root
"""Create an algorithm that reads a number and displays its double, triple and square root."""


# First, we ask the user for an input
num = float(input("Enter a number: "))

# So we multiply by two and by three to get double and triple
double_num = num * 2
triple_num = num * 3

# We raise our variable to the power of 0.5, so we get its square root
sqrt_num = num**0.5

# Then we print everything
print(f"Given the value {num}, it's double is {double_num}")
print(f"It's triple is {triple_num} and the square root is {sqrt_num} ")


"""The square root is the inverse operation of the power, 
so calculating the square root of a number n 
is figuring out which number squared gives n."""
