import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    Plano(ventana,MIDDLE)
    pygame.display.flip()

    fin = False
    P = []

    while not fin:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                                       
                    Vector(ventana,MIDDLE,[100,100])
                    Vector(ventana,MIDDLE,[100,-100])
                    SumVectors(ventana,[100,100],[100,-100])
                    
                    
