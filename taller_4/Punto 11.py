#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:17:49 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
x=np.linspace(-1,1,7)
def funcion(x):
    return(np.sqrt(1+(np.exp(-x**2))))
h=x[1]-x[0]
y=funcion(x)
def integrar(y):
    suma=0
    suma+=y[0]+y[-1]
    for i in range(len(y[1:-1])):
        if i%2 == 0:
            suma+=4*(y[i+1])
        else:
            suma+=2*(y[i+1])
    return suma*h/3
integral=integrar(y)
print("El valor de la integral es: ", integral)