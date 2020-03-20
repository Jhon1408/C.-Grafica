import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    Plano(ventana,MIDDLE)
    fin = False
    Plano(ventana,MIDDLE)
    pitagoricas(ventana,3,300)
    #Comentario de prueba
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
    
                
