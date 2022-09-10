# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:07:41 2022

@author: Esteban Gomez
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def Function(x):
    return (3*x**5)+(5*x**4)-(x**3)

x = np.linspace(-1,7,100)
y = Function(x)

plt.plot(x,y)
plt.axhline(y=0,color='r')

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)


def NewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
    
    error = 1
    it=0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
    print('raiz:', xn,it)
    
    if it == itmax:
        return False
    else:
        return xn
    
root = NewtonMethod(Function,Derivative,1)

def GetAllRoots(x,tolerancia=8):
    
    Roots = np.array([])
    
    for i in x:
        root = NewtonMethod(Function,Derivative,i)
        
        if root != False:
            
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

print(GetAllRoots(x,8))