# Exercise 072: Number by Extension

''' Create a program that has a fully populated 
Tuple with a count in words,from zero to twenty. 

Your program should read a number from the keyboard 
(between 0 and 20) and display it in full.
'''

number_extension = ('zaro', 'one', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                    'Eleven', 'Twelve', 'thirteen', 'Fourteen', 'Fifhteen', 'Sixteen', 'Seventeen', 'Eighteen',
                    'nineteen', 'Twenty')


for i in number_extension:
    count= int(input('Enter a number: '))
    
    for j in range((count + 1) - count):
        print(f'You entered the number {count}, that written in full is {number_extension[count]}')
    
    control = str(input('Wish to continue: [Yes or No]')).strip()
    if control in 'Nn':
        break
