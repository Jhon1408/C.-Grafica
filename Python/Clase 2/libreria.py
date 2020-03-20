import pygame

ANCHO = 800
ALTO = 600
NEGRO = [0,0,0]
VERDE = [0,255,0]
BLANCO = [255,255,255]

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