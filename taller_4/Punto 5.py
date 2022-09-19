# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:15:22 2022

@author: Esteban Gomez
"""

#metodo del Trapecio 
import numpy as np


fx = lambda x: np.exp(-x**2)
a = 0
b = 1
tramos = 200

suma = 0 
h = (b-a)/tramos 
xi = a
for i in range(0, tramos, 1):
    Atrapecio = h*(fx(xi)+fx(xi+h))/2
    suma = suma + Atrapecio 
    xi = xi + h 
integral = suma

muestraslinea = (tramos+1)*10

print("tramos: ", tramos)
print("Integral: ", integral )






