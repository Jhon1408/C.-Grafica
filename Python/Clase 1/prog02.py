import pygame
ALTO = 500
ANCHO = 700

pygame.init()

ventana = pygame.display.set_mode([ANCHO, ALTO])

bounce = 500

fin = False

X = 90
Y = 30

pygame.draw.line(ventana, [255, 255, 255], [X,Y], [X+200,Y], 6)
pygame.display.flip()

reloj = pygame.time.Clock()

while not fin:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
    if bounce == 500:
        reloj.tick(180)
        ventana.fill(0)
        Y = Y + 1
        pygame.draw.line(ventana, [255, 255, 255], [X,Y], [X+200,Y], 6)
        pygame.display.flip()
        if Y > 500:
            bounce = 0
    if bounce == 0:
        reloj.tick(120)
        ventana.fill(0)
        Y = Y - 1
        pygame.draw.line(ventana, [255, 255, 255], [X,Y], [X+200,Y], 6)
        pygame.display.flip()
        if Y < 0:
            bounce = 500
    
            