# Exercise 113 - Analyzing IPs

"""Write a program that reads a text file containing a list of IP addresses 
and generates another file containing a report of valid and invalid 
IP addresses. The input file has the following format:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256


The output file has the following format:

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256

"""

with open("test.txt", "r") as f:
    f_content = f.read()
    print(f_content)
