# Extra list 04 - Lists

### A list of extra exercises for those who are eager to learn. (づ｡◕‿‿◕｡)づ

The exercises vary in difficulty, some being trivial, others quite challenging.

---

- Exercise 001 - Write a program that simulates a roll of the dice. Roll the die 100 times and store the results in a vector. Then show how many times each value was achieved. Tip: use a vector of counters(1-6) and a function to generate random numbers, simulating the rolls of the dice
 
- Exercise 002 - ACME Inc., a company of 500 employees, is having disk space problems on its file server. To try to solve this problem, the Network Administrator needs to know the space occupied by the users, and identify the users with the most occupied space. Through a program, downloaded from the Internet, he managed to generate the following file, called "users.txt":

|alexandre | 456123789
:--: | :--:
|anderson | 1245698456
|antonio | 123456456
|carlos | 91257581
|cesar | 987458
|rosemary | 789456125

In this file, the username is 15 characters long. From this file, you must create a program that generates a report, called "report.txt", in the following format:

|ACME Inc. | Usage of disk space by users|||
:--: |:--: | :--: | :--: 
Nr. | Usuário | Used space | % of usage
1 | alexandre | 434,99 MB | 16,85%
2 | anderson | 1187,99 MB | 46,02%
3 | antonio | 117,73 MB | 4,56%
4 | carlos | 87,03 MB | 3,37%
5 | cesar | 0,94 MB | 0,04%
6 | rosemary | 752,88 MB | 29,16%

Total occupied space: 2581.57 MB
Average space occupied: 430.26 MB

The input file must be read only once, and the data stored in memory, if necessary, in order to speed up the execution of the program. The conversion of the space occupied on disk, from bytes to megabytes, must be done through a separate function, which will be called by the main program. The percentage of use must also be calculated through a function, which will be called by the main program.

- Exercise 003 - Write a program that reads an array of 5 integers and displays them.

- Exercise 004 - Write a program that reads an array of 10 real numbers and displays them in reverse order.

- Exercise 005 - Make a Program that reads 4 grades, shows the grades and the average on the screen.

- Exercise 006 - Write a program that reads a 10-character vector, and tells you how many consonants were read. Print the consonants.

- Exercise 007 - Write a program that reads 20 integers and stores them in an array. Store the even numbers in the EVEN vector and the ODD numbers in the odd vector. Print the three vectors.
 
- Exercise 008 - Make a program that asks for the four grades of 10 students, calculate and store the average of each student in a vector, print the number of students with an average greater than or equal to 7.0.

- Exercise 009 - Write a program that reads a vector of 5 integers, displays the sum, multiplication and numbers.
 
- Exercise 010 - The ages and heights of 30 students were recorded. Make a program that determines how many students over 13 are taller than the average height of these students.
 
- Exercise 011 - Make a program that takes the average temperature for each month of the year and stores them in a list. After that, calculate the annual average of temperatures and show all temperatures above the annual average, and in which month they occurred (show the month in full: 1 – January, 2 – February, . . . ).
 
- Exercise 012 - Write a program that reads an indefinite number of values, corresponding to grades, ending the data entry when a value equal to -1 is informed (which should not be stored). After this data entry, do: Show the amount of values that were read; Display all values in the order they were entered, one next to the other; Display all values in reverse order, one below the other; Calculate and display the sum of the values; Calculate and display the average of the values; Calculate and display the amount of values above the calculated average; Calculate and display the number of values below seven; End the program with a message;
 
- Exercise 013 - Use a list to solve the following problem. A company pays its salespeople on a commission basis. The seller receives $200 per week plus 9 percent of his gross sales for that week. For example, a salesperson who had gross sales of $3000 in one week receives $200 plus 9 percent of $3000, for a total of $470. Write a program (using an array of counters) that determines how many salespeople received salaries in the following ranges of values:

|$200  |$299|
:--:|:--:
|$300  |$399|
|$400  |$499|
|$500  |$599|
|$600  |$699|
|$700  |$799|
|$800  |$899|
|$900  |$999|
|$1000 |onwards|

Challenge: Create a formula to get to the list position from salary, without doing lots of nested ifs.
 
- Exercise 014 - Using lists, write a program that asks a person 5 questions about a crime. The questions are: "Did you call the victim?", "Were you at the crime scene?", "Do you live near the victim?", "Did it to the victim?", "Have you ever worked with the victim?". The program must at the end issue a rating on the person's participation in crime. If the person answers positively to 2 questions, they should be classified as "Suspect", between 3 and 4 as "Accomplice" and 5 as "Murderer". Otherwise, he will be classified as "Innocent". 
 
