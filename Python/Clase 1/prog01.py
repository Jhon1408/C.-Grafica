import pygame

pygame.init()

ventana = pygame.display.set_mode([700, 500])
'''A = [90,90]
B = [300,300]
C = [300,30]

pygame.draw.line(ventana, [255, 255, 255], A, B, 6)
pygame.draw.line(ventana, [255, 255, 255], B, C, 6)
pygame.draw.line(ventana, [255, 255, 255], C, A, 6)
'''
X = 90
Y = 30

pygame.draw.line(ventana, [255, 255, 255], [X,Y], [X+200,Y], 6)
pygame.display.flip()

fin = False

while not fin:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_s):
                ventana.fill(0)
                Y = Y + 6
                pygame.draw.line(ventana, [255, 255, 255], [X,Y], [X+200,Y], 6)
                pygame.display.flip()
            if event.key == (pygame.K_w):
                ventana.fill(0)
                Y = Y - 6
                pygame.draw.line(ventana, [255, 255, 255], [X,Y], [X+200,Y], 6)
                pygame.display.flip()
            if event.key == (pygame.K_d):
                ventana.fill(0)
                X = X + 50
                pygame.draw.line(ventana, [255, 255, 255], [X,Y], [X+200,Y], 6)
                pygame.display.flip()
            if event.key == (pygame.K_a):
                ventana.fill(0)
                X = X - 50
                pygame.draw.line(ventana, [255, 255, 255], [X,Y], [X+200,Y], 6)
                pygame.display.flip()
