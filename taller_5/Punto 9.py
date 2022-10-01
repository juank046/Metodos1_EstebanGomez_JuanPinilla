#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 23:10:12 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt

def funcion(x1,x2,x3,x4,x5,x6,x7,x8):
    return (2**-7)*(x1+x2+x3+x4+x5+x6+x7+x8)**2
def integral(N,a,b):
    x1=np.random.uniform(a,b,size=N)
    x2=np.random.uniform(a,b,size=N)
    x3=np.random.uniform(a,b,size=N)
    x4=np.random.uniform(a,b,size=N)
    x5=np.random.uniform(a,b,size=N)
    x6=np.random.uniform(a,b,size=N)
    x7=np.random.uniform(a,b,size=N)
    x8=np.random.uniform(a,b,size=N)
    valor=funcion(x1, x2, x3, x4, x5, x6, x7, x8)
    return np.average(valor)*(b-a)
integralR=integral(10000, 0, 1)
print("El valor de la integral por montecarlo es: ",integralR) 
print("El valor real es: ",25/192)
