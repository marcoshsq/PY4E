# Python Exercise 018 - Sine, Cosine and Tangent
''' Write a program that reads any angle and displays the sine value on the screen,
cosine and tangent of this angle.'''

import math

# Em graus radianos

an = float(input('Insira o valor do ângulo: '))
ang = math.radians(an)
sen_rad = math.sin(ang)
cos_rad = math.cos(ang)
tan_rad = math.tan(ang)

print(f'O seno é: {sen_rad:.2f} O cosseno é: {cos_rad:.2f} e a tangente é: {tan_rad:.2f}')

# Em graus centigrados

sen_deg = sen_rad * (180/math.pi)
cos_deg = cos_rad * (180/math.pi)
tan_deg = tan_rad * (180/math.pi)

print(f'O seno é: {sen_deg:.2f} O cosseno é: {cos_deg:.2f} e a tangente é: {tan_deg:.2f}')

# ou 

seno = math.degrees(sen_rad)
cosen = math.degrees(cos_rad)
tang = math.degrees(tan_rad)

print(f'O seno é: {seno:.2f} O cosseno é: {cosen:.2f} e a tangente é: {tang:.2f}')
