import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])

    pygame.draw.line(ventana, [255, 255, 255], [ANCHO/2, ALTO], [ANCHO/2, 0], 1)
    pygame.draw.line(ventana, [255, 255, 255], [ANCHO, ALTO/2], [0, ALTO/2], 1)
    pygame.display.flip()

    fin = False

    while not fin:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ventana.fill(0)
                pygame.draw.line(ventana, [255, 255, 255], [event.pos[0], ALTO], [event.pos[0], 0], 1)
                pygame.draw.line(ventana, [255, 255, 255], [ANCHO, event.pos[1]], [0, event.pos[1]], 1)
                pygame.display.flip()
