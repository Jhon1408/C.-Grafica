import pygame
from libreria import *

if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    Plano(ventana,MIDDLE)
    fin = False
    A = [0,0]
    B = [150,30]
    C = TransformPtoC(B)
    aux = [100,30]
    D = TransformPtoC(aux)
    E = TransformPtoC(aux)
    F = A
    P = [TransformCtoS(A),TransformCtoS(TransformPtoC(B)),TransformCtoS(Trasladar(C,[0,100])),TransformCtoS(Trasladar(D,[0,100])),TransformCtoS(Trasladar(E,[0,50])),TransformCtoS(Trasladar(F,[0,50]))]
    print(P)
    pygame.draw.polygon(ventana, BLANCO, P)
    pygame.display.flip()
    punto(ventana,TransformCtoS(A))
    punto(ventana,TransformCtoS(TransformPtoC(B)))
    punto(ventana,TransformCtoS(Trasladar(C,[0,100])))
    punto(ventana,TransformCtoS(Trasladar(D,[0,100])))
    punto(ventana,TransformCtoS(Trasladar(E,[0,50])))
    punto(ventana,TransformCtoS(Trasladar(F,[0,50])))
    #Comentario de prueba
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
    
                
