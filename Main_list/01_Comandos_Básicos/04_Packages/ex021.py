# Exercício Python 021: Tocando um MP3
'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame
pygame.init()
pygame.mixer.music.load("arquivo_de_música.mp3")
pygame.mixer.music.play()
input()

'''Aparentemente, para fazer o programar tocar uma música é necessarios
fazer um input'''