- Exercise 015 - In a long jump competition each athlete is entitled to five jumps. The athlete's result will be determined by the average of the remaining five values. You must make a program that receives the name and the five distances reached by the athlete in his jumps and then informs the name, the jumps and the average of the jumps. The program must be closed when the athlete's name is not informed. The program output should look like the example below:

       Athlete: Rodrigo Curvello

       First Jump: 6.5m;
       Second Jump: 6.1 m;
       Third Jump: 6.2 m;
       Fourth Jump: 5.4 m;
       Fifth Jump: 5.3 m;

       Final result:
       Athlete: Rodrigo Curvello
       Jumps: 6.5 - 6.1 - 6.2 - 5.4 - 5.3;
       Average jumps: 5.9 m
 
- Exercise 016 - A major television station wants to make a poll among its viewers to find out who is the best player after each game. For this, it is necessary to develop a program, which will be used by the operators, to compute the votes. Your team was hired to develop this program, using the C++ programming language. To compute each vote, the operator will enter a number, between 1 and 23, corresponding to the player's shirt number. A player number equal to zero, indicates that voting has ended. If an invalid number is entered, the program should ignore it, display a brief warning message, and re-ask for another number. After voting is over, the program should display:

      The total votes cast;
      The numbers and respective votes of all players who received votes;
      The percentage of votes of each of these players;
      The number of the player chosen as the best player in the match, along with the number of votes and percentage of votes given to him.

Note that invalid votes and the trailing zero should not count as votes. The result appears ordered by player number. The program must make use of arrays. The program should perform the calculation of the percentage of each player through a function. This function will receive two parameters: the number of votes of a player and the total votes. The function will calculate the percentage and return the calculated value. Below is an example screen. The arrangement of information should be as close to the example as possible. The data is fictitious and may change with each execution of the program. At the end, the program must also record the data referring to the voting result in a text file on the disk, following the same arrangement shown on the screen.

     Poll: Who was the best player?

     Player number (0=end): 9
     Player number (0=end): 10
     Player number (0=end): 9
     Player number (0=end): 10
     Player number (0=end): 11
     Player number (0=end): 10
     Player number (0=end): 50
     Enter a value between 1 and 23 or 0 to exit!
     Player number (0=end): 9
     Player number (0=end): 9
     Player number (0=end): 0

     Voting result:

     8 votes were counted.

     Player Votes %
     9 4 50.0%
     10 3 37.5%
     11 1 12.5%
     The best player was number 9, with 4 votes, corresponding to 50% of the total votes.
 
- Exercise 017 - A research company needs to tabulate the results of the following survey taken from a large number of organizations:

"What is the best Operating System for use on servers?"

Possible answers are:

    1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Other

You were hired to develop a program that reads the results of the poll and reports the result of the poll at the end. The program should read the values ​​until the value 0 is informed, which ends the data entry. Values ​​other than those valid for the program (0 to 6) should not be accepted. The values ​​referring to each of the options must be stored in an array. After the data have been completely informed, the program must calculate the percentage of each of the competitors and inform the winner of the poll. The output format was given by the company, and is as follows:
Operating System Votes %

     ------------------- ----- ---
     Windows Server 1500 17%
     Unix 3500 40%
     Linux 3000 34%
     Netware 500 5%
     Mac OS 150 2%
     Other 150 2%
     ------------------- -----
     Total 8800

The most voted Operating System was Unix, with 3500 votes, corresponding to 40% of the votes.
 
- Exercise 018 - The Tabajara Organizations decided to give a bonus to their employees in recognition of the good results achieved during the past year. For this, it hired you to develop the application that will serve as a projection of how much will be spent with the payment of this allowance.

After meetings involving the executive board, the financial board and representatives of the labor union, the following form of calculation was arrived at:
a.Each employee will receive the equivalent of 20% of their gross December salary; a.The floor allowance will be 100 reais, that is, those employees whose salary is very low receive this minimum amount; At this time, there should be no concern with employees with shorter tenure, discounts, taxes or other particularities. Your program should allow you to enter the salary of an indefinite (unknown) number of salaries. A salary value of 0 (zero) ends typing. After entering all the data, the program must calculate the amount of the allowance granted to each employee, according to the rule defined above. At the end, the program must present:

    The salary of each employee, together with the amount of the allowance;
    The total number of employees processed;
    The total amount to be spent on the payment of the allowance;
    The number of employees who will receive the minimum amount of 100 reais;
    The highest amount paid as an allowance; The screen below is an example of running the program, for illustrative purposes only. The values ​​can change with each execution of the program.

    Projection of Expenses with Allowance
    ==================================

    Salary: 1000
    Salary: 300
    Salary: 500
    Salary: 100
    Salary: 4500
    Salary: 0

    Salary - Allowance
    BRL 1000.00 - BRL 200.00
    BRL 300.00 - BRL 100.00
    BRL 500.00 - BRL 100.00
    BRL 100.00 - BRL 100.00
    BRL 4500.00 - BRL 900.00

    5 employees were processed
    Total spent on allowances: BRL 1400.00
    Minimum amount paid to 3 employees
    Highest amount of allowance paid: BRL 900.00

    
