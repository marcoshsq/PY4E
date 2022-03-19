import math
# Exercise 018 - Sine, Cosine and Tangent
''' Write a program that reads any angle and displays the sine, cosine and tangent value on the screen of this angle.'''

# in degrees radians

an = float(input('Enter the angle: '))
ang = math.radians(an)
sen_rad = math.sin(ang)
cos_rad = math.cos(ang)
tan_rad = math.tan(ang)

print(f'The Sine is: {sen_rad:.2f}. The Cosine is: {cos_rad:.2f} and the Tangent is: {tan_rad:.2f}')

# in degrees centigrade

sen_deg = sen_rad * (180/math.pi)
cos_deg = cos_rad * (180/math.pi)
tan_deg = tan_rad * (180/math.pi)

print(f'The Sine is: {sen_deg:.2f}. The Cosine is: {cos_deg:.2f} and the Tangent is: {tan_deg:.2f}')

# or 

seno = math.degrees(sen_rad)
cosen = math.degrees(cos_rad)
tang = math.degrees(tan_rad)

print(f'The Sine is: {seno:.2f}. The Cosine is: {cosen:.2f} and the Tangent is: {tang:.2f}')
