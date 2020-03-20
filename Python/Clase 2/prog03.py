import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    Plano(ventana,[ANCHO/2,ALTO/2])
    pygame.display.flip()

    P = []
    
    fin = False

    while not fin:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    P.append([event.pos[0], event.pos[1]])
                if event.button == 3:
                    ventana.fill(0)
                    Plano(ventana,[ANCHO/2,ALTO/2])
                    pygame.draw.polygon(ventana, VERDE, P, 1)
                    pygame.display.flip()                    
                if event.button == 4:
                    for j in range(20):
                        for i in P:
                            i[1] = i[1]-2
                        ventana.fill(0)
                        Plano(ventana,[ANCHO/2,ALTO/2])
                        pygame.draw.polygon(ventana, VERDE, P, 1)
                        pygame.display.flip()
                if event.button == 5:
                    for j in range(20):
                        for i in P:
                            i[1] = i[1]+2
                        ventana.fill(0)
                        Plano(ventana,[ANCHO/2,ALTO/2])
                        pygame.draw.polygon(ventana, VERDE, P, 1)
                        pygame.display.flip()