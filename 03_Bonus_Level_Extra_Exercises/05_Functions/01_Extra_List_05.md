# Extra list 05 - Functions

### A list of extra exercises for those who are eager to learn. (づ｡◕‿‿◕｡)づ

The exercises vary in difficulty, some being trivial, others quite challenging.

---

- Exercise 001 - Make a program to print:

       1
       2 2
       3 3 3
       .....
       n n n n n n ... n
                 
to an n informed by the user. Use a function that takes an integer n value and prints up to the nth line.

- Exercise 002 - Make a program to print:

       1
       1 2
       1 2 3
       .....
       1 2 3 ... n

to an n informed by the user. Use a function that takes an integer n value and prints up to the nth line.

- Exercise 003 - Write a program, with a function that takes three arguments, and that provides the sum of these three arguments.

- Exercise 004 - Write a program, with a function that needs an argument. The function returns the character value 'P' if its argument is positive, and 'N' if its argument is zero or negative.

- Exercise 005 - Write a program with a function called SumTax. The function has two formal parameters: TaxTax, which is the amount of sales tax expressed as a percentage, and cost, which is the cost of an item before tax. The function “changes” the cost amount to include sales tax.

- Exercise 006 - Write a program that converts from 24-hour notation to 12-hour notation. For example, the program must convert 14:25 to 2:25 P.M. The input is given in two integers. There must be at least two functions: one to do the conversion and one for the output. Record the A.M./P.M. as an 'A' value for A.M. and 'P' for P.M. Thus, the function to perform the conversions will have a formal parameter to register if it is A.M. or PM Include a loop that allows the user to repeat this calculation for new input values as often as desired.

- Exercise 007 - Write a program that uses the PaymentAmount function to determine the amount to be paid for an installment of an account. The program must ask the user for the amount of the installment and the number of days in delay and pass these values to the valuePayment function, which will calculate the amount to be paid and return this amount to the program that called it. The program should then display the amount to be paid on the screen. After execution, the program must ask for another installment amount again and continue like this until a value equal to zero is informed for the installment. At this point, the program must be closed, displaying the report for the day, which will contain the amount and total value of installments paid on the day. The amount to be paid is calculated as follows. For payments without delay, charge the value of the installment. When there is a delay, charge a 3% fine, plus 0.1% interest per day of delay.

- Exercise 008 - Write a function that informs the number of digits of a given integer number.

- Exercise 009 - Reverse of the number. Write a function that returns the reverse of a given integer. For example: 127 -> 721.

- Exercise 010 - Craps game. Make a program to implement a game of Craps. The player rolls a pair of dice, getting a value between 2 and 12. If, on the first roll, you roll 7 or 11, you are a "natural" and you have won. If you roll a 2, 3 or 12 on the first roll, this is called "craps" and you've lost. If, on the first roll, you rolled a 4, 5, 6, 8, 9 or 10, this is your "Point". Your objective now is to keep rolling the dice until you get that number again. You lose, however, if you roll a 7 before rolling that Point again.

- Exercise 011 - Date with month in full. Construct a function that takes a date in the format DD/MM/YYYY and returns a string in the format D of sameExtension of YYYY. Optionally validate the date and return NULL if the date is invalid.

- Exercise 012 - Shuffles word. Build a function that takes a string as a parameter and returns another string with the characters scrambled. For example: if function receives the word python, it can return npthyo, ophtyn or any other possible combination, randomly. Standardize in your function that all characters will be returned in uppercase or lowercase, regardless of how they were typed.

- Exercise 013 - Draw frame. Construct a function that draws a rectangle using the characters '+' , '−' and '| '. This function must receive two parameters, rows and columns, and the default value is the minimum value equal to 1 and the maximum value is 20. If values outside the range are informed, they must be modified to values within the range so elegant.

- Exercise 014 -  Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

      8  3  4 
      1  5  9
      6  7  2
      
Write a function that identifies and displays all magic squares with the above characteristics on the screen. Tip: produce all possible combinations and check the sum when you complete each square. Using a vector from 1 to 9 seems to be simpler than using a 3x3 matrix.
