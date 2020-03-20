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
    polygonSize = 3

    while not fin:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    P = capturePoints(P,event, ventana,1)
                    if len(P) == polygonSize:
                        cartesianPolygon(ventana,P)
                        Q = P
                if event.button == 4:
                    if len(P) == polygonSize:
                        ESCALA = 2
                        Q = Escale(Q)
                        Reset(ventana)
                        cartesianPolygon(ventana,Q)      
                if event.button == 5:
                    if len(P) == polygonSize:
                        ESCALA = 0.5
                        Q = Escale(Q)
                        Reset(ventana)
                        cartesianPolygon(ventana,Q)                     
                if event.button == 1:
                        P = []
                        Q = []
                        Reset(ventana)

                        

                    
                    
