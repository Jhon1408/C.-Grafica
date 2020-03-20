import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    P = [] # type: List[Any]
    Pendulum = createPendulum(ventana, [MIDDLE[0],0], 300, ROJO)
    P.append(Pendulum)
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        if len(P) > 0:
            P[0].draw(ventana)
            P[0].applyForce(GRAVITY)
            ventana.fill(NEGRO)
    
                
