#Fazer programa que abra e reproduza o audio de um arquivo mp3. (DICA: MODULO)
#MONA COM TODO RESPEITO VC TA MALUCA, GUANABARA?

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('herdeirawaka.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

#fiz, mas não entendi 100%



