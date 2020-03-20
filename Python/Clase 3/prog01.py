import pygame
from libreria import *

def triangle(ventana, pos, size):
    P = [[pos[0],pos[1]+size], [pos[0],pos[1]-size], [pos[0]+size,pos[1]]]
    Plano(ventana,[ANCHO/2,ALTO/2])
    pygame.draw.polygon(ventana, VERDE, P, 1)
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    Plano(ventana,[ANCHO/2,ALTO/2])
    pygame.display.flip()

    fin = False

    while not fin:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    triangle(ventana,[event.pos[0],event.pos[1]],50)