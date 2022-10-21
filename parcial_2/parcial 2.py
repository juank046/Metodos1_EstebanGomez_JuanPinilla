#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:45:50 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

position=np.zeros((4,2))
position[0]=[1,1]
position[1]=[-1,1]
position[2]=[-1,-1]
position[3]=[1,-1]
a00=sym.Symbol("a00")
a10=sym.Symbol("a10")
a01=sym.Symbol("a01")
a11=sym.Symbol("a11")
def temp(x,y):
    a=np.array([[a00,a01],[a10,a11]])
    sumk_=0
    for i in range(2):
        for j in range(2):
            sumk_+=a[i,j]*(x**i)*(y**j)
    return sumk_
x=sym.Symbol("x")
y=sym.Symbol("y")
ks=np.array([1.,2.,0.5,0.3])
M=np.array([[1,1,1,1],[1,-1,1,-1],[1,-1,-1,1],[1,1,-1,-1]])
p=np.linalg.solve(M,ks)
l=temp(x,y)
print(l)
def temp1(x,y,p):
    return p[0]+p[1]*x+p[2]*y+p[3]*x*y

print(temp1(1,1,p))
print(temp1(-1,1,p))
print(temp1(1,-1,p))
print(temp1(-1,-1,p))
print(temp1(0,0.5,p))
x=np.arange(-1,1,0.1)
y=np.arange(-1,1,0.1)
x,y=np.meshgrid(x,y)
z=x.copy()
filas=x.shape[0]
columnas=x.shape[1]
for i in range(filas):
    for j in range(columnas):
        z[i,j]=temp1(x[i,j],y[i,j],p)
fig=plt.figure(figsize=(5,5))
ax1=fig.add_subplot(1,1,1)
ax1.pcolor(x,y,z,cmap="coolwarm")
fig2=plt.figure(figsize=(5,5))
ax2=fig.add_subplot(2,2,1,projection="3d")
ax2.plot_surface(x,y,z,cmap="coolwarm")

