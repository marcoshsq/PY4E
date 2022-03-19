# Exercise 021: Playing a song
'''Help python sing.'''

import pygame
pygame.init()
pygame.mixer.music.load("music_file.mp3")
pygame.mixer.music.play()
input()


