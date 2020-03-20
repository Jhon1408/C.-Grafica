import math
import pygame
import random
import time
#colores
blanco = [255,255,255]
negro = [0,0,0]
rojo = [255,0,0]
azul = [0,0,255]
verde = [0,255,0]
#dimensiones pantalla
ancho,alto = [600,600]
#centro de la pantalla
centro_x = ancho//2
centro_y = alto//2
origen = [centro_x,centro_y]

def color_aleatorio():
    return [random.randrange(255),random.randrange(255),random.randrange(255)]

#funcion que dibuja el plano cartesiano
def Plano_Cartesiano(pantalla):
    ox=origen[0]
    oy=origen[1]
    pygame.draw.line(pantalla,blanco,[ox,0],[ox,alto])
    pygame.draw.line(pantalla,blanco,[0,oy],[ancho,oy])

def Plano_Cartesiano_nuevo(pantalla,origen):
    ox=origen[0]
    oy=origen[1]
    pygame.draw.line(pantalla,blanco,[ox,0],[ox,alto])
    pygame.draw.line(pantalla,blanco,[0,oy],[ancho,oy])

#funcion para dibujar una Recta con el mouse
def Recta(coordenadas,pantalla,a,b):
    pygame.draw.line(pantalla,color_aleatorio(),coordenadas[a],coordenadas[b])

#funcion para dibujar un punto con el click
def Punto(coordenada,pantalla):
    pygame.draw.circle(pantalla,rojo,coordenada,4)

#dibujar triangulo
def Triangulo_Auto(coordenadas,pantalla):
    Recta(coordenadas,pantalla,0,1)
    Recta(coordenadas,pantalla,1,2)
    Recta(coordenadas,pantalla,0,2)

#funcion para dibujar un triangulo con el clicl
def Triangulo(coordenadas,pantalla,cont):
    if cont == 1:
        Recta(coordenadas,pantalla,cont-1,cont)
    if cont == 2:
        Recta(coordenadas,pantalla,cont-1,cont)
    if cont == 3:
        Recta(coordenadas,pantalla,cont-3,cont-1)

#pasar de cartesiano a pantalla
def A_Cartesiano(punto):
    xp=punto[0]-centro_x
    yp=-punto[1]+centro_y
    p=[xp,yp]
    return p

#pasar de pantalla a cartesiano
def A_Pantalla(punto):
    xp = punto[0]+ centro_x
    yp = -punto[1]+ centro_y
    p =[xp,yp]
    return p

#Escalar
def Escalar(punto,escala):
	xp = punto[0]*escala[0]
	yp = punto[1]*escala[1]
	p=[xp,yp]
	return p

#Rotar
def Rotar_Horario(punto,angulo):
    rad = math.radians(angulo)
    xp = punto[0]*math.cos(rad)-punto[1]*math.sin(rad)
    yp = punto[0]*math.sin(rad)+punto[1]*math.cos(rad)
    p = [xp,yp]
    return p

def Rotar_AntiHorario(punto,angulo):
    rad = math.radians(angulo)
    xp = punto[0]*math.sin(rad)+punto[1]*math.cos(rad)
    yp = -punto[0]*math.cos(rad)+punto[1]*math.sin(rad)
    p = [xp,yp]
    return p
#Trasladar
def Trasladar(punto,traslacion):
	xp=punto[0]+traslacion[0]
	yp=punto[1]+traslacion[1]
	p=[xp,yp]
	return p

#pasa unos puntos de pantalla a cartesiano
def Puntos_A_Cartesiano(puntos):
    for i in range(len(puntos)):
        	puntos[i] = A_Cartesiano(puntos[i])
    return puntos

#pasa unos puntos de cartesiano a pantalla
def Puntos_A_Pantalla(puntos):
	for i in range(len(puntos)):
		      puntos[i] = A_Pantalla(puntos[i])
	return puntos

def Escalar_Puntos(puntos,escala):
	for i in range(len(puntos)):
		puntos[i] = Escalar(puntos[i],escala)
	return puntos

