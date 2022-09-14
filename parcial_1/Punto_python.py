#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:02:27 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return np.sqrt(np.tan(x))
x=np.linspace(0.1,1.1,100)
h=0.01
def derivada_progresiva(x,f):
    return(-3*(f(x))+4*(f(x+h))-(f(x+(2*h))))/(2*h)
y=derivada_progresiva(x, funcion)
def derivada_central(x,f):
    return (f(x+h)-f(x-h))/(2*h)
y1=derivada_central(x, funcion)
def derivada_real(x):
    numerador=((1/np.cos(x)))**2
    denominador=2*(np.sqrt(np.tan(x)))
    return numerador/denominador
real=derivada_real(x)
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,3)
ax3 = fig.add_subplot(2,2,4)
ax1 = fig.add_subplot(2,2,2)
ax.plot(x,y,color="r")
ax2.plot(x,y1,color="k")
ax3.plot(x,real)
error1=np.abs(real-y)
error2=np.abs(real-y1)
ax1.scatter(x,error1)
ax1.scatter(x,error2,color="r")
error_ambas=np.abs(error1-error2)
print("Como se puede observar en la gráfica, ambos errores tienen un orden de presición de 3 y de 4 en algunos casos, pero nunca menor a este.")