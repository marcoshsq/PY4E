# Python Exercise 026 - First and Last Occurrence of a String
'''Make a program that reads a sentence on the keyboard and shows how many times the letter "A" appears,
what position it first appears in and what position it appears last time.'''

name = input('Insert name: ').casefold().strip()
num_a = name.count('a') 
first_a = name.find('a')
last_a = name.rfind('a')

print(f'A letra A aparece {num_a} vezes na frase')
print(f'A primeira letra A aparece na posição {first_a + 1}')
print(f'A ultima letra A apareceu na posição {last_a + 1}')
