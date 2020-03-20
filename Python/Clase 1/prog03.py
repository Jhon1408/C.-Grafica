import pygame
ALTO = 500
ANCHO = 700

pygame.init()

ventana = pygame.display.set_mode([ANCHO, ALTO])

flag = 250

R = 20

reloj = pygame.time.Clock()

pygame.draw.circle(ventana, [255,255,255], [int(ANCHO/2),int(ALTO/2)], R)
pygame.display.flip()

fin = False
while not fin:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
    if event.type == pygame.MOUSEMOTION:
        reloj.tick(180)
        ventana.fill(0)
        pygame.draw.circle(ventana, [255,255,255], event.pos, R)
        pygame.display.flip()
        if flag == 250:
            R = R + 1
            if R == 250:
                flag = 20
        if flag == 20:
            R = R - 1
            if R == 20:
                flag = 250