import pygame
from libreria import *

def triangle(ventana, pos, size, P):
    tP = [[pos[0],pos[1]+size], [pos[0],pos[1]-size], [pos[0]+size,pos[1]]]
    pygame.draw.polygon(ventana, VERDE, tP, 1)
    pygame.display.flip()

def connect(ventana, pos):
    for i,j in zip(pos, pos[1:]):
        for k in range(3):
            pygame.draw.line(ventana, VERDE, i[k], j[k], 1)



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
                    triangle(ventana,[event.pos[0],event.pos[1]],50,P)
                    P.append([[event.pos[0],event.pos[1]+50], [event.pos[0],event.pos[1]-50], [event.pos[0]+50,event.pos[1]]])
                    if(len(P) > 0):
                        connect(ventana, P)