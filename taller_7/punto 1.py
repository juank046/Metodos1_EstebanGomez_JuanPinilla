#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:20:59 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def funcion_1(x):
    return 2*x -2

def funcion_2(x):
    return 1/2 - x/2

def funcion_3(x):
    return 4 - x

A = [[2,-1],[1,2],[1,1]]
b = [2,1,4]
A = np.array(A)
b = np.array(b)
AT = np.dot(A.T,A)
bT = np.dot(A.T,b)    
xsol = np.linalg.solve(AT,bT)

x = range(-5,5)

plt.plot(x,[funcion_1(i) for i in x])
plt.plot(x,[funcion_2(i) for i in x])
plt.plot(x,[funcion_3(i) for i in x])
plt.scatter(xsol[1],xsol[0],color='r')
plt.xlim(-5,5)
plt.ylim(-5,5)
print("El sistema no tiene soluciones")
N=200
X=np.linspace(-5,5,N)
Y=np.copy(X)

points=np.zeros((N,N))
XX,YY=np.meshgrid(X,Y)

for i in range(len(X)):
    for j in range(len(X)):   
        p=np.array([X[i],X[j]])
        points[i,j]=np.linalg.norm(np.dot(A,p)-b)
min_=np.min(points)
j,i=np.where(points==min_)
p_min=np.array([float(X[i]),float(Y[j])])
fig = plt.figure()
ax1 = fig.add_subplot(111, projection = '3d')
ax1.scatter(XX,YY,points, c = points, cmap= "coolwarm")
ax1.scatter(p_min[0],p_min[1],color="r")
             