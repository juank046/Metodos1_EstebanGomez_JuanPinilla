# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 22:58:06 2022

@author: Esteban Gomez
"""

import numpy as np 
import matplotlib.pyplot as plt 

a, b = 0, 1
angulos = np.arange(0, 6*np.pi, 0.01)
lista = list(angulos)
def arquimedes():
    Lista = []
    for i in lista:
         r = a + b*i
         Lista.append(r)
         
    return Lista
         
def cartesianasX(Lista: list):
    ejeX= []
    for i in Lista:
        
            x = i*np.cos(i)
            ejeX.append(x)
            
    return ejeX
    

def cartesianasY(Lista: list):
    ejeY= []
    for i in Lista:
        
            x = i*np.sin(i)
            ejeY.append(x)
            
    return ejeY   

def grafica():
    plt.plot(cartesianasX(lista), cartesianasY(lista))
    plt.show()
    
grafica()
          


    