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
                    setMiddle(ventana,event.pos)
                    if len(P) > 0:
                        for i in P:
                            pygame.draw.circle(ventana, VERDE, TransformCtoS(i), 5)
                            pygame.display.flip()
                if event.button == 3:
                    P.append(TransformStoC([event.pos[0],event.pos[1]]))
                    print(P)
                    if len(P) > 0:
                        for i in P:
                            pygame.draw.circle(ventana, VERDE, TransformCtoS(i), 5)
                            pygame.display.flip()
                    
