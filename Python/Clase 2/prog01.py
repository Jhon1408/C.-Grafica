import pygame

pygame.init()

ANCHO = 700
ALTO = 500

ventana = pygame.display.set_mode([ANCHO, ALTO])

pygame.draw.line(ventana, [255, 255, 255], [ANCHO/2, ALTO], [ANCHO/2, 0], 1)
pygame.draw.line(ventana, [255, 255, 255], [ANCHO, ALTO/2], [0, ALTO/2], 1)
pygame.display.flip()

fin = False

while not fin:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
