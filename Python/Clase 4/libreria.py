import pygame

ANCHO = 600
ALTO = 600
NEGRO = [0,0,0]
VERDE = [0,255,0]
BLANCO = [255,255,255]
MIDDLE = [ANCHO/2,ALTO/2]

def Plano(v,p):
    '''
    v: ventana donde se crea el Plano
    p: posicion de origen del Plano
    '''
    posx=p[0]
    posy=p[1]
    v.fill(NEGRO)
    pygame.draw.line(v,BLANCO,[0,posy],[ANCHO, posy])
    pygame.draw.line(v,BLANCO,[posx,0],[posx, ALTO])
    pygame.display.flip()

def triangle(ventana, pos, size):
    P = [[pos[0],pos[1]+size], [pos[0],pos[1]-size], [pos[0]+size,pos[1]]]
    Plano(ventana,[ANCHO/2,ALTO/2])
    pygame.draw.polygon(ventana, VERDE, P, 1)
    pygame.display.flip()

def setMiddle(v,p):
    MIDDLE[0] = p[0]
    MIDDLE[1] = p[1]
    Plano(v,MIDDLE)

def TransformStoC(p):
    C = 0
    T = []
    if p[0] > MIDDLE[0]:
        if p[1] > MIDDLE[1]:
            C = 4
        if p[1] <= MIDDLE[1]:
            C = 1
    elif p[0] <= MIDDLE[0]:
        if p[1] > MIDDLE[1]:
            C = 3
        if p[1] <= MIDDLE[1]:
            C = 2
    if C == 1:
        T = [int(p[0]-MIDDLE[0]),int(-p[1]+MIDDLE[1])]
    if C == 2:
        T = [int(p[0]-MIDDLE[0]),int(-p[1]+MIDDLE[1])]
    if C == 3:
        T = [int(p[0]-MIDDLE[0]),int(-p[1]+MIDDLE[1])]
    if C == 4:
        T = [int(p[0]-MIDDLE[0]),int(-p[1]+MIDDLE[1])]
    return T

def TransformCtoS(p):
    C = 0
    T = []
    if p[0] > MIDDLE[0]:
        if p[1] > MIDDLE[1]:
            C = 4
        if p[1] <= MIDDLE[1]:
            C = 1
    elif p[0] <= MIDDLE[0]:
        if p[1] > MIDDLE[1]:
            C = 3
        if p[1] <= MIDDLE[1]:
            C = 2
    if C == 1:
        T = [int(p[0]+MIDDLE[0]),int(-p[1]+MIDDLE[1])]
    if C == 2:
        T = [int(p[0]+MIDDLE[0]),int(-p[1]+MIDDLE[1])]
    if C == 3:
        T = [int(p[0]+MIDDLE[0]),int(p[1]+MIDDLE[1])]
    if C == 4:
        T = [int(p[0]+MIDDLE[0]),int(p[1]+MIDDLE[1])]
    return T