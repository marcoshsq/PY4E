# Exercise 114 - 

'''ACME Inc., a company of 500 employees, is having disk space problems on its 
file server. To try to solve this problem, the Network Administrator needs to 
know the space occupied by the users, and identify the users with the most 
occupied space. Through a program, downloaded from the Internet, he managed 
to generate the following file, called "users.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

In this file, the username is 15 characters long. From this file, you must 
create a program that generates a report, called "report.txt", 
in the following format:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB


The input file must be read only once, and the data stored in memory, 
if necessary, in order to speed up the execution of the program. The conversion 
of the space occupied on disk, from bytes to megabytes, must be done through 
a separate function, which will be called by the main program. 
The percentage of use must also be calculated through a function, 
which will be called by the main program.

'''
