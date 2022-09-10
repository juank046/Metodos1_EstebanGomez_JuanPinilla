# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:29:04 2022

@author: Esteban Gomez
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sympy as sym
#import Raices_2 as ra

#Formula de Rodrigues 
def GetLegendre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = (x**2-1)**n
    
    p = sym.diff(y,x,n)/(2**n * np.math.factorial(n))
    
    return p

polinomios = []
n=20
for i in range(n+1):
    polinomios.append(GetLegendre(i))

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

x = sym.Symbol('x',Real=True)

for i in range(1,n+1):
    f = polinomios[i]
    funcion = sym.lambdify([x], f, 'numpy')

def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
    
    error = 1
    it=0
    
    while (error > precision) and (it < itmax):
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
    
    
    if it == itmax:
        return False
    else:
        return xn

def GetAllRoots(x,tolerancia=8):
    
    Roots = np.array([])
    
    for i in x:
        root = GetNewtonMethod(funcion ,Derivative,i)
        
        if root != False:
            
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

xtrial = np.linspace(-1,1,100)
for i in range(1,n+1):
    f = polinomios[i]
    funcion = sym.lambdify([x], f, 'numpy')
    Roots = GetAllRoots(xtrial)
    print('%i:'%i, Roots)
  








