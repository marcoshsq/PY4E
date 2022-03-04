# Python Exercise 010: Currency Converter
'''Create a program that reads how much money in reais a person has in their wallet and shows how many dollars they can buy.'''

money_real = float(input('Qual quantia você possui: '))
dolar = money_real / 5.10
print(f'Com R${money_real} você pode comprar US${dolar:.2f} ') 
