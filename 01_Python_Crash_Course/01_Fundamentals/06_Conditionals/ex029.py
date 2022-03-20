# Exercise 029 - Electronic Radar
'''Write a program that reads the speed of a car. If he has 80 km,
show a message saying he has been fined.
The fine will cost R$7.00 for each km over the limit.'''


velocity = float(input('what is the speed of the car: '))
if velocity > 80 :
    print('FINED! You have exceeded the 80km/h limit ')
    traffic_ticket = (velocity - 80) * 7
    print(f'You must pay a fine of R${traffic_ticket}')
else :
    print('You have not exceeded the speed limit.')
print('Have a nice day')
