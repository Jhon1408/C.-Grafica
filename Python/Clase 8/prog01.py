import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    P = [] # type: List[Any]
    Q = [] # type: List[Any]
    R = [] # type: List[Any]
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if len(P) == 0:
                        Circle = createObject('Circle', ventana, 10, event.pos[0], event.pos[1], VERDE)
                        P.append(Circle)
                    else:
                        del P[0]
                        Circle = createObject('Circle', ventana, 10, event.pos[0], event.pos[1], VERDE)
                        P.append(Circle)
                    if len(Q) > 0:
                        del Q[0]
                    if len(R) > 0:
                        del R[0]
                if event.button == 3:
                    if len(Q) == 0:
                        Circle = createObject('Circle', ventana, 10, event.pos[0], event.pos[1], ROJO)
                        Q.append(Circle)
                    else:
                        del Q[0]
                        Circle = createObject('Circle', ventana, 10, event.pos[0], event.pos[1], ROJO)
                        Q.append(Circle)
                    if len(P) > 0:
                        del P[0]
                    if len(R) > 0:
                        del R[0]
                if event.button == 2:
                    if len(R) == 0:
                        Circle = createObject('Circle', ventana, 10, event.pos[0], event.pos[1], AZUL)
                        R.append(Circle)
                    else:
                        del R[0]
                        Circle = createObject('Circle', ventana, 10, event.pos[0], event.pos[1], AZUL)
                        R.append(Circle)
                    if len(P) > 0:
                        del P[0]
                    if len(Q) > 0:
                        del Q[0]
        ventana.fill(NEGRO)
        if len(P) > 0:
                P[0].applyForce(GRAVITY)
                P[0].applyForce(FORDWARD)
                P[0].draw(ventana)
        if len(Q) > 0:
                Q[0].applyForce(GRAVITY)
                Q[0].applyForce(BACKWARD)
                Q[0].draw(ventana)
        if len(R) > 0:
                R[0].applyForce(GRAVITY)
                R[0].draw(ventana)
                
