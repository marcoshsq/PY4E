# Extra Exercise 010

"""Make a program that asks how much you earn per hour and the number of hours worked in the month.
Calculate and show the total of your salary in that month, knowing that 11% is deducted for Income Tax,
8% for the INSS and 5% for the union, make a program that gives us:

a) gross salary.
b) how much you paid to the INSS.
c) how much he paid to the union.
d) the net salary.
e) calculate the discounts and the net salary, according to the table below:

+ Gross Salary: R$
- Income Tax (11%): BRL
- INSS (8%): BRL
- Union (5%): BRL
= Net Salary: R$

Obs.: Gross Salary - Discounts = Net Salary."""


hour_pay = float(input("Earning per hour: "))
worked_hour = float(input("Hours of work: "))
gross_salary = hour_pay * worked_hour
ir = gross_salary * 0.11
inss = gross_salary * 0.08
sindicate = gross_salary * 0.05
net_salary = gross_salary - (ir + inss + sindicate)
print(f"O seu salário bruto é: R${gross_salary}")
print(
    f"Foram descontados R${ir} de IR(11%), R${inss} de INSS(8%) e R${sindicate} do sindicato"
)
print(f"O seu salário liquido é R${net_salary}")
