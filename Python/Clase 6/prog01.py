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
                if event.button == 3:
                    if len(P) == 0:
                        ventana = pygame.display.set_mode([ANCHO, ALTO])
                        Plano(ventana,MIDDLE)
                        pygame.display.flip()
                    P = capturePoints(P,event, ventana,1)
                    if len(P) == 2:
                        print(cartesianLine(ventana,P[0],P[1]))
                        P = []
                        

                    
                    
