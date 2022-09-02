#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:30:54 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
x=np.linspace(-10,10)
M=[1,-2,1]
def funcion(x):
    exponencial=np.exp(-x**2)
    return 1/(pow(1+exponencial,1/2))
function=funcion(x)
h=0.05
simbolo = sym.Symbol('x')
def derivada(x,f):
    lista=[]
    i=1
    while 1<=i<=48:
        suma=0
        m=-1
        while m <=1:
            valor=(M[m+1])*f(x[i]-(m*h))
            suma+=valor
            m+=1 
        resultado=(1/(h*h))*suma
        lista.append(resultado)
        i+=1
        
    return lista
def derivada_real(x):
    numerador=(np.exp(-x**2))*x
    denominador=(1+np.exp(-x**2))
    return (numerador)/(pow(denominador,3/2))

derivative2=derivada(x,funcion)
derivative2.insert(0,0.0)
#derivative2.insert(1,0.0)
derivative2.append(0.0)
#derivative2.append(0.0)
error2=np.abs(derivada_real(x)-derivative2)
plt.plot(x,derivative2)
print(derivative2)
