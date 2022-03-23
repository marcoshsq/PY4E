# Exercise 071 - ATM Simulator

'''Create a program that simulates the operation of an ATM.

At the beginning, ask the user what will be the amount to be withdrawn (integer)
and the program will inform how many bills of each value will be delivered.

OBS: consider that the ATM has notes of R$50, R$20, R$10 and R$1.'''

print(f'Welcome to Python Bank')
withdraw = int(input('What amount do you want to withdraw: \n'))
total = withdraw
bills = 50
total_bills = 0
while True:
    if total >= bills:
        total -= bills
        total_bills += 1
    else:
        if total_bills > 0:
            print(f'You withdraw {total_bills} bills of R${bills}')
        if bills == 50:
            bills = 20
        elif bills == 20:
            bills = 10
        elif bills == 10:
            bills = 1
            total_bills = 0
        if total == 0:
            break
