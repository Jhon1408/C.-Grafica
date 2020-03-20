import pygame
import math

ANCHO = 600
ALTO = 600
NEGRO = [0,0,0]
VERDE = [0,255,0]
BLANCO = [255,255,255]
ROJO = [255,0,0]
MIDDLE = [int(ANCHO/2),int(ALTO/2)]
ESCALA = 0.5

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

def setEscale(n):
    ESCALA = n

def TransformCtoS(Punto): #pasa de coordenadas cartesianas a pantalla
    PuntoX = MIDDLE[0] + Punto[0]
    PuntoY = MIDDLE[1] - Punto[1]
    PuntoFinal = [PuntoX,PuntoY]
    return PuntoFinal

def TransformStoC(Punto):
    C = 0
    if Punto[0] >= MIDDLE[0] and Punto[1] <= MIDDLE[1]:
        C = 1
    if Punto[0] < MIDDLE[0] and Punto[1] <= MIDDLE[1]:
        C = 2
    if Punto[0] < MIDDLE[0] and Punto[1] > MIDDLE[1]:
        C = 3
    if Punto[0] >= MIDDLE[0] and Punto[1] > MIDDLE[1]:
        C = 4

    if C == 1:
        PuntoX = Punto[0] - MIDDLE[0]
        PuntoY = MIDDLE[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 2:
        PuntoX = Punto[0] - MIDDLE[0]
        PuntoY = MIDDLE[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 3:
        PuntoX = Punto[0] - MIDDLE[0]
        PuntoY = MIDDLE[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal
    if C == 4:
        PuntoX = Punto[0] - MIDDLE[0]
        PuntoY = MIDDLE[1] - Punto[1]
        PuntoFinal = [PuntoX,PuntoY]
        return PuntoFinal

def Vector(v,s,d):
    '''
    v: ventana donde se crea el Plano
    s: posicion de origen
    d: posicion de destino
    '''
    pygame.draw.line(v, VERDE, s, TransformCtoS(d))
    pygame.display.flip()

def SumVectors(v, vec1, vec2):
    dest = [vec1[0] + vec2[0],vec1[1] + vec2[1]]
    pygame.draw.line(v, ROJO, MIDDLE, TransformCtoS(dest))
    pygame.display.flip()

def capturePoints(P,e,v,draw):
    P.append(TransformStoC([e.pos[0],e.pos[1]]))
    if(draw == 1):
        if len(P) > 0:
            for i in P:
                pygame.draw.circle(v, VERDE, TransformCtoS(i), 5)
                pygame.display.flip()
    return P

def cartesianLine(v,A,B):
    m = Pendiente(A,B)
    b = Desfase(A,m)
    for i in range(-MIDDLE[0],MIDDLE[0]):
        variableX = i
        variableY = (m * variableX) + b
        pygame.draw.circle(v, ROJO, TransformCtoS([int(variableX), int(variableY)]), 2)
        pygame.display.flip()
    if b > 0:
        equation = "Y = "+ str(m) +"X + "+ str(b)
    else:
        equation = "Y = "+ str(m) +"X "+ str(b)
    return equation

def cartesianPolygon(v, P):
    S = []
    for i in P:
        S.append(TransformCtoS(i))
    pygame.draw.polygon(v, VERDE, S, 2)
    pygame.display.flip()

#Linea Recta

def Pendiente(Punto1, Punto2):
    Pendientey = float(Punto2[1] - Punto1[1])
    Pendientex = float(Punto2[0] - Punto1[0])
    Pendiente = float(Pendientey / Pendientex)
    return Pendiente

def Desfase(Punto, pendiente):
    Corte = float(Punto[1] - (pendiente * Punto[0]))
    return Corte

def Reset(ventana):
    ventana.fill(NEGRO)
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    Plano(ventana,MIDDLE)
    pygame.display.flip()

def Escale(P):
    Q = P
    for i in Q:
        i[0] = i[0]*ESCALA
        i[1] = i[1]*ESCALA
    return Q

def RotateCenter(P,angle):
    Q = P
    for i in Q:
        x = i[0]
        y = i[1]
        i[0] = x*math.cos(math.radians(angle)) + y*math.sin(math.radians(angle))
        i[1] = -x*math.sin(math.radians(angle)) + y*math.cos(math.radians(angle))
    return Q

def RotatePoint(ventana,P,angle,center):
    Q = P
    for i in Q:
        x = i[0]
        y = i[1]
        i[0] = x*math.cos(math.radians(angle)) + y*math.sin(math.radians(angle))
        i[1] = -x*math.sin(math.radians(angle)) + y*math.cos(math.radians(angle))
    return Q