def Trasladar_Puntos(puntos,traslacion):
	for i in range(len(puntos)):
		puntos[i] = Trasladar(puntos[i],traslacion)
    #return puntos

def Rotar_Puntos_Horario(puntos,angulo):
	for i in range(len(puntos)):
		puntos[i] = Rotar_Horario(puntos[i],angulo)
    #return puntos

def Rotar_Puntos_AntiHorario(puntos,angulo):
	for i in range(len(puntos)):
		puntos[i] = Rotar_AntiHorario(puntos[i],angulo)
    #return puntos

def Esta_Cerca(mouse,punto):
    error=10
    ls=[]
    ls.append(punto[0])
    ls.append(punto[1])
    p1=ls[0]
    p2=ls[1]
    lim_inf_x=p1-error
    lim_inf_y=p2-error
    lim_sup_x=p1+error
    lim_sup_y=p2+error
    if(((mouse[0]<=lim_sup_x)and(mouse[0]>=lim_inf_x)) and
        ((mouse[1]<=lim_sup_y)and(mouse[1]>=lim_inf_y))):
        return True
    else:
        return False

def Pitagoricas(num_lados,Magnitud):
	Angulo = 0;
	R = []
	for i in range(num_lados):
		punto = (Magnitud*math.cos(Angulo),Magnitud*math.sin(Angulo))
		R.append(punto)
		Angulo += math.radians(360/num_lados)
	return R

def patron1(pantalla,color,x,y,mag):

    pygame.draw.line(pantalla,rojo,[x,y],[(10+x),y],mag)
    x += 10
    pygame.draw.line(pantalla,rojo,[x,y],[x,(y-20)],mag)
    y -= 20
    pygame.draw.line(pantalla,rojo,[x,y],[(x+10),y],mag)
    x += 10

def marco(pantalla,color,x,y,magnitud):
    a = x
    b = y
    while x < ancho - a :
        patron1(pantalla,color,x,y,magnitud)
        x += (a +10)
    x = a
    while y  < alto - b:
        patron1(pantalla,color,x,y,magnitud)
        y += (b+10)
    y = alto - b +10
    while x < ancho -a:
        patron1(pantalla,color,x,y,magnitud)
        x += (a+10)
    x = ancho - 40
    while y > 0 + b:
        patron1(pantalla,color,x,y,magnitud)
        y -= (b+10)

def coordenadas_polares(r,angulo):
    angu1= math.radians(angulo)
    p =(int(r*math.cos(angu1)), int(r*math.sin(angu1)))
    return p

def Rosa_polar(a,tam):
	R = []
	for i in range(0,360):
		r = tam*(math.cos(a*math.radians(i)))
		p = coordenadas_polares(r,i)
		R.append(p)
	return R

def lemniscata(tam):
    R = []
    for i in range(0,360):
        r=(tam*tam)*(math.cos((2*math.radians(i))))
        if (r>0):
            b=coordenadas_polares(math.sqrt(r),i)
            R.append(b)
    return R

# tipos de caracoles
#el caracol con rizo el b > a
#el cardiode a = b
def caracoles(a,b,tam):
    R = []
    for i in range(0,360):
        r= tam*(a +(b*math.cos(math.radians(i))))
        p = coordenadas_polares(r,i)
        R.append(p)
    return R

def patron2(pantalla,color,x,y,mag):

    pygame.draw.line(pantalla,rojo,[x,y],[(20+x),y],mag)
    pygame.draw.line(pantalla,rojo,[x+10,y],[x+10,y+10],mag)

def marco1(pantalla,color,x,y,magnitud):
    a = x
    b = y
    while x < ancho - a :
        patron2(pantalla,color,x,y+10,magnitud)
        x += (a +10)
    x = a
    y = alto - b +10
    while x < ancho -a:
        patron2(pantalla,color,x,y,magnitud)
        x += (a+10)
    x = ancho - 40
    print(x)
    while y > 0 + (2*b):
        x -= 30
        y -= 30
        patron2(pantalla,color,x,y,magnitud)