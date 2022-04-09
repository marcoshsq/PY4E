<div align="center">
  
# Python can be your calculator :nerd_face: :computer:	
  
</div>

## Lesson 03 Content:

1. [Python Operators](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#python-operators)
2. [Arithmetic operators](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#arithmetic-operators-examples-from-highest-to-lowest-precedence)
3. [Python Assignment Operators](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#python-assignment-operators-assignment-operators-are-used-to-assign-values-to-variables)
4. [Python Comparison Operators](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#python-comparison-operators-comparison-operators-are-used-to-compare-two-values)
5. [Python Logical Operators](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#python-logical-operators-logical-operators-are-used-to-combine-conditional-statements)
6. [Python Identity Operators](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#python-identity-operators-identity-operators-are-used-to-compare-the-objects-not-if-they-are-equal-but-if-they-are-actually-the-same-object-with-the-same-memory-location)
7. [Python Membership Operators](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#python-membership-operators-membership-operators-are-used-to-test-if-a-sequence-is-presented-in-an-object)
8. [Python Bitwise Operators](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#python-bitwise-operators-bitwise-operators-are-used-to-compare-binary-numbers)
9. [Lesson Wrap Up](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#lesson-wrap-up)
10. [Conclusion](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#conclusion)
11. [More content](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/Lesson_03_Python_can_be_your_calculator.md#more-content)

---

### Python Operators:

To do calculations in python we have two approaches, we use the built-in operators together with a little daring and joy, or we use specific packages.
Let's start with the first option.

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

##

### Arithmetic operators examples, from Highest to Lowest precedence:

| Operator | Operation | Example |
| :--: | :--: | :--: |
| ** | Exponent | 2 ** 3 = 8
| % |	Modulus/Remainder |	22 % 8 = 6
| // |	Integer division |	22 // 8 = 2
| / |	Division |	22 / 8 = 2.75
| * |	Multiplication |	3 * 3 = 9
| - |	Subtraction |	5 - 2 = 3
| + |	Addition |	2 + 2 = 4

##

### Python Assignment Operators, assignment operators are used to assign values to variables:

| Operator | Example | Same As |
| :--: | :--: | :--: |
| =	| x = 5 | x = 5 |
| += |	x += 3 |	x = x + 3 |	
| -= |	x -= 3 |	x = x - 3	|
| *= |	x*= 3	 | x = x * 3 | 
| /= |	x /= 3 |	x = x / 3 |
| %= |	x %= 3 |	x = x % 3	|
| /= |	x //= 3	 | x = x // 3 |	
| **= |	x **= 3 |	x = x ** 3	|
| &= |	x &= 3 |	x = x & 3	 |
| != |	x != 3 |	x = x ! 3	|
| ^= |	x ^= 3 |	x = x ^ 3	|
| >>= |	x >>= 3 |	x = x >> 3	|
| <<= |	x <<= 3 |	x = x << 3|

##

### Python Comparison Operators, comparison operators are used to compare two values:

| Operator |	Name |	Example |
| :--: | :--: | :--: |
|==	| Equal |	x == y |	
|!=|	Not equal |	x != y	|
|>|	Greater than |	x > y	|
|<|	Less than	| x < y	|
|>=|	Greater than or equal to|	x >= y	|
|<=|	Less than or equal to	| x <= y | 

##

### Python Logical Operators, logical operators are used to combine conditional statements:

| Operator |	Description |	Example	|
| :--: | :--: | :--: |
| and |	Returns True if both statements are true |	x < 5 and  x < 10	
| or |	Returns True if one of the statements is true	| x < 5 or x < 4	
| not |	Reverse the result, returns False if the result is true |	not (x < 5 and x < 10)

##

### Python Identity Operators, identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

| Operator |	Description |	Example |
| :--: | :--: | :--: |
| is | 	Returns True if both variables are the same object |	x is y	
| is not |	Returns True if both variables are not the same object |	x is not y

##

### Python Membership Operators, membership operators are used to test if a sequence is presented in an object:

| Operator |	Description |	Example |	
| :--: | :--: | :--: |
| in | 	Returns True if a sequence with the specified value is present in the object |	x in y	
| not in |	Returns True if a sequence with the specified value is not present in the object | x not in y	

##

### Python Bitwise Operators, bitwise operators are used to compare (binary) numbers:

| Operator |	Name |	Description |
| :--: | :--: | :--: |
| & |	AND	| Sets each bit to 1 if both bits are 1 |
| ^ |	XOR |	Sets each bit to 1 if only one of two bits is 1 |
| ~ |	NOT |	Inverts all the bits |
| << |	Zero fill left shift |	Shift left by pushing zeros in from the right and let the leftmost bits fall off |
| >> |	Signed right shift |	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

##

Okay, there are a lot of operators, I'll recommend you two things, first, go play around with it, remember, you can't break Python. second, let's do some exercises.

5. Exercise 005 - Write a program that reads an integer and displays its successor and predecessor on the screen. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex005.py)
6. Exercise 006 - Create an algorithm that reads a number and displays its double, triple and square root. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex006.py)
7. Exercise 007 - Develop a program that reads a student's grades, calculates and displays their average. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex007.py)
8. Exercise 008 - Create a program that reads a value in meters and display it converted to centimeters and millimeters. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex008.py)
9. Exercise 009 - Make a program that reads a number and display its multiplication table. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex009.py)
10. Exercise 010 - Create a program that reads how much money a person has in their wallet, then show how many dollars he can buy. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex010.py)
11. Exercise 011 - Write a program that reads the width and height of a wall in meters, calculate its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of 2 square meters. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex011.py)
12. Exercise 012 - Make an algorithm that reads the price of a product and displays its new price, with a 5% discount. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex012.py)
13. Exercise 013 - Make an algorithm that reads an employee's salary and displays their new salary, with a 15% increase. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex013.py)
14. Exercise 014 - Write a program that converts a temperature by typing in degrees Celsius and convert to degrees Fahrenheit. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex014.py)
15. Exercise 015 - Write a program that asks the number of kilometers traveled by a rental car and the number of days for which it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven. [Solution](https://github.com/marcoshsq/Python_Crash_Course/blob/main/01_Python_Crash_Course/01_Fundamentals/03_Calculation/ex015.py)

---

### Lesson Wrap Up:

Python has these operators:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

---

### Conclusion:

In this lesson we talk about operators in python, and we solve several arithmetic exercises, in the next lesson we will talk about packages.

---

## More content

- [Python Operators](https://www.w3schools.com/python/python_operators.asp)
