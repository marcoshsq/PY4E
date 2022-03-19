# Exercise 010: Currency Converter 
'''Create a program that reads how much money a person has in their wallet,
then show how many dollars he can buy.'''

money_real = float(input('How much money do you have: '))
dolar = money_real / 5.10
print(f'With R${money_real} you can buy US${dolar:.2f} ') 
