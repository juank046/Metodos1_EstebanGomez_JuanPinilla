# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:40:18 2022

@author: Esteban Gomez
"""

#Punto 16 
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def GetNewtonMethod(f,df,xn,itmax = 100000, precision=1e-8):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            xn1 = xn - f(xn)/df(xn)

            error = np.abs(f(xn)/df(xn))
        
        except ZeroDivisionError:
            print("zero division")
            
        xn  = xn1
        it += 1
    
    if it == itmax:
        return False
    else:
        return xn
    
def GetAllRoots(f,df,x, tolerancia=9):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(f,df,i)
          
        if root != False:
            
            croot = np.round( root, tolerancia ) 
            
            if croot not in Roots:
                Roots = np.append( Roots, croot )
    Roots.sort()
    
    return Roots

lague = []
der_lague = []
x = sym.Symbol('x',Real=True)
n=30 

def GetLaguerre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = sym.exp(-x)*x**n
    
    p = sym.exp(x)*sym.diff(y,x,n)/(np.math.factorial(n))
    
    return p

for i in range(n+1):
    
    poly = GetLaguerre(i)
    
    lague.append(poly)
    der_lague.append(sym.diff(poly,x,1))

def GetRootsPolynomial(n,xi,poly,dpoly):
    
    x = sym.Symbol('x',Real=True)
    
    pn = sym.lambdify([x],poly[n],'numpy')
    dpn = sym.lambdify([x],dpoly[n],'numpy')
    Roots = GetAllRoots(pn,dpn,xi,tolerancia=8)
    
    return Roots

xi = np.linspace(0,100,200)
n = 5
raices = GetRootsPolynomial(n,xi,lague,der_lague)

def weights(Roots,Laguerre):
    
    Weights = []
    x = sym.Symbol('x',Real=True)
    poly = sym.lambdify([x],lague[n+1],'numpy')
    
    for r in Roots:
        Weights.append(r/((n+1)**2 * poly(r)**2))
    return Weights
Weights = weights(raices,lague)

f = lambda x : (x**3 * np.exp(x))/((np.exp(x))-1)
a = -1
b = 1
t = 0.5*((b-a)*raices + a + b)

Integral = np.sum( Weights*f(t))
Integral_real=(np.pi**4)/15
Integral,Integral_real

Accuracy=[]
for n in range(2,11):
    Roots = GetRootsPolynomial(n,xi,lague,der_lague)
    Weights = weights(Roots,lague)
    t = 0.5*((b-a)*Roots + a + b)
    Integral = np.sum( Weights*f(t))
    error=(Integral/Integral_real)
    Accuracy.append(error)  
    
    x=np.linspace(2,10,9)
plt.grid()
plt.plot(x,Accuracy,"o",label="Laguerre cuadrature accuracy")



