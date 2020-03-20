import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    Plano(ventana,MIDDLE)
    pygame.display.flip()

    fin = False
    P = []
    Q = []
    polygonSize = 1

    while not fin:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    P = capturePoints(P,event, ventana,1)
                    if len(P) == polygonSize:
                        Vector(ventana,MIDDLE,P[0])
                        Q = P
                if event.button == 4:
                    if len(P) == polygonSize:
                        Q = RotateCenter(Q,0.1)
                        #Reset(ventana)
                        Vector(ventana,MIDDLE,P[0])
                if event.button == 5:
                    if len(P) == polygonSize:
                        Q = RotateCenter(Q,-0.1)
                        #Reset(ventana)
                        Vector(ventana,MIDDLE,P[0])
                if event.button == 1:
                        P = []
                        Q = []
                        Reset(ventana)