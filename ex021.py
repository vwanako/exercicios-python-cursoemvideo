# make a program that opens and plays a mp3 file

import pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('.mp3')
pygame.mixer.music.play(loops=0, start=0)
pygame.event.wait()
