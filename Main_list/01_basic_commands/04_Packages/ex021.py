# Python Exercise 021: Playing an MP3
'''Make a Python program that opens and plays the audio from an MP3 file.'''

import pygame
pygame.init()
pygame.mixer.music.load("arquivo_de_música.mp3")
pygame.mixer.music.play()
input()

'''Aparentemente, para fazer o programar tocar uma música é necessarios
fazer um input'''
