import pygame
from libreria import *

def pattern(ventana, pos):
    Pdiv = [[pos[0],pos[1]],[pos[0]+15,pos[1]],[pos[0]+15,pos[1]+15],[pos[0],pos[1]+15], [pos[0],pos[1]+5], [pos[0]+10,pos[1]+5], [pos[0]+10,pos[1]+10], [pos[0]+5,pos[1]+10]]
    for i, j in zip(Pdiv, Pdiv[1:]):
        pygame.draw.line(ventana, VERDE, i, j, 1)
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    Plano(ventana,[ANCHO/2,ALTO/2])
    pygame.display.flip()

    fin = False

    while not fin:
        for i in range(30):
            pattern(ventana,[i*20,580])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pattern(ventana,[event.pos[0],event.pos[1]])
            