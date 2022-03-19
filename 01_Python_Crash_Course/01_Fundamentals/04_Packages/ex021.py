import pygame
# Exercise 021: Playing a song
'''Help python sing.'''

pygame.init()
pygame.mixer.music.load("music_file.mp3")
pygame.mixer.music.play()
input()


