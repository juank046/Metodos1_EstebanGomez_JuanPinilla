# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:37:20 2022

@author: Esteban Gomez
"""

#problema de aplicacion 

import numpy as np
import matplotlib.pyplot as plt

#DISCRETIZACION
X = np.linspace(-4,4,25)
Y = np.linspace(-4,4,25)
CorX, CorY = np.meshgrid(X,Y)

#CIRCULO
angulo = np.linspace(0, 2*np.pi,200)
r = 2
a = r*np.cos(angulo)
b = r*np.sin(angulo)


#PUNTOS QUE ESTAN FUERA DEL CIRCULO
ECUACION_CIRCULO= np.sqrt(CorX**2+CorY**2)
out = ECUACION_CIRCULO > r

#POTENCIAL DE FLUJO Y DERIVADAS
v = 2
f = lambda x,y: v*x*(1-((r**2)/(x**2+y**2)))

#Derivadas 
h = 0.001
def Derivada_parcial_x(f,x,y,H):
    return (f(x+h,y)-f(x-h,y))/(2*h)
def Derivada_parcial_y(f,x,y,H):
    return (f(x,y-h)-f(x,y+h))/(2*h)
Vx= Derivada_parcial_x( f,CorX[out], CorY[out], h)
Vy = Derivada_parcial_y(f,CorX[out],CorY[out], h)


fig, ax = plt.subplots()
#Circulo 
ax.plot(a,b,color='r')
#flechas
ax.quiver(CorX[out], CorY[out], Vx, Vy, color = "b", alpha = 0.9)
ax.set(xlabel='x [cm]', ylabel='y [cm]')

plt.show()
