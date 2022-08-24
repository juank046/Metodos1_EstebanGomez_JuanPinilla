# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:57:53 2022

@author: Esteban Gomez
"""

#numero aureo 
import fibonacci as fi 
import math as m
import matplotlib.pyplot as plt

def numero_aureo():
    numero_aureo=(1+m.sqrt(5))/2
    x = 20
    puntos = []
    for i in range(2,x+1):
        aproximacion_numeroaureo=fi.fibonacci(i+1)[i]/fi.fibonacci(i-1)[i]
        puntos.append(aproximacion_numeroaureo)
        plt.plot(puntos)
        plt.show()
    
numero_aureo()