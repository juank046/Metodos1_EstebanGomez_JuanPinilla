#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 23:13:06 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10)
M=[1,0,-1]
def funcion(x):
    exponencial=np.exp(-x**2)
    return 1/(pow(1+exponencial,1/2))
function=funcion(x)
h=0.05
def derivada(x,f):
    lista=[]
    i=1
    while 1<=i<=48:
        suma=0
        m=-1
        while m <=1:
            valor=(M[m+1])*f(x[i-m])
            suma+=valor
            m+=1 
        resultado=(1/(2*h))*suma
        lista.append(resultado)
        i+=1
        
    return lista
def derivada_real(x):
    numerador=(np.exp(-x**2))*x
    denominador=(1+np.exp(-x**2))
    return (numerador)/(pow(denominador,3/2))

derivative1=derivada(x,funcion)
derivative1.insert(0,0.0)
derivative1.append(0.0)
error1=np.abs(derivada_real(x)-derivative1)
plt.plot(x,derivative1)
print(error1)
