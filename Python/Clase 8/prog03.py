import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    P = [] # type: List[Any]
    Circle = createCircle(ventana,10,MIDDLE[0],10,VERDE)
    P.append(Circle)
    P[0].applyForce([FORDWARD,0])
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        if len(P) > 0:
            P[0].draw(ventana)
            P[0].wallBounce()
            P[0].applyGravity()
            ventana.fill(NEGRO)
    
                
