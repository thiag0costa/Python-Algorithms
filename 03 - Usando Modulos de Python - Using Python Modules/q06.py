# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
# Write a program in python that open and play a mp3 audio file.

import os; print(os.getcwd())
import pygame
pygame.mixer.init()
pygame.mixer.music.load('Desafio21audio.mp3')
pygame.mixer.music.play()
input()
