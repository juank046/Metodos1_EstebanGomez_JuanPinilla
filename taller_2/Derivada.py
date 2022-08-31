#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:24:21 2022

@author: juancamilo
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10)
h=0.05


def funcion(x):
    exponencial=np.exp(-x**2)
    return 1/(pow(1+exponencial,1/2))

def derivadaC(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)
def derivada_real(x):
    numerador=(np.exp(-x**2))*x
    denominador=(1+np.exp(-x**2))
    return (numerador)/(pow(denominador,3/2))

derivative=derivadaC(x, funcion, h)
error=np.abs(derivada_real(x)-derivative)
print("Derivada: ",derivative)
print("Error: ",error)
plt.plot(x,derivative)